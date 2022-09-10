# コードを記載
S = input()
day_dict = {
    "Monday": 5,
    "Tuesday": 4,
    "Wednesday": 3,
    "Thursday": 2,
    "Friday": 1,
}

for k, v in day_dict.items():
    if S == k:
        print(v)
