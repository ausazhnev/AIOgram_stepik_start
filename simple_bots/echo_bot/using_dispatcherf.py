from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

BOT_TOKEN: str = ""  # указать токен своего бота

bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()


async def command_start(message: Message) -> None:
    await message.answer(
        text=(
            "Добро пожаловать в Эхо-бот!\n"
            "Пора начать общение."
        )
    )


async def command_help(message: Message) -> None:
    await message.answer(
        text=(
            "Напиши боту сообщение и получи ответ\n"
            "Попробуй переболтать бота )"
        )
    )


async def any_message(message: Message) -> None:
    await message.reply(
        text=(
            message.text
        )
    )


dp.message.register(command_start, Command(commands="start"))
dp.message.register(command_help, Command(commands="help"))
dp.message.register(any_message)

if __name__ == "__main__":
    print('Бот запущен.')
    dp.run_polling(bot)
