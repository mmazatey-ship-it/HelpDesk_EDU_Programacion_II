# Justificacion de relaciones del modelo HelpDesk EDU

## User y Ticket: solicitante

La asociacion `User "1" -- "0..*" Ticket` indica que cada ticket tiene exactamente un solicitante y que un usuario puede no tener tickets o solicitar muchos. Ambas entidades mantienen identidad propia: el usuario existe aunque no tenga tickets y un ticket conserva la referencia de su solicitante.

## User y Ticket: tecnico asignado

La asociacion `User "0..1" -- "0..*" Ticket` indica que un ticket puede no tener tecnico al crearse o tener un unico tecnico asignado. Un tecnico puede estar asociado con cero o muchos tickets. El tecnico no depende del ticket para existir.

## Ticket y Comment

La composicion `Ticket "1" *-- "0..*" Comment` indica que un ticket contiene cero o muchos comentarios y que cada comentario pertenece a un unico ticket. El rombo negro se coloca del lado de `Ticket` porque es el todo. Si se elimina el ticket, sus comentarios dejan de tener contexto y se eliminan con el.

## Ticket y History

La composicion `Ticket "1" *-- "0..*" History` indica que un ticket contiene cero o muchos registros de historial y que cada registro pertenece a un unico ticket. El rombo negro se coloca del lado de `Ticket`. El historial depende del ciclo de vida del ticket porque registra solamente sus cambios y eventos.

## User y Article

La asociacion `User "1" -- "0..*" Article` indica que cada articulo tiene un autor y que un usuario puede publicar cero o muchos articulos. El usuario y el articulo tienen identidad independiente, por lo que no existe composicion.
