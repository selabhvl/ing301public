class Sykkelcomputer:

    def __init__(self, sensor: Sensor):
        # 1..* mutlitplisitett
        self.primaer_sensor = sensor
        self.rest_sensorer = []
    

class Sensor:

    def __init__(self, computer: Sykkelcomputer):
        self.computer = computer


class Position:

    def __init__(self, lengdegrad: float, breddegrad: float, hoeyde: float):
        self.lengdegrad = lengdegrad
        self.breddegrad = breddegrad
        self.hoeyde = hoeyde
    

class GPSSensor(Sensor):

    def __init__(self, computer, position: Position):
        super().__init__(computer)
        self.position = position




class Fartsmaaler(Sensor):

    def __init__(self, computer, fart_i_ms: float):
        super().__init__(computer)
        self.fart_i_ms = fart_i_ms
    

class TemperaturSensor(Sensor):

    def __init__(self, computer, temp_i_C: float):
        super().__init__(computer)
        self.temp_i_C = temp_i_C
    

class Pulsklokke(Sensor):
    
    def __init__(self, computer, hjertefrekvens_i_bpm: int):
        super().__init__(computer)
        self.hjertefrekvens_i_bpm = hjertefrekvens_i_bpm

    def op(self):
        pass