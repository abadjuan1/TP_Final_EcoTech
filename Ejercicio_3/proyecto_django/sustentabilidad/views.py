from django.shortcuts import render
from .metricas import obtener_metricas_consumo


def vista_panel_sustentabilidad(request):
    registros = [
        {"planta": "Norte", "consumo_kwh": 1200},
        {"planta": "Sur", "consumo_kwh": 850},
        {"planta": "Este", "consumo_kwh": 1400}
    ]

    metricas = obtener_metricas_consumo(registros)

    contexto = {
        "total_emisiones": metricas["total_emisiones"],
        "planta_mayor_consumo": metricas["planta_mayor_consumo"],
        "registros": registros
    }

    return render(request, "sustentabilidad/panel.html", contexto)
