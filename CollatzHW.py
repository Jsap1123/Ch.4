#Write a program named collatz() that has one parameter named number
#If number is even print (number // 2)
#If number is odd print (3 * number + 1)


def collatz(num):

    if num % 2 == 0:
        print(num // 2)
        return num // 2

    elif num % 2 == 1:
        number = (3 * num + 1);
        print(number);
        return number


print('Enter a number');
num = int(input());
while num != 1:
    num = collatz(int(num));
