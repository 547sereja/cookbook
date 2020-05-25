import re
from pprint import pprint
def read_cook_book_from_file(file_name):
    with open(file_name, encoding='utf8') as file:
        cook_book = {}
        cook_dish = ''
        for line in file:
            line = line.strip()
            if '|' not in line and len(line) and re.match('\D', line):
                cook_book.setdefault(line, [])
                cook_dish = line
            elif '|' in line:
                line = line.split('|')
                cook_book[cook_dish].append({'ingredient_name': line[0], 'quantity': int(line[1]), 'measure': line[2]})
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_cook_book_from_file('recipes.txt')
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            name = ingredient['ingredient_name']
            if name in shop_list:
                shop_list[name]['quantity'] += ingredient['quantity'] * person_count
            else:
                shop_list[name] = {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}
    return shop_list

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 7))




















#         cook_book = {}
#         cook_dish = ''
#         for line in file:
#             line = line.strip()
#             if '|' not in line and len(line) and re.match('\D', line):
#                 cook_book.setdefault(line, [])
#                 cook_dish = line
#             elif '|' in line:
#                 line = line.split(' | ')
#                 cook_book[cook_dish].append({'ingredient_name': line[0], 'quantity': int(line[1]), 'measure': line[2]})
#     return cook_book

# # print(read_cook_book_from_file('recipes.txt'))


# def get_shop_list_by_dishes(dishes, person_count):
#     cook_book = read_cook_book_from_file('recipes.txt')
#     shop_list = {}
#     for dish in dishes:
#         for ingredient in cook_book[dish]:
#             name = ingredient['ingredient_name']
#             if name in shop_list:
#                 shop_list[name]['quantity'] += ingredient['quantity'] * person_count
#             else:
#                 shop_list[name] = {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}
#     return shop_list

# pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2))















# with open('recipes.txt', encoding='utf8') as file:
#     cook_dict = {}
#     for line in file:
#         dish_name = line.strip()
#         counter = int(file.readline().strip())
#         cook_dict[dish_name] = []
#         for i in range(counter):
#             ingredient = file.readline().strip().split('|')
#             temp_dict = {'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]}
#             cook_dict[dish_name].append(temp_dict)
#         file.readline()
# print(cook_dict)





# from pprint import pprint
# def create_book(book):
#     with open('recipes.txt', encoding='utf8') as file:
#             cook_book = {}
#             for line in file:
#                 dish_name = line.strip()
#                 cook_book[dish_name] = []
#                 counter = int(file.readline().strip())
#                 for i in range(counter):
#                     ingredients = file.readline().strip().split('|')
#                     temp_dict = {'ingredient_name': ingredients[0], 'quantity': ingredients[1], 'measure': ingredients[2]}
#                     cook_book[dish_name].append(temp_dict)
#                 file.readline()
#                 return cook_book


# def get_shop_list_by_dishes(dishes, persons):
#     cook_dict = create_book('recipes.txt')
#     shoplist = {}
#     for dish_name in dishes:
#         if dish_name in cook_dict:
#             for ingredients in cook_dict[dish_name]:
#                 if ingredients['ingredient_name'] in shoplist:
#                     shoplist[ingredients['ingredient_name']]['quantity'] += int((ingredients['quantity']) * persons)
#                 else:
#                     shoplist[ingredients['ingredient_name']] = {'measure': ingredients['measure'],
#                                                                 'quantity': int(ingredients['quantity']) * persons}
#     return shoplist
# pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 5))