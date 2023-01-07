import requests
from datetime import datetime
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN


def get_data():
    reg = requests.get('https://yobit.net/api/3/ticker/btc_usd')
    response = reg.json()
    sell_price = response['btc_usd']['sell']
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}")


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши что-нибудь")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши что-нибудь!")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


def summ(a, b):
    return a + b


if __name__ == '__main__':
    print(summ(2, 220))
    # get_data()
# executor.start_polling(dp)
