from dataclasses import dataclass, field

from .enums import TicketStatus


@dataclass
class Ticket:
    id: int
    title: str
    description: str
    category: str
    priority: str
    requester_id: int
    assignee_id: int | None = None
    status: TicketStatus = TicketStatus.OPEN
    comments: list[str] = field(default_factory=list)
