import argparse

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

if (len(args.days) < len(args.time_of_day)):
    print("Nie możesz określić większej ilości pór dnia niż dni!!!")
    exit()
elif (len(args.days) > len(args.time_of_day)):
    args.time_of_day += ["w"] * (len(args.days) - len(args.time_of_day))

# args.months, args.days, args.time_of_day są tej samej długości
# args.create - True - utworzenie pliku, False - odczytanie danych