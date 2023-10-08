"""
black_area='a'
white_area='w'
chess_field=[]
for i in range(16):
    middleware_array=[]
    for j in range(16):
        if (i+j) % 2 == 0:
            middleware_array.append('b')
        else:
            middleware_array.append('w')
        chess_field.append(middleware_array)
print(chess_field)
"""
"""
def hellow_name(name):
    print("hellow, "+ str(name))

hellow_name("Egor")
"""
"""
def create_chess_field(size, color1='b', color2='w'):
    black_area = 'a'
    white_area = 'w'
    chess_field = []
    for i in range(size):
        middleware_array = []
        for j in range(size):
            if (i+j) % 2 == 0:
                middleware_array.append(color1)
            else:
                middleware_array.append(color2)
        chess_field.append(middleware_array)
    return chess_field


arr1 = create_chess_field(8, 'r', 'b')
arr2 = create_chess_field(4, 'b', 'w')
arr3 = create_chess_field(2, 'r', 'w')
print(arr1, arr2, arr3)
"""
"""
import random
import math
import colorama
def calculator(num1,num2,operation ='+'):
    if operation =='+':
        return num1 + num2
    elif operation=='-':
        return num1-num2
    elif operation=="*":
        return num1*num2
result1=calculator(1,2)
result2=calculator(10,calculator(10,5),"*")
print(result1, result2)
print(random.randint(1,100))
"""
"""
import colorama
print(colorama.Fore.BLUE,"hellow world")
"""
"""
from les2.functions import my_print
my_print()
"""
"""
import random
import colorama
def generate_password(lenght, register=False, special=False):
    chars='qwerrtdsf[]asdasdsdklgs;dk;123124zcx6754@#$%'
    register_chars="QWEEEEEEEEEEEEEERRRRRRRTYYYYYYYYYYYYUUUUUUUU"
    special_chars="!@#$%^&*()[{}]"
    password=''
    if register:
        chars+=register_chars
    if special:
        chars+=special_chars
    for i in range(lenght):
        password+=random.choice(chars)    
    return password
password=generate_password(8,special=True,register=True)
print(colorama.Fore.RED,password)
"""
"""
def find_index(l,k):
    for i in range(len(l)-1):
        for j in range(len(l)):
            if l[i]+l[j] == k:
                return i,j
    return None
print(find_index([1,2,3,4],6))
"""
"""
def replace(l,k,n):
    middle_calue=l[k]
    l[k]=l[n]
    l[n]=middle_value
    l[k],l[n]=l[n],l[k]
    """
def custom_print(*words):
    for i in words:
        print(i)
custom_print(1, 2, 3)
