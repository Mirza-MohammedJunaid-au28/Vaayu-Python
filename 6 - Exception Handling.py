"""
try:
    # Some Code.... 

except:
    # optional block
    # Handling of exception (if required)

else:
    # execute if no exception

finally:
    # Some code .....(always executed)
"""

try:
    num1 = int(input("Enter Num 1 : "))
    num2 = int(input("Enter Num 2 : "))
    ans = num1 / num2
except ZeroDivisionError:
    print('Number Cannot Divide by 0')
else:
    print(f"{num1} / {num2} = {ans}")
finally:
    print('Divison Completed')


"""
Input :

Enter Num 1 : 50
Enter Num 2 : 10
50 / 10 = 5.0
Divison Completed


Enter Num 1 : 50
Enter Num 2 : 0
Number Cannot Divide by 0
Divison Completed

"""