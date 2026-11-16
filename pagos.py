from datetime import datetime
from config import PRECIO_RACION

def registrar_pago(estudiante, cantidad):
    total = PRECIO_RACION * cantidad

    print("=== TICKET COMEDOR UNIVERSITARIO ===")
    print("Estudiante:", estudiante)
    print("Cantidad:", cantidad)
    print("Total: S/", f"{total:.2f}")
    print("Fecha:", datetime.now().strftime("%d/%m/%Y %H:%M"))

registrar_pago("Estudiante UNAMBA", 2)