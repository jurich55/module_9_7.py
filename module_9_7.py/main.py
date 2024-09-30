'''   Разминка   '''
# def func_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("----- что-то делаем перед вызовом функции -----")
#         res = func(*args, **kwargs)
#         print("----- что-то делаем после вызова функции -----")
#         return res
#     return wrapper
#
#
# @func_decorator
# def sme_fnc(title, tag):
#     print(f"{title}, {tag}")
#     return f"<{tag}>{title}</{tag}>"
#
# # sme_fnc = func_decorator(sme_fnc)
# res = sme_fnc("Python навсегда!", 'h1')
# print(res)
# print('______________________________')
#
'''        Домашнее задание          '''

def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        for i in range(2, int(result)):
            if i == 1:
                continue
            if int(result) % i == 0:
                is_primes = False
                print('Составное')
                break
            else:
                is_primes = True
                print('Простое')
            return result
    return wrapper

@is_prime
def sum_three(*args):
    result = sum(args)
    return result

result = sum_three(2, 3, 6)
print(result)
