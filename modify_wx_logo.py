#!/usr/bin/env python
# -*- coding: utf-8 -*-


from PIL import Image, ImageDraw, ImageFont

# 创建图片对象
headImage = Image.open(r"D:\\123.webp")

# 获取图片对象的宽高
w, h = headImage.size

# 创建字体对象
font = ImageFont.truetype(r'D:\\PYthonProject\\msyh.ttc', int(h / 4))

# 绘制圆形
ImageDraw.Draw(headImage).pieslice(
    [(w / 3 * 2, 0), (w, h / 3)], 0, 360, fill='red')
ImageDraw.Draw(headImage).text(
    (w * 0.76, h * 0.02), '3', font=font, fill='white')

# 展示绘制结果(使用系统默认的图片浏览器)
headImage.show()

# 保存绘制结果
headImage.save('D:/wode.jpg')
