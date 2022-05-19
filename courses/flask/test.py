import requests

x = requests.post("http://127.0.0.1:7777/stocks", json={"ticker": "TSLA"})
print(x)
print(x.content)
r = requests.get("http://127.0.0.1:7777/stocks")
print(r)
print(r.content)
