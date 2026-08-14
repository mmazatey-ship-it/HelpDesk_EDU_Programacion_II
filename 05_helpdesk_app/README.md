# 05_helpdesk_app

## Estructura

- `modelos.py`: clases `Usuario` y `Ticket`.
- `servicios.py`: operaciones para registrar, listar, buscar, asignar tecnico y cambiar estado.
- `main.py`: menu de consola y punto de entrada.

## Ejecucion

```text
python main.py
```

## Flujo probado

1. Registrar el ticket 201.
2. Asignar el tecnico disponible al ticket 201.
3. Cambiar el estado del ticket 201 a `In Progress`.
4. Listar el ticket y verificar solicitante, tecnico y estado.
