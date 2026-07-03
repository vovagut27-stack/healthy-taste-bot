import asyncio
import json
import logging
import os
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse

from aiogram.types import Update

from bot.app import create_bot_and_dispatcher

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

_bot = None
_dp = None
_db = None
_initialized = False


async def _ensure_app():
    global _bot, _dp, _db, _initialized
    if _bot is None:
        from config import Config

        config = Config.from_env()
        _bot, _dp, _db = create_bot_and_dispatcher(config)
    if not _initialized:
        await _db.init()
        _initialized = True
    return _bot, _dp


async def _handle_update(body: bytes) -> None:
    bot, dp = await _ensure_app()
    data = json.loads(body.decode("utf-8"))
    update = Update.model_validate(data)
    await dp.feed_update(bot, update)


def _register_webhook() -> dict:
    token = os.getenv("BOT_TOKEN", "")
    if not token:
        return {"ok": False, "error": "BOT_TOKEN not configured on Vercel"}

    vercel_url = (
        os.getenv("WEBHOOK_URL")
        or os.getenv("VERCEL_PROJECT_PRODUCTION_URL")
        or os.getenv("VERCEL_URL")
        or "healthy-taste-bot.vercel.app"
    )
    base = vercel_url if vercel_url.startswith("http") else f"https://{vercel_url}"
    webhook_url = f"{base.rstrip('/')}/api/webhook"

    payload = json.dumps({"url": webhook_url}).encode("utf-8")
    request = urllib.request.Request(
        f"https://api.telegram.org/bot{token}/setWebhook",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            result = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        return {"ok": False, "error": exc.read().decode("utf-8"), "webhook_url": webhook_url}
    except Exception as exc:
        return {"ok": False, "error": str(exc), "webhook_url": webhook_url}

    result["webhook_url"] = webhook_url
    return result


class handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        query = parse_qs(urlparse(self.path).query)
        if "setup" in query:
            result = _register_webhook()
            status = 200 if result.get("ok") else 503
            payload = json.dumps(result, ensure_ascii=False)
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(payload.encode("utf-8"))
            return

        payload = json.dumps({"ok": True, "service": "Healthy Taste Bot webhook"})
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(payload.encode("utf-8"))

    def do_POST(self) -> None:
        try:
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)
            asyncio.run(_handle_update(body))
            payload = json.dumps({"ok": True})
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(payload.encode("utf-8"))
        except ValueError as exc:
            logger.error("Configuration error: %s", exc)
            payload = json.dumps({"ok": False, "error": str(exc)})
            self.send_response(503)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(payload.encode("utf-8"))
        except Exception:
            logger.exception("Webhook error")
            payload = json.dumps({"ok": False})
            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(payload.encode("utf-8"))
