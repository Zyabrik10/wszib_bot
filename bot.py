'''
Version: 1.0.0
Name: wszib_bot
Description: Telegram bot for wszib students
'''

# asyncio is a library to write concurrent code using the async/await syntax.
import asyncio
from aiogram import Bot, Dispatcher
from handlers.nuh_uh import router as router_nuh_uh  # our router
import os

from dotenv import load_dotenv
load_dotenv() #configure env vars


async def main():

    # creating bot instance with specific token
    # so that we can ensure with wich bot we are working
    bot = Bot(token=os.getenv("TOKEN"))

    # Dispatcher will listeting to messages user sends
    # each time user sends a message dispatcher will be activated
    dp = Dispatcher()

    # in order to have clean bot.py and all request transport to other file
    # so our dispatcher still handle requests we need to use method 'include_router'
    # and put our router in it
    dp.include_router(router_nuh_uh)

    # it does what it says
    print("Bot has been started")

    # make our dispatcher listen to our bots requests
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot is done")
