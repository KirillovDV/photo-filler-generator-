import telebot
from PIL import Image, ImageDraw, ImageFont

# Токен бота, полученный от BotFather
TOKEN = 'your_bot_token_here'

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

        # Создание изображения с заданным разрешением и белым фоном
        img = Image.new('RGB', (width, height), color='#FFFFFF')

        # Создание объекта ImageDraw для рисования на изображении
        draw = ImageDraw.Draw(img)

        # Вывод разрешения в центре изображения
        text = f"{width}x{height}"
        font_size = int(min(width, height) * 0.1)
        font = ImageFont.truetype("SFProText-Regular.ttf", font_size)
        text_width, text_height = draw.textsize(text, font=font)
        text_x = (width - text_width) // 2
        text_y = (height - text_height) // 2
        draw.text((text_x, text_y), text, font=font, fill='#000000')

        # Сохранение изображения
        img_file = f'img_{width}x{height}.png'
        img.save(img_file)

        # Отправляем изображение пользователю
        with open(img_file, 'rb') as f:
            bot.send_photo(message.chat.id, f)

    except ValueError:
        bot.send_message(message.chat.id, "Неправильный формат команды. Используйте команду /image <ширина> <высота>.")
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {e}")


# Запускаем бота
bot.polling()
