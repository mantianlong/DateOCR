# coding: utf-8
# 格式2023.01.02  James_Fajardo
import os
import cv2
import numpy as np
from PIL import Image, ImageFont
from glob import glob
from handright import Template, handwrite
import random


def generate_date():
    year_list = ['2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2028', '2029', '2030', '2031',
                 '2032']
    year = random.sample(year_list, 1)[0]
    month_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '01', '02', '03', '04', '05', '06',
                  '07', '08', '09']
    month = random.sample(month_list, 1)[0]
    day_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '01', '02', '03', '04', '05', '06',
                '07', '08', '09', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                '27', '28', '29', '30', '31']
    day = random.sample(day_list, 1)[0]
    if month.startswith('0') and len(day) == 1:
        day = '0' + day
    date_ch, date_en = year + '年' + month + '月' + day + '日', year + '.' + month + '.' + day + '.'
    return date_ch, date_en


if __name__ == '__main__':
    ttf_files = glob('./font_rh/*/*.ttf')
    nums = 400
    for i in range(nums):
        print('start generate {}.'.format(i))
        for ttf in ttf_files:
            text_ch, text_en = generate_date()
            template_ch = Template(
                background=Image.new(mode="1", size=(676, 106), color=1),
                font=ImageFont.truetype(
                    ttf,
                    size=100),
                perturb_x_sigma=0.3,
                perturb_y_sigma=0.4,
                perturb_theta_sigma=0.3,
            )
            images_ch = handwrite(text_ch, template_ch)
            for im_ch in images_ch:
                assert isinstance(im_ch, Image.Image)
                #im.show()
                out_file_ch = os.path.join(r'dataset_01',
                                           text_ch +'.jpg')
                im_ch.save(out_file_ch)

            # en
            template_en = Template(
                background=Image.new(mode="1", size=(552, 106), color=1),
                font=ImageFont.truetype(
                    ttf,
                    size=100),
                perturb_x_sigma=0.3,
                perturb_y_sigma=0.4,
                perturb_theta_sigma=0.3,
            )
            images_en = handwrite(text_en, template_en)
            for im_en in images_en:
                assert isinstance(im_en, Image.Image)
                # im.show()
                out_file_en = os.path.join(r'dataset_01',
                                           text_en +'.jpg')
                im_en.save(out_file_en)
        print('finish generate {}.'.format(i))