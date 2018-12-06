
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import numpy as np
from server_model import CaptchaModel

def read_classes(classes_file):
    with open(classes_file) as fp:
        classes = [ c.strip() for c in fp.readlines()]
    return np.array(classes)

ocr_model_meta = './model_data/ocr.ckpt-1108000.meta'
ocr_model_para = './model_data/ocr.ckpt-1108000'

cap_model_meta = './model_data/densenet_121.ckpt-145000.meta'
cap_model_para = './model_data/densenet_121.ckpt-145000'

classes_path = './model_data/12306_classes.txt'
classes = read_classes(classes_path)

model = CaptchaModel(ocr_model_meta=ocr_model_meta,
                     ocr_model_para=ocr_model_para,
                     cap_model_meta=cap_model_meta,
                     cap_model_para=cap_model_para)

from time import time as tc
tic = tc()

print("load model done")
for x in range(2, 19):
    word_ind, objs_ind = model.predict('/Users/dtstack/PycharmProjects/Crack12306WithAI/misc/captcha/e_{}.jpg'
                                       .format(str(x)))
    word = classes[word_ind]
    objs = classes[objs_ind]
    print("e_{}.jpg".format(str(x)), unicode(word[0], "utf-8"), objs[0])
print('time elapsed:{:.2f}'.format(tc()-tic))

model.close()




