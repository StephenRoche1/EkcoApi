import requests as rq
import pandas as pd
class DevTools:
    def MakeAPIURL(a):
        Base_URL='https://geocode.xyz/[place]?json=1'#this is a constant string with a placeholder
        NewURl=Base_URL.replace('[place]',a.capitalize())#replace the placeholder with a capitalised entry
        return NewURl

    def pullLat(a):
        while True:
            try:
                response = rq.get(a)#pull the data
                result = response.json()#load the data using a json block
                break
            except Exception as e:
                print(str(e))
        return result
    def COOr(a):
        JsonObj = DevTools.pullLat(DevTools.MakeAPIURL(a))
        data= pd.DataFrame.from_dict(JsonObj)
        return data

    def makeTempUrl(a,b):
        Base_URL = 'https://api.open-meteo.com/v1/forecast?latitude=%5blatt%5d&amp;longitude=%5blong%5d&amp;hourly=temperature_2m'
        Url1 = Base_URL.replace('latt',a)
        finalUrl = Url1.replace('longt',b)
        return finalUrl
    def RequestTempRange(a):
        while True:#continuelly pull until success achieved
            try:
                response = rq.get(a)
                result = response.json()
                break
            except Exception as e:
                print(e)
            return result

    def temps(a,b):
        JsonObj = DevTools.pullLat(DevTools.makeTempUrl(a,b))#create the object using the url
        print(JsonObj['hourly'])#pull the section held by the object
        data = pd.DataFrame({'time': JsonObj['time'],'temperature': JsonObj['temperature_2m']})#set the plot using th time and temperature as the axis
        return data.plot.bar(rot=0)#return the pandas plot

