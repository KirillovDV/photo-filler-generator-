from PIL import Image, ImageDraw, ImageFont

class ImageCreator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.img = Image.new('RGB', (width, height), color='#FFFFFF')
        self.draw = ImageDraw.Draw(self.img)

    def add_text(self):
        text = f"{self.width}x{self.height}"
        font_size = int(min(self.width, self.height) * 0.1)
        font = ImageFont.truetype("SFProText-Regular.ttf", font_size)
        text_width, text_height = self.draw.textsize(text, font=font)
        text_x = (self.width - text_width) // 2
        text_y = (self.height - text_height) // 2
        self.draw.text((text_x, text_y), text, font=font, fill='#000000')

    def save_image(self):
        self.add_text()
        self.img.save(f'img_{self.width}x{self.height}.png')


width = int(input("Введите ширину изображения: "))
height = int(input("Введите высоту изображения: "))

creator = ImageCreator(width, height)
creator.save_image()