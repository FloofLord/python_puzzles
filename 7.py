import pickle
import requests


url = "http://www.pythonchallenge.com/pc/def/banner.p"
resp = requests.get(url)
a = pickle.loads(resp.content)

for i in a:
    for j in i:
        print(j[0]*j[1],end="")
    print("\n")
    