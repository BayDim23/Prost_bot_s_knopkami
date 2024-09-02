from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder





main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Показать больше')],
], resize_keyboard=True)




inline_keybo = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Новости", url='https://lenta.ru/')],
   [InlineKeyboardButton(text="Музыка", url='https://vk.com/audio-2001428143_123428143')],
   [InlineKeyboardButton(text="Видео", url='https://vk.com/video-192002772_456245654')]
])

inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Привет', callback_data='hello')],
    [InlineKeyboardButton(text='Пока', callback_data='bye')]
    ])


inline_key = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Опция 1', callback_data='Опция 1')],
    [InlineKeyboardButton(text='Опция 2', callback_data='Опция 2')]
    ])