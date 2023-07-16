operator = input('Enter a operator (+ - * /): ')
num1 = float(input('Enter Number 1: '))
num2 = float(input('Enter number 2: '))

if operator == "+":
    result = num1 + num2
    print(f'Result:{round(result, 2)}')
elif operator == "-":
    result = num1 - num2
    print(f'Result:{round(result, 2)}')
elif operator == "*":
    result = num1 * num2
    print(f'Result:{round(result, 2)}')
elif operator == "/":
    result = num1 / num2
    print(f'Result:{round(result, 2)}')
else:
    print(f'{operator} is not a valid operator')
