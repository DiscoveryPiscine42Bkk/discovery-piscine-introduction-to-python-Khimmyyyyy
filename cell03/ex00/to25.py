#!/usr/bin/python3
def main():
    try: 
        num = int(input("Enter a number less than 25: "))
        if num > 25:
            print("Error")
            return 
        while num <= 25:
            print(f"Inside the loop, my variable is {num}")
            num += 1 
    except ValueError:
        print("Please enter a valid number.") 

if __name__=="__main__":
    main()             