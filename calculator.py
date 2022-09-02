global num,firstCalc
num = 0
firstCalc = False

def addition():
    global num,firstCalc

    if(firstCalc == False):
        operand1,operand2 = takeInput()
        ans = operand1 + operand2
        print(f'{operand1} + {operand2} = {ans}')
        num = ans
        firstCalc = True
        menu()
    else:
        print('1. Add in previous value')
        print('2. Add new operands')
        print('3. Exit')
        choice = int(input('Enter : '))
        if(choice == 1):
            operand1 = num
            operand2 = int(input('Enter Number 2 : '))
            ans = operand1 + operand2
            print(f'{operand1} + {operand2} = {ans}')
            num = ans
            menu()
        elif(choice == 2):
            firstCalc = False
            addition()
        elif(choice == 3):
            menu()
        else:
            print('!!! Enter a Valid Number !!!')
            addition()

def subtraction():
    global num,firstCalc

    if(firstCalc == False):
        operand1,operand2 = takeInput()
        ans = operand1 - operand2
        print(f'{operand1} - {operand2} = {ans}')
        num = ans
        firstCalc = True
        menu()
    else:
        print('1. Subtract in previous value')
        print('2. Subtract new operands')
        print('3. Exit')
        choice = int(input('Enter : '))
        if(choice == 1):
            operand1 = num
            operand2 = int(input('Enter Number 2 : '))
            ans = operand1 - operand2
            print(f'{operand1} - {operand2} = {ans}')
            num = ans
            menu()
        elif(choice == 2):
            firstCalc = False
            subtraction()
        elif(choice == 3):
            menu()
        else:
            print('!!! Enter a Valid Number !!!')
            subtraction()

def multiplication():
    global num,firstCalc

    if(firstCalc == False):
        operand1,operand2 = takeInput()
        ans = operand1 * operand2
        print(f'{operand1} X {operand2} = {ans}')
        num = ans
        firstCalc = True
        menu()
    else:
        print('1. Multiply in previous value')
        print('2. Multiply new operands')
        print('3. Exit')
        choice = int(input('Enter : '))
        if(choice == 1):
            operand1 = num
            operand2 = int(input('Enter Number 2 : '))
            ans = operand1 * operand2
            print(f'{operand1} X {operand2} = {ans}')
            num = ans
            menu()
        elif(choice == 2):
            firstCalc = False
            multiplication()
        elif(choice == 3):
            menu()
        else:
            print('!!! Enter a Valid Number !!!')
            multiplication()

def division():
    global num,firstCalc

    if(firstCalc == False):
        operand1,operand2 = takeInput()
        ans = operand1 / operand2
        print(f'{operand1} / {operand2} = {ans}')
        num = ans
        firstCalc = True
        menu()
    else:
        print('1. Division in previous value')
        print('2. Divison new operands')
        print('3. Exit')
        choice = int(input('Enter : '))
        if(choice == 1):
            operand1 = num
            operand2 = int(input('Enter Number 2 : '))
            ans = operand1 / operand2
            print(f'{operand1} / {operand2} = {ans}')
            num = ans
            menu()
        elif(choice == 2):
            firstCalc = False
            division()
        elif(choice == 3):
            menu()
        else:
            print('!!! Enter a Valid Number !!!')
            division()

def percentage():
    global num,firstCalc

    if(firstCalc == False):
        print('Note : 1st Enter Number and 2nd Percentage')
        operand1,operand2 = takeInput()
        ans =  operand2 / operand1 *100
        print(f'{operand1} % {operand2} = {ans}')
        num = ans
        firstCalc = True
        menu()
    else:
        print('1. Percentage in previous value')
        print('2.Percentage new operands')
        print('3. Exit')
        choice = int(input('Enter : '))
        if(choice == 1):
            operand1 = num
            operand2 = int(input('Enter Number 2 : '))
            ans =  operand2 / operand1 *100
            print(f'{operand1} % {operand2} = {ans}')
            num = ans
            menu()
        elif(choice == 2):
            firstCalc = False
            percentage()
        elif(choice == 3):
            menu()
        else:
            print('!!! Enter a Valid Number !!!')
            percentage()
  
def modulus():
    global num,firstCalc

    if(firstCalc == False):
        operand1,operand2 = takeInput()
        ans =  operand1 % operand2
        print(f'{operand1} Modulus {operand2} = {ans}')
        num = ans
        firstCalc = True
        menu()
    else:
        print('1. Modulus in previous value')
        print('2.Modulus new operands')
        print('3. Exit')
        choice = int(input('Enter : '))
        if(choice == 1):
            operand1 = num
            operand2 = int(input('Enter Number 2 : '))
            ans =  operand1 % operand2
            print(f'{operand1} Modulus {operand2} = {ans}')
            num = ans
            menu()
        elif(choice == 2):
            firstCalc = False
            modulus()
        elif(choice == 3):
            menu()
        else:
            print('!!! Enter a Valid Number !!!')
            modulus()
  
def primeNumber():
    global num,firstCalc
    if(firstCalc == False):
        operand1 = int(input('Enter Number : '))
        
        isPrime = checkPrime(operand1)
        
        if(isPrime):
            print(f'{operand1} is Not a prime number')
        else:
            print(f'{operand1} is  a prime number')

        num = operand1
        firstCalc = True
        menu()
    else:
        print('1. Check Prime Number of Previous Value')
        print('2. Find Prime Number of another Number')
        print('3. Exit')
        choice = int(input('Enter : '))
        if(choice == 1):
            operand1 = num
            isPrime = checkPrime(operand1)
            if(isPrime):
                print(f'{operand1} is Not a prime number')
            else:
                print(f'{operand1} is  a prime number')
            menu()
            
        elif(choice == 2):
            firstCalc = False
            primeNumber()
        elif(choice == 3):
            menu()
        else:
            print('!!! Enter a Valid Number !!!')
            primeNumber()
  
def checkPrime(num):
    isPrime = False
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                isPrime = True
                break
    else:
        print('Number Should be Greater than 1')
        primeNumber()

    return isPrime 
    

def takeInput():
    operand1 = int(input('Enter Number 1 : '))
    operand2 = int(input('Enter Number 2 : '))
    return operand1,operand2

def menu():
    try:
        print('<========== Calculator ============>')
        print('1. Addition')
        print('2. Subtract')
        print('3. Multiply')
        print('4. Divide')
        print('5. Percentage')
        print('6. Modulus')
        print('7. Prime Number')
        print('8. Exit')
        choice = int(input('Enter : '))
    
        if(choice == 1):
            addition()
        elif(choice == 2):
            subtraction()
        elif(choice == 3):
            multiplication()
        elif(choice == 4):
            division()
        elif(choice == 5):
            percentage()
        elif(choice == 6):
            modulus()
        elif(choice == 7):
            primeNumber()
        elif(choice == 8):
            print('!!! \U0001F607 Thank You !!!')
    
    except:
        print('!!! Enter a Valid Number !!!')

menu()