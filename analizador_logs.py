import re
counter = 0
errors = []

# Leyendo el archivo con el nombre correcto
with open("data_machine_A.txt", 'r') as file:
    for line in file:
        line = line.strip()
        if "ERROR" in line:
            print(line)
            counter += 1
            errors.append(line)

print(f" El total de errores es : {counter}")
for error_line in errors:
    print(error_line)

    #Imprimo la fecha del error 
    error_date = re.search(r"\d+-\d+-\d+", error_line)
    print(error_date.group())

    #Imprimo la hora del error 
    error_time = re.search(r"\d+:\d+:\d+", error_line)
    print(error_time.group())

    #Imprimo el ID de la maquina 
    machine_id = re.search(r"[A-Z]+-\d+", error_line)
    print(machine_id.group())

    #Imprimo el error
    error_match = re.search(r"\[ERROR\] [A-Z]+-\d+", error_line)
    error_code = error_match.group().replace("[ERROR] ", "")
    print(error_code) 
