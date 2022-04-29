from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import cancel_markup
from config import bot

# states
class FSMAdmin(StatesGroup):
    photoOfTheDish = State()
    name = State()
    descriptionofthedish = State()
    price = State()

async def fsm_start(message: types.Message):
    await FSMAdmin.photoOfTheDish.set()
    await bot.send_message(message.chat.id,
                           f"Привет {message.from_user.full_name}, скинь фотко еды",
                           reply_markup=cancel_markup)

async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photoOfTheDish'] = message.photo[0].file_id
    await FSMAdmin.next()
    await bot.send_message(message.chat.id, "Название еды?")

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await bot.send_message(message.chat.id, "Описание блюда?")

async def load_descriptionofthedish(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['descriptionofthedish'] = int(message.text)
        await bot.send_message(message.chat.id, "Я сказал только числа!!!")


# async def load_(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['region'] = message.text
#     async with state.proxy() as data:
#         await bot.send_message(message.chat.id, str(data))
#     await state.finish()
#     await bot.send_message(message.chat.id, "Все свободен)")

async def cancal_price(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    else:
        await state.finish()
        await message.reply("ОК")

def register_hendler_fsmAdminGetUser(dp: Dispatcher):
    dp.register_message_handler(cancal_price, state="*", commands="cancel")
    dp.register_message_handler(cancal_price, Text(equals='cancel', ignore_case=True),state="*")

    dp.register_message_handler(fsm_start, commands=["menu"])
    dp.register_message_handler(load_photo, state=FSMAdmin.photoOfTheDish, content_types=["photo"])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_descriptionofthedish, state=FSMAdmin.descriptionofthedish)
    # dp.register_message_handler(load_price, state=FSMAdmin.price)
