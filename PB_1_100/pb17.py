# https://projecteuler.net/problem=17

num_dict = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "one thousand"
}

seq = ""
for i in range(1,21):
    seq += num_dict.get(i)

for i in range(21,100):
    div = i // 10
    resto = i % 10
    seq += num_dict.get(div*10) + num_dict.get(resto)

seq += "onehundred"

for i in range(101,1000):
    hundreds = i // 100
    tens = (i - (hundreds*100)) // 10
    unit = i % 10

    seq += num_dict.get(hundreds) + "hundred"
    if i%100 != 0:
        seq += "and"
    if tens > 1:
        seq += num_dict.get(tens * 10) + num_dict.get(unit) 
    else:
        seq += num_dict.get(int(str(tens) + str(unit)))

seq += "onethousand"
    
with open("string.txt","a") as file:
    file.write(seq)
print(len(seq))

