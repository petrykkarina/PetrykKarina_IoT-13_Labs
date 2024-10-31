from enum import Enum
from math import fabs

class PlanetType(Enum):
    TERRESTRIAL = "Terrestrial" 
    JOVIAN = "Jovian"            

class Planet:
    def __init__(self, name, mass, orbital_velocity, mean_temperature, length_of_day, distance_from_sun, planet_type):
        self.__name = name
        self.__mass = mass 
        self.__orbital_velocity = orbital_velocity 
        self.__mean_temperature = mean_temperature  
        self.__length_of_day = length_of_day  
        self.__distance_from_sun = distance_from_sun  
        self.__planet_type = planet_type   

    def get_name(self):
        return self.__name

    def get_mass(self):
        return self.__mass

    def get_orbital_velocity(self):
        return self.__orbital_velocity

    def get_mean_temperature(self):
        return self.__mean_temperature

    def get_length_of_day(self):
        return self.__length_of_day

    def get_distance_from_sun(self):
        return self.__distance_from_sun

    def get_planet_type(self):
        return self.__planet_type

    def __str__(self):
        return f"Planet: {self.__name}, Type: {self.__planet_type.value}, Mass: {self.__mass} kg, " \
               f"Orbital Velocity: {self.__orbital_velocity} km/s, Temperature: {self.__mean_temperature}°C, " \
               f"Length of Day: {self.__length_of_day} hours, Distance from Sun: {self.__distance_from_sun} km"

    def __del__(self):
        print(f"Planet {self.__name} видалено")

class Planetary:
    def __init__(self):
        self.planets = []

    def add_planet(self, planet):
        self.planets.append(planet)

    def sort_by_day_length(self):
        self.planets.sort(key=lambda p: p.get_length_of_day())
        print("Планети відсортовано за довжиною дня.")

    def find_distance_between(self, planetA, planetB):
        distance = fabs(planetA.get_distance_from_sun() - planetB.get_distance_from_sun())
        print(f"Відстань між {planetA.get_name()} та {planetB.get_name()}: {distance} км")
        return distance

    def find_average_mass(self):
        if not self.planets:
            return 0
        total_mass = sum(planet.get_mass() for planet in self.planets)
        average_mass = total_mass / len(self.planets)
        print(f"Середня маса планет: {average_mass} кг")
        return average_mass

    def display_all_planets(self):
        for planet in self.planets:
            print(planet)

def main():
    earth = Planet("Earth", 5.972e24, 29.78, 15, 24, 1.496e8, PlanetType.TERRESTRIAL)
    jupiter = Planet("Jupiter", 1.898e27, 13.07, -108, 9.93, 7.785e8, PlanetType.JOVIAN)
    mars = Planet("Mars", 6.39e23, 24.07, -63, 24.6, 2.279e8, PlanetType.TERRESTRIAL)

    solar_system = Planetary()
    solar_system.add_planet(earth)
    solar_system.add_planet(jupiter)
    solar_system.add_planet(mars)

    print("\nІнформація про планети:")
    solar_system.display_all_planets()

    solar_system.sort_by_day_length()
    print("\nПланети після сортування за довжиною дня:")
    solar_system.display_all_planets()

    print("\nОбчислення відстані між планетами:")
    solar_system.find_distance_between(earth, jupiter)


    print("\nОбчислення середньої маси планет:")
    solar_system.find_average_mass()

if __name__ == "__main__":
    main()
