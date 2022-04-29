from aiogram import types, Dispatcher
from config import bot, dp
import async
io
import aioschedul

#
# # def check_student_points(class_points, student_point):
# #     return True if (sum(class_points) // len(class_points)) < student_point else False
# #     # if student_point <= class_points.:
# #     #     print(False)
# #     # else:
# #     #     student_point > class_points
# #     #     print(True)
# #
# #
# # check_student_points(class_points=[12, 52, 32, 44, 86, 100], student_point=50)
# #
# # def Descending_Order(num):
# #     return int("".join(sorted(list(str(num)), reverse=True)))
# #
# #     # return True if int(num.sort) else False
# #
# # print(Descending_Order(5226265531123435998))
#
# import schedule
# import time
#
# def job():
#     print("I'm working...")
#
# # Run job every 3 second/minute/hour/day/week,
# # Starting 3 second/minute/hour/day/week from now
# schedule.every(3).seconds.do(job)
# schedule.every(3).minutes.do(job)
# schedule.every(3).hours.do(job)
# schedule.every(3).days.do(job)
# schedule.every(3).weeks.do(job)
#
# # Run job every minute at the 23rd second
# schedule.every().minute.at(":23").do(job)
#
# # Run job every hour at the 42rd minute
# schedule.every().hour.at(":42").do(job)
#
# # Run jobs every 5th hour, 20 minutes and 30 seconds in.
# # If current time is 02:00, first execution is at 06:20:30
# schedule.every(5).hours.at("20:30").do(job)
#
# # Run job every day at specific HH:MM and next HH:MM:SS
# schedule.every().day.at("10:30").do(job)
# schedule.every().day.at("10:30:42").do(job)
#
# # Run job on a specific day of the week
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)
#
# from schedule import every, repeat, run_pending
# import time
#
# @repeat(every(10).minutes)
# def job():
#     print("I am a scheduled job")
#
# while True:
#     run_pending()
#     time.sleep(1)
#

async def wake_up():
    await bot.send_message(chat_id=chat_id, text="Эржан вставай")


async def scheduler(time):
    aioschedule.every().minute.at(time).do(wake_up)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

if message.text.startswith("Hello"):
    await message.reply("ok")
        # await scheduler(message.text.replace("разбуди меня в", " "))