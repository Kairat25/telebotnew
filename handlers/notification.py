from aiogram import types, Dispatcher
from config import bot, dp
import asyncio
import aioschedule




async def wake_up():
    await bot.send_message(chat_id=chat_id, text="Эржан вставай")

async def scheduler(time):
    aioschedule.every().day.do(wake_up)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)



# @dp.message_handler()
async def echo_message(message: types.Message):
    global chat_id
    chat_id=message.chat.id

    # Check bad words
    bad_words = "java bitch дурак балбес эшек".split()

    for i in bad_words:
        if i in message.text.lower():
            await message.delete()
            await bot.send_message(message.chat.id,
                           f"{message.from_user.full_name}, сам ты {i}!!!"
                           )

    # Send dice
    if message.text.lower() == 'dice':
        await bot.send_dice(message.chat.id, emoji="🎯")
    # notification
    if message.text.startswith("разбуди меня в"):
        await message.reply("ok")
        await scheduler(message.text.replace("разбуди меня в", " "))
    # pin message
    # if message.text.startswith('pin'):
    #     await bot.send_sticker(message.chat.id, message.message_id)


def register_hendlers_notification(dp: Dispatcher):
    dp.register_message_handler(echo_message)