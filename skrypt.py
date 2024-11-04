import argparse
import os
import csv
import random

def get_amount_of_days(days_range):
    days = ["pn", "wt", "śr", "cz", "pt", "sb", "nd"]
    days_range = days_range.split("-")
    if len(days_range) == 1:
        return 1
    try:
        start_index = days.index(days_range[0])
        end_index = days.index(days_range[1])
    except ValueError:
        print("Niepoprawny zakres dni tygodnia!!!")
        exit()
    if start_index > end_index:
        return 7 - start_index + end_index + 1
    return end_index - start_index + 1

parser = argparse.ArgumentParser(description="Tworzenie/Odczyt struktury katalogów/pliku.")
parser.add_argument("-m", "--months", nargs='+', required=True, help="Lista miesięcy (np. styczeń luty)")
parser.add_argument("-d", "--days", nargs='+', required=True, help="Lista zakresów dni tygodnia (np. pn-wt pt)")
parser.add_argument("-tod", "--time_of_day", nargs='*', default=['r'], choices=['r', 'w'],
                    help="Wybór pory dnia (r: rano, w: wieczorem), domyślnie rano.")
parser.add_argument("-c", "--create", action="store_true", 
                    help="Bez użycia flagi skrypt odczyta, a z użyciem utworzy plik.")

args = parser.parse_args()


if (len(args.months) != len(args.days)):
    print("Liczba miesięcy i dni musi być taka sama!!!", len(args.months), len(args.days))
    exit()

amount_of_days = 0
for day in args.days:
    amount_of_days += get_amount_of_days(day)

if (amount_of_days < len(args.time_of_day)):
    print("Nie możesz określić większej ilości pór dnia niż dni!!!")
    exit()
elif (amount_of_days > len(args.time_of_day)):
    args.time_of_day += ["w"] * (amount_of_days - len(args.time_of_day))

# args.months, args.days, args.time_of_day są tej samej długości
# args.create - True - utworzenie pliku, False - odczytanie danych

DAYS = ["pn", "wt", "śr", "cz", "pt", "sb", "nd"]
MONTHS = ["Sty", "Lut", "Mar", "Kwi", "Maj", "Cze",
            "Lip", "Sie", "Wrz", "Paź", "Lis", "Gru"]

def create_paths(months, days, times_of_days, create):
    sum = 0
    iterator = iter(times_of_days)
    for index in range(len(months)):
        month = months[index]
        day = days[index]

        start_day, end_day = day.split('-') if '-' in day else (day, day)
        index_start = DAYS.index(start_day)
        index_end = DAYS.index(end_day)
        selected_days = DAYS[index_start:index_end + 1]

        for day_of_the_week in selected_days:
            file = 'Dane.csv'
            tod = next(iterator)
            path_to_file = os.path.join(month, day_of_the_week, tod, file)
            path = os.path.join(month, day_of_the_week, tod)
            os.makedirs(path, exist_ok=True)

            if create:
                create_file(path_to_file)
            else:
                sum += read_file(path_to_file)


    if not create:
        print("Suma = " + str(sum))

def create_file(path):
    if not os.path.exists(path):
        with open(path, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=";")
            
            writer.writerow(["Model", "Wynik", "Czas"])
            
            model = random.choice(["A", "B", "C"])
            wynik = random.randint(0, 1000)
            czas = f"{random.randint(0, 1000)}s"
            
            writer.writerow([model, wynik, czas])
            
            print(f"Plik {path} został utworzony.")
    else:
        print(f"Plik {path} już istnieje.")


def read_file(path_to_file):
    if os.path.exists(path_to_file):
        with open(path_to_file, 'r') as file:
            reader = csv.reader(file, delimiter=";")
            lines = list(reader)
            if not (len(lines) > 1 and len(lines[1]) > 2):
                print(f"Błędny format pliku {path_to_file}")
                return 0
            else:
                if lines[1][0] == 'A':
                    return lines[1][2]
                else:
                    return 0
    else:
        print(f"Plik {path_to_file} nie istnieje.")
        return 0

create_paths(args.months, args.days, args.time_of_day, args.create)
