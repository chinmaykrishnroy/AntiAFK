from PIL import Image, ImageDraw

def create_icon(filename="icon"):
    size = (64, 64)
    bg_color = (0, 0, 0)
    circle_color = (255, 255, 255)

    img = Image.new("RGB", size, bg_color)
    draw = ImageDraw.Draw(img)
    draw.ellipse((16, 16, 48, 48), fill=circle_color)

    img.save(filename, format="ICO")

if __name__ == "__main__":
    create_icon()
    print("Icon saved as 'icon'")
