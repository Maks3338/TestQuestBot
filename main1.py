from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
API_TOKEN: str = '5832385892:AAH8eD2FICY0fB0lhnNAnj4zoD9bHNzHgk8'
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher(bot)
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup()
button_1: KeyboardButton = KeyboardButton('Собак 🦮')
button_2: KeyboardButton = KeyboardButton('Огурцов 🥒')
button_3: KeyboardButton = KeyboardButton('Бананов ')
button_4: KeyboardButton = KeyboardButton('Людей')
button_5: KeyboardButton = KeyboardButton('Машин')
keyboard.add(button_1, button_2,button_3,button_4,button_5)
async def process_start_command(message: types.Message):
    await message.answer('Чего кошки боятся больше?', reply_markup=keyboard)
async def process_dog_answer(message: types.Message):
    await message.answer('Да, несомненно, кошки боятся собак. Но вы видели как они боятся огурцов?', reply_markup=ReplyKeyboardRemove())
async def process_cucumber_answer(message: types.Message):
    await message.answer('Да, иногда кажется, что огурцов кошки боятся больше', reply_markup=ReplyKeyboardRemove())
async def process_banana_answer(message: types.Message):
    await message.answer('Нет,кошки вообще не боятся бананов. Но вы видели как они боятся огурцов?', reply_markup=ReplyKeyboardRemove())
async def process_people_answer(message: types.Message):
    await message.answer('Да, хотя смотря какой человек. Но вы видели как они боятся огурцов?', reply_markup=ReplyKeyboardRemove())
async def process_cars_answer(message: types.Message):
    await message.answer('Да, но очень слабо. Но вы видели как они боятся огурцов?', reply_markup=ReplyKeyboardRemove())
dp.register_message_handler(process_start_command, commands='start')
dp.register_message_handler(process_dog_answer, text='Собак 🦮')
dp.register_message_handler(process_cucumber_answer, text='Огурцов 🥒')
dp.register_message_handler(process_banana_answer, text='Бананов ')
dp.register_message_handler(process_people_answer, text='Людей')
dp.register_message_handler(process_cars_answer, text='Машин')
if __name__ == '__main1__':
    executor.start_polling(dp, skip_updates=True)
