import csv
from datetime import datetime
import re

# 1. Cargar la cronología completa del archivo en memoria
all_lines = []
with open("data_machine_A.txt", 'r', encoding='utf-8') as file:
    for line in file:
        all_lines.append(line.strip())

# 2. Emparejar cada ERROR con su respectivo R-000 y calcular downtime
downtimes = []
counter = 0

for i, line in enumerate(all_lines):
    if "ERROR" in line:
        counter += 1
        error_date = re.search(r"\d+-\d+-\d+", line)
        error_time = re.search(r"\d+:\d+:\d+", line)
        error_dt = datetime.strptime(f"{error_date.group()} {error_time.group()}", "%Y-%m-%d %H:%M:%S")
        error_machine = re.search(r"[A-Z]+-\d+", line).group()

        # Buscar la recuperación de la misma máquina
        for next_line in all_lines[i + 1:]:
            next_machine_match = re.search(r"[A-Z]+-\d+", next_line)
            if next_machine_match and next_machine_match.group() == error_machine and "R-000" in next_line:
                recovery_date = re.search(r"\d+-\d+-\d+", next_line)
                recovery_time = re.search(r"\d+:\d+:\d+", next_line)
                recovery_dt = datetime.strptime(f"{recovery_date.group()} {recovery_time.group()}", "%Y-%m-%d %H:%M:%S")

                downtime_seconds = (recovery_dt - error_dt).total_seconds()
                downtime_minutes = int(downtime_seconds / 60)

                downtimes.append((error_machine, downtime_minutes))
                break

# 3. Mostrar resumen en consola
print(f"El total de errores es : {counter}")
for machine, minutes in downtimes:
    print(f"{machine}: {minutes} minutos de downtime")

# 4. Exportar a CSV (Fase 5)
with open("downtime_report.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Machine", "Downtime minutes"])
    writer.writerows(downtimes)

print("Reporte downtime_report.csv generado con éxito.")
