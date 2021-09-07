from asyncio import run_coroutine_threadsafe, get_event_loop
from aiogram import executor, types
from aiogram.types import ChatType

from misc import dp, t_bot, vk_bot_group, vk_bot_user, tg_group_id, vk_group_id
from vkbottle import GroupEventType, GroupTypes


@vk_bot_group.on.raw_event(GroupEventType.WALL_POST_NEW, dataclass=GroupTypes.WallPostNew)
async def group_join_handler(event: GroupTypes.WallPostNew):
    if event.object.from_id != vk_group_id:
        await t_bot.send_message(tg_group_id, event.object.text)


@dp.message_handler(chat_type=ChatType.SUPERGROUP)
async def channel_post(message: types.Message):
    await vk_bot_user.api.wall.post(owner_id=vk_group_id, from_group=1, message=message.text)


if __name__ == "__main__":
    run_coroutine_threadsafe(vk_bot_group.run_polling(), get_event_loop())
    executor.start_polling(dp, skip_updates=True)
