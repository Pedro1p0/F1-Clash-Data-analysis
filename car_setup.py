class CarPart:
    def __init__(self, name, speed, power_unit, cornering, reliability, pitstop_time):
        self.name = name
        self.speed = speed
        self.power_unit = power_unit
        self.cornering = cornering
        self.reliability = reliability
        self.pitstop_time = pitstop_time


class Breaks(CarPart):
    def __init__(self):
        super().__init__("Breaks", 0, 0, 0, 0, 0.0)


class Gearbox(CarPart):
    def __init__(self):
        super().__init__("Gearbox", 0, 0, 0, 0, 0.0)


class RearWing(CarPart):
    def __init__(self):
        super().__init__("Rear Wing", 0, 0, 0, 0, 0.0)


class FrontWing(CarPart):
    def __init__(self):
        super().__init__("Front Wing", 0, 0, 0, 0, 0.0)


class Suspension(CarPart):
    def __init__(self):
        super().__init__("Suspension", 0, 0, 0, 0, 0.0)


class Engine(CarPart):
    def __init__(self):
        super().__init__("Engine", 0, 0, 0, 0, 0.0)


class F1Car:
    def __init__(self, breaks, gearbox, rearwing, frontwing, suspension, engine, name):
        self.breaks = breaks
        self.gearbox = gearbox
        self.rearwing = rearwing
        self.frontwing = frontwing
        self.suspension = suspension
        self.engine = engine
        self.name = name

    def display_status(self):
        print("Status do Carro F1:")
        print(f"Breaks: {self.breaks.name}")
        print(f"Gearbox: {self.gearbox.name} ")
        print(f"Rear Wing: {self.rearwing.name}")
        print(f"Front Wing: {self.frontwing.name}")
        print(f"Suspension: {self.suspension.name}")
        print(f"Engine: {self.engine.name}")

    def car_atributes(self):
            speed_total = (
                self.breaks.speed + self.gearbox.speed + self.rearwing.speed +
                self.frontwing.speed + self.suspension.speed + self.engine.speed
            )
            power_unit_total = (
                self.breaks.power_unit + self.gearbox.power_unit + self.rearwing.power_unit +
                self.frontwing.power_unit + self.suspension.power_unit + self.engine.power_unit
            )
            cornering_total = (
                self.breaks.cornering + self.gearbox.cornering + self.rearwing.cornering +
                self.frontwing.cornering + self.suspension.cornering + self.engine.cornering
            )
            reliability_total = (
                self.breaks.reliability + self.gearbox.reliability + self.rearwing.reliability +
                self.frontwing.reliability + self.suspension.reliability + self.engine.reliability
            )
            pitstop_time_total = (
                self.breaks.pitstop_time + self.gearbox.pitstop_time + self.rearwing.pitstop_time +
                self.frontwing.pitstop_time + self.suspension.pitstop_time + self.engine.pitstop_time
            )
            team_score = (
                speed_total + power_unit_total + cornering_total + reliability_total + (pitstop_time_total/0.02)
            )
            
            # print(f"Speed : {speed_total}")
            # print(f"power_unit : {power_unit_total}")
            # print(f"Cornering : {cornering_total}")
            # print(f"Reliability : {reliability_total}")
            # print(f"Pitstop : {round(pitstop_time_total,2)}s")
            # print(f"team_score = {team_score}")
            
            return speed_total, power_unit_total, cornering_total, reliability_total, pitstop_time_total, team_score


# Criando instâncias das peças do carro
breaks = Breaks()
gearbox = Gearbox()
rearwing = RearWing()
frontwing = FrontWing()
suspension = Suspension()
engine = Engine()


# Criando instâncias das peças do carro e configurando valores
breaks = Breaks()
breaks.speed = 36
breaks.power_unit = 33
breaks.cornering = 23
breaks.reliability = 22
breaks.pitstop_time = 0.59

gearbox = Gearbox()
gearbox.speed = 24
gearbox.power_unit = 22
gearbox.cornering = 38
gearbox.reliability = 36
gearbox.pitstop_time = 0.55

rearwing = RearWing()
rearwing.speed = 50
rearwing.power_unit = 26
rearwing.cornering = 27
rearwing.reliability = 23
rearwing.pitstop_time = 0.53

frontwing = FrontWing()
frontwing.speed = 23
frontwing.power_unit = 27
frontwing.cornering = 50
frontwing.reliability = 24
frontwing.pitstop_time = 0.49

suspension = Suspension()
suspension.speed = 22
suspension.power_unit = 24
suspension.cornering = 36
suspension.reliability = 37
suspension.pitstop_time = 0.53

engine = Engine()
engine.speed = 34
engine.power_unit = 25
engine.cornering = 22
engine.reliability = 21
engine.pitstop_time = 0.35


# Criando uma instância do carro de F1 com as peças
meu_carro = F1Car(breaks, gearbox, rearwing, frontwing, suspension, engine, 10)
#print(meu_carro.car_atributes())
# Exibindo o status das peças do carro
# meu_carro.car_atributes()
