from utils.addition import addition
from utils.multiplication import multiplication


def operation(val1,val2):
    add_res = addition(val1,val2)
    mul_res = multiplication(val1,val2)

    print(f'result of addition is {add_res}')
    print(f'result of multiplication is {mul_res}')