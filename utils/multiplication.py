from utils.addition import addition


def multiplication(a,b):
    result=1
    for i in range(b):
        result= addition(result,a)
    return result