# Program to fetch PC's environment varables
import os

for x in list(os.environ):
    print(f'{x:<30} \t {os.environ.get(x)}') 