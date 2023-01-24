from PIL import Image, ImageFont, ImageDraw
import os

class image_changer_class:
    def image_changer(day: int):
        
        UPPER = 500
        image_path = os.path.abspath(r'source_files/baseImgMemeNew.jpg')
        font_path = os.path.abspath(r'source_files/calibrib.ttf')

        base_image = Image.open(image_path)

        image_width, image_height = base_image.size
        image_center = (image_width/2, image_height/2)

        editable_image = ImageDraw.Draw(base_image)

        text_font = ImageFont.truetype(font_path, 70)
        main_text = 'dia {}'.format(day)

        text_measure = editable_image.textbbox((0, 0), main_text, text_font)
        text_offset = (text_measure[2]/2, text_measure[3]/2)

        text_position = (image_center[0]-text_offset[0], image_center[1]-text_offset[1]-UPPER)

        editable_image.text(text_position, main_text, (0, 0, 0), font=text_font)
        base_image.save('todays_image.jpg'.format(day))

if __name__ == '__main__':
    image_changer_class.image_changer(9999)