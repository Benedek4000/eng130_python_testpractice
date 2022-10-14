# Python Test Practice

## Task 1: Fizzbuzz

fizzbuzz game in fizzbuzz.py:

```python
while True:
    try:
        length = int(input("enter fizzbuzz length: "))
        break
    except:
        print("invalid value")

while True:
    try:
        fizz = int(input("enter fizz: "))
        break
    except:
        print("invalid value")

while True:
    try:
        buzz = int(input("enter buzz: "))
        break
    except:
        print("invalid value")

for i in range(length):
    if (i+1) % fizz == 0:
        if (i+1) % buzz == 0:
            print("fizzbuzz")
        else:
            print("fizz")
    else:
        if (i+1) % buzz == 0:
            print("buzz")
        else:
            print(i+1)
```

## Task 2: Shopping

shopping simulator in shopping.py:
user can:
- see the products in the shop
- add products to their basket
- remove products from their basket
- see what's in their basket

products can be identified by their name or their product number

the code:
```python
products = {
    1: "Bread",
    2: "Milk",
    3: "Pasta",
    4: "Ham",
    5: "Cheese",
    6: "Tomato"
}

basket = []


def find_index(option):
    for item in products.items():
        if option == item[1]:
            return item[0]
            break


def see_products():
    print('PRODUCTS:')
    for item in products.items():
        print(f'   Item {item[0]}: {item[1]}')
    print('')


def add_products():
    while True:
        option = input('Enter product or product number (enter 0 to finish shopping): ')
        if option == '0':
            print('')
            break
        else:
            try:
                if int(option) in products.keys():
                    basket.append(products[int(option)])
                else:
                    print('INVALID OPTION!')
                    continue
            except:
                if option.lower().title() in products.values():
                    basket.append(products[find_index(option.lower().title())])
                else:
                    print('INVALID OPTION!')
                    continue


def remove_products():
    while True:
        option = input('Enter product or product number (enter 0 to finish removing products): ')
        if option == '0':
            print('')
            break
        else:
            try:
                if (int(option) in products.keys()) and (products[int(option)] in basket):
                    basket.remove(products[int(option)])
                else:
                    print('INVALID OPTION!')
                    continue
            except:
                if (option.lower().title() in products.values()) and (option.lower().title() in basket):
                    basket.remove(products[find_index(option.lower().title())])
                else:
                    print('INVALID OPTION!')
                    continue


def see_basket():
    if len(basket) == 0:
        print('Your basket is empty.')
    else:
        print('Contents of your basket:')
        for item in products.items():
            if basket.count(item[1]) != 0:
                print(f'   {basket.count(item[1])} {item[1]}')
    print('')


while True:
    print('Tasks available:\n   1: see products\n   2: add products to basket\n   3: remove products from basket\n   4: see basket\n   5: Exit')
    task = input('Please choose task : ')
    print('')
    if task == '1':
        see_products()
    elif task == '2':
        add_products()
    elif task == '3':
        remove_products()
    elif task == '4':
        see_basket()
    elif task == '5':
        break
    else:
        print('INVALID TASK!')
        continue

```