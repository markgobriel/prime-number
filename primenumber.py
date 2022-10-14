# WHAT IS A PRIME NUMBER?
# a prime number is a number that is only divisble by itself and by 1
# e.g.: 3, 5, 7, 11, 13, 17 ...
# 0 and 1 however, are NOT prime numbers

def main():

    num = int(input("enter your number here "))

    if num > 1:

        for i in range(2,num):
            if (num % i == 0):
                print(num, "is not a prime number.")
                break

        else:
            print(num, "is a prime number.")

    else: 
        print(num, "is not a prime number.")

    repeat=input("do you want to check if another number is prime? ").lower()

    if repeat == "yes":
        main()

    else:
        print("bye!")
        exit()


main()