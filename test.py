from utils.addition import addition
from utils.multiplication import multiplication
from operation.base_operation import operation

val1 = int(input("Enter your value1 : "))
val2 =int(input("Enter your value2: "))

print('result from addition',addition(val1,val2))
print('result from multiplication',multiplication(val1,val2))
print('result from operation')
operation(val1,val2)