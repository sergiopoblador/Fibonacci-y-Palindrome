mes=input("Enter the word and see if it is palindrome ")
if mes==mes[::-1]:
    print("This word is palindrome")
else:
    print("This word is not palindrome")