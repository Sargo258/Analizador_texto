texto = input("Introduce tu texto: ")
letra1 = input("Introduce una letra: ")
letra2 = input("Introduce una letra: ")
letra3 = input("Introduce una letra: ")


lista_texto = list(texto)


letras_ingresadas = [letra1, letra2, letra3]


conteo_letra1 = lista_texto.count(letra1)
conteo_letra2 = lista_texto.count(letra2)
conteo_letra3 = lista_texto.count(letra3)


cantidad_caracteres = len(texto)
contiene_python = "python" in texto.lower()
palabras = texto.split()
texto_unido = ' '.join(palabras)


resultado = (
    f"Texto: {texto}\n"
    f"Texto invertido: {texto[::-1]}.\n"
    f"'{letra1}' aparece {conteo_letra1} veces en el texto.\n"
    f"'{letra2}' aparece {conteo_letra2} veces en el texto.\n"
    f"'{letra3}' aparece {conteo_letra3} veces en el texto.\n"
    f"La primera letra del texto es {texto[0]} y {texto[-1]} es la ultima es letra.\n"
    f"El texto ontiene la plabara 'python'?, {contiene_python}.\n"
    f"Cantidad total de caracteres en el texto: {cantidad_caracteres}"
)


print(resultado)