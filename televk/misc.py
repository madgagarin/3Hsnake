import logging
from aiogram import Bot as tBot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from vkbottle.bot import Bot as vBot

# Инициализация бота и диспетчера
t_bot = tBot(token='1996982451:AAEirWtwvFxVst1GDLn94gQ6h1Hjx4KzrYc')
dp = Dispatcher(t_bot, storage=MemoryStorage())

tg_group_id = -1001225817597


vk_bot_user = vBot(token='1304db8531031d28225d6b470b6b5258ce69a65fdd5b7ed32c6b4a29e200e01df803a502c544b9d08cfda')
vk_bot_group = vBot(token='4c5520a9f6e616d76909d4bd6a69d2359d3a78ce39faa45252f5856b42a31108025fbd6176f243ee13248')
vk_group_id = -206983113
