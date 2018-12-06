import requests
import time
import base64


g_idx = 1
while 1:
    g_idx = g_idx + 1
    rd = int(time.time() * 1000)

    callback = "jQuery19105886771588237287_{}".format(str(rd))

    url_12306 = "https://kyfw.12306.cn/passport/captcha/captcha-image64?   login_site=E&module=login&rand=sjrand&{}" \
            "&callback=&_={}".format(str(rd), str(callback), str(rd))

    url_12306 = "https://kyfw.12306.cn/passport/captcha/captcha-image64?login_site=E&module=login&rand=sjrand&1543492440226&callback=jQuery191018867855739200468_1543492428407&_=1543492428409"

    r = requests.get(url_12306)

    rp = r.text
    idx = rp.find("image\":\"")
    base64_str = rp[idx+8:len(rp)-4]
    print(base64_str)
    print(rp)

    img_data = base64.b64decode(base64_str)
    file=open('./captcha/e_{}.jpg'.format(str(g_idx)),'wb')
    file.write(img_data)
    file.close()
    # time.sleep(0.1)
    print("save {} img".format(str(g_idx)))
