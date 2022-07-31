pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print('You ordered ' + pizza['crust'] + "-crust pizza " +
    "with the following toppings:")
for topping in pizza['toppings']: 
    print("\t" + topping)