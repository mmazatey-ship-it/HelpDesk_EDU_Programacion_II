from modelos import Usuario
from servicios import asignar_tecnico, cambiar_estado, listar_tickets, registrar_ticket


def pedir_campo(nombre):
    while True:
        valor = input(f"{nombre}: ").strip()
        if valor:
            return valor
        print(f"{nombre} es obligatorio.")


def pedir_entero(nombre):
    while True:
        try:
            valor = int(input(f"{nombre}: ").strip())
            if valor > 0:
                return valor
            print("El valor debe ser mayor que cero.")
        except ValueError:
            print("Ingrese un numero valido.")


def mostrar_menu():
    print("\n1. Registrar ticket")
    print("2. Asignar tecnico")
    print("3. Cambiar estado")
    print("4. Listar tickets")
    print("5. Salir")
    return input("Seleccione una opcion: ").strip()


def ejecutar_menu():
    solicitante = Usuario(1, "Ana Lopez", "ana.lopez@umg.edu.gt", "student")
    tecnico = Usuario(2, "Luis Perez", "luis.perez@umg.edu.gt", "technician")
    tickets = []

    print(f"Solicitante disponible: {solicitante}")
    print(f"Tecnico disponible: {tecnico}")

    while True:
        opcion = mostrar_menu()
        try:
            if opcion == "1":
                identificador = pedir_entero("Identificador")
                titulo = pedir_campo("Titulo")
                categoria = pedir_campo("Categoria")
                prioridad = pedir_campo("Prioridad")
                ticket = registrar_ticket(
                    tickets,
                    identificador,
                    titulo,
                    categoria,
                    prioridad,
                    solicitante,
                )
                print(f"Ticket registrado: {ticket.id}")
            elif opcion == "2":
                identificador = pedir_entero("Identificador del ticket")
                ticket = asignar_tecnico(tickets, identificador, tecnico)
                print(f"Tecnico asignado a ticket {ticket.id}.")
            elif opcion == "3":
                identificador = pedir_entero("Identificador del ticket")
                nuevo_estado = pedir_campo("Nuevo estado")
                ticket = cambiar_estado(tickets, identificador, nuevo_estado)
                print(f"Estado actualizado a {ticket.estado}.")
            elif opcion == "4":
                registros = listar_tickets(tickets)
                if len(registros) == 0:
                    print("No hay tickets registrados.")
                else:
                    for ticket in registros:
                        print(ticket)
            elif opcion == "5":
                print("Fin del programa.")
                break
            else:
                print("Opcion invalida.")
        except ValueError as error:
            print(f"Operacion no realizada: {error}")


if __name__ == "__main__":
    ejecutar_menu()
