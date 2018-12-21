#Type Conversions

'''
In this exercise the aim is to try out different datatypes. 
Start by defining two variables, and assign the first variable the float value 10.6411. 
The second variable gets a string "Stringline!" as a value.

Convert the first variable to an integer, and multiply the variable with the string by 2. 
After this, finalize the program to print out the results in the following way:

Integer conversion cannot do roundings: 10
Multiplying strings also causes trouble: Stringline!Stringline!
'''

number1 = 10.6411
st1 = "Stringline!"
st2 = st1*2
num1 = int(number1)
print("Integer conversion cannot do roundings: "+str(num1))
print("Multiplying strings also causes trouble: "+st2)