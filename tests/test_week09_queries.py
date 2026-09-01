from app.models.enums import TicketStatus
from app.services.tickets import TicketService


def create_ticket(service, title, category, requester_id=1):
    return service.create(
        title=title,
        description="Caso de prueba",
        category=category,
        priority="Medium",
        requester_id=requester_id,
    )


def test_list_by_technician_returns_only_assigned_tickets():
    service = TicketService()
    first = create_ticket(service, "No imprime", "Hardware")
    second = create_ticket(service, "No ingresa", "Software")
    service.assign_technician(ticket_id=first.id, technician_id=10)
    service.assign_technician(ticket_id=second.id, technician_id=20)

    assert service.list_by_technician(10) == [first]


def test_list_by_category_returns_only_matching_category():
    service = TicketService()
    hardware = create_ticket(service, "No imprime", "Hardware")
    create_ticket(service, "No ingresa", "Software")

    assert service.list_by_category("hardware") == [hardware]


def test_list_by_status_returns_only_matching_status():
    service = TicketService()
    open_ticket = create_ticket(service, "Caso abierto", "General")
    resolved_ticket = create_ticket(service, "Caso resuelto", "General")
    service.update_status(resolved_ticket.id, TicketStatus.RESOLVED)

    assert service.list_by_status("open") == [open_ticket]
    assert service.list_by_status(TicketStatus.RESOLVED) == [resolved_ticket]


def test_queries_return_empty_list_when_no_ticket_matches():
    service = TicketService()
    create_ticket(service, "No imprime", "Hardware")

    assert service.list_by_technician(99) == []
    assert service.list_by_category("Red") == []
    assert service.list_by_status("closed") == []


def test_status_query_accepts_spaces_and_rejects_unknown_values():
    service = TicketService()
    ticket = create_ticket(service, "Caso en proceso", "Software")
    service.update_status(ticket.id, "In Progress")

    assert service.list_by_status("in progress") == [ticket]

    try:
        service.list_by_status("unknown")
    except ValueError as error:
        assert str(error) == "Estado no permitido."
    else:
        raise AssertionError("Se esperaba un estado no permitido")
