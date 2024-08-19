import requests

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
resp = requests.get(url)
print(str(resp.content))

offset = 0
for i in range(0,400):
    print(i)
    url = f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={offset}"
    resp = requests.get(url)
    content = resp.content
    print(content)
    offset =  str(content).replace("'","").split(" ")[-1]
    print(offset)

    #peak.html