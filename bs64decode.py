#!/usr/bin/python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys
import urllib

code = ("https://base64.guru/decode/{}".format(sys.argv[1]))
sayfa = urllib.request.urlopen(code)

suop = BeautifulSoup(sayfa,"html.parser")
hash = suop.find("")
ana = suop.find("code").text
print("HASH:"+sys.argv[1])
print("DECODEHASH:"+ana)