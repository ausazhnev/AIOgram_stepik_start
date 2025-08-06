import random
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

user = {'in_game': False,
        'secret_number': None,
        'attempts': None,
        'total_games': 0,
        'wins': 0
        }


def get_random_num() -> int:
    return random.randint(1, 100)


BOT_TOKEN: str = ''  # Указать токен.

bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()


async def command_start(message: Message) -> None:
    await bot.send_message(
        chat_id=message.chat.id,
        text=(
            "Добро пожаловать!\n"
            "Я готов играть с тобой в игру - \"Угадай число\"\n"
            "Что бы узнать правила, используй команду /rules\n"
            "Хочешь начать игру?"
        )
    )


async def other_message(message: Message) -> None:
    if user['in_game']:
        await bot.send_message(
            chat_id=message.chat.id,
            text=(
                "Ты в игре, можешь прислать мне\n"
                " - свое число\n"
                " - команду: /cancel что бы завершить текущую игру, но тогда ты проиграешь!"
            )
        )
    else:
        await bot.send_message(
            chat_id=message.chat.id,
            text=("я не понимаю твое сообщение, ты можешь:\n"
                  " - Получить статистику, команда /stat\n"
                  " - Что бы начать новую игру, команда /game\n"
                  " - Хочешь начать новую игру?"
                  )
        )


async def send_stat(message: Message) -> None:
    await bot.send_message(
        chat_id=
    )


dp.message.register(command_start, CommandStart)
dp.message.register(send_stat, Command(commands='stat'))
dp.message.register(other_message)

if __name__ == "__main__":
    print("Бот запущен.")
    dp.run_polling(bot)
