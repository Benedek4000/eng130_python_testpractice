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
