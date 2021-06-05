import requests

url = "https://api.kawalcorona.com/indonesia/"
data = requests.get(url).json()

# gunakan perulangan untuk menampilkan data
for i in data:
    print("[+]  Author    :Rianda Fuad Shafly")
    print("[+]  Info      :Data Covid Indonesia")
    print("[+]  Website   :www.riandafuadshafly.my.id")
    print("[+]  Contact   :bangrianda456@gmail.co")
    print("")
    print("[+]  Negara    :" +i["name"])
    print("[+]  Positif   :" +i["positif"])
    print("[+]  Sembuh    :" +i["sembuh"])
    print("[+]  Meninggal :" +i["meninggal"])
    print("[+]  Dirawat   :" +i["dirawat"])