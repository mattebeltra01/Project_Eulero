# https://projecteuler.net/problem=19

# Months:
# Jan, Mar, May, Jul, Aug, Oct, Dec = 31 Days
# Apr, Jun, Sept, Nov = 30 Days
# Normal year = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31
# Feb = 28
# Feb = 29 year divisible by 4 but not for 100 unless is divisible by 400

import numpy as np

years = np.arange(1901,2001)

m31 = list(range(1,32))
m30 = list(range(1,31))
m29 = list(range(1,30))
m28 = list(range(1,29))

year_norm = m31 + m28 + m31 + m30 + m31 + m30 + m31 + m31 + m30 + m31 + m30 + m31
year_leap = m31 + m29 + m31 + m30 + m31 + m30 + m31 + m31 + m30 + m31 + m30 + m31

complete = []

for i in years:
    if i % 400 == 0:
        complete += year_leap
    elif i % 100 == 0:
        complete += year_norm
    elif i % 4 == 0:
        complete += year_leap
    else:
        complete += year_norm

complete = np.array(complete)
for i in range(len(complete)):
    if complete[i] != 1:
        complete[i] = 0


idx = 1
sunday_mask = np.zeros_like(complete)
for i in range(len(sunday_mask)):
    idx += 1
    if idx % 7 == 0:
        sunday_mask[i] = 1
        i = 0

complete = complete * sunday_mask
print(complete.sum())