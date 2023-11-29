cook_book = {}
with open('data.txt', 'rt', encoding='utf-8') as fl:
    for line in fl:
        new_name = fl.readline().strip()
        print(new_name)
        count = int(fl.readline())
        print(count)
        dish_ing = []
        for x in range(count):
            cook = fl.readline().split()[::2]
            print(cook)
            ingredient_name, quantity, measure = cook
            dish_ing.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            empty = fl.readline()
            cook_book['new_name'] = dish_ing
    print(cook_book)

