from PIL import Image, ImageDraw, ImageFont


class ImgPrinter():
    def print_list(self, list_to_print=[], output_path='sys_cli_out.jpg', width=450, height=150, color='orange'):
        image = Image.new("RGB", (width, height), color)
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()
        for idx, value in enumerate(list_to_print):
            draw.text((10, idx*20 + 10), value, font=font)
        image.save(output_path)
