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

ATTEMPTS: int = 5
STAR_WORDS: list[str] = ['да', 'давай', 'сыграем', 'игра', 'играть', 'хочу играть']


def get_random_num() -> int:
    return random.randint(1, 100)


BOT_TOKEN: str = '6141970881:AAH4JCKHk9lbpTYGg9t6lPaH45IShtidXY8'  # Указать токен.

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


async def command_rules(message: Message) -> None:
    await bot.send_message(
        chat_id=message.chat.id,
        text=(
            'Правила игры:\n\nЯ загадываю число от 1 до 100, '
            f'а вам нужно его угадать\nУ вас есть {ATTEMPTS} '
            'попыток\n\nДоступные команды:\n/rules - правила '
            'игры и список команд\n/cancel - выйти из игры\n'
            '/stat - посмотреть статистику\n\nДавай сыграем?\n'
            'Что бы начать играть просто напиши что согласен или хочешь сыграть :)'
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
                  " - Что бы прочитать правила, команда /rules\n"
                  " - Хочешь начать новую игру?"
                  )
        )


async def send_stat(message: Message) -> None:
    await bot.send_message(
        chat_id=message.chat.id,
        text=(
            "Твоя статистика:\n"
            f"Сыграно игр: {user['total_games']}\n"
            f"Победил: {user['wins']}"
        )
    )


async def command_cancel(message: Message) -> None:
    if user['in_game']:
        user['in_game'] = False
        await bot.send_message(
            chat_id=message.chat.id,
            text=(
                'Вы вышли из игры. Если захотите сыграть '
                'снова - напишите об этом'
            )
        )
    else:
        await bot.send_message(
            chat_id=message.chat.id,
            text=(
                'Ты сейчас не в игре\n'
                'Начнем новую игру?'
            )
        )


async def start_new_game(message: Message) -> None:
    if not user['in_game']:
        user['in_game'] = True
        user['secret_number'] = get_random_num()
        user['attempts'] = ATTEMPTS
        user['total_games'] += 1
        await bot.send_message(
            chat_id=message.chat.id,
            text=(
                'Ура!\n\nЯ загадал число от 1 до 100, '
                'попробуй угадать!'
            )
        )
    else:
        await bot.send_message(
            chat_id=message.chat.id,
            text=(
                'Пока мы играем в игру я могу '
                'реагировать только на числа от 1 до 100 '
                'и команды /cancel и /stat'
            )
        )


async def is_number(message: Message) -> None:
    send_text: str = ('Мы сейчас не играем\n'
                      'Давай сыграем?')
    if user['in_game']:
        user['attempts'] -= 1
        user_num = int(message.text)
        if user['secret_number'] == user_num:
            send_text = ('Ура!!! Вы угадали число!\n\n'
                         'Может, сыграем еще?')
            user['in_game'] = False
            user['wins'] += 1
        elif user['attempts'] == 0:
            user['in_game'] = False
            send_text = ('К сожалению, у вас больше не осталось '
                         'попыток. Вы проиграли :(\n\nМое число '
                         f'было {user["secret_number"]}\n\nДавайте '
                         'сыграем еще?')
        elif user_num > user['secret_number']:
            send_text = 'Мое число меньше'
        elif user_num < user['secret_number']:
            send_text = 'Мое число больше'
    await bot.send_message(
        chat_id=message.chat.id,
        text=send_text
    )


dp.message.register(command_start, CommandStart())
dp.message.register(send_stat, Command(commands='stat'))
dp.message.register(command_rules, Command(commands='rules'))
dp.message.register(command_cancel, Command(commands='cancel'))
dp.message.register(start_new_game, F.text.lower().in_(STAR_WORDS))
dp.message.register(is_number, lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
dp.message.register(other_message)

if __name__ == "__main__":
    print("Бот запущен.")
    dp.run_polling(bot)
