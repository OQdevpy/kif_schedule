import asyncio

from aiogram import types, Dispatcher
from aiogram.dispatcher import DEFAULT_RATE_LIMIT
from aiogram.dispatcher.handler import CancelHandler, current_handler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils.exceptions import Throttled
from loader import bot
import sqlite3


class ThrottlingMiddleware(BaseMiddleware):
    """
    Simple middleware
    """

    def __init__(self, limit=DEFAULT_RATE_LIMIT, key_prefix='antiflood_'):
        self.rate_limit = limit
        self.prefix = key_prefix
        super(ThrottlingMiddleware, self).__init__()

    async def on_process_message(self, message: types.Message, data: dict):          

        handler = current_handler.get()
        dispatcher = Dispatcher.get_current()
        if handler:
            limit = getattr(handler, "throttling_rate_limit", self.rate_limit)
            key = getattr(handler, "throttling_key", f"{self.prefix}_{handler.__name__}")
        else:
            limit = self.rate_limit
            key = f"{self.prefix}_message"
        try:
            await dispatcher.throttle(key, rate=limit)
        except Throttled as t:
            await self.message_throttled(message, t)
            raise CancelHandler()

    async def message_throttled(self, message: types.Message, throttled: Throttled):

        handler = current_handler.get()

        dispatcher = Dispatcher.get_current()

        if handler:

            key = getattr(handler, 'throttling_key', f"{self.prefix}_{handler.__name__}")

        else:

            key = f"{self.prefix}_message"


        # Calculate how many time is left till the block ends

        delta = 1


        # Prevent flooding

        if throttled.exceeded_count <= 2:

            # await message.reply('Too many requests! ')
            pass


        # Sleep.

            await asyncio.sleep(delta)


        # Check lock status

        thr = await dispatcher.check_key(key)


        # If current message is not last with current key - do not send message

        if thr.exceeded_count == throttled.exceeded_count:

            # await message.reply('Unlocked.')
            pass