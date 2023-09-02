from PIL import Image,ImageFont,ImageDraw
import os
def get_concat_h(imgs):
    images = []
    font = ImageFont.truetype("arial.ttf",size=35)
    for i in imgs:
        img = Image.open('downloads/images/'+i)
        img.thumbnail((300,200))
        draw = ImageDraw.Draw(img)
        draw.text((10, 10),i.split('.')[1],font=font,fill='black')
        images.append(img)

    dst = Image.new('RGB',(600,600))
    dst.paste(images[0],(0, 0))
    dst.paste(images[1],(0, 200))
    dst.paste(images[2],(0, 400))
    dst.paste(images[3],(300, 0))
    dst.paste(images[4],(300, 200))
    dst.paste(images[5],(300, 400))
    img_name = 'downloads/gr_images/gr.'
    for i in imgs:
        img_name += i.split('.')[1]+'_'
    img_name=img_name+'.jpg'
    dst.save(img_name)
    return img_name

def get_gr_photo(keys):
    images = []
    gr_photo_name = ''
    for k in keys:
        gr_photo_name += f'{k}_'
    if f'gr.{gr_photo_name}.jpg' in os.listdir('downloads/gr_images'):
        return f'downloads/gr_images/gr.{gr_photo_name}.jpg'
    print('topilmadi..')
    for file in os.listdir('downloads/images'):
        if int(file.split('.')[1]) in keys:
            images.append(file)
    return get_concat_h(images)


