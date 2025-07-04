from eventos import consultar_evento
from participantes import consultar_participante


def inscrever(id_participante, codigo_evento):
    participante = consultar_participante(id_participante)
    evento = consultar_evento(codigo_evento)

    if not participante or not evento:
        return print("Participante ou evento não encontrado.")

    if codigo_evento in participante['eventos_inscritos']:
        print("Participante já está inscrito neste evento.")
        return None

    participante['eventos_inscritos'].append(codigo_evento)
    evento['participantes'].append(id_participante)
    return True
