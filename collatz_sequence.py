def collatz(number):
    if number % 2 == 0: 
        print(number // 2)
        return number // 2
    else:   
        print(3 * number + 1)
        return 3 * number + 1

try:       
    num = input('Enter number: ')
    num = int(num)
    while num != 1:
        num = collatz(num)
except ValueError:
    print('Value Error, please enter an integer.')