def is_prime(func):
    def wrapper(*args, **kwargs):
        check_func = func(*args, **kwargs)
        for i in range(2, check_func):
            if i == check_func - 1 and int(check_func) % i:
                print('Простое')
            elif int(check_func) % i:
                pass
            else:
                print('Составное')
                break
        return check_func
    return wrapper


@ is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
