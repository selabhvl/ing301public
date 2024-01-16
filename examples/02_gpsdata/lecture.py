fil = open("/Users/past-madm/Projects/teaching/ing301/ing301public/examples/02_gpsdata/gpslogs/short.csv", "r")
liste = fil.readlines()
foerste = liste[0]
liste2 = foerste.split(',')
for x in liste2:
    print(x)