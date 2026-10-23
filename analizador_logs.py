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
