cook_book = {}
def get_cooking_book():
    with open('recipes.txt') as file_to_read:
        while True:
            recipe_name = file_to_read.readline().strip()
            if recipe_name.strip() == '':
                break
            number_of_ingredients = int(file_to_read.readline().strip())
            list_of_ingredients = []
            for i in range(number_of_ingredients):
                ingredient = file_to_read.readline().strip().split(' | ')
                ingredients = {'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]), 'measure': ingredient[2]}
                list_of_ingredients.append(ingredients)
                cook_book.update({recipe_name: list_of_ingredients})
    print(cook_book)
get_cooking_book()

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_shop_list_item = dict(ingredient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    print(shop_list)
get_shop_list_by_dishes(['Омлет'], 2)








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
    
