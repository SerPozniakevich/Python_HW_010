from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import requests
from datetime import datetime

API_TOKEN = 'Token'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Напишите город, в котором желаете узнать погоду')


@dp.message_handler()
async def get_weather(message: types.Message):

    try:
        r = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid=4321a3d417b53045aa1b6617c529c910&units=metric&lang=ru")
        data = r.json()
        # print(data)

        city = data["name"]
        cur_weather = data['main']['temp']
        wind = data['wind']['speed']
        des = data['weather']
        des_dict = des[0]
        des_pr = des_dict['description']
        await message.reply(f'Сейчас: {datetime.now().strftime("%d.%m.%Y. %H:%M")} (+4 MCK)\n\
 в городе: {city}  {des_pr}\n  температура: {cur_weather} {chr(176)}C\n   скорость ветра: {wind} м/с')

    except:
        await message.reply('Проверьте название города')


if __name__ == '__main__':

    print('Бот включён')
    executor.start_polling(dp, skip_updates=True) # пропуск команд отправленных до старта бота
    print('Бот выключен')