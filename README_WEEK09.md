# Semana 9: consultas de tickets

La iteración agrega consultas del servicio de tickets para responder preguntas del negocio usando las relaciones del ticket.

## Consultas

- `list_by_technician(technician_id)` devuelve únicamente los tickets asignados al técnico indicado.
- `list_by_category(category)` devuelve únicamente los tickets de la categoría solicitada, sin distinguir mayúsculas ni minúsculas.
- `list_by_status(status)` acepta texto o `TicketStatus` y devuelve únicamente los tickets con ese estado.

## Validación

```text
uv run pytest -q
```

Las pruebas cubren asignación, categoría, estado, resultados vacíos y normalización de estados.
