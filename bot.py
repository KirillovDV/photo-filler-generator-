import telebot
from image_generator import ImageCreator
from config import TG_TOKEN
# Токен бота, полученный от BotFather
TOKEN = TG_TOKEN

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)


# Функция, которая будет вызываться при получении команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Этот бот может создать изображение с заданным разрешением и выводом разрешения в центре.")


# Функция, которая будет вызываться при получении команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, "Этот бот может создать изображение с заданным разрешением и выводом разрешения в центре. Чтобы создать изображение, введите команду /image <ширина> <высота>.")


# Функция, которая будет вызываться при получении команды /image <ширина> <высота>
@bot.message_handler(commands=['image'])
def create_image(message):
    try:
        # Получаем ширину и высоту из сообщения пользователя
        _, width, height = message.text.split()
        width = int(width)
        height = int(height)

        # Создаем изображение
        create = ImageCreator(width, height)
        img_file = create.save_image()

        # Отправляем изображение пользователю
        with open("img_file.png", 'rb') as f:
            bot.send_document(message.chat.id, f)

    except ValueError:
        bot.send_message(message.chat.id, "Неправильный формат команды. Используйте команду /image <ширина> <высота>.")
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {e}")


# Запускаем бота
