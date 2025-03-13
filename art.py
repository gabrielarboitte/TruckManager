from utils import *


# What a cool truck :D

prettyTruck8 = '''
            ═╗ 
 ╭──────────┐║┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
 ║╭───╮    ││║┃ ╔════╗╔════╗╔════╗╔════╗╔════╗╔════╗╔════╗╔════╗ ┃
 ║│   │    ││║┃ ║ __ ║║ __ ║║ __ ║║ __ ║║ __ ║║ __ ║║ __ ║║ __ ║ ┃
┍┙╰───╯ ── │╞╣┃ ╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝ ┃
│  ╭────╮  │╞╣┃  ╭────╮                        ╭────╮╭────╮╭────╮┃
┕━━│ {} │───┴╨┻━━│ {} │━━━━━━━━━━━━━━━━━━━━━━━━│ {} ││ {} ││ {} │┛
   ╰────╯        ╰────╯                        ╰────╯╰────╯╰────╯
'''

prettyTruck6 = '''
            ═╗ 
 ╭──────────┐║┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
 ║╭───╮    ││║┃ ╔════╗╔════╗╔════╗╔════╗╔════╗╔════╗ ┃
 ║│   │    ││║┃ ║ __ ║║ __ ║║ __ ║║ __ ║║ __ ║║ __ ║ ┃
┍┙╰───╯ ── │╞╣┃ ╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝ ┃
│  ╭────╮  │╞╣┃  ╭────╮                  ╭────╮╭────╮┃
┕━━│ {} │───┴╨┻━━│ {} │━━━━━━━━━━━━━━━━━━│ {} ││ {} │┛
   ╰────╯        ╰────╯                  ╰────╯╰────╯
'''

prettyTruck4 = '''
            ═╗ 
 ╭──────────┐║┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
 ║╭───╮    ││║┃ ╔════╗ ╔════╗ ╔════╗ ╔════╗ ┃
 ║│   │    ││║┃ ║ __ ║ ║ __ ║ ║ __ ║ ║ __ ║ ┃
┍┙╰───╯ ── │╞╣┃ ╚════╝ ╚════╝ ╚════╝ ╚════╝ ┃
│  ╭────╮  │╞╣┃  ╭────╮               ╭────╮┃
┕━━│ {} │───┴╨┻━━│ {} │━━━━━━━━━━━━━━━│ {} │┛
   ╰────╯        ╰────╯               ╰────╯
'''


def truck_status(truck):
    # Shows the truck status
    if truck.max_weight is None or truck.max_volume is None:  # Error prevention
        print("Couldn't show the status because your truck's capacity is not defined yet!")
        wait_key()
        clear_lines()
        return
    total_weight = truck.get_total_weight()  # Sr. G
    remaining_weight = truck.max_weight - total_weight  # Sr. G
    #
    print('''╔═══════════════════╗
║ Weight Capacities ║
╚═══════════════════╝''')  # Sr. G
    print("Loaded weight: ", total_weight, "kg", sep="")  # Sr. G
    print("Remaining weight: ", remaining_weight, "kg", sep="")  # Sr. G
    print("Maximum weight: ", truck.max_weight, "kg", sep="")  # Sr. G
    print()  # Sr. G
    print(f"{colors.FAINT}Press any key to continue...{colors.END}")  # Sr. G
    wait_key()  # Sr. G
    clear_lines(8)  # Sr. G
    # # # # # SIR G # # # # #
    print('''╔════════════════════╗
║ Package Capacities ║
╚════════════════════╝''')
    print("Packages loaded:", len(truck.packages))  # Sr. G
    print("Package slots remaining:", truck.max_volume - len(truck.packages))  # Sr. G
    print("Maximum packages quantity:", truck.max_volume)  # Sr. G
    print()  # Sr. G
    print(f"{colors.FAINT}Press any key to continue...{colors.END}")  # Sr. G
    wait_key()  # Sr. G
    clear_lines(8)  # Sr. G
    #
    print('''╔══════════════╗
║ Value Status ║
╚══════════════╝''')  # Sr. G
    covered = truck.max_volume * 15 - truck.get_transport_cost()  # Sr. G
    lines_to_erase = 9  # Sr. G
    print(f"Transported value: {truck.get_total_value():.2f}R$")  # Sr. G
    print(f"Transport cost: {truck.get_transport_cost():.2f}R$")  # Sr. G
    if covered >= 0:  # Sr. G
        print(f"Remaining value: {covered:.2f}R$")  # Sr. G
    else:  # Sr. G
        print(f"Additional cost: {covered / -1.5 * 0.8:.2f}R$")  # Sr. G
        print(f"Total cost: {truck.max_volume * 15 + covered / -1.5 * 2.3:.2f}R$")  # Sr. G
        lines_to_erase += 1  # Sr. G
    print(f"Maximum coverage value: {truck.max_volume * 15:.2f}R$")  # Sr. G
    print()  # Sr. G
    print(f"{colors.FAINT}Press any key to continue...{colors.END}")  # Sr. G
    wait_key()  # Sr. G
    clear_lines(lines_to_erase)  # Sr. G


def print_main_menu(day_finished):
    if day_finished:
        option_1 = f'{colors.GREEN}1{colors.END} - Begin the day, set your truck\'s capacities'
        option_2 = f'{colors.GRAY}[Locked, start another day first]{colors.END}'
        option_5 = f'{colors.GRAY}[Locked, your workday is already over]{colors.END}'
        option_6 = f'{colors.GREEN}6{colors.END} - Show a report of the day'
    else:
        option_1 = f'{colors.GRAY}[Locked, your day has already started]{colors.END}'
        option_2 = f'{colors.GREEN}2{colors.END} - Stop the truck to load or unload packages'
        option_5 = f'{colors.GREEN}5{colors.END} - End the day'
        option_6 = f'{colors.GRAY}[Locked, finish the workday first]{colors.END}'

    print(f'''            {colors.RED}╔══════════════════════════╗     
            ║    {colors.YELLOW}Truck Manager{colors.END} {colors.CYAN}2000{colors.RED}    ║             
╔═══════════╩══════════════════════════╩═══════════╗
║ {option_1}{" " * (55 - len(option_1))}{colors.RED}   ║
║ {option_2}{" " * (54 - len(option_2))}{colors.RED}    ║
║ {colors.GREEN}3{colors.END} - Check on the truck{colors.RED}                           ║
║ {colors.GREEN}4{colors.END} - Show packages{colors.RED}                                ║
║ {option_5}{" " * (54 - len(option_5))}{colors.RED}    ║
║ {option_6}{" " * (43 - len(option_6))}{colors.RED}               ║
║ {colors.GREEN}7{colors.END} - Exit the program{colors.RED}                             ║
╚══════════════════════════════════════════════════╝{colors.END}
''')


def print_sub_menu(packages, maximum):
    option_1 = f'{colors.GRAY}[locked, your truck is full]{colors.END}' if packages == maximum \
        else f'{colors.PINK}1{colors.END} - Add new package         '
    option_2 = f'{colors.GRAY}[locked, your truck is empty]{colors.END}' if not packages \
        else f'{colors.PINK}2{colors.END} - Unload the last package  '
    print(f'''{colors.BLUE}         ╔════════════════╗ 
         ║   {colors.GREEN}Truck Stop{colors.BLUE}   ║
╔════════╩════════════════╩════════╗
║ {option_1}{colors.BLUE}     ║
║ {option_2}{colors.BLUE}    ║
║ {colors.PINK}3{colors.END} - Go back to the road{colors.BLUE}          ║
╚══════════════════════════════════╝{colors.END}
''')


# Why do all lines say Frank? Only Frank knows
def show_report(truck):  # Frank
    if not truck.stop_history:  # Prevents errors and displays a funny message
        print("!!! There is no report, because you didn't work today !!!")  # Frank
        wait_key()  # Frank
        clear_lines()  # Frank
        return  # Frank
    report_weight = [package.weight for package in truck.package_history]  # Frank
    report_added = [stop.loaded_packages for stop in truck.stop_history]  # Rlz
    report_stop_weight = [stop.departure_weight for stop in truck.stop_history]  # Rlz
    # # # Frank
    print(f"{colors.YELLOW}During the day...{colors.END}")  # Frank
    print()  # Frank
    print(f"> The lightest package weighted {min(report_weight)}kg")  # Frank
    print(f"{colors.WHITE}> The heaviest package weighted {max(report_weight)}kg")  # Frank
    print()  # Frank
    print(f"{colors.END}> The lowest number of packages added in a single stop was {min(report_added)}")  # Frank
    print(f"{colors.WHITE}> The highest number of packages added in a single stop was {max(report_added)}")  # Frank
    print()  # Frank
    print(f"{colors.END}> The lowest cargo weight in your truck during departure "  # Frank
          f"was {min(report_stop_weight)}kg")  # Frank
    print(f"{colors.WHITE}> The highest cargo weight in your truck during departure "  # Frank
          f"was {max(report_stop_weight)}kg{colors.END}")  # Frank
    print()  # Frank
    lines_to_clear = 14  # Frank
    if truck.statistics[0]:  # Frank
        print(f"{colors.RED}> The highest excess weight throughout was {truck.statistics[0]}kg")  # Frank
        print(f"> The highest uncovered value costed in total {truck.statistics[1]:.2f}R$"  # Frank
              f" (transport + additional){colors.END}")  # Frank
        lines_to_clear += 1  # Frank
    else:  # Frank
        print(f"{colors.GREEN}- There was no excess weight today{colors.END}")  # Frank
    print()  # Frank
    print(f"{colors.FAINT}Press any key to continue...{colors.END}")  # Frank
    wait_key()  # Frank
    clear_lines(lines_to_clear)  # Frank


# The comments are just for the lulz, this is artwork and only prints stuff
