import telebot
from telebot import types
from getdf import coder, getDF, getRatingSt

token = '5077133016:AAFeAjz4GDOe_39siIkaenFULthrEQ07YLY'
bot = telebot.TeleBot(token)
answers = []

def req(l: list):
    result = coder(l)
    print(result)
    result = getDF(result)
    result = getRatingSt(result)
    return result

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_button = types.KeyboardButton("Старт")
    keyboard.add(start_button)
    
    bot.send_message(message.chat.id, '👋Привет! Нажми на кнопку "Старт", чтобы начать.', reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "Старт")
def handle_start_button(message):
    bot.send_message(message.chat.id, '🔮Я могу предсказать твой результат за этот семестр. ✍Ответь на вопросы. Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    # print(*l)
    try:
        age = int(message.text)
        if age < 7 or age > 25:
            bot.send_message(message.chat.id, 'Пожалуйста, введите возраст от 7 до 25 лет.')
            bot.register_next_step_handler(message, get_age)
        else:
            answers.append(age)
            bot.send_message(message.chat.id, f'Отлично! Тебе {age} лет. Дальше; какой у тебя пол? (введите "мужской" или "женский")')
            bot.register_next_step_handler(message, get_gender)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите корректный возраст (число).')
        bot.register_next_step_handler(message, get_age)

def get_gender(message):
    # print(*l)
    gender = message.text.lower() 
    if gender not in ['мужской', 'женский']:
        bot.send_message(message.chat.id, 'Пожалуйста, введите "мужской" или "женский".')
        bot.register_next_step_handler(message, get_gender)
    else:
        answers.append(gender)
        bot.send_message(message.chat.id, f'Хорошо! Ты указал, что твой пол: {gender}. Какой уровень образования у твоих родителей? (введите: Нет, Средняя школа, Колледж, Бакалавриат, Высшее)')
        bot.register_next_step_handler(message, get_parental_education)

def get_parental_education(message):
    # print(*l)
    get_parental_education = message.text.lower()
    valid_education = ['нет', 'средняя школа', 'немного колледжа', 'бакалавриат', 'высшее']
    if get_parental_education not in valid_education:
        bot.send_message(message.chat.id, 'Пожалуйста, введите корректный уровень образования.')
        bot.register_next_step_handler(message, get_parental_education)
    else:
        answers.append(get_parental_education)
        bot.send_message(message.chat.id, 'Отлично! Ты указал(а) уровень образования родителей. ⌛Сколько часов в неделю ты учишься? (введите от 0 до 40)')
        bot.register_next_step_handler(message, get_study_time)

def get_study_time(message):
    # print(*l)
    try:
        study_time = float(message.text)
        if study_time < 0 or study_time > 40:
            bot.send_message(message.chat.id, 'Пожалуйста, введите время обучения от 0 до 40 часов.')
            bot.register_next_step_handler(message, get_study_time)
        else:
            answers.append(study_time)
            bot.send_message(message.chat.id, f'Хорошо! Ты указал(а), что ты учишься {study_time} часов в неделю. Сколько пропусков у тебя было в этом году? (введите от 0 до 30)')
            bot.register_next_step_handler(message, get_skips)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите корректное количество часов (число).')
        bot.register_next_step_handler(message, get_study_time)

def get_skips(message):
    # print(*l)
    try:
        skips = int(message.text)
        if skips < 0 or skips > 30:
            bot.send_message(message.chat.id, 'Пожалуйста, введите количество пропусков от 0 до 30.')
            bot.register_next_step_handler(message, get_skips)
        else:
            answers.append(skips)
            bot.send_message(message.chat.id, f'Хорошо! Ты указал(а), что у тебя было {skips} пропуска(ов) в этом году. 👩‍🏫 Есть ли у тебя репетиторство? (введите "да" или "нет")')
            bot.register_next_step_handler(message, get_repetitorstvo)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите корректное количество пропусков (число).')
        bot.register_next_step_handler(message, get_skips)

def get_repetitorstvo(message):
    # print(*l)
    repetitorstvo = message.text.lower()
    if repetitorstvo not in ['да', 'нет']:
        bot.send_message(message.chat.id, 'Пожалуйста, введите "да" или "нет".')
        bot.register_next_step_handler(message, get_repetitorstvo)
    else:
        answers.append(repetitorstvo)
        bot.send_message(message.chat.id, f'Спасибо! Ты указал(а) своё репетиторство. 👨‍👩‍👧‍👦 Поддерживают ли тебя родители? (введите: низкая, умеренная, высокая, очень высокая.)')
        bot.register_next_step_handler(message, get_parental_support)

def get_parental_support(message):
    # print(*l)
    support = message.text.lower()
    if support not in ['низкая', 'умеренная', 'высокая', 'очень высокая']:
        bot.send_message(message.chat.id, 'Пожалуйста, введите корректный уровень поддержки родителей.')
        bot.register_next_step_handler(message, get_parental_support)
    else:
        answers.append(support)
        bot.send_message(message.chat.id, f'Спасибо! Ты указал(а) уровень поддержки родителей. Теперь введи средний балл твоих текущих оченок. Например 4.3')
        print(answers)
        bot.register_next_step_handler(message, get_gpa)

def get_gpa(message):
    try:
        gpa = float(message.text)
        if gpa < 0 or gpa > 5:
            bot.send_message(message.chat.id, 'Пожалуйста, введите число 0 до 5.')
            bot.register_next_step_handler(message, get_gpa)
        else:
            answers.append(gpa)
            bot.send_message(message.chat.id, f'Хорошо! Ты указал(а), что средний балл твоих оценок {gpa}')
            answer = req(answers)
            bot.send_message(message.chat.id, f'Отлично! Твоя оценка: {5-float(answer[0][0])}')
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите корректное количество пропусков (число).')
        bot.register_next_step_handler(message, get_gpa)

bot.polling()
#Запуск бота