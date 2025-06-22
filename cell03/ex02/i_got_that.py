while True:
    user_input = input("What you gotta say:")
    if user_input.lower() == 'stop' : 
        break 
    else:
        print(f"I got that! Anything else?: {user_input}")