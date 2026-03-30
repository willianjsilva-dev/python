from datetime import time
from time import sleep

num = int(input('Digite um numero para ver a sua tabuada : '))
print(f'\033[31mTABUADA DO {num} !\033[m')
print('-*-' * 4)

for c in range (1 ,11):
    sleep(0.5)
    print(f'\033[32m {num} x {c} = {num * c}\033[m')

print('-*-' * 4)