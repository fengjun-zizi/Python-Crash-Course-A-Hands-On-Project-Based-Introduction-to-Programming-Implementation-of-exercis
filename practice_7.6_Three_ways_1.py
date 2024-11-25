
prompt = "Please enter you pizza toppings "
pizza_toppings = []
active = True 

while active :
    toppings = input (prompt)

    if toppings == 'quit' :
        active = False 
    else :
        pizza_toppings.append(toppings)
        print(f"There is you pizza toppings {toppings} ! ")


print(" \n Your complete list of pizza toppings :")
print(pizza_toppings)