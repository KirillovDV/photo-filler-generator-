from PIL import Image, ImageDraw, ImageFont

# Получение разрешения изображения от пользователя
width = int(input("Введите ширину изображения: "))
height = int(input("Введите высоту изображения: "))

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
img.save(f'img_{width}x{height}.png')
