# Imports
import argparse  # Argument parser, smoother than argv

from art import print_main_menu, print_sub_menu, truck_status, show_report  # Menus
from classes import Truck, Package, StopTracker  # The package, tracker and truck objects
from utils import *

truck = None  # Defines the global variable of your truck


def load_package():
    # First, gets the package's weight, but returns if the users cancels the operation
    try:
        package_weight = ask_number(f"Please, provide the {colors.UNDERLINE}weight{colors.END} "
                                    f"of your package: ", float, 1, 99)
        package_value = ask_number(f"Now provide the {colors.UNDERLINE}value{colors.END} "
                                   f"of your package: ", float, 0.01)
    except KeyboardInterrupt:
        return

    # Defines the end value as the difference between the transport cost and the package value
    transport_cost = package_weight * 1.5  # Each kg costs 1.50R$ in transport

    # Prints the total package cost and compares it to the raw transport cost
    print(f"The {colors.RED}transport cost{colors.END} for this {package_weight}kg "
          f"package will be {colors.UNDERLINE}{transport_cost:.2f}R${colors.END}.", end=" ")
    if len(truck.packages):
        print(f"Summing its {colors.BOLD}{package_value:.2f}R${colors.END} value to the cargo, the total value "
              f"will be {colors.BOLD}{truck.get_total_value() + package_value:.2f}R${colors.END}", end="")
    else:
        print(f"Its value is {colors.BOLD}{package_value:.2f}R${colors.END}", end="")

    # Gets the total weight of the loaded packages
    total_weight = truck.get_total_weight()  # Summing weights from a global would be a kiddo's work
    if total_weight + package_weight > truck.coverage:  # If over the insurance coverage
        additional = (total_weight + package_weight - truck.coverage) * 0.8  # Additional cost of exceeding kg
        print(", but the weight surpasses what the insurance company covers, "
              f"so there will be an {colors.RED}additional cost{colors.END} "
              f"of {colors.UNDERLINE}{additional:.2f}R${colors.END}, "
              f"bringing the cost up to {colors.BOLD}{transport_cost + additional:.2f}R${colors.END}.")
    else:
        print(".")

    # If the package is heavier than the remaining weight, refuses it automatically
    if truck.max_weight - total_weight < package_weight:
        print(f"- The package weight surpasses your truck limits, "
              f"so it was automatically {colors.RED}refused{colors.END}")
        print()
        return

    if ask_boolean("Type y to accept this package, n to cancel"):  # Asks the user if they really want the package
        truck.add_package(Package(package_weight, package_value))  # Appends the new package to the list
        print(f"- The package was {colors.GREEN}accepted{colors.END}!")
        print()
        return True  # Only if it was really loaded
    else:  # Refuses if either n is selected or if the program gets interrupted
        print(f"- The package was {colors.RED}refused{colors.END}")
        print()


# Used to remove the last package from the list
def unload_package():
    last_package = truck.packages[-1]  # -1 grabs the last index, as -2 would get the one before it
    if ask_boolean(f"Do you really want to unload the last package ({last_package.weight}kg)? [y/n]"):
        truck.packages.remove(last_package)  # Removes the selected package from the list, if the user agrees
        print(f"- The last package ({last_package.weight}kg) was unloaded!")
        print()
    return  # False and None cases are already treated by the ask_boolean function


# This function is called when the truck makes a stop to load/unload packages
def stop_menu():
    tracker = StopTracker()
    while True:
        print_sub_menu(len(truck.packages), truck.max_volume)
        # The submenu selector is as sophisticated graphically as the main menu
        # Because we have the best designer in the world
        print("Choose one")
        try:
            choice = wait_key()
        except KeyboardInterrupt:
            choice = "3"  # The exit function
        finally:
            clear_lines(9)  # Clears the menu

        # Executes functions accordingly
        match choice:
            case "1":
                if len(truck.packages) < truck.max_volume:  # Works only when there are free package slots
                    if load_package():  # not Frank
                        tracker.loaded_packages += 1  # Frank
            case "2":
                if len(truck.packages):               # Works only if there are packages in the truck
                    unload_package()
            case "3":
                if tracker.loaded_packages:  # Prevents the truck from saving empty trackers
                    tracker.departure_weight = truck.get_total_weight()  # Frank
                    truck.stop_history.append(tracker)  # Frank
                break


# Starts the user menu
def main():
    global truck
    warning = None  # Used to display warnings, in case they exist
    day_finished = False  # If option 5 has been already selected

    purge()
    print(f"- Welcome to the {colors.PINK}super {colors.YELLOW}Truck Manager {colors.BLUE}2000{colors.END}!")
    print()
    print(f"{colors.BLUE}- The workday started!{colors.END}")
    print()
    while True:
        if warning:  # Prints any existing warning over the actual menu
            print(colors.RED + warning + colors.END)
        print_main_menu(day_finished)
        # Prompts the user choice
        print("Choose one of the options above")
        try:  # Prompts the user choice and converts it to an integer
            choice = wait_key()
        except KeyboardInterrupt:  # If receives an interruption
            choice = "7"  # Exit function
        finally:  # Receiving error or not...
            clear_lines(13 + (warning is not None))  # Clears the menu without messing up the logs
            warning = None

        match choice:  # Matches the selected choice
            case "1":  # Start day function
                if day_finished:
                    truck = Truck()       # First of all, resets the truck
                    day_finished = False  # Restarts the day
                    truck.initialize()    # And then initializes
                    purge()
                    print(f"{colors.BLUE}- The workday started!{colors.END}")
                    print()
            case "2":
                # Tries to initialize to check if the truck is already defined
                truck.initialize()
                if truck.max_volume is None or truck.max_weight is None:  # In case any of them is None...
                    print("You cannot make a stop without specifying your truck's capacities!")  # 1. Complains
                    try:
                        wait_key()
                    except KeyboardInterrupt:
                        pass
                    clear_lines()
                    continue  # 2. Starts the next iteration
                if day_finished:  # In case the user has already finished the workday
                    continue  # Ignores
                # The stop menu is a submenu which lets you load or unload packages
                stop_menu()
            case "3":
                try:
                    truck_status(truck)
                except KeyboardInterrupt:
                    continue
            case "4":  # This function shows a nice representation of your truck
                truck.display_packages()
            case "5":  # Function used to finish operations by this day
                if not day_finished:
                    print(f"{colors.PINK}- The workday is over!{colors.END}")
                    print()
                    day_finished = True
            case "6":  # Function used to generate a report after the day is over
                if day_finished:
                    show_report(truck)

            case "7":
                print("Goodbye!")
                exit()
            case _:
                warning = "(Please, select a valid option!)"


# If this file is the main file (and not serving only as an import)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='An useful manager created to help '
                                                 'you with your truck management job.')
    parser.add_argument('-mv',
                        metavar="volume",
                        type=int,
                        help='Specifies the maximum volume space in your truck (in m°).')
    parser.add_argument('-mw',
                        metavar="weight",
                        type=float,
                        help='Specifies the maximum weight your truck can carry (in kg).')

    args = parser.parse_args()       # Parse and validate user input
    truck = Truck(args.mv, args.mw)  # Sets the global truck variable

    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye! (whoa you're fast)")
        exit()
