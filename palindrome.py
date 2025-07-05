n=int(input("Enter a number"))
original=n
reverse=0

while n !=0:              #loops run tilol all digits are used
  digit=n%10              
  reverse=reverse*10+digit       #Add digit to the reverse
  n=n//10                        #Remove last digit
if original == reverse:
    print("Palindrome Number")
else:
    print("Not a palindrome number")