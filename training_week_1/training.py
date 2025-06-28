# lambda_function

lst = list(range(21))


def get_filter(a, filter=None):
    if filter is None:
        return a
    
    res = []
    for x in a:
        if filter(x):
            res.append(x)

    return res

r = get_filter(lst, lambda x: x > 0)
print(r)


# Замыкание (closure)


def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter = make_counter()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3

# Декораторы

def my_decorator(func):
    def wrapper():
        print('-=Начало обертки декоратора=-')
        func()
        print('-=Конец обертки декоратора=-')
    return wrapper

@my_decorator
def say_hello():
    print('ФУНКЦИЯ, КОТОРАЯ ОБОРАЧИВАЕТСЯ')

say_hello()



