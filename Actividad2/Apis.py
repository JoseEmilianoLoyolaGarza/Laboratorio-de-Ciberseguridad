import http.client, urllib.parse,requests
conn = http.client.HTTPConnection('api.mediastack.com')

result = []
Tempe=[]
Viento=[]
Tiempo=[]

params = urllib.parse.urlencode({
    'access_key': '3cf0194ef4b6a2f194077d61d81978cc',
    'categories': '-general,-sports',
    'sort': 'published_desc',
    'countries':'es',
    'languages':'es',
    'limit': 4,
    })
 
conn.request('GET', '/v1/news?{}'.format(params))
 
res = conn.getresponse()
data = res.read()
info=data.decode('utf-8')
info=info.replace(',','\n')
print(info)

city = ["España","México"]
for i in city:
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=3a2cf50f2a79afd48d052c1b776cd452&units=metric".format(i) 

    res = requests.get(url)

    data = res.json()

    temp = data["main"]["temp"]
    vel_viento = data["wind"]["speed"]
    descripcion = data["weather"][0]["description"]
    Tempe.append(temp)
    Viento.append(vel_viento)
    Tiempo.append(descripcion)
print(Viento)
print(Tempe)
print(Tiempo)