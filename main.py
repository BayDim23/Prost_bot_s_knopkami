import asyncio
from aiogram import Bot, Dispatcher, F , types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message,FSInputFile, CallbackQuery
from config import TOKEN
import logging
from email import message


from gtts import gTTS
import key as kb

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=TOKEN)
dp = Dispatcher()



@dp.message(CommandStart())
async def start(message: Message):
    await message.answer( f'Выбери опцию' , reply_markup= kb.inline_keyboard )

@dp.callback_query(F.data == 'hello')
async def hello(callback: CallbackQuery):
   await callback.message.answer(f'Привет!, {callback.from_user.first_name} !')

@dp.callback_query(F.data == 'bye')
async def bye(callback: CallbackQuery):
   await callback.message.answer(f'До свидания , {callback.from_user.first_name} !')



@dp.message(Command('links'))
async def links(message: Message):
   await message.answer(f'Обработка ссылок', reply_markup=kb.inline_keybo)



@dp.message(Command('dynamic'))
async def dynamic(message: Message):
    await message.answer( f'Выбери опцию' , reply_markup= kb.inline_key)

@dp.message(F.text == 'Опция 1')
async def dynamic(message: Message):
   await message.answer('Опция 1')

@dp.message(F.text == 'Опция 2')
async def dynamic(message: Message):
   await message.answer('Опция 2')



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":  # Исправлено имя
    asyncio.run(main())