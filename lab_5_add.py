class Planet:

    def __init__(self, name, water, temperature, pressure):
        self.name = name
        self.water = water
        self.temperature = temperature
        self.pressure = pressure

    def calculate_vyzhyvannia(self):
        water_score = self.water
        temp_score = max(0, 1 - abs(self.temperature - 15) / 50)
        pressure_score = max(0, 1 - abs(self.pressure - 1))
        vyzhyvannia = (water_score + temp_score + pressure_score) / 3
        return vyzhyvannia


planets = [
    Planet("Mercury", water=0.0, temperature=167, pressure=0.000001),
    Planet("Venus", water=0.0, temperature=464, pressure=92),
    Planet("Earth", water=1.0, temperature=15, pressure=1),
    Planet("Mars", water=0.1, temperature=-60, pressure=0.01),
    Planet("Jupiter", water=0.0, temperature=-108, pressure=1000),
    Planet("Saturn", water=0.0, temperature=-139, pressure=100),
    Planet("Uranus", water=0.0, temperature=-195, pressure=1.2),
    Planet("Neptune", water=0.0, temperature=-201, pressure=1.5),
    Planet("Pluto", water=0.0, temperature=-229, pressure=0.00001),
]

top_planets = sorted(planets, key=lambda planet: planet.calculate_vyzhyvannia(), reverse=True)[:3]

print("Топ-3 планети для виживання:")
for i in range(3):
    planet = top_planets[i]
    vyzhyvannia = planet.calculate_vyzhyvannia()
    vyzhyvannia = round(planet.calculate_vyzhyvannia(), 2)
    print(f"{i + 1}. {planet.name}: Коефіцієнт виживання = {vyzhyvannia}")
