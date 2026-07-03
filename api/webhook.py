import asyncio
import json
import logging
from http.server import BaseHTTPRequestHandler

from aiogram.types import Update

from bot.app import create_bot_and_dispatcher
from config import Config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

_bot = None
_dp = None
_db = None
_initialized = False


async def _ensure_app():
    global _bot, _dp, _db, _initialized
    if _bot is None:
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


class handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
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
