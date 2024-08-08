import json
import base64
import hashlib
from config import *
from timestamp import *
from urllib.parse import quote_plus
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256

timestamp, formatted_time = timestamps()


def gen_sign(data):
    try:
        keys = sorted(data.keys())

        data_str = "&".join(f"{key}={data[key]}" for key in keys)
        data_str += salt

        hash_obj = hashlib.md5(data_str.encode("utf-8"))
        sign = hash_obj.hexdigest()
    except Exception as e:
        print("[-] Error generate sign")

    if sign:
        print("[+] success generate sign")
    return sign


def gen_mainSign(data):
    try:
        sorted_params = sorted(data.items())
        param_str = "&".join(
            f"{k}={quote_plus(json.dumps(v)) if isinstance(v, dict) else quote_plus(str(v))}"
            for k, v in sorted_params
        )
        key = RSA.importKey(privateKeyString)
        # 创建一个SHA256哈希对象
        hash_obj = SHA256.new(param_str.encode())
        # 创建一个签名者
        signer = PKCS1_v1_5.new(key)
        # 对哈希对象进行签名
        signature = signer.sign(hash_obj)
        # 对签名进行Base64编码，并替换"/"和"+"字符
        signature = base64.b64encode(signature).decode()
        mainSign = signature.replace("/", "_").replace("+", "-")
    except Exception as e:
        print("[-] Error generate mainsign")

    if mainSign:
        print("[+] success generate mainsign")

    return mainSign


if __name__ == "__main__":
    data = {
        "marketingId": "1816854086004391938",
        "round": "14:00",
        "secretword": "茉莉奶绿 茉莉花香",
        "s": 2,
        "stamp": 1723097366818,
    }
    data = gen_sign(data)
    print(data)
