import random

class Vehicle:
    def __init__(self, name, speed, durability):
        self.name = name
        self.speed = speed
        self.durability = durability

    def performance(self):
        """
        Calculate performance as a combination of speed and durability.
        """
        return self.speed * random.uniform(0.8, 1.2) + self.durability * random.uniform(0.5, 1.5)

class RaceSimulation:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def simulate_race(self, n_races=1):
        """
        Simulate n_races and determine the overall winner.
        """
        results = {vehicle.name: 0 for vehicle in self.vehicles}

        for _ in range(n_races):
            performances = [(vehicle.name, vehicle.performance()) for vehicle in self.vehicles]
            winner = max(performances, key=lambda x: x[1])[0]
            results[winner] += 1

        overall_winner = max(results, key=results.get)
        return results, overall_winner

# Example usage
if __name__ == "__main__":
    sim = RaceSimulation()

    # Add vehicles
    sim.add_vehicle(Vehicle("Motorcycle", speed=90, durability=50))
    sim.add_vehicle(Vehicle("Car", speed=80, durability=70))
    sim.add_vehicle(Vehicle("Truck", speed=60, durability=90))

    # Simulate races
    results, winner = sim.simulate_race(n_races=10)
    print("Race Results:", results)
    print("Overall Winner:", winner)