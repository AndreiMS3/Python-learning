""" 
This project is a fantasy name generator.
It consists in two lists: suffixes and prefixes; a capitalize() method to capitalize suffixes;  
a create_fantasy_name() that creates one name and later will be used to generate 10 random names in 
a random_names variable; a fire in name
"""


import random
from functools import reduce

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

#Capitalize words from the list.
def capitalize_suffix(suffix):
    return suffix.capitalize()

#Capitalizes words from suffixes and stores it in a variable.
capitaized_suffixes= list(map(capitalize_suffix,suffixes))


#Generate random fantasy name.
def create_fantasy_name(list_1, list_2):
  return random.choice(list_1) + ' ' + random.choice(list_2)


#In a list comprehension way:
random_names = [create_fantasy_name(capitaized_suffixes, prefixes) for _ in range(10)]

print(random_names)   

#Checks if "Fire" is in name
def fire_in_name(name):
    return "Fire" in name

#Returns a String of 2 names.        
def concatenate_names(name1, name2): 
    return str(name1)+ "" + str(name2)       


#Use filter() and apply fire_in_name() to the random_names list.
def filter_fire_in_name():
    return list(filter(fire_in_name, random_names))

#Use reduce() and apply concatenate_names() to the filtered names.
def reduced_names():
    return reduce(concatenate_names,random_names)


""" Prints the generated fantasy names, the filtered names that 
include "Fire", and the reduced names.
"""
def display_name_info():
    for name in random_names: 
        print (name)
    print(f"Names with´Fire´ in it: {filter_fire_in_name()}")    
    print(f"Reduced names:  {reduced_names()}")

display_name_info()    