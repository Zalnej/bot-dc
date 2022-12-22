from PIL import Image, ImageDraw, ImageFont

def cycat(text):

    font = ImageFont.truetype('arial.ttf', 32)
    image = Image.open('cytat.jpg')
    draw = ImageDraw.Draw(image)
    line_width = 800  # Maximum width of a line in pixels
    lines = []
    for line in text.split('\n'):
        line_words = line.split(' ')
        i = 0
        while i < len(line_words):
            # Try adding words to the line until it is full
            line_text = line_words[i]
            i += 1
            while i < len(line_words) and draw.textsize(line_text + ' ' + line_words[i], font=font)[0] < line_width:
                line_text += ' ' + line_words[i]
                i += 1
            lines.append(line_text)
            #print(line_text)
        # Calculate the position of the first line of text
        text_width, text_height = draw.textsize(lines[0], font=font)
        x = (image.width - text_width) / 2
        y = (image.height - text_height * len(lines)) / 2

        # Draw each line of text on the image
        for line in lines:
            draw.text((x, y), line, font=font, fill=(255, 0, 0))
            y += text_height
        font = ImageFont.truetype('arial.ttf', 45)
        draw.text((1100, 700), w, font=font, fill=(255, 0, 0))
        # Save the modified image to a different file
        image.save('cytat_p.jpg')

w='ja'
x='dlaczego to działaja japierodle kurrasdasd aswd qwr qwer qfr qsrf qwr qwr qwert qwert qwr qwr qw'
#cycat(x)
#with open('logi.txt', 'r', encoding='utf8', errors='ignore') as h:
#    h.write("Pierwsza linia\n")
#h.close()


# Append-adds at last
# append mode
