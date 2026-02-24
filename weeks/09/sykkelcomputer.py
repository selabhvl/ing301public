class Sykkelcomputer:

    def __init__(self, startposisjon: Position):
        # 1..* multiplisitett
        self.primaer_sensor = GPSSensor(self, startposisjon)
        self.rest_sensorer = []

    # Fassade
    def legg_til_faartsmaaler(self, start_hastighet: float):
        self.rest_sensorer.append(Fartsmaaler(self, start_hastighet))

    def __iter__(self):
        return ComputerSensorIterator(self)

    # ...

class ComputerSensorIterator:

    def __init__(self, computer: Sykkelcomputer):
        self.computer = computer
        self.poisition = -1

    def __next__(self):
        if self.poisition == -1:
            result = self.computer.primaer_sensor
            self.poisition += 1
            return result
        else:
            if self.poisition == len(self.computer.rest_sensorer):
                raise StopIteration()
            else:
                result = self.computer.rest_sensorer[self.poisition]
                self.poisition += 1
                return result
        


    

class Sensor:

    def __init__(self, computer: Sykkelcomputer):
        self.computer = computer

    
    def record(self) -> str:
        pass # abstrakt


class Position:

    def __init__(self, lengdegrad: float, breddegrad: float, hoeyde: float):
        self.lengdegrad = lengdegrad
        self.breddegrad = breddegrad
        self.hoeyde = hoeyde

    def __repr__(self):
        return "(" + str(self.lengdegrad) + ", " + str(self.breddegrad) + ")"
    

class GPSSensor(Sensor):

    def __init__(self, computer, position: Position):
        super().__init__(computer)
        self.position = position

    def record(self) -> str:
        return str(self.position)




class Fartsmaaler(Sensor):

    def __init__(self, computer, fart_i_ms: float):
        super().__init__(computer)
        self.fart_i_ms = fart_i_ms

    def record(self) -> str:
        return str(self.fart_i_ms) + " m/s"
    

class TemperaturSensor(Sensor):

    def __init__(self, computer, temp_i_C: float):
        super().__init__(computer)
        self.temp_i_C = temp_i_C

    def record(self) -> str:
        return str(self.temp_i_C) + " Degrees Celsius"
    

class Pulsklokke(Sensor):
    
    def __init__(self, computer, hjertefrekvens_i_bpm: int):
        super().__init__(computer)
        self.hjertefrekvens_i_bpm = hjertefrekvens_i_bpm

    def record(self)  -> str:
        return str(self.hjertefrekvens_i_bpm) + " b/m"
    

computer = Sykkelcomputer(Position(60.5, 5.5, 20))
computer.legg_til_faartsmaaler(20.0)

for sensor in computer:
    print("Fikk måling: " +  sensor.record())


