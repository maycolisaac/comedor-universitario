
from config import PRECIO_RACION, AFORO_MAXIMO

def generar_reporte(raciones_vendidas):
    ingresos = raciones_vendidas * PRECIO_RACION
    disponibles = AFORO_MAXIMO - raciones_vendidas

    print("=== REPORTE COMEDOR UNIVERSITARIO ===")
    print("Raciones vendidas:", raciones_vendidas)
    print("Ingresos: S/", f"{ingresos:.2f}")
    print("Capacidad máxima:", AFORO_MAXIMO)
    print("Raciones disponibles:", disponibles)

if __name__ == "__main__":
    generar_reporte(25)
