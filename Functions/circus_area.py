import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2


print(calculate_circle_area(5))
print(calculate_circle_area(6))



#Define the higher-order function
def apply_operation(operation, numbers):
    result= [] #Array vacío con los resultados a generar.
    for num in numbers:  #Por cada número en números...
        result.append(operation(num)) #Se añade a la lista el resultado de la operación sobre el número
    return result     #Devuelve la lista de resultados.

# Example operation
def double(x):
  return x * 2

# List of numbers
numbers_list = [1, 2, 3, 4, 5]

# Using the higher-order function
doubled_numbers = apply_operation(double, numbers_list)

# Displaying the outcomes
print('Original Numbers:', numbers_list)
print('Doubled Numbers:', doubled_numbers)


def translator(language):
    #This dictionary has the language as key and another dictionary with words as values.
    translations = {
  'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
  'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
  'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'},
   "romanian": {"hello": "salut","goodbye":"larevedere","thank you":"multumesc"}
    }
    
    
    def translate_word(word): #The word is going to be in english.
        
        if word.lower() in translations[language]:
            return translations [language] [word.lower()]
        else:
           return 'Translation not available'
    return translate_word         

translate_to_spanish = translator('spanish')
print(translate_to_spanish('hello')) 

translate_to_romanian = translator('romanian')
print(translate_to_romanian("thank you"))