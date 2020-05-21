
def create_book(book_name):
    with open('recipes.txt', encoding='UTF-8') as fi:
        cook_dict = {}
        for line in fi:
            dish_name = line.strip()
            cook_dict[dish_name] = []
            counter = int(fi.readline().strip())
            for i in range(counter):
                ingredients = fi.readline().strip().split('|')
                temp_dict = {'ingredient_name': ingredients[0], 'quantity': ingredients[1], 'measure': ingredients[2]}
                cook_dict[dish_name].append(temp_dict)
            fi.readline()
        return cook_dict


def get_shop_list_by_dishes(dishes, persons):
    cook_dict = create_book('recipes.txt')
    shoplist = {}
    for dish_name in dishes:
        if dish_name in cook_dict:
            for ingredients in cook_dict[dish_name]:
                if ingredients['ingredient_name'] in shoplist:
                    shoplist[ingredients['ingredient_name']]['quantity'] += int((ingredients['quantity']) * persons)
                else:
                    shoplist[ingredients['ingredient_name']] = {'measure': ingredients['measure'],
                                                                'quantity': int(ingredients['quantity']) * persons}
    return shoplist







# def create_shop_list():
#   person_count = int(input('Введите количество человек: '))
#   dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
#     .lower().split(', ')
#   shop_list = get_shop_list_by_dishes(dishes, person_count)
#   print_shop_list(shop_list)

# create_shop_list()





# def get_dict(file_name):
#     my_dict = {}
#     with open(file_name) as the_file:
#         for the_text in the_file:
#             the_text = the_text.strip()
#             the_text = the_text.replace("|", "")
#             the_text = the_text.split(",")
#             for i in len(the_text):
#             print(i)    



# get_dict('recipes.txt')

# def file_into_dictionary(filename):
#     cook_book = {}
#     with open(filename, 'r') as file_to_read:
#         while True:
#             recipe_name = file_to_read.readline().strip()
#             if recipe_name.strip() == '':
#                 break
#             number_of_ingredients = int(file_to_read.readline().split())
#             list_of_ingredients = []
#             for i in range(number_of_ingredients):
#                 ingredient = file_to_read.readline().split('|')
#                 ingredients = {'ingredient_name': ingredient[0], 'quantity': int(str(ingredient[1])), 'measure': ingredient[2]}
#                 list_of_ingredients.append(ingredients)
#             cook_book.update({recipe_name: list_of_ingredients})


#             print(cook_book)
    
