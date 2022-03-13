import requests as rq
import pandas as pd
class DevTools:
    def MakeAPIURL(a):
        Base_URL='https://geocode.xyz/[place]?json=1'
        NewURl=Base_URL.replace('[place]',a.capitalize())
        return NewURl

    def pullLat(a):
        while True:
            try:
                response = rq.get(a)
                result = response.json()
                break
            except Exception as e:
                print(str(e))
        return result
    def COOr(a):
        JsonObj = DevTools.pullLat(DevTools.MakeAPIURL(a))
        data= pd.DataFrame.from_dict(JsonObj)
        return data
    def extractCoor(a):
        latt = a['latt']
        long = a['longt']
        return latt,long

    def makeTempUrl(a,b):
        Base_URL = 'https://api.open-meteo.com/v1/forecast?latitude=%5blatt%5d&amp;longitude=%5blong%5d&amp;hourly=temperature_2m'
        Url1 = Base_URL.replace('latt',a)
        finalUrl = Url1.replace('longt',b)
        return finalUrl
    def RequestTempRange(a):
        while True:
            try:
                response = rq.get(a)
                result = response.json()
                break
            except Exception as e:
                print(e)
            return result

    def temps(a,b):
        JsonObj = DevTools.pullLat(DevTools.makeTempUrl(a,b))
        print(JsonObj['hourly'])
        data = pd.DataFrame({'time': JsonObj['time'],'temperature': JsonObj['temperature_2m']})
        return data.plot.bar(rot=0)

