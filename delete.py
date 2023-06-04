import asyncio
from pyrogram import Client

app = Client("my_account") 
chat_id=-1001234564 # Enter your chat ID

async def main():
    async with app:
        await app.delete_messages(chat_id,  message_ids=range(1, 1000)) # Change Range of messges


asyncio.run(main())
