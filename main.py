import time
import random
ask = 0
all_user = []
user = ''
symbol_ = ['1', '2', '3', '5', '6', '7', '8', '9', '0']
while True:
    user += '+7 '
    for i in range(1, 11):
        v = random.randint(1, 6)
        user += symbol_[v]
        ask += 1
    time.sleep(1)
    print(user)
    if user == all_user:
        for i in range(1, 7):
            v = random.randint(1, 6)
            user += symbol_[v]
    user = ''
