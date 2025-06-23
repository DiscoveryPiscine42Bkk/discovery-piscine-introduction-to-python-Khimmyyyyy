#!/usr/bin/python3
while True:
    user_input = input("What you gotta say:")
    if user_input == 'STOP' : 
        break 
    else:
        print(f"I got that! Anything else?: {user_input}")