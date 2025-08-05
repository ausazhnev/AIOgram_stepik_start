from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

BOT_TOKEN: str = '' # Вписать токен бота

bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()


@dp.message(Command(commands='start'))
async def command_start(message: Message)-> None:
    await message.answer(
        text=(
            """Добро пожаловать в эхо-бот.
            Пора начать общаться!"""
        )
    )


@dp.message(Command(commands='help'))
async def command_help(message: Message) -> None:
    await message.answer(
        text=(
            """Напиши мне сообщение.
            А я буду тебе отвечать."""
        )
    )


@dp.message()
async def echo_message(message: Message) -> None:
    try:
        await message.send_copy(
            chat_id=message.chat.id
        )
    except TypeError:
        await message.reply(
            text=(
                """Не известный апдейт"""
            )
        )

if __name__ == "__main__":
    print('Бот запущен.')
    dp.run_polling(bot)
