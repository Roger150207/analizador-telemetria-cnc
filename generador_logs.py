import random
from datetime import datetime, timedelta

# Datos base de los errores 
fails = ["ERROR-101: fake_temperature", "ERROR-102: low_pressure_hydraulic", "ERROR-103: fail_motor"]
info_messages = ["start_cycle", "monitoring_stable", "piece_completed"]
machines = ["CNC-01", "CNC-02", "ROBOT-07"]


def escribir_linea(file, log_time, machine, level, message):
    timestamp = log_time.strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"{timestamp} [{machine}] [{level}] {message}\n"
    file.write(log_line)


def generar_log(file_name, lines=100):
    # Fecha de inicio simulada (Año, Mes, Dia, Hora, Min, Seg)
    current_time = datetime(2026, 10, 23, 6, 0, 0)

    # archivos
    with open(file_name, 'w', encoding='utf-8') as file:
        for _ in range(lines):

            is_failure = random.random() < 0.10

            if is_failure:
                machine = random.choice(machines)
                message = random.choice(fails)
                escribir_linea(file, current_time, machine, "ERROR", message)

                repair_time = random.randint(15, 60)
                current_time += timedelta(minutes=repair_time)

                escribir_linea(file, current_time, machine, "INFO", "R-000 production_resumed")

                time_jump = random.randint(1, 5)
                
            else:
                machine = random.choice(machines)
                message = random.choice(info_messages)
                escribir_linea(file, current_time, machine, "INFO", message)
                time_jump = random.randint(1, 5)

            current_time += timedelta(minutes=time_jump)

if __name__ == "__main__":
    print("Simulating machine CNC...")
    generar_log("data_machine_A.txt", lines=50)
    print("Log create succesfuly.")

