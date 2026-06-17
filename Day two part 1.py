# STRING
# sequence of series 
# in python it can be a single string ',double string '',or thriple chords '''
# example
film='''THE TERMINATOR dark fate'''
print(film)
print(type(film))

# Escape sequence 
# \' hello '
# \"bye "
# \n - new line 
# \t - tab space 
# \b-backspace (spares no space )
# \\n will give u a \n without it being on the next line 
date="17 \\nmarch "
print(date)
print(type(date))

# raw string 
# Gives the string code exactly how it is 
# example 
quote=r"ghandhi \tonce said \nthat 'violence is never the answer'"
print(quote)

# input function 
# a=input('enter a number')
# b=input('enter another number')
# print(a+b)

# Type casting\ casting 
# implicit
# explicit 
a=10
b=20
print(int(a)+int(b))
# another 
a= 'jairus'  
b= ' jaison'
print(a+ b)
# string format 
Name='jairus'
Age=18 
married_status = 'unmarried'
rating= 7
result=f"my name is {Name},my age is{Age},my married status is {married_status} and my rating is {rating}"
print(result)
# Loops 

# While loop
# it is a conditioned based loop 
i= 1
sumo=0
sume=0
while i<=100:
    if (i%2==0):
        sume=sume+i
        i=i+1
    else:
        sumo=sumo+i
        i=i+1
print(sumo)
print(sume)