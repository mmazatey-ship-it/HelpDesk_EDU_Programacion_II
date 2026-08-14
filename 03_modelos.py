class Usuario:
    def __init__(self, identificador, nombre, email, rol):
        self.id = identificador
        self.nombre = nombre
        self.email = email
        self.rol = rol

    def __str__(self):
        return f"Usuario {self.id}: {self.nombre} | {self.email} | Rol: {self.rol}"


class Ticket:
    ESTADOS_VALIDOS = ["Open", "In Progress", "Resolved", "Closed", "Cancelled"]

    def __init__(self, identificador, titulo, categoria, prioridad, solicitante, tecnico=None, estado="Open"):
        if estado not in self.ESTADOS_VALIDOS:
            raise ValueError("Estado inicial no permitido.")
        self.id = identificador
        self.titulo = titulo
        self.categoria = categoria
        self.prioridad = prioridad
        self.solicitante = solicitante
        self.tecnico = None
        self._status = estado
        if tecnico is not None:
            self.asignar_tecnico(tecnico)

    @property
    def status(self):
        return self._status

    def asignar_tecnico(self, tecnico):
        if tecnico.rol.lower() != "technician":
            raise ValueError("El usuario asignado debe tener el rol technician.")
        self.tecnico = tecnico

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado not in self.ESTADOS_VALIDOS:
            raise ValueError("Estado no permitido.")
        self._status = nuevo_estado

    def __str__(self):
        tecnico = self.tecnico.nombre if self.tecnico else "Sin asignar"
        return (
            f"Ticket {self.id}: {self.titulo} | Categoria: {self.categoria} | "
            f"Prioridad: {self.prioridad} | Solicitante: {self.solicitante.nombre} | "
            f"Tecnico: {tecnico} | Estado: {self._status}"
        )


def main():
    solicitante = Usuario(1, "Ana Lopez", "ana.lopez@umg.edu.gt", "student")
    tecnico = Usuario(2, "Luis Perez", "luis.perez@umg.edu.gt", "technician")

    ticket_1 = Ticket(101, "Sin acceso al correo", "Software", "High", solicitante)
    ticket_2 = Ticket(102, "Teclado sin respuesta", "Hardware", "Medium", solicitante)
    ticket_3 = Ticket(103, "Sin conexion de red", "Network", "Critical", solicitante)

    ticket_1.asignar_tecnico(tecnico)
    ticket_1.cambiar_estado("In Progress")

    try:
        ticket_2.cambiar_estado("Pendiente")
    except ValueError as error:
        print(f"Estado no actualizado: {error}")

    usuarios = [solicitante, tecnico]
    tickets = [ticket_1, ticket_2, ticket_3]

    print("Usuarios")
    for usuario in usuarios:
        print(usuario)

    print("\nTickets")
    for ticket in tickets:
        print(ticket)


if __name__ == "__main__":
    main()
