class User:
    def __init__(self, identificador, nombre, email, rol):
        self.id = identificador
        self.nombre = nombre
        self.email = email
        self.rol = rol
        self.articles = []

    def solicitar_ticket(self, identificador, titulo, categoria, prioridad):
        return Ticket(identificador, titulo, categoria, prioridad, self)

    def publicar_articulo(self, identificador, titulo, contenido):
        articulo = Article(identificador, titulo, contenido, self)
        self.articles.append(articulo)
        return articulo


class Ticket:
    def __init__(self, identificador, titulo, categoria, prioridad, solicitante):
        self.id = identificador
        self.titulo = titulo
        self.categoria = categoria
        self.prioridad = prioridad
        self.solicitante = solicitante
        self.tecnico = None
        self.estado = "Open"
        self.comments = []
        self.history = []

    def asignar_tecnico(self, tecnico):
        self.tecnico = tecnico
        self.agregar_historial(f"Tecnico asignado: {tecnico.nombre}")

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        self.agregar_historial(f"Estado cambiado a {nuevo_estado}")

    def agregar_comentario(self, identificador, autor, mensaje, fecha):
        comentario = Comment(identificador, autor, mensaje, fecha)
        self.comments.append(comentario)
        return comentario

    def agregar_historial(self, accion, fecha="Sin fecha"):
        registro = History(len(self.history) + 1, accion, fecha)
        self.history.append(registro)
        return registro


class Comment:
    def __init__(self, identificador, autor, mensaje, fecha):
        self.id = identificador
        self.autor = autor
        self.mensaje = mensaje
        self.fecha = fecha

    def editar(self, mensaje):
        self.mensaje = mensaje


class History:
    def __init__(self, identificador, accion, fecha):
        self.id = identificador
        self.accion = accion
        self.fecha = fecha

    def registrar_accion(self, accion):
        self.accion = accion


class Article:
    def __init__(self, identificador, titulo, contenido, autor):
        self.id = identificador
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor

    def actualizar_contenido(self, contenido):
        self.contenido = contenido


def main():
    solicitante = User(1, "Ana Lopez", "ana.lopez@umg.edu.gt", "student")
    tecnico = User(2, "Luis Perez", "luis.perez@umg.edu.gt", "technician")
    ticket = solicitante.solicitar_ticket(201, "Sin acceso a plataforma", "Software", "High")
    ticket.asignar_tecnico(tecnico)
    comentario = ticket.agregar_comentario(1, solicitante, "Se registro el incidente.", "2026-08-14")
    ticket.cambiar_estado("In Progress")
    articulo = tecnico.publicar_articulo(1, "Acceso a plataforma", "Verifique las credenciales.")

    print(f"Ticket: {ticket.id} | Estado: {ticket.estado}")
    print(f"Tecnico: {ticket.tecnico.nombre}")
    print(f"Comentario: {comentario.mensaje}")
    print(f"Historial: {ticket.history[-1].accion}")
    print(f"Articulo: {articulo.titulo}")


if __name__ == "__main__":
    main()
