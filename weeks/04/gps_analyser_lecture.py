# filstien vil være annerledes på din maskin
# også husk på Windows må du erstatte hver enkelt "\" med en dobbelt "\\"
file = open("/Users/past-madm/Projects/teaching/ing301/ing301public/weeks/04/gpslogs/short.csv")
innhold = file.read()
print(type(innhold))
print(innhold)
linjer = innhold.split("\n")
print(type(linjer))
file.close()