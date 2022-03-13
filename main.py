from methodFile import DevTools as DT
#Devtools  is a class file created for the purposes of pulling json data
#a simple snippet of the base tools i have created over the years
active=True
citySearch= input("input the city you would like to search")
myCitylat = DT.COOr(citySearch)
lattitude=myCitylat['latt'][0]
longitude = myCitylat['longt'][0]
print(longitude,lattitude)
print(DT.temps(lattitude,longitude))




