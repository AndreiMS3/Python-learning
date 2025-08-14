
letras = input("Introduce la cadena a invertir: ")


def invertir(letras):
    resultado = ""
    for letra in reversed(letras):
        resultado += letra
    return resultado

print (invertir(letras))    