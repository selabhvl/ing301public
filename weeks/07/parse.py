from datetime import datetime

SHORT_ROUTE = "./weeks/04/gpslogs/short.csv"
LONG_ROUTE = "./weeks/04/gpslogs/long.csv"
MEDIUM_ROUTE = "./weeks/04/gpslogs/medium.csv"
WC_ROUTE = "./weeks/04/gpslogs/vm.csv"


def read_file(fil):
    file = open(fil)
    result = []
    innhold = file.read()
    linjer = innhold.split("\n")
    for linje in linjer[1:]:
        linje_delt = linje.split(',')
        result.append((
            datetime.fromisoformat(linje_delt[0]), # tidspunkt
            float(linje_delt[1]), # latitude
            float(linje_delt[2]), # longitude
            float(linje_delt[3]) # høyde
            ))
    file.close()
    return result