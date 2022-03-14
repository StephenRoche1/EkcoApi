from methodFile import DevTools as DT
#Devtools  is a class file created for the purposes of pulling json data
#a simple snippet of the base tools i have created over the years
active=True
citySearch= input("input the city you would like to search")
myCitylat = DT.COOr(citySearch)
lattitude=myCitylat['latt'][0]#use the first indexed iteration of longitude and latitude as it
longitude = myCitylat['longt'][0]
DT.temps(lattitude,longitude) #apply the plot using the pandas function




