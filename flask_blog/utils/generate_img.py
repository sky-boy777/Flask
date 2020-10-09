from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random

def random_RGB():
    '''随机生成RGB'''
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def yzm():
    '''生成图片验证码'''
    s = 'qwertyuiop1234567890lkjhgfdsazxcvbnm'   # 26个单词跟0-9数字
    size = (120, 60)  # 图片大小
    yzm_img = Image.new('RGB', size, color=random_RGB())  # 生成画布，随机生成RGB颜色
    my_font = ImageFont.truetype('static/fonts/ARIALUNI.TTF', size=50)  # 添加字体文件，字体大小
    draw = ImageDraw.Draw(yzm_img)  # 创建画图对象

    code = ''  # 初始化验证码

    # 开始绘制
    for i in range(4):
        t = random.choice(s)  # 从s里面随机选取一个
        code += t  # 保存验证码，后面用来跟前端的比较
        # xy坐标,注意字体间隔                  字体        字体颜色
        draw.text(xy=(i*30, 0), text=t, font=my_font, fill=random_RGB())

    # 画干扰线
    for j in range(5):
        draw.line(xy=((5, random.randint(10, 55)), (115, random.randint(10, 50))), fill=random_RGB())
    # 添加滤镜
    yzm_img = yzm_img.filter(ImageFilter.DETAIL)
    return code, yzm_img

if __name__ == '__main__':
    code, yzm_img = yzm()
    # yzm_img.show()