def pedir_opcion():
    print("\n1. Registrar ticket")
    print("2. Listar tickets")
    print("3. Buscar por solicitante")
    print("4. Resumen por prioridad")
    print("5. Salir")
    return input("Seleccione una opcion: ").strip()


def pedir_numero_ticket(tickets):
    while True:
        try:
            numero = int(input("Numero de ticket: ").strip())
            if numero <= 0:
                print("El numero debe ser mayor que cero.")
            elif any(ticket["numero"] == numero for ticket in tickets):
                print("El numero de ticket ya existe.")
            else:
                return numero
        except ValueError:
            print("Ingrese un numero de ticket valido.")


def pedir_campo(nombre):
    while True:
        valor = input(f"{nombre}: ").strip()
        if valor:
            return valor
        print(f"{nombre} es obligatorio.")


def pedir_valor_permitido(nombre, valores):
    valores_normalizados = {valor.lower(): valor for valor in valores}
    while True:
        respuesta = input(f"{nombre} ({', '.join(valores)}): ").strip().lower()
        if respuesta in valores_normalizados:
            return valores_normalizados[respuesta]
        print(f"{nombre} invalida.")


def registrar_ticket(tickets):
    categorias = ["General", "Hardware", "Software", "Network"]
    prioridades = ["Low", "Medium", "High", "Critical"]
    ticket = {
        "numero": pedir_numero_ticket(tickets),
        "solicitante": pedir_campo("Solicitante"),
        "titulo": pedir_campo("Titulo"),
        "descripcion": pedir_campo("Descripcion"),
        "categoria": pedir_valor_permitido("Categoria", categorias),
        "prioridad": pedir_valor_permitido("Prioridad", prioridades),
        "status": "Open",
    }
    tickets.append(ticket)
    print("Ticket registrado correctamente.")


def listar_tickets(tickets):
    if len(tickets) == 0:
        print("No hay tickets registrados.")
        return

    print("\nTickets registrados")
    for ticket in tickets:
        print(
            f"#{ticket['numero']} | {ticket['titulo']} | "
            f"Solicitante: {ticket['solicitante']} | "
            f"Prioridad: {ticket['prioridad']} | Estado: {ticket['status']}"
        )


def buscar_por_solicitante(tickets):
    solicitante = input("Solicitante a buscar: ").strip()
    encontrados = [
        ticket
        for ticket in tickets
        if ticket["solicitante"].lower() == solicitante.lower()
    ]

    if len(encontrados) == 0:
        print("No se encontraron tickets para el solicitante indicado.")
        return

    print(f"\nTickets de {solicitante}:")
    for ticket in encontrados:
        print(f"#{ticket['numero']} | {ticket['titulo']} | {ticket['status']}")


def mostrar_resumen(tickets):
    prioridades = ["Low", "Medium", "High", "Critical"]
    print("\nResumen por prioridad")
    for prioridad in prioridades:
        cantidad = sum(1 for ticket in tickets if ticket["prioridad"] == prioridad)
        print(f"{prioridad}: {cantidad}")


def ejecutar_menu():
    tickets = []
    while True:
        opcion = pedir_opcion()
        if opcion == "1":
            registrar_ticket(tickets)
        elif opcion == "2":
            listar_tickets(tickets)
        elif opcion == "3":
            buscar_por_solicitante(tickets)
        elif opcion == "4":
            mostrar_resumen(tickets)
        elif opcion == "5":
            print("Fin del programa.")
            break
        else:
            print("Opcion invalida.")


if __name__ == "__main__":
    ejecutar_menu()
