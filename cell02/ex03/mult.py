#!/usr/bin/python3
def main():
    try:
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))

        result = num1*num2
        print(f"{num1}x{num2} = {result}")

        if result > 0:
            print("The result is positive.")
        elif result < 0:
            print("The result is negative.")    
        else:
            print("The result is positive and negative.")    

    except ValueError:
        print("Please enter valid integers.")        

if __name__== "__main__":
    main()
