class Usuario:
    def __init__(self, identificador, nombre, email, rol):
        self.id = identificador
        self.nombre = nombre
        self.email = email
        self.rol = rol

    def __str__(self):
        return f"{self.nombre} ({self.rol})"


class Ticket:
    ESTADOS_VALIDOS = ["Open", "In Progress", "Resolved", "Closed", "Cancelled"]

    def __init__(self, identificador, titulo, categoria, prioridad, solicitante):
        self.id = identificador
        self.titulo = titulo
        self.categoria = categoria
        self.prioridad = prioridad
        self.solicitante = solicitante
        self.tecnico = None
        self._estado = "Open"

    @property
    def estado(self):
        return self._estado

    def asignar_tecnico(self, tecnico):
        if tecnico.rol.lower() != "technician":
            raise ValueError("El usuario debe tener el rol technician.")
        self.tecnico = tecnico

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado not in self.ESTADOS_VALIDOS:
            raise ValueError("Estado no permitido.")
        self._estado = nuevo_estado

    def __str__(self):
        tecnico = self.tecnico.nombre if self.tecnico else "Sin asignar"
        return (
            f"#{self.id} | {self.titulo} | Categoria: {self.categoria} | "
            f"Prioridad: {self.prioridad} | Solicitante: {self.solicitante.nombre} | "
            f"Tecnico: {tecnico} | Estado: {self.estado}"
        )
