import requests

BASE="http://127.0.0.1:5000/"

data=[{"likes":65,"name":"howtobasic","views":100000},
      {"likes":10,"name":"horses","views":10000},
      {"likes":13,"name":"Raylan","views":1000}]

for i in range(len(data)):
    response=requests.put(BASE+"video/"+str(i),data[i])
    print(response.json())

# input()
# response=requests.delete(BASE+"video/0")
# print(response)
input()
response=requests.get(BASE+"video/2")
print(response.json())