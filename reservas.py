from config import AFORO_MAXIMO

reservas = []

def registrar_reserva(estudiante):
    if len(reservas) >= AFORO_MAXIMO:
        print("No hay cupos disponibles")
        return

    reservas.append(estudiante)
    print("Reserva registrada para:", estudiante)


def mostrar_reservas():
    print("Reservas registradas:", len(reservas))
    print("Cupos disponibles:", AFORO_MAXIMO - len(reservas))


if __name__ == "__main__":
    registrar_reserva("Estudiante 1")
    registrar_reserva("Estudiante 2")
    mostrar_reservas()