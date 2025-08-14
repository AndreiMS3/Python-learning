""" 
* EJERCICIO:

 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""

for i in range(10,56):
    if i % 2 == 0 and i != 16 and i % 3 != 0 :
        print(i)
   
""" 
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
"""    

def funcion(param1,param2)-> int:
    numI = 0
    for i in range (1,101):
        if i % 3 == 0 and i % 5 == 0  :
            print(param1 + param2)
        elif i % 5 == 0:
            print(param2)
        elif i % 3 == 0:
            print(param1 )  
        else:
            print(i)  
            numI += 1    
    return  numI

funcion("Hola", "Lola")


""" 
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
"""

agenda = {
    "Digi": 642642642,
    "Ani": 642211308,
}
def buscar_numero(contacto):
    return agenda.values(contacto)

def anadir_contacto(contacto, numero):
    agenda[contacto] = numero

def actualizar_contacto(contacto, nuevo_numero):
    agenda[contacto] = nuevo_numero
            
    