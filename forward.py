import asyncio
from pyrogram import Client

app = Client("my_account") 
to_chat = -1009257942354    # Replace with your own group or channel ID
from_chat = -100932580252  # Replace with your own group or channel ID

async def main():
    async with app:
            await app.forward_messages(to_chat, from_chat, message_ids=range(1, 1000)) # Change range 
        
asyncio.run(main())
