import os
import datetime
import module
import pickle
import pandas as pd
from tabulate import tabulate

# Variabel tabel
habits = ['Reading', 'Studying', 'Exercise']
sunday = ['-']  * len(habits)
monday = ['-'] * len(habits)
tuesday = ['-'] * len(habits)
wednesday = ['-'] * len(habits)
thursday = ['-'] * len(habits)
friday = ['-'] * len(habits)
saturday = ['-'] * len(habits)

# Variabel lainnya
choice = int(1)
nowday = datetime.datetime.now()

# Load
habits = pickle.load(open("./log/habit.dat", "rb"))
sunday = pickle.load(open("./log/sun.dat", "rb"))
monday = pickle.load(open("./log/mon.dat", "rb"))
tuesday = pickle.load(open("./log/tue.dat", "rb"))
wednesday = pickle.load(open("./log/wed.dat", "rb"))
thursday = pickle.load(open("./log/thu.dat", "rb"))
friday = pickle.load(open("./log/fri.dat", "rb"))
saturday = pickle.load(open("./log/sat.dat", "rb"))

while (choice !=  0):

    os.system('cls')
    print("Welcome To Habit Tracker")
    print("------------------------")
    print("1. Edit your habit")
    print("2. Checklist your habit")
    print("0. Exit")
    print("------------------------")
    print(nowday.strftime("%a, %d %B %Y" ))

    table = pd.DataFrame({
        'Habit' : habits,
        'Sun' : sunday,
        'Mon' : monday,
        'Tue' : tuesday,
        'Wed' : wednesday,
        'Thu' : thursday,
        'Fri' : friday,
        'Sat' : saturday
    })

    print(tabulate(table, headers="keys", tablefmt="pretty"))
    choice = int(input("Type between 0-2 : "))

    # Pemilihan input
    if (choice < 3) and (choice > 0):
        os.system('cls')
        if (choice == 1):
            print("------------------------")
            print("1. Add")
            print("2. Remove")
            print("0. Back")
            print("------------------------")
            choice_addrem = int(input("Enter between 1-2 : "))
            if (choice_addrem == 1):
                module.addHabit(habits, sunday, monday, tuesday, wednesday, thursday, friday, saturday)
            elif (choice_addrem == 2):
                module.removeHabit(habits, sunday, monday, tuesday, wednesday, thursday, friday, saturday)
            else:
                continue
            
        if (choice == 2):
            os.system('cls')
            print("------------------------")
            print("1. for checklist or 'v'")
            print("2. for dechecklist or '-'")
            print("0. Back")
            print("------------------------")
            choice_addrem = int(input("Enter between 1-2 : "))
            if (choice_addrem == 1):
                module.checkDayV(habits, sunday, monday, tuesday, wednesday, thursday, friday, saturday)
            elif (choice_addrem == 2):
                module.checkDay_(habits, sunday, monday, tuesday, wednesday, thursday, friday, saturday)
            else:
                continue
            
    elif (choice == 0):
        # Savefile
        module.saveFile(habits, sunday, monday, tuesday, wednesday, thursday, friday, saturday)
        print("Good Bye")
        exit()
    else:
        os.system('cls')
        print("!!! ALERT !!!\nPlease input between 0-2\ntype enter to continue")
        input()