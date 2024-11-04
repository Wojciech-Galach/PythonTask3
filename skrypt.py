import argparse

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

print("Miesiące: ", args.months)
print("Dni: ", args.days)
print("Pory dnia: ", args.time_of_day)
print("Utworzenie pliku: ", args.create)