# EJERCICIO 1 - SANITIZACION Y ANALISIS DE SENSORES

def limpiar_registro_sensor(registro_raw):
    """Limpia los datos de un sensor y devuelve un diccionario nuevo."""
    sensor_id = registro_raw.get("sensor_id", "SIN-ID")
    temperatura = registro_raw.get("temperatura", "0")
    ubicacion = registro_raw.get("ubicacion", "Ubicacion desconocida")

    # Quitamos espacios y la letra C de la temperatura.
    sensor_id = str(sensor_id).strip()
    temperatura = str(temperatura).strip().replace("C", "").strip()

    # Convertimos la temperatura de texto a numero decimal.
    temperatura = float(temperatura)

    # Si la ubicacion esta vacia, usamos el valor por defecto.
    ubicacion = str(ubicacion).strip()
    if ubicacion == "":
        ubicacion = "Ubicacion desconocida"

    return {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion
    }


def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    """Devuelve los IDs en alerta y el promedio de temperatura."""
    lista_sensores_alerta = []
    suma_temperaturas = 0

    for sensor in lista_sensores_limpios:
        if sensor["temperatura"] > umbral_temperatura:
            lista_sensores_alerta.append(sensor["sensor_id"])

        suma_temperaturas += sensor["temperatura"]

    if len(lista_sensores_limpios) > 0:
        promedio_temperatura = suma_temperaturas / len(lista_sensores_limpios)
    else:
        promedio_temperatura = 0

    return (lista_sensores_alerta, promedio_temperatura)


# BLOQUE PRINCIPAL: probamos el recorrido completo.
if __name__ == "__main__":
    registros_crudos = [
        {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": " Planta Norte "},
        {"sensor_id": "SENSOR-002", "temperatura": "31.2C", "ubicacion": "Planta Sur"},
        {"sensor_id": " SENSOR-003 ", "temperatura": "28.0C"}
    ]

    sensores_limpios = []

    for registro in registros_crudos:
        sensor_limpio = limpiar_registro_sensor(registro)
        sensores_limpios.append(sensor_limpio)

    alertas, promedio = generar_resumen_sensores(sensores_limpios, 30.0)

    print("REPORTE DE SENSORES")
    print("-------------------")
    print("Sensores limpios:", sensores_limpios)
    print("Sensores en alerta:", alertas)
    print(f"Promedio de temperatura: {promedio:.2f} °C")