prompt = "Please enter you pizza toppings : "
pizza_toppings = []

while True :
    toppings = input (prompt)
    
    if toppings == 'quit' :
        break
    else :
        pizza_toppings.append(toppings)
        print(f"There is you pizza toppings {toppings} ! ")

print("\nYour complete list of pizza toppings:")
print(pizza_toppings)