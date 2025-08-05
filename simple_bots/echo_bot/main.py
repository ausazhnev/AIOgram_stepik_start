from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN: str = ""  # Вставить свой токен

# Создание объекта Bot и Dispatcher
bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands="start"))
async def command_start(message: Message) -> None:
    await message.answer(
        text=(
            'Привет!\n'
            'Я Эхо-Бот, и буду отвечать тебе на все твои сообщения!'
        )
    )


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands="help"))
async def command_halp(message: Message) -> None:
    await message.answer(
        text=(
            "Ты пишешь мне сообщение.\n"
            "Я пишу тебе в ответ, тот же текст!"
        )
    )

# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def any_message(message: Message) -> None:
    await message.reply(
        text=(
            message.text
        )
    )

if __name__ == "__main__":
    dp.run_polling(bot)