"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2022-01-12"
-------------------------------------------------------
"""
# Imports

# Constants
from Food import Food
from pickle import TRUE, FALSE
#week 1
def get_food():
    """
    ----
    """
    name= input("Enter Name: ")
    print("Enter Origin")
    print(Food.origins())
    origin=int(input("Enter origin: "))
    vegi = input("Vegeratrian or not (Y/N): ")
    if vegi == "Y":
        is_vegitarian=True
    else:
        is_vegitarian = False
    calories = int(input("Enter Calories: "))
    food = Food(name, origin, is_vegitarian, calories)
    return food

def read_food(line):
    """
    ---
    """
    line = line.split("|")
    name=line[0]
    origin=int(line[1])
    if line[2]==True:
        is_vegetarian=True
    else:
        is_vegetarian=False
    calories=int(line[3])
        
    food = Food(name,origin,is_vegetarian,calories)
    return food
def read_foods(file_variable):
    """
    ---
    """
    list = []
    for food_string in file_variable:
        list.append(read_food(food_string))
    return (list)
def write_foods(file_name,foods):
    for food in foods: 
        file_name.write("{}|{}|{}|{}\n".format(
            food.name,food.origin,food.is_vegetarian,food.calories))
    return
def get_vegetarian(foods):
    """
    --
    """
    vegan=[]
    #create a list for it
    for food in foods:
        if food.is_vegetarian:
            vegan.append(food)        
    return vegan
#week 2
def by_origin(foods,origin):
    """
    ---
    """
    assert origin in range(len(Food.ORIGIN))
    origins=[]
    for i in foods:
        if i.origin==origin:
            origins.append(i)
    return(origins)
def average_calories(foods):
    """
    ---
    """
    total=0
    for i in foods:
        total+=i.calories
    average = total//len(foods)
    return(average)
def calories_by_origin(foods, origin):
    """
    ---
    """
    assert origin in range(len(Food.ORIGIN))
    total=0
    counter=0
    for i in foods:
        if i.origin==origin:
            counter+=1
            total+=i.calories
    average= total//counter
    return (average)
def food_table(foods):
    """
    ---
    """
    f=sorted(foods)
    print("Food                                Origin       Vegetarian Calories")
    print("----------------------------------- ------------ ---------- --------")
    for food in f:
        print("{:35} {:12} {:>10} {:8}".format(food.name,Food.ORIGIN[food.origin],str(food.is_vegetarian),food.calories))
    return
def food_search(foods,origin,max_cals,is_veg):
    """
    ---
    """
    assert origin in range(-1,len(Food.ORIGIN))
    list1=[]
    for i in foods:
        if(origin==i.origin or origin==-1)and(is_veg==i.is_vegetarian or is_veg==False) and (max_cals==0 or max_cals>=i.calories):
            list1.append(i)
    return(list1)