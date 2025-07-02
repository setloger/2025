import random
from string import ascii_lowercase, ascii_uppercase
chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
N = int(input())
random.seed(1)
# indx = random.randint(0, len(chars)-1)

# установка зерна датчика случайных чисел (не менять)
# здесь продолжайте программу

def my_func_gen(N, chars):    
    while True:
        my_str = ''
        for i in range(N):
            indx = random.randint(0, len(chars)-1)
            my_str += chars[indx]            
        yield my_str
                   
             

my_gen = my_func_gen(N, chars)

for i in range(10):
    print(next(my_gen))

# ----------


