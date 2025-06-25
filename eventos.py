from participantes import participantes
eventos = []
ids_eventos = set()


def adicionar_evento(codigo, nome, data):
    if codigo in ids_eventos:
        print("Evento com esse código já existe.")
        return None

    novo_evento = {
        'codigo': codigo,
        'nome': nome,
        'data': data,
        'participantes': []
    }

    eventos.append(novo_evento)
    print(f"Evento {nome} cadastrado com sucesso.")
    ids_eventos.add(codigo)
    return novo_evento


def consultar_evento(codigo_evento):
    for evento in eventos:
        if evento['codigo'] == codigo_evento:
            return evento
    return None


def listar_eventos():
    if not eventos:
        print("Nenhum evento cadastrado.")
    else:
        for evento in eventos:
            print(
                f"Código: {evento['codigo']}, Nome: {evento['nome']}, Data: {evento['data']}, Participantes: {len(evento['participantes'])}")


def editar_evento(codigo, novo_nome=None, nova_data=None):
    evento = consultar_evento(codigo)
    if not evento:
        print("Evento não encontrado.")
        return None

    if novo_nome:
        evento['nome'] = novo_nome
    if nova_data:
        evento['data'] = nova_data
    print(f"Evento {codigo} atualizado com sucesso.")
    return evento


def remover_evento(codigo):
    global eventos
    evento = next((e for e in eventos if e['codigo'] == codigo), None)
    if not evento:
        print("Evento não encontrado.")
        return None

    [p['eventos_inscritos'].remove(
        codigo) for p in participantes if codigo in p['eventos_inscritos']]
    eventos = [e for e in eventos if e['codigo'] != codigo]
    ids_eventos.discard(codigo)
    print(f"Evento {codigo} removido com sucesso.")