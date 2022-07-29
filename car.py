class Car:
    def __init__(self):
        self.speed = 0
        self.gear = 1
        self.direction = 0  # front of car
        self.broken = False  # indicates whether car is broken
        self.simulation = []
        self.simulation_loaded = False

    def accelerate(self):
        # check if car is broken – do nothing if it is
        # check if we are in reverse or in forward gear
        # modify speed (increase 5 miles an hour)
        # if speed to high (>80 or < -10) limit to either 80 or -10
        # change gear if necessary (automatic)
        # display status
        pass

    def brake(self):
        # check if car is broken – do nothing if it is
        # check if we are in reverse or in forward gear
        # modify speed (decrease 5 miles and hour)
        # change gear if necessary (automatic)
        # display status
        pass

    def turn_steering_wheel(self, direction_change):
        # check if car is broken – do nothing if it is
        # check to see if car is in reverse
        # modify direction based on direction change and direction
        # -1 = left, 0 = straight on, 1 = right if going forward
        # 1 = left, 0 = straight on, -11 = right if going in reverse
        pass

        # display status

    def change_gear(self, selected_gear='FORWARD'):
        # selected_gear is either FORWARD or REVERSE
        # check to see if car is broken – do nothing if it is
        # check to see if car is going forward when reverse is selected and vice versa.Car breaks if so
        # work out what gear you need to be in based on car’s speed
        # Loop one gear at a time, either changing up or down, to get to required gear
        if self.broken:
            return
        if self.gear > 0 and selected_gear == 'REVERSE':
            self.broken = True
            return
        if selected_gear == 'REVERSE':
            self.gear = 0
            return

    def display_stats(self):
        disp = f"Speed = {self.speed}, Gear = {self.gear}, Direction = {self.direction}"
        print(disp)

    def load_simulation(self, filename):
        self.simulation = []
        with open(filename) as simulation_steps:
            for line in simulation_steps:
                self.simulation.append(line.rstrip())
        self.simulation_loaded = True

    def run_simulation(self):
        for step in self.simulation:
            if step == 'FORWARD':
                self.change_gear()
            elif step == 'ACCELERATE':
                pass
            elif step == 'LEFT':
                pass
            elif step == 'RIGHT':
                pass
            elif step == 'BRAKE':
                pass
            elif step == 'REVERSE':
                self.change_gear('REVERSE')
            elif step == 'ACCELERATE':
                pass
            elif step == 'BRAKE':
                pass
            elif step == 'FORWARD':
                pass
            else:
                print("Invalid simulation step")


if __name__ == '__main__':
    my_car = Car()
    my_car.load_simulation("simulation.txt")
    my_car.run_simulation()
