import asyncio
import uvicorn

from app.application import app
from app.telebot.start import run_aiogram_bot


async def main():
    await asyncio.gather(
        run_aiogram_bot(),
        asyncio.create_task(serve_fastapi(app))
    )


async def serve_fastapi(app):
    import uvicorn
    config = uvicorn.Config(app, host="0.0.0.0", port=8000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
