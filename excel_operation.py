# -*- coding:utf-8 -*-
import xlwt
import xlsxwriter
from PIL import Image
from xlsxwriter import Workbook


def read(file):
    pass

'''
插入图片 xlwt 只支持bmp格式
'''
def write_xlwt():
    workbook = xlwt.Workbook(encoding='utf-8')
    style = xlwt.XFStyle()
    font_yahei = xlwt.Font()

    font_yahei.name = '微软雅黑'
    font_yahei.bold = True
    style.font = font_yahei

    sheet_10 = workbook.add_sheet('十月账单')
    #行、列、值、样式
    sheet_10.write(0, 0, '十月账单', style)

    # 将gif转为bmp进行存储
    # img = Image.open("Big.gif").convert('RGB').save('big.bmp')
    # sheet_10.insert_bitmap('big.bmp', 3, 3)

    # 将png转为bmp进行存储
    Image.open('zhihu.png').convert('RGB').save('zhihu.bmp')
    sheet_10.insert_bitmap('zhihu.bmp', 4, 4)

    # 将jpeg转为bmp进程存储
    Image.open('banma.jpeg').convert('RGB').save('banma.bmp')
    sheet_10.insert_bitmap('banma.bmp', 7, 30)


    sheet_11 = workbook.add_sheet('十一月账单')
    sheet_11.write(0, 0, '十一月账单')


    workbook.save('账单.xls')

def write_xlslwriter():
    workbook = Workbook('images.xlsx')
    worksheet = workbook.add_worksheet('sht_01')
    worksheet.write('A2', 'Insert an image in a cell:')
    worksheet.insert_image('B2', 'captcha.jpg')
    workbook.close()

if __name__ == '__main__':
    write_xlwt()

