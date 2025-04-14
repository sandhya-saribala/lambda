#addition operation using def and lambda function
n=10,2
def add(first,second):
    print(first+second)
add(10,2)

add_lambda=lambda a,b:a+b
result_lambda=add_lambda(3,4)
print(result_lambda)

#subtraction operation using def and lambda function
n=12,3
def sub(first,second):
    print(first-second)
sub(12,3)

sub_lambda=lambda a,b:a-b
result_lambda=sub_lambda(4,7)
print(result_lambda)

#multiplication operation using def and lambda function
n=12,45
def mul(first,second):
    print(first*second)
mul(12,45)

mul_lambda=lambda a,b:a*b
result_lambda=mul_lambda(2,5)
print(result_lambda)

#division operation using def and lambda function
n=23,34
def div(first,second):
    print(first/second)
div(23,34)

div_lambda=lambda a,b:a/b
result_lambda=div_lambda(23,54)
print(result_lambda)

#modulos operation using def and lambda function
n=12,45
def mod(first,second):
    print(first%second)
mod(12,45)

mod_lambda=lambda a,b:a%b
result_lambda=mod_lambda(2,5)
print(result_lambda)

#floor div operation using def and lambda function
n=23,34
def floor_div(first,second):
    print(first//second)
floor_div(12,45)

floor_div_lambda=lambda a,b:a//b
result_lambda=floor_div_lambda(22,55)
print(result_lambda)


