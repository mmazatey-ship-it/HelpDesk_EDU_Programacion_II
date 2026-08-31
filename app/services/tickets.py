from app.models.entities import Ticket
from app.models.enums import TicketStatus


class TicketService:
    def __init__(self):
        self._tickets: list[Ticket] = []
        self._next_id = 1

    def create(
        self,
        title: str,
        description: str,
        category: str,
        priority: str,
        requester_id: int,
    ) -> Ticket:
        ticket = Ticket(
            id=self._next_id,
            title=title,
            description=description,
            category=category,
            priority=priority,
            requester_id=requester_id,
        )
        self._tickets.append(ticket)
        self._next_id += 1
        return ticket

    def assign_technician(self, ticket_id: int, technician_id: int) -> Ticket:
        ticket = self._find(ticket_id)
        ticket.assignee_id = technician_id
        return ticket

    def update_status(self, ticket_id: int, status: str | TicketStatus) -> Ticket:
        ticket = self._find(ticket_id)
        ticket.status = self._normalize_status(status)
        return ticket

    def list_by_technician(self, technician_id: int) -> list[Ticket]:
        return [ticket for ticket in self._tickets if ticket.assignee_id == technician_id]

    def list_by_category(self, category: str) -> list[Ticket]:
        expected = self._normalize_text(category)
        return [ticket for ticket in self._tickets if self._normalize_text(ticket.category) == expected]

    def list_by_status(self, status: str | TicketStatus) -> list[Ticket]:
        expected = self._normalize_status(status)
        return [ticket for ticket in self._tickets if ticket.status == expected]

    def _find(self, ticket_id: int) -> Ticket:
        for ticket in self._tickets:
            if ticket.id == ticket_id:
                return ticket
        raise ValueError("Ticket no encontrado.")

    @staticmethod
    def _normalize_text(value: str) -> str:
        return " ".join(value.strip().casefold().split())

    @staticmethod
    def _normalize_status(status: str | TicketStatus) -> TicketStatus:
        if isinstance(status, TicketStatus):
            return status
        value = status.strip().casefold().replace(" ", "_")
        try:
            return TicketStatus(value)
        except ValueError as error:
            raise ValueError("Estado no permitido.") from error
