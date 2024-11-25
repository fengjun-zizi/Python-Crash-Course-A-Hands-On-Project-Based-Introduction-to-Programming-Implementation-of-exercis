prompt = 'Please enter you age : '

while True :
    age = int(input (prompt))
    if 0 <= age and age < 3 :
        print(f"It is free . ")
        break
    elif  3 <= age and age < 12 :
        print('It is 10 dollar . ')
        break
    elif age >= 12 :
        print('It is 15 dollar . ')
        break

print("Thank you")