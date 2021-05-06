import os

import requests
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
import KeyBoards
#
#
from MishaAPI import URLhandler, URLSchedule

load_dotenv()
bot = Bot(token=os.getenv('APIBOT'))
dp = Dispatcher(bot)
r = os.getenv('FIRASS')
url = URLhandler()
urls = URLSchedule()


@dp.message_handler(commands=['start'])
async def send_welcome(message):
    await message.answer("Приветствую тебя! Я знаю какое сегодня расписание, все данные по предметам и список преподавателей", reply_markup=KeyBoards.greet_kb)


@dp.message_handler(commands=['help'])
async def send_help(message):
    await message.answer("Бот с расписанием, данными по предметам, информацией по преподавателям\
    .\r\nСписок команд:\r\n1) /Кейс технологии\r\n2) /Алгоритмы\r\n3) /БЖД\r\n4) /Информационная \
    безопасность\r\n5) /Машинное обучение\r\n6) /Сетевые технологии\r\n7) /Физическая культура\r\n8)\
     /Экономика \r\n9) /Преподаватели \r\n10) /Расписание\r\n11) /Очередь")


@dp.message_handler(regexp=r'Кейс[\s_]+технологии')
async def send_case(message):
    await message.answer(requests.get(url.subjects()).json()[0].get('title'))
    await message.answer(requests.get(url.subjects()).json()[0].get('description'))


@dp.message_handler(regexp='Алгоритмы')
async def send_alg(message):
    await message.answer(requests.get(url.subjects()).json()[1].get('title'))
    await message.answer(requests.get(url.subjects()).json()[1].get('description'))


@dp.message_handler(regexp='БЖД')
async def send_bgd(message):
    await message.answer(requests.get(url.subjects()).json()[2].get('title'))
    await message.answer(requests.get(url.subjects()).json()[2].get('description'))


@dp.message_handler(regexp='ОИБ')
async def send_oib(message):
    await message.answer(requests.get(url.subjects()).json()[3].get('title'))
    await message.answer(requests.get(url.subjects()).json()[3].get('description'))


@dp.message_handler(regexp=r'Машинное[\s_]+обучение')
async def send_ml(message):
    await message.answer(requests.get(url.subjects()).json()[4].get('title'))
    await message.answer(requests.get(url.subjects()).json()[4].get('description'))


@dp.message_handler(regexp=r'Сетевые[\s_]+технологии')
async def send_st(message):
    await message.answer(requests.get(url.subjects()).json()[5].get('title'))
    await message.answer(requests.get(url.subjects()).json()[5].get('description'))


@dp.message_handler(regexp='Физ-ра')
async def send_fiz(message):
    await message.answer(requests.get(url.subjects()).json()[6].get('title'))
    await message.answer(requests.get(url.subjects()).json()[6].get('description'))


@dp.message_handler(regexp='Экономика')
async def send_eco(message):
    await message.answer(requests.get(url.subjects()).json()[7].get('title'))
    await message.answer(requests.get(url.subjects()).json()[7].get('description'))


@dp.message_handler(regexp='Очередь')
async def send_eco(message):
    await message.answer("Ссылка на сайт с записью в очередь: https://sdayu-labu.gnkdev.space/")


@dp.message_handler(regexp='Преподаватели')
async def send_teachers(message):
    infomation = requests.get(url.teachers()).json()
    teachers = ''
    for i in range(len(infomation)):
        teachers += infomation[i].get('lastName') + '\r\n'
        teachers += infomation[i].get('firstName') + '\r\n'
        teachers += infomation[i].get('patronymyc') + '\r\n'
        teachers += infomation[i].get('email') + '\r\n'
        if infomation[i].get('phoneNumber') == "Не предоставлен":
            teachers += "\r\n"

        else:
            teachers += infomation[i].get('phoneNumber')
            teachers += "\r\n\r\n"
    await message.answer(teachers)


@dp.message_handler(regexp='Расписание')
async def send_schedule(message):
    schedule = ''
    infomation = requests.get(urls.schedule()).json()
    n = 1
    for i in range(len(infomation)):
        if infomation[i].get('date') == urls.date():
            schedule += str(n) + '. ' + infomation[i].get('discipline') + '\r\n'
            schedule += 'Аудитория: ' + infomation[i].get('auditorium') + '\r\n'
            schedule += 'Тип занятия: ' + infomation[i].get('kindOfWork') + '\r\n'
            schedule += 'Продолжительность: ' + infomation[i].get('beginLesson') + '-' + \
                        requests.get(urls.schedule()).json()[i].get('endLesson') + '\r\n'
            schedule += 'Преподаватель: ' + infomation[i].get('lecturer') + '\r\n'
            if infomation[i].get('subGroup') is None:
                schedule += '\r\n\r\n'
            else:
                schedule += 'Подгруппа: ' + infomation[i].get('subGroup') + '\r\n\r\n'
            n += 1
        else:
            continue
    if schedule == '':
        schedule = 'Сегодня нет пар'
        await message.answer(schedule)
    else:
        await message.answer(schedule)


@dp.message_handler()
async def echo_all(message):
    await message.reply(message.text)


executor.start_polling(dp, skip_updates=True)
