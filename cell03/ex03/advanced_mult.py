i=0 
while i <= 10:
    print(f"Table de {i}:", end = "")
    j = 0 
    while j <= 10:
       print(i*j,end = " ")
    j += 1  # Increment the inner loop counter 
    print()
    i += 1 # Increment the outer loop counter 
