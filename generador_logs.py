import random
from datetime import datetime, timedelta

# 1. Datos base de los errores 
fails = ["ERROR-101: fake_temperature", "ERROR-102: low_pressure_hydraulic", "ERROR-103: fail_motor"]
mensajes_info = ["start_cycle", "monitoring_stable", "piece_completed"]
maquinas = ["CNC-01", "CNC-02", "ROBOT-07"]


def escribir_linea(archivo, tiempo, maquina, nivel, mensaje):
    marca_tiempo = tiempo.strftime("%Y-%m-%d %H:%M:%S")
    linea_log = f"{marca_tiempo} [{maquina}] [{nivel}] {mensaje}\n"
    archivo.write(linea_log)


def generar_log(nombre_archivo, lineas=100):
    # 2. Fecha de inicio simulada (Año, Mes, Dia, Hora, Min, Seg)
    tiempo_actual = datetime(2026, 10, 23, 6, 0, 0)

    # 3. Manejo de archivos
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        for _ in range(lineas):

            # 4. Lógica de probabilidad: 90% del tiempo opera normal, 10% falla
            es_falla = random.random() < 0.10

            if es_falla:
                maquina = random.choice(maquinas)
                mensaje = random.choice(fails)
                escribir_linea(archivo, tiempo_actual, maquina, "ERROR", mensaje)

                tiempo_reparacion = random.randint(15, 60)
                tiempo_actual += timedelta(minutes=tiempo_reparacion)

                escribir_linea(archivo, tiempo_actual, maquina, "INFO", "R-000 production_resumed")

                salto_tiempo = random.randint(1, 5)
                
            else:
                maquina = random.choice(maquinas)
                mensaje = random.choice(mensajes_info)
                escribir_linea(archivo, tiempo_actual, maquina, "INFO", mensaje)
                salto_tiempo = random.randint(1, 5)

            tiempo_actual += timedelta(minutes=salto_tiempo)


# 7. Punto de entrada (Equivalente al main)
if __name__ == "__main__":
    print("Simulando máquina CNC...")
    generar_log("datos_maquina_A.txt", lineas=50)
    print("Log generado con éxito.")