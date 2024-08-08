# fmt: off
import execjs
import urllib.parse


def gen_type(data):
    try:
        with open("type_1286.js", mode="r") as f:
            js = f.read()
            type_1286 = execjs.compile(js)
            res = type_1286.call("get_sig", data)
            res = urllib.parse.quote(res)
    except Exception as e:
        print("[-] Error generate type__1286")
    if res:
        print("[+] success generate type__1286")
    return res


if __name__ == "__main__":
    i = "eqjxuDyDnDgDB0KYDsD7IbGQI3qOYYCRK0eD"
    data = 'https://mxsa.mxbc.net/api/v1/h5/marketing/secretword/confirm{"marketingId":"1816854086004391938","round":"14:00","secretword":"茉莉奶绿 茉莉花香","sign":"a76dd84976cd74df86a4b2f3816eaf9e","s":2,"stamp":1723097366818}'
    r = gen_type(data)
    print(len(r))
    d = set(i) - set(r)
    print(d)
    print(r)
