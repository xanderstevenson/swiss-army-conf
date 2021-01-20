from prettytable import PrettyTable
import os



def main_menu():
    menu = PrettyTable(['OPTION', 'CONFIG'])
    menu.add_row(["1", "Running Config"])
    menu.add_row(["2", "Gigabit Ethernet Interfaces"])
    menu.add_row(["3", ""])
    print(menu)
    choice = int(input("Please select an option: "))
    os.system('clear')
    
    if choice == 1:
        running_config(username, password)

    if choice == 2:
        interfaces(username, password)