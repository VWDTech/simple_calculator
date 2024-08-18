def main():
    while True:
        try:
            number1 = float(input('Enter your first number: '))
            number2 = float(input('Enter your second number: '))
            
            print('+ - * /')
            operation = input('Choose your operation: ')
            
            if operation == '+':
                result = number1 + number2
                print(f'Result: {result}')
                
            elif operation == '-':
                result = number1 - number2
                print(f'Result: {result}')
                
            elif operation == '*':
                result = number1 * number2
                print(f'Result: {result}')
                
            elif operation == '/':
                if number2 != 0:
                    result = number1 / number2
                    print(f'Result: {result}')
                else:
                    print('Error: Division by zero is not allowed.')
                
            else:
                print('This operation is not found.')
                
        except ValueError:
            print('Invalid input. Please enter numeric values.')
        
        except KeyboardInterrupt:
            print("\nExiting the calculator. Goodbye!")
            break

if __name__ == '__main__':
    main()