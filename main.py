from aiogram import executor
from config import dp
import logging
from handlers import callback, client, notification, fsmAdminGetUser, inline
from database import bot_db


async def on_start_up(_):
    bot_db.sql_create()


client.register_hendlers_client(dp)
callback.register_hendlers_callback(dp)
inline.register_handler_inline(dp)
fsmAdminGetUser.register_hendler_fsmAdminGetUser(dp)

notification.register_hendlers_notification(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False, on_startup=on_start_up)


# from aiogram import executor
# from config import dp
# import logging
# from handlers import callback, client, notification, fsmAdminGetUser, fsmAdminMenu, inline
# from database import bot_db
#
#
# async def on_start_up(_):
#     bot_db.sql_create()
#
# client.register_hendlers_client(dp)
# callback.register_hendlers_callback(dp)
# inline.register_handler_inline(dp)
#
# fsmAdminGetUser.register_hendler_fsmAdminGetUser(dp)
# fsmAdminMenu.register_hendler_fsmAdminGetUser(dp)
#
# notification.register_hendlers_notification(dp)
#
# if __name__ == '__main__':
#     logging.basicConfig(level=logging.INFO)
#     executor.start_polling(dp, skip_updates=False)