# -*- encoding=utf-8 -*-

import sys
import urllib3
from config import *
from timestamp import *
from gen_sign import *
from gen_type import *

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

Access_Token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ3eF8xODE4MTk0NDY2NTMyOTA5MDU3IiwiaWF0IjoxNzIzMDQ3NzY2fQ.L-u01x-i2xiZq7XGh-KmUu3CCckIJyJC49lyyuh5X6_4jZ5On951EjVwCsQdYxlZjIBopIxX0Wam-uc42PXzCA"


def get_info():
    url = base_url + "/api/v1/h5/marketing/secretword/info"
    timestamp, formatted_time = timestamps()
    data = {
        "marketingId": "1816854086004391938",
        "s": "2",
        "stamp": timestamp,
    }
    sign = gen_sign(data)
    data.update({"sign": sign})
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Access-Token": Access_Token,
    }

    response = session.get(
        url,
        params=data,
        headers=headers,
        verify=False,
        proxies=NoProxy,
    )

    try:
        res_data = response.json()["data"]
        hintWord = res_data["hintWord"]
        hintWord = hintWord.split("：")[1].strip()
        if hintWord:
            print("[+] success secretword\n ", hintWord)

        return hintWord
    except Exception as e:
        print("Error secretword", e)
        print(response.text)


def main(secretword):
    url = base_url + "/api/v1/h5/marketing/secretword/confirm"

    timestamp, formatted_time = timestamps()
    hour = datetime.now().hour

    data = {
        "marketingId": "1816854086004391938",
        "round": str(hour) + ":00",
        "secretword": secretword,
        "s": 2,
        "stamp": timestamp,
    }
    sign = gen_sign(data)
    data = {
        "marketingId": "1816854086004391938",
        "round": str(hour) + ":00",
        "secretword": secretword,
        "sign": sign,
        "s": 2,
        "stamp": timestamp,
    }
    data = json.dumps(data).replace(" ", "")
    data_1286 = url + data
    type__1286 = gen_type(data_1286)
    url = url + "?type__1286=" + type__1286

    headers = {
        "Access-Token": Access_Token,
        "Content-Type": "application/json; charset=UTF-8",
    }

    print("[*] submit secretword")
    while True:
        response = session.post(
            url, data=data, headers=headers, proxies=NoProxy, verify=False
        )
        if "很抱歉，由于您访问的URL有可能对网站造成安全威胁，您的访问被阻断" in response.text:
            print("[!] warning: 请求被阻断")
            break
        elif response.text.startswith("<!doctype html>"):
            print("[!] warning: 请求包错误")
            break
        msg = response.json()["msg"]
        if "太火爆了" in msg:
            time.sleep(0.5)
        elif "已抢完" in msg:
            print("[-] fail 已抢完")
            # break
            sys.exit(0)
        elif "sign expired" in msg:
            print("[!] fail sign expired")
            sys.exit(1)
        else:
            print("[+] 有点幸运\n", response.text)
            sys.exit(1)


if __name__ == "__main__":
    secretword = get_info()
    main(secretword)
