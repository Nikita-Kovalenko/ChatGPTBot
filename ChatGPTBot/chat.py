import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = '6129431252:AAH8J_oesmNgRKk3j0ZwW0tS4CNdmPlu_Bk'

openai.api_key = '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'

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler()
async def send(message: types.Message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.9,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,    
        presence_penalty=0.6,
        stop=["You:"]
    )
    
    await message.answer(response['choices'][0]['text'])

executor.start_polling(dp, skip_updates=True)




