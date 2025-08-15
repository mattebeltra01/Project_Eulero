# https://projecteuler.net/problem=22

import pandas as pd

alphabet_dict = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26
}

with open("PB_1_100/names.txt", "r", encoding="utf-8") as f:
    raw = f.read().strip()

names = [nome.strip().strip('"') for nome in raw.split(",")]

df = pd.DataFrame(names, columns=["name"])

df = df.sort_values(by = "name")
df = df.reset_index()

score = 0
for j in range(len(df)):
    parola = df.loc[j]["name"]
    word_sum = 0
    for i in range(len(parola)):
        word_sum += int(alphabet_dict.get(parola[i]))
    score += (j + 1) * word_sum

print(score)
