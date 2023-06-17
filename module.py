import os
import pickle
import pandas as pd
import datetime
from tabulate import tabulate

# Menambah habit
def addHabit(habit, Sun, Mon, Tue, Wed, Thu, Fri, Sat):
    os.system('cls')
    newHabit = input("Type your new habit : ")
    habit.append(newHabit)
    os.system('cls')
    print(tabulate((pd.DataFrame(habit)), headers= ["List"], tablefmt="pretty"))
    print("Successfully add new habit")
    print("Press enter to continue")

    Sun.append("-")
    Mon.append("-")
    Tue.append("-")
    Wed.append("-")
    Thu.append("-")
    Fri.append("-")
    Sat.append("-")

# Menghapus habit
def removeHabit(habit, Sun, Mon, Tue, Wed, Thu, Fri, Sat):
    os.system('cls')
    print(tabulate((pd.DataFrame(habit)), headers= ["List"], tablefmt="pretty"))
    remHabit = int(input("Select the habit you want to remove : "))
    habit.remove(habit[remHabit])
    os.system('cls')
    print(tabulate((pd.DataFrame(habit)), headers= ["List"], tablefmt="pretty"))
    print("Successfully remove your habit")
    input("Press enter to continue")

    Sun.remove(Sun[remHabit])
    Mon.remove(Mon[remHabit])
    Tue.remove(Tue[remHabit])
    Wed.remove(Wed[remHabit])
    Thu.remove(Thu[remHabit])
    Fri.remove(Fri[remHabit])
    Sat.remove(Sat[remHabit])

def checkDayV(habit, Sun, Mon, Tue, Wed, Thu, Fri, Sat):
    nowday = int((datetime.datetime.now()).strftime('%w'))
    os.system('cls')
    print(tabulate((pd.DataFrame(habit)), headers= ["List"], tablefmt="pretty"))
    choice_habit = int(input("Choose the habit : "))

    if (nowday == 0):
        os.system('cls')
        Sun.pop(choice_habit)
        Sun.insert(choice_habit, 'v')
    elif (nowday == 1):
        os.system('cls')
        Mon.pop(choice_habit)
        Mon.insert(choice_habit, 'v')
    elif (nowday == 2):
        os.system('cls')
        Tue.pop(choice_habit)
        Tue.insert(choice_habit, 'v')
    elif (nowday == 3):
        os.system('cls')
        Wed.pop(choice_habit)
        Wed.insert(choice_habit, 'v')
    elif (nowday == 4):
        os.system('cls')
        Thu.pop(choice_habit)
        Thu.insert(choice_habit, 'v')
    elif (nowday == 5):
        os.system('cls')
        Fri.pop(choice_habit)
        Fri.insert(choice_habit, 'v')
    elif (nowday == 6):
        os.system('cls')
        Sat.pop(choice_habit)
        Sat.insert(choice_habit, 'v')
    
def checkDay_(habit, Sun, Mon, Tue, Wed, Thu, Fri, Sat):
    nowday = int((datetime.datetime.now()).strftime('%w'))
    os.system('cls')
    print(tabulate((pd.DataFrame(habit)), headers= ["List"], tablefmt="pretty"))
    choice_habit = int(input("Choose the habit : "))

    if (nowday == 0):
        os.system('cls')
        Sun.pop(choice_habit)
        Sun.insert(choice_habit, '-')
    elif (nowday == 1):
        os.system('cls')
        Mon.pop(choice_habit)
        Mon.insert(choice_habit, '-')
    elif (nowday == 2):
        os.system('cls')
        Tue.pop(choice_habit)
        Tue.insert(choice_habit, '-')
    elif (nowday == 3):
        os.system('cls')
        Wed.pop(choice_habit)
        Wed.insert(choice_habit, '-')
    elif (nowday == 4):
        os.system('cls')
        Thu.pop(choice_habit)
        Thu.insert(choice_habit, '-')
    elif (nowday == 5):
        os.system('cls')
        Fri.pop(choice_habit)
        Fri.insert(choice_habit, '-')
    elif (nowday == 6):
        os.system('cls')
        Sat.pop(choice_habit)
        Sat.insert(choice_habit, '-')

def saveFile(habit, Sun, Mon, Tue, Wed, Thu, Fri, Sat):
    pickle.dump(habit, open("./log/habit.dat", "wb"))
    pickle.dump(Sun, open("./log/sun.dat", "wb"))
    pickle.dump(Mon, open("./log/mon.dat", "wb"))
    pickle.dump(Tue, open("./log/tue.dat", "wb"))
    pickle.dump(Wed, open("./log/wed.dat", "wb"))
    pickle.dump(Thu, open("./log/thu.dat", "wb"))
    pickle.dump(Fri, open("./log/fri.dat", "wb"))
    pickle.dump(Sat, open("./log/sat.dat", "wb"))