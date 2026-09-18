from abc import ABC, abstractmethod
from datetime import datetime


class IncidenciaNoEncontradaError(Exception):
    pass


class EstadoInvalidoError(Exception):
    pass


class Incidencia:
    ESTADOS_VALIDOS = {"Abierta", "En progreso", "Resuelta", "Cerrada"}

    def __init__(self, identificador, titulo, descripcion, categoria, prioridad):
        self._id = identificador
        self._titulo = titulo
        self._descripcion = descripcion
        self._categoria = categoria
        self._prioridad = prioridad
        self._estado = "Abierta"
        self._fecha_creacion = datetime.now()

    @property
    def id(self):
        return self._id

    @property
    def titulo(self):
        return self._titulo

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def categoria(self):
        return self._categoria

    @property
    def prioridad(self):
        return self._prioridad

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, nuevo_estado):
        if nuevo_estado not in self.ESTADOS_VALIDOS:
            raise EstadoInvalidoError(
                f"Estado no permitido: {nuevo_estado}."
            )
        self._estado = nuevo_estado

    @property
    def fecha_creacion(self):
        return self._fecha_creacion

    def __str__(self):
        return (
            f"#{self.id} | {self.titulo} | {self.categoria} | "
            f"Prioridad: {self.prioridad} | Estado: {self.estado}"
        )


class CanalNotificacion(ABC):
    @abstractmethod
    def notificar(self, mensaje: str) -> None:
        raise NotImplementedError


class NotificacionConsola(CanalNotificacion):
    def notificar(self, mensaje: str) -> None:
        print(f"[consola] {mensaje}")


class NotificacionEmailSimulado(CanalNotificacion):
    def notificar(self, mensaje: str) -> None:
        print(f"[email simulado] {mensaje}")


class GestorIncidencias:
    def __init__(self):
        self._incidencias = []
        self._siguiente_id = 1

    def crear_incidencia(
        self, titulo, descripcion, categoria, prioridad
    ) -> Incidencia:
        incidencia = Incidencia(
            self._siguiente_id,
            titulo,
            descripcion,
            categoria,
            prioridad,
        )
        self._incidencias.append(incidencia)
        self._siguiente_id += 1
        return incidencia

    def listar_incidencias(self) -> list[Incidencia]:
        return list(self._incidencias)

    def buscar_por_id(self, id_incidencia: int) -> Incidencia:
        for incidencia in self._incidencias:
            if incidencia.id == id_incidencia:
                return incidencia
        raise IncidenciaNoEncontradaError(
            f"No existe la incidencia con id {id_incidencia}."
        )

    def cambiar_estado(self, id_incidencia: int, nuevo_estado: str) -> None:
        incidencia = self.buscar_por_id(id_incidencia)
        incidencia.estado = nuevo_estado

    def eliminar_incidencia(self, id_incidencia: int) -> None:
        incidencia = self.buscar_por_id(id_incidencia)
        self._incidencias.remove(incidencia)


if __name__ == "__main__":
    gestor = GestorIncidencias()
    primera = gestor.crear_incidencia(
        "No inicia sesión",
        "El estudiante no puede ingresar al portal.",
        "Acceso",
        "Alta",
    )
    segunda = gestor.crear_incidencia(
        "No imprime constancia",
        "La constancia no se genera correctamente.",
        "Documentos",
        "Media",
    )

    gestor.cambiar_estado(primera.id, "En progreso")

    try:
        gestor.cambiar_estado(segunda.id, "Pendiente")
    except EstadoInvalidoError as error:
        print(f"Cambio rechazado: {error}")

    for incidencia in gestor.listar_incidencias():
        print(incidencia)

    mensaje = f"Se creó la incidencia #{primera.id}: {primera.titulo}"
    canales = [NotificacionConsola(), NotificacionEmailSimulado()]
    for canal in canales:
        canal.notificar(mensaje)
