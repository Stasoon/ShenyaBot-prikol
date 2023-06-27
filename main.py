import random
import asyncio

from aiogram import Dispatcher, Bot, types, executor
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove

from keep_alive import keep_alive


TOKEN = "5980678332:AAEIdKBppGcuYqWiVpYYBa2JTFtfcrMfxjI"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

yes_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add('Да!')
heart_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add('❤')

symbols = ['💍', '🍄', '💄', '🍺', '🍫']

photos = [
    'AgACAgIAAxkBAAIBv2PUU0W1AXCL6wwFmpWN3-4epWvmAAKxwzEbEQOgSnD1PoTqUzp_AQADAgADcwADLQQ',
    'AgACAgIAAxkBAAIBwGPUU0X0Al9lIqi_pDROm4dT5RxQAAKywzEbEQOgSuXJcv_z0naWAQADAgADcwADLQQ',
    'AgACAgIAAxkBAAIBwWPUU0UiWUZRQu88bmEY1WSFUYKrAAKzwzEbEQOgSvIjeCzbDSLZAQADAgADcwADLQQ',
    'AgACAgIAAxkBAAIBwmPUU0WAMoAlinkGbRzyQIIQpz8iAAK0wzEbEQOgSp-G8E2WAAGuMAEAAwIAA3MAAy0E',
    'AgACAgIAAxkBAAIBw2PUU0VN5xHgrkLEt5AdiZUe1BQbAAK1wzEbEQOgShLtjVa2MWMZAQADAgADcwADLQQ',
    'AgACAgIAAxkBAAIBxGPUU0WSI1ENypMFrqCcPbVGy3IIAAKqwzEbEQOgSozXq5iMvgnZAQADAgADcwADLQQ',
    'AgACAgIAAxkBAAIBxWPUU0XX9Ezm27uOFx1QURVUMIgjAAKrwzEbEQOgSlLVlISQPmnBAQADAgADcwADLQQ',
    'AgACAgIAAxkBAAIBxmPUU0UKqVpxiPqxgf0WK7V2s_K5AAKswzEbEQOgSlmYn5jZTGZaAQADAgADcwADLQQ',
    'AgACAgIAAxkBAAIBx2PUU0UOWJ8_NDd7xjKreAbyqs6IAAKmwzEbEQOgSlPhwxwyDtdnAQADAgADcwADLQQ',
    'AgACAgIAAxkBAAIByGPUU0Wwp29Ul2olcFQokkK6_CPzAAKnwzEbEQOgShfAW8ouMlaeAQADAgADcwADLQQ',
    'AgACAgIAAxkBAAIByWPUU0lo5BLZqO0s8DcajUOvgH32AAKuwzEbEQOgSqLhCXrzlLoGAQADAgADcwADLQQ',
    'AgACAgIAAxkBAAIBymPUU0nugNrX5OWEyytV-Z9-5ejXAAKvwzEbEQOgSpqvJZpaEs1sAQADAgADcwADLQQ',
    'AgACAgIAAxkBAAIBy2PUU0kljeMWM3D9NcdmjcX4OvvsAAKXwzEbEQOgSsfNCPOY0ebvAQADAgADcwADLQQ',
    'AgACAgIAAxkBAAIBzGPUU0ny_sAUeWYsYdo7IEJefwRCAAKawzEbEQOgStpWDOpzuBd9AQADAgADcwADLQQ',
    'AgACAgIAAxkBAAIBzWPUU0kxNWzlCGkOtcbVOyA7rD6LAAKpwzEbEQOgSjpkDn-bYDIBAQADAgADcwADLQQ',
    'AgACAgIAAxkBAAIBzmPUU0kry8wnMEr1JL-bLhhK0HLwAAKdwzEbEQOgSp-jyoMWecoOAQADAgADcwADLQQ',
    'AgACAgIAAxkBAAIBz2PUU0nRU8BWemFBET-lT8edCx_TAAKfwzEbEQOgSllxsLJAwEJMAQADAgADcwADLQQ',
    'AgACAgIAAxkBAAIB0GPUU0mL7l2aJrh1Er9EeF4EAAHq-wACoMMxGxEDoEq94NHINmSIbAEAAwIAA3MAAy0E',
    'AgACAgIAAxkBAAIB0WPUU0kRHx5VxQABUX8BTCuWWXxD2wACjsMxGxEDoErCebekTOAvqAEAAwIAA3MAAy0E',
    'AgACAgIAAxkBAAIB0mPUU0lz4D_ghide_UDKIdQKAmJbAAKPwzEbEQOgSml7OXRbEpeaAQADAgADcwADLQQ',
    'AgACAgIAAxkBAAIB02PUU0sb8wkbRtpPf80zoC7COOydAAKRwzEbEQOgSjFj6xOFUEC7AQADAgADcwADLQQ',
    'AgACAgIAAxkBAAIB1GPUU0sWxobqxcQEuV7y3XBnGZZpAAKSwzEbEQOgSrtvWrmt8__YAQADAgADcwADLQQ',
    'AgACAgIAAxkBAAIB1WPUU0sZKh8IGhVUAZwFPMO-ltD9AAKUwzEbEQOgShdqQr54Y4AFAQADAgADcwADLQQ',
    'AgACAgIAAxkBAAIB1mPUU0tKzSjU_50BNX5mVYBJx-1QAAKWwzEbEQOgSuJQT_nvSYVDAQADAgADcwADLQQ',
    'AgACAgIAAxkBAAIB12PUU0sMt8ShanOo1lQ5xtrLL9eLAAKwwzEbEQOgSob59OV4ei8DAQADAgADcwADLQQ',

]


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.from_user.username == 'iamprianik':
        await message.reply("Привет, Таня!!! \nЭто Казино с щенками. Чтобы выиграть щенков, "
                            "ты должна пожертвовать мне одно сердечко.")
    else:
        await message.reply("Это Казино с щенками. Чтобы выиграть щенков, "
                            "ты должна пожертвовать мне одно сердечко.")
    await message.answer("Ты готова?", reply_markup=yes_kb)


@dp.message_handler(text='Да!')
async def yes_answer(message: types.Message):
    await message.answer('Тогда пожертвуй сердечко и казино запустится! \n\n' +
                         'P.S. Прости, что не дал тебе права выбора на прошлом шаге', reply_markup=heart_kb)


@dp.message_handler(text='❤')
async def kasino(message: types.Message):
    await message.answer('Барабанная дробь...', reply_markup=ReplyKeyboardRemove())
    baraban = await message.answer('💍  🍄  💄')
    symb1, symb2, symb3 = 0, 0, 0
    previous_result = ''

    for i in range(1, 10):
        symbols_count = len(symbols) - 1
        symb1 = symbols[random.randint(0, symbols_count)]
        symb2 = symbols[random.randint(0, symbols_count)]
        symb3 = symbols[random.randint(0, symbols_count)]
        if previous_result != f'{symb1}  {symb2}  {symb3}':
            await baraban.edit_text(text=f'{symb1}  {symb2}  {symb3}')
            await asyncio.sleep(0.12)
        previous_result = f'{symb1}  {symb2}  {symb3}'

    if symb1 == symb2 == symb3:
        await message.answer('Ура!!! Джекпот! Держи трёх щенков.')
        await bot.send_photo(message.from_id, photo=photos[random.randint(0, len(photos) - 1)], protect_content=True)
        await asyncio.sleep(0.12)
        await bot.send_photo(message.from_id, photo=photos[random.randint(0, len(photos) - 1)], protect_content=True)
        await asyncio.sleep(0.12)
        await bot.send_photo(message.from_id, photo=photos[random.randint(0, len(photos) - 1)], protect_content=True)
    elif symb1 == symb2 or symb1 == symb3 or symb2 == symb3:
        await message.answer('Ты выиграла! Но ты можешь получить джекпот... А, впрочем, держи одного щенка.')
        await bot.send_photo(message.from_id, photo=photos[random.randint(0, len(photos) - 1)], protect_content=True)
    else:
        await message.answer('Ты проиграла :( \nНо не расстраивайся, можешь попытаться ещё раз')
    await message.answer('Хочешь ещё раз попытать удачу?', reply_markup=heart_kb)


@dp.message_handler(content_types=['photo'])
async def load_photos(message: types.Message):
    print(f"'{message.photo[0].file_id}',")


if __name__ == "__main__":
    keep_alive()
    executor.start_polling(dp)
