def get_dict(file_name):
    my_dict = {}
    with open(file_name) as the_file:
        for the_text in the_file:
            the_text = the_text.strip()
            the_text = the_text.replace("|", "")
            the_text = the_text.split(",")
            for i in len(the_text):

                print(i)    



get_dict('recipes.txt')

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
    
# file_into_dictionary('recipes.txt')
# def get_cooking_book():
#     with open('cooking_book.txt', encoding="utf-8") as file_to_read:
#         while True:
#             recipe_name = file_to_read.readline().strip()
#             if recipe_name.strip() == '':
#                 break
#             number_of_ingredients = int(file_to_read.readline().strip())
#             list_of_ingredients = []
#             for i in range(number_of_ingredients):
#                 ingredient = file_to_read.readline().strip().split(' | ')
#                 ingredients = {'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]), 'measure': ingredient[2]}
#                 list_of_ingredients.append(ingredients)
#             cook_book.update({recipe_name: list_of_ingredients})
