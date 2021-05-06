from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnCase = KeyboardButton("/Кейс_технологии")
btnAlg = KeyboardButton("/Алгоритмы")
btnBgd = KeyboardButton("/БЖД")
btnOib = KeyboardButton("/ОИБ")
btnMl = KeyboardButton("/Машинное_обучение")
btnSt = KeyboardButton("/Сетевые_технологии")
btnFr = KeyboardButton("/Физ-ра")
btnEc = KeyboardButton("/Экономика")
btnTeachers = KeyboardButton("/Преподаватели")
btnSchedule = KeyboardButton("/Расписание")
btnQueue = KeyboardButton("/Очередь")

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(btnSchedule, btnAlg).add(btnBgd, btnMl).add(btnCase, btnSt).add(btnFr, btnEc,
                                                                                    btnOib, btnTeachers, btnQueue)
