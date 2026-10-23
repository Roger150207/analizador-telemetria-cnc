import re
contador = 0
errores = []

with open("datos_maquina_A.txt", 'r') as archivo:
    for linea in archivo:
        linea = linea.strip()
        if "ERROR" in linea:
            print(linea)
            contador += 1
            errores.append(linea)

print(f" El total de errores es : {contador}")
for e in errores:
    print(e)

    #Imprimo la fecha del error 
    date = re.search(r"\d+-\d+-\d+", e)
    print(date.group())

    #Imprimo la hroa del error 
    time = re.search(r"\d+:\d+:\d+", e)
    print(time.group())

    #Imprimo el ID de la maquina 
    id = re.search(r"[A-Z]+-\d+", e)
    print(id.group())

    #Imprimo el error
    error = re.search(r"\[ERROR\] [A-Z]+-\d+", e)
    codigo_error = error.group().replace("[ERROR] ", "")
    print(codigo_error) 

