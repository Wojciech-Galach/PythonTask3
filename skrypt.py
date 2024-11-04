import argparse

def create_days_string(day_range: str):
    days = ["pn", "wt", "śr", "cz", "pt", "sb", "nd"]
    day_range = day_range.split("-")
    if (len(day_range) == 1):
        if (day_range[0] not in days):
            print("wrong day name")
            exit()
        return day_range[0]
    elif (len(day_range) == 2):
        try:
            start_index = days.index(day_range[0])
            end_index = days.index(day_range[1])
        except ValueError:
            print("wrong day name")
            exit()
        if (start_index < end_index):
            return (",").join(days[start_index:end_index+1])
        else:
            return (",").join(days[start_index:len(days)]) + "," + (",").join(days[0:end_index+1])
        return "x"

    else:
        print("Niepoprawny zakres dni tygodnia!!!")
        exit()

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

args.days = [create_days_string(day) for day in args.days]

amount_of_days = 0
for day in args.days:
    amount_of_days += len(day.split(","))

if (amount_of_days < len(args.time_of_day)):
    print("Nie możesz określić większej ilości pór dnia niż dni!!!")
    exit()
elif (amount_of_days > len(args.time_of_day)):
    args.time_of_day += ["w"] * (amount_of_days - len(args.time_of_day))

# args.months, args.days, args.time_of_day są tej samej długości
# args.create - True - utworzenie pliku, False - odczytanie danych
