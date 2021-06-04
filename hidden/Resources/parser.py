import requests
import re

def parser(url, addr):
    new_url = url + addr
    r = requests.get(new_url)
    if addr == "README" and re.findall('[0-9]', r.text):
        print(new_url)
        print(r.text)
    lst = re.findall('">(.*)</a>', r.text)
    for addr in lst[1:]:
        parser(new_url, addr)
    return


parser("http://192.168.99.107/", ".hidden/")