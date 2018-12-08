# -*- coding: utf-8 -*-
'''
12306 captcha recognize
@wuji
test by: Python 3.6, Tensorflow 1.7.1

需要准备的数据有三类（共7个文件），全部放在./model_data目录下
1、模型类别映射文件，模型预测出来的是类别编号（训练时设定），用于还原模型原类别信息
2、ocr模型，用于识别验证码需要识别的关键字，共3个文件分别是 xxx.data-00000-of-00001, xxx.meta, xxx.index
3、验证码物体模型，用于识别验证码需要识别的物体，共3个文件分别是 yyy.data-00000-of-00001, yyy.meta, yyy.index
'''
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '3' # 指定GPU（如果有需要）
import numpy as np
from server_model import CaptchaModel
from time import time as tc

# 读取类别编号映射类别文件，将模型识别出来的编号还原为类别
def read_classes(classes_file):
    with open(classes_file) as fp:
        classes = [ c.strip() for c in fp.readlines()]
    return np.array(classes)

# 模型加载数据路径
ocr_model_meta = './model_data/ocr.ckpt-1108000.meta'
ocr_model_para = './model_data/ocr.ckpt-1108000' # 需要注意, 模型参数文件后缀 ".data-00000-of-00001" 不需要写入路径

cap_model_meta = './model_data/densenet_121.ckpt-145000.meta'
cap_model_para = './model_data/densenet_121.ckpt-145000'

classes_path = './model_data/12306_classes.txt'
classes = read_classes(classes_path)

# 加载模型
model = CaptchaModel(ocr_model_meta=ocr_model_meta,
                     ocr_model_para=ocr_model_para,
                     cap_model_meta=cap_model_meta,
                     cap_model_para=cap_model_para)

# ============ 调用示例 ============
# 建议加上日志系统，把识别的图片、识别结果保存， 方便后面问题的排查以及对验证码产生的规律进行统计分析


def crack_captcha(captcha_img):

    tic = tc()
    print("模型加载完毕")
    word_ind, objs_ind = model.predict(captcha_img)
    word = classes[word_ind]
    objs = classes[objs_ind]
    print(unicode(word[0], "utf-8"), objs[0])

    print('time elapsed:{:.2f}'.format(tc()-tic))
    return word[0]
    # model.close() # 程序结束时把模型关闭




