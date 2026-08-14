def pedir_numero_ticket():
    while True:
        try:
            numero = int(input("Numero de ticket: ").strip())
            if numero > 0:
                return numero
            print("El numero debe ser mayor que cero.")
        except ValueError:
            print("Ingrese un numero de ticket valido.")


def pedir_campo(nombre):
    while True:
        valor = input(f"{nombre}: ").strip()
        if valor:
            return valor
        print(f"{nombre} es obligatorio.")


def pedir_opcion(nombre, opciones):
    opciones_normalizadas = {opcion.lower(): opcion for opcion in opciones}
    while True:
        valor = input(f"{nombre} ({', '.join(opciones)}): ").strip().lower()
        if valor in opciones_normalizadas:
            return opciones_normalizadas[valor]
        print(f"{nombre} invalida. Opciones: {', '.join(opciones)}.")


def main():
    categorias = ["General", "Hardware", "Software", "Network"]
    prioridades = ["Low", "Medium", "High", "Critical"]

    ticket = {
        "numero": pedir_numero_ticket(),
        "solicitante": pedir_campo("Solicitante"),
        "titulo": pedir_campo("Titulo"),
        "descripcion": pedir_campo("Descripcion"),
        "categoria": pedir_opcion("Categoria", categorias),
        "prioridad": pedir_opcion("Prioridad", prioridades),
        "status": "Open",
    }

    print("\nTicket registrado")
    print(f"Numero: {ticket['numero']}")
    print(f"Solicitante: {ticket['solicitante']}")
    print(f"Titulo: {ticket['titulo']}")
    print(f"Descripcion: {ticket['descripcion']}")
    print(f"Categoria: {ticket['categoria']}")
    print(f"Prioridad: {ticket['prioridad']}")
    print(f"Estado: {ticket['status']}")


if __name__ == "__main__":
    main()
