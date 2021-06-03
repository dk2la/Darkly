import requests
import re

def verfy_locations(url):
    with open('/Users/sjakku/Desktop/common.txt', 'r') as f:
        wl = f.read().splitlines()
        f.close()

    v = set()

    for w in wl:
        r= requests.get(url + w)
        if r.status_code == 404:
            continue
        if re.findall('<img src="images/WrongAnswer.gif" alt="">', r.text):
            continue
        


        print(r.url + "\t\t" + str(r.status_code))

verfy_locations("http://192.168.99.107/?page=media&src=")