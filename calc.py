print('Welcome to the calculator world!!')
print('Please type the math operation you want to complete')
print("+ for addition \n - for subraction \n * for multiplication \n / for division \n ** for power \n % for modulus")
 
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
operator = input('Which operator do you want to use?: ')

if operator == '+':
     print(num1 + num2)

elif operator == '-':
     print(num1 - num2)

elif operator == '*':
    print(num1 * num2)

elif  operator == '/':
    print(num1 / num2)

elif operator == '**':
    print(num1 ** num2)

elif operator == '%':
    print(num1 % num2)



