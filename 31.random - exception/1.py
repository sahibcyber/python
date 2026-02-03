# semple() - finkiyasi - 2 parametr qebul edir. 1 ci parametr deyerler olan list

# 2 ci paramtr hemin list - in icinden random formatasecilen deyerlerin sayi.

import random

ededler = [1, 2, 3, 4, 5, 6, 7, 8, 9]

random_numune = random.sample(ededler, 3)

print(random_numune)