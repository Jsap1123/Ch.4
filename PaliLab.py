#Write a function to determine if it is a palindrome
#Ask user to enter a word

another = 'y'
while another == 'y':

    def reverse(word):
        word = word[::-1];
        return word

    print('Enter a word: ');
    word = input();

    if word == reverse(word):
        print(reverse(word) + ' is a palindrome')
    else:
        print(reverse(word) + ' is not a palindrome')
    print('another (y/n) ');
    another = input();

