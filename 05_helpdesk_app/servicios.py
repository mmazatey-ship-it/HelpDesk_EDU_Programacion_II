from modelos import Ticket


def registrar_ticket(tickets, identificador, titulo, categoria, prioridad, solicitante):
    if buscar_ticket(tickets, identificador) is not None:
        raise ValueError("El identificador de ticket ya existe.")
    ticket = Ticket(identificador, titulo, categoria, prioridad, solicitante)
    tickets.append(ticket)
    return ticket


def listar_tickets(tickets):
    return list(tickets)


def buscar_ticket(tickets, identificador):
    for ticket in tickets:
        if ticket.id == identificador:
            return ticket
    return None


def asignar_tecnico(tickets, identificador, tecnico):
    ticket = buscar_ticket(tickets, identificador)
    if ticket is None:
        raise ValueError("Ticket no encontrado.")
    ticket.asignar_tecnico(tecnico)
    return ticket


def cambiar_estado(tickets, identificador, nuevo_estado):
    ticket = buscar_ticket(tickets, identificador)
    if ticket is None:
        raise ValueError("Ticket no encontrado.")
    ticket.cambiar_estado(nuevo_estado)
    return ticket
