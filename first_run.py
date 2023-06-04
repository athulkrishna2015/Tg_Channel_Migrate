import asyncio
from pyrogram import Client

api_id = 1234
api_hash = "cnaiwfnnckwaerfncakdaifoifkawnf"

app = Client("my_account", api_id, api_hash) 

async def main():
    async with app:
            await app.send_message("me", "Pyrogram Session Created")


asyncio.run(main())
