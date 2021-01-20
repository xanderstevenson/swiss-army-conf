from prettytable import PrettyTable
import os

def main_menu():
    menu = PrettyTable(['OPTION', 'CONFIG'])
    menu.add_row(["1", "Running Config"])
    menu.add_row(["2", "Interfaces"])
    menu.add_row(["3", ""])
    print(menu)
    choice = int(input("Please select an option: "))
    os.system('clear')