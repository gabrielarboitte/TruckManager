from art import prettyTruck4, prettyTruck6, prettyTruck8
from utils import clear_lines, wait_key, ask_number, colors


# Defines the stop class, which is used to track the values
class StopTracker: 
    def __init__(self): 
        self.loaded_packages = 0 
        self.departure_weight = 0.


# Defines the package class, which is used to have a specific weight and value for each package
class Package:
    def __init__(self, weight=float, value=float):  # The values must be of float type
        self.weight = weight
        self.value = value


# Defines the truck class, used for a better use of a single truck object instead of a thousand globals
class Truck:
    def __init__(self, max_volume=None, max_weight=None):
        # Sets the truck maximum capacity
        self.max_volume = None
        self.coverage = None
        self.truck_art = None
        self.stop_history = []
        self.package_history = []
        self.statistics = [0., 0.] 

        if max_volume:
            self.set_volume(max_volume)

        if max_weight:
            self.max_weight = round(max_weight, 3)
        else:
            self.max_weight = None
        self.packages = []

    # adds another package and makes the appropriate validations
    def add_package(self, pack):
        self.packages.append(pack)  # Adds the package to the list
        self.package_history.append(pack)  # And also to the history
        excess_weight = self.get_total_weight() - self.coverage
        excess_value = excess_weight * 2.3
        self.statistics[0] = max(self.statistics[0], excess_weight)  # Checks on the statistical max weight
        self.statistics[1] = max(self.statistics[1], excess_value)  # Checks on the statistical max value

    # Gets the total weight of packages your truck is currently carrying
    def get_total_weight(self):
        return round(float(sum([package.weight for package in self.packages])), 3)  # List comprehensions are the future

    # Gets the total transport cost of your packages
    def get_transport_cost(self):
        return self.get_total_weight() * 1.5

    # Gets the total value of the packages your truck is currently carrying
    def get_total_value(self):
        return sum([package.value for package in self.packages])  # List comprehensions are the future!

    # Sets a new volume and also the truck art
    def set_volume(self, max_volume):
        if max_volume is not None:
            self.max_volume = max_volume
            self.coverage = max_volume * 10

            # Selects the right art for your truck
            if max_volume <= 4:
                self.truck_art = prettyTruck4
            elif max_volume <= 6:
                self.truck_art = prettyTruck6
            else:
                self.truck_art = prettyTruck8

    # Displays graphically the truck capacity
    def display_packages(self):
        if self.truck_art is None:
            print("You didn't specify your truck's capacity yet!")
            wait_key()
            clear_lines()
            return
        truck_image = self.truck_art
        packs = len(self.packages)
        lines_to_clear = 12
        if self.max_volume > 8:
            lines_to_clear += 1
            print("Some slots may not appear because your truck is too big")
        print(f"─── Your truck has {'no' if self.max_volume == packs else self.max_volume - packs} free slot"
              f"{'s' if self.max_volume - packs > 1 else ''} ───")

        if packs > 8:
            packages = self.packages[-8:]  # If your truck has more than 8 packages, display only the last ones
        else:
            packages = self.packages
        truck_image = truck_image.replace("{}", colors.PINK + "{}" + colors.END)
        for pack in packages:
            truck_image = truck_image.replace(" __ ", str(round(pack.weight)).zfill(2) + "kg", 1)
        print(truck_image)
        print(f"{colors.FAINT}Press any key to continue...{colors.END}")
        wait_key()
        clear_lines(lines_to_clear)

    # Initializes the truck values if they are None
    def initialize(self):
        # In case the maximum volume is not yet specified
        if self.max_volume is None:
            try:
                self.set_volume(ask_number("Please, provide the maximum capacity your truck supports (in m³): ",
                                           desired_type=int, minimum=1))
            except KeyboardInterrupt:
                pass

        # In case the maximum weight is not yet specified
        if self.max_weight is None:
            try:
                self.max_weight = ask_number("Please, provide the maximum weight your truck can carry (in kg): ",
                                             desired_type=float, minimum=1)
            except KeyboardInterrupt:
                pass
