from aiogram import types
from config import bot, dp


@dp.message_handler(content_types=["text"])
async def echo_message(message: types.Message):

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

    # pin message
    if message.text.startswith('pin'):
        await bot.pin_chat_message(message.chat.id, message.message_id)
