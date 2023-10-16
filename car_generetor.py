import car_setup as cs

# This script will create all combinations for the cars

# breaks

wildcore = cs.Breaks()
wildcore.name = 'wildcore'
wildcore.speed = 36
wildcore.cornering = 23
wildcore.power_unit = 33
wildcore.reliability = 22
wildcore.pitstop_time = 0.59

suspense = cs.Breaks()
suspense.name = 'suspense'
suspense.speed = 20
suspense.cornering = 32
suspense.power_unit = 23
suspense.reliability = 21
suspense.pitstop_time = 0.37

the_warden = cs.Breaks()
the_warden.name = 'the warden'
the_warden.speed = 26
the_warden.cornering = 28
the_warden.power_unit = 27
the_warden.reliability = 25
the_warden.pitstop_time = 0.43

onyx = cs.Breaks()
onyx.name = 'onxy'
onyx.speed = 26
onyx.cornering = 23
onyx.power_unit = 25
onyx.reliability = 50
onyx.pitstop_time = 0.49

axiom = cs.Breaks()
axiom.name = 'axiom'
axiom.speed = 14
axiom.cornering = 34
axiom.power_unit = 18
axiom.reliability = 15
axiom.pitstop_time = 0.67

crisis_xl = cs.Breaks()
crisis_xl.name = 'crisis X1'
crisis_xl.speed = 27
crisis_xl.cornering = 16
crisis_xl.power_unit = 18
crisis_xl.reliability = 19
crisis_xl.pitstop_time = 0.51

essense = cs.Breaks()
essense.name = 'essense'
essense.speed = 14
essense.cornering = 13
essense.power_unit = 12
essense.reliability = 25
essense.pitstop_time = 0.76

breaks_starter = cs.Breaks()
breaks_starter.name = 'breaks starter'
breaks_starter.speed = 1
breaks_starter.cornering = 1
breaks_starter.power_unit = 1
breaks_starter.reliability = 1
breaks_starter.pitstop_time = 1


# Gearboxs

voyage = cs.Gearbox()
voyage.name = 'Voyage'
voyage.speed = 23
voyage.cornering = 28
voyage.power_unit = 22
voyage.reliability = 27
voyage.pitstop_time = 0

vector = cs.Gearbox()
vector.name = 'Vector'
vector.speed = 24
vector.cornering = 38
vector.power_unit = 22
vector.reliability = 36
vector.pitstop_time = 0.55

kick_shift = cs.Gearbox()
kick_shift.name = 'Kick Shift'
kick_shift.speed = 18
kick_shift.cornering = 19
kick_shift.power_unit = 29
kick_shift.reliability = 19
kick_shift.pitstop_time = 0.45

verdict = cs.Gearbox()
verdict.name = 'Verdict'
verdict.speed = 33
verdict.cornering = 18
verdict.power_unit = 20
verdict.reliability = 30
verdict.pitstop_time = 0.63

spectrum = cs.Gearbox()
spectrum.name = 'Spectrum'
spectrum.speed = 20
spectrum.cornering = 25
spectrum.power_unit = 21
spectrum.reliability = 23
spectrum.pitstop_time = 0.53

swiftcharge = cs.Gearbox()
swiftcharge.name = 'Swiftcharge'
swiftcharge.speed = 14
swiftcharge.cornering = 23
swiftcharge.power_unit = 22
swiftcharge.reliability = 16
swiftcharge.pitstop_time = 0.71

switch_r_00 = cs.Gearbox()
switch_r_00.name = 'Switch R 00'
switch_r_00.speed = 12
switch_r_00.cornering = 13
switch_r_00.power_unit = 11
switch_r_00.reliability = 14
switch_r_00.pitstop_time = 0.47

gearbox_starter = cs.Gearbox()
gearbox_starter.name = 'Gearbox Starter'
gearbox_starter.speed = 1
gearbox_starter.cornering = 1
gearbox_starter.power_unit = 1
gearbox_starter.pitstop_time = 1


# rear wings

typhon = cs.RearWing()
typhon.name = 'Typhon'
typhon.speed = 50
typhon.cornering = 27
typhon.power_unit = 26
typhon.reliability = 23
typhon.pitstop_time = 0.53

transcendence = cs.RearWing()
transcendence.name = 'Transcendence'
transcendence.speed = 24
transcendence.cornering = 22
transcendence.power_unit = 36
transcendence.reliability = 37
transcendence.pitstop_time = 0.53

freeflare = cs.RearWing()
freeflare.name = 'Free Flare'
freeflare.speed = 21
freeflare.cornering = 33
freeflare.power_unit = 20
freeflare.reliability = 22
freeflare.pitstop_time = 0.37

the_patron = cs.RearWing()
the_patron.name = 'The Patron'
the_patron.speed = 23
the_patron.cornering = 21
the_patron.power_unit = 19
the_patron.reliability = 37
the_patron.pitstop_time = 0.61

the_wasp = cs.RearWing()
the_wasp.name = 'The wasp'
the_wasp.speed = 16
the_wasp.cornering = 24
the_wasp.power_unit = 23
the_wasp.reliability = 14
the_wasp.pitstop_time = 0.69

the_matador = cs.RearWing()
the_matador.name = 'The Matador'
the_matador.speed = 26
the_matador.cornering = 15
the_matador.power_unit = 12
the_matador.reliability = 11
the_matador.pitstop_time = 0.76

phantom_x = cs.RearWing()
phantom_x.name = 'Phantom-X'
phantom_x.speed = 26
phantom_x.cornering = 15
phantom_x.power_unit = 12
phantom_x.reliability = 11
phantom_x.pitstop_time = 0.76

rearwing_starter = cs.RearWing()
rearwing_starter.name = 'RearWing Starter'
rearwing_starter.speed = 1
rearwing_starter.cornering = 1
rearwing_starter.power_unit = 1
rearwing_starter.reliability = 1
rearwing_starter.pitstop_time = 1


# FrontWing

virtue = cs.FrontWing()
virtue.name = 'Virtue'
virtue.speed = 23
virtue.cornering = 50
virtue.power_unit = 27
virtue.reliability = 24
virtue.pitstop_time = 0.49

thunderclap = cs.FrontWing()
thunderclap.name = 'Thunderclap'
thunderclap.speed = 35
thunderclap.cornering = 23
thunderclap.power_unit = 21
thunderclap.reliability = 33
thunderclap.pitstop_time = 0.55

trailblazer = cs.FrontWing()
trailblazer.name = 'Trailblazer'
trailblazer.speed = 21
trailblazer.cornering = 23
trailblazer.power_unit = 42
trailblazer.reliability = 20
trailblazer.pitstop_time = 0.57

zeno = cs.FrontWing()
zeno.name = 'Zeno'
zeno.speed = 25
zeno.cornering = 23
zeno.power_unit = 22
zeno.reliability = 26
zeno.pitstop_time = 0.53

the_vagabond = cs.FrontWing()
the_vagabond.name = 'The Vagabond'
the_vagabond.speed = 31
the_vagabond.cornering = 20
the_vagabond.power_unit = 23
the_vagabond.reliability = 21
the_vagabond.pitstop_time = 0.35

feral_punch = cs.FrontWing()
feral_punch.name = 'Feral Punch'
feral_punch.speed = 13
feral_punch.cornering = 15
feral_punch.power_unit = 22
feral_punch.reliability = 21
feral_punch.pitstop_time = 0.73

the_scout = cs.FrontWing()
the_scout.name = 'The Scout'
the_scout.speed = 13
the_scout.cornering = 27
the_scout.power_unit = 15
the_scout.reliability = 21
the_scout.pitstop_time = 0.73

frontwing_starter = cs.FrontWing()
frontwing_starter.name = 'Frontwing Starter'
frontwing_starter.speed = 1
frontwing_starter.cornering = 1
frontwing_starter.power_unit = 1
frontwing_starter.reliability = 1
frontwing_starter.pitstop_time = 1


# Suspension

sigma = cs.Suspension()
sigma.name = 'Sigma'
sigma.speed = 32
sigma.cornering = 28
sigma.power_unit = 30
sigma.reliability = 29
sigma.pitstop_time = 0.39

presence = cs.Suspension()
presence.name = 'Presence'
presence.speed = 23
presence.cornering = 26
presence.power_unit = 24
presence.reliability = 22
presence.pitstop_time = 0.2

horizon = cs.Suspension()
horizon.name = 'Horizon'
horizon.speed = 22
horizon.cornering = 36
horizon.power_unit = 24
horizon.reliability = 37
horizon.pitstop_time = 0.53

radiance = cs.Suspension()
radiance.name = 'Radiance'
radiance.speed = 25
radiance.cornering = 17
radiance.power_unit = 26
radiance.reliability = 19
radiance.pitstop_time = 0.65

icon_v3 = cs.Suspension()
icon_v3.name = 'Icon V3'
icon_v3.speed = 17
icon_v3.cornering = 13
icon_v3.power_unit = 16
icon_v3.reliability = 23
icon_v3.pitstop_time = 0.54

rodeo = cs.Suspension()
rodeo.name = 'Rodeo'
rodeo.speed = 23
rodeo.cornering = 22
rodeo.power_unit = 15
rodeo.reliability = 14
rodeo.pitstop_time = 0.69

the_equator = cs.Suspension()
the_equator.name = 'The Equator'
the_equator.speed = 20
the_equator.cornering = 19
the_equator.power_unit = 18
the_equator.reliability = 21
the_equator.pitstop_time = 0.61

suspension_starter = cs.Suspension()
suspension_starter.name = 'Suspension Starter'
suspension_starter.speed = 1
suspension_starter.cornering = 1
suspension_starter.power_unit = 1
suspension_starter.reliability = 1
suspension_starter.pitstop_time = 1


# Engines

cloudroar = cs.Engine()
cloudroar.name = 'Cloudroar'
cloudroar.speed = 26
cloudroar.cornering = 24
cloudroar.power_unit = 50
cloudroar.reliability = 27
cloudroar.pitstop_time = 0.55

avalanche = cs.Engine()
avalanche.name = 'Avalanche'
avalanche.speed = 34
avalanche.cornering = 22
avalanche.power_unit = 25
avalanche.reliability = 21
avalanche.pitstop_time = 0.35

the_rover = cs.Engine()
the_rover.name = 'The Rover'
the_rover.speed = 27
the_rover.cornering = 25
the_rover.power_unit = 28
the_rover.reliability = 24
the_rover.pitstop_time = 0.53

twinburst = cs.Engine()
twinburst.name = 'TwinBurst'
twinburst.speed = 16
twinburst.cornering = 29
twinburst.power_unit = 18
twinburst.reliability = 17
twinburst.pitstop_time = 0.51

enigma = cs.Engine()
enigma.name = 'Enigma'
enigma.speed = 16
enigma.cornering = 13
enigma.power_unit = 23
enigma.reliability = 25
enigma.pitstop_time = 0.69

nova = cs.Engine()
nova.name = 'Nova'
nova.speed = 31
nova.cornering = 13
nova.power_unit = 15
nova.reliability = 16
nova.pitstop_time = 0.71

brute_force = cs.Engine()
brute_force.name = 'Brute Force'
brute_force.speed = 21
brute_force.cornering = 19
brute_force.power_unit = 36
brute_force.reliability = 18
brute_force.pitstop_time = 0.63

engine_starter = cs.Engine()
engine_starter.name = 'Engine Starter'
engine_starter.speed = 1
engine_starter.cornering = 1
engine_starter.power_unit = 1
engine_starter.reliability = 1
engine_starter.pitstop_time = 1


# Crie instâncias de todas as peças
breaks_options = [wildcore, suspense, the_warden, onyx, axiom, crisis_xl, essense, breaks_starter]
gearbox_options = [voyage, vector, kick_shift, verdict, spectrum, swiftcharge, switch_r_00, gearbox_starter]
rearwing_options = [typhon, transcendence, freeflare, the_patron, the_wasp, the_matador, phantom_x, rearwing_starter]
frontwing_options = [virtue, thunderclap, trailblazer, zeno, the_vagabond, feral_punch, the_scout, frontwing_starter]
suspension_options = [sigma, presence, horizon, radiance, icon_v3, rodeo, the_equator, suspension_starter]
engine_options = [cloudroar, avalanche, the_rover, twinburst, enigma, nova, brute_force, engine_starter]


all_cars = []
count = 0
# Percorra todas as combinações de peças
for breaks in breaks_options:
    for gearbox in gearbox_options:
        for rearwing in rearwing_options:
            for frontwing in frontwing_options:
                for suspension in suspension_options:
                    for engine in engine_options:
                        # Crie uma instância do carro com a combinação atual
                        cars = cs.F1Car(breaks, gearbox, rearwing, frontwing, suspension, engine, count)
                        count = count + 1
                        all_cars.append(cars)

# Agora, a lista 'all_cars' contém todas as combinações possíveis de carros
# Você pode acessar cada carro individualmente usando all_cars[index], onde 'index' é um número de 0 a (total de combinações - 1)

# Exemplo: Acessar a primeira combinação de carro
primeiro_carro = all_cars[0]

# Exemplo: Acessar a segunda combinação de carro
segundo_carro = all_cars[1]

# ... E assim por diante

# Você pode iterar sobre a lista 'all_cars' para acessar todas as combinações geradas
# for carro in all_cars:
#     print(f"Combinação de Peças: {carro.breaks.name}, {carro.gearbox.name}, {carro.rearwing.name}, {carro.frontwing.name}, {carro.suspension.name}, {carro.engine.name}")
#     print(f"Team Score: {carro.car_atributes()[-1]}")
#     print()
# print(len(all_cars))


team_scores = [car.car_atributes()[-1] for car in all_cars]
