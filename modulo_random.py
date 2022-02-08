"""
from random import random

for i in range(10):
    print(random())

from random import uniform

for i in range(6):
    print(uniform(1, 60))
"""

from random import randint

for i in range(6):
    print(randint(1, 61), end=', ')