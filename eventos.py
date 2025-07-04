from participantes import participantes

eventos = [
    {
        'codigo': 'EVT001',
        'nome': 'Introdução à IA',
        'data': '2025-07-15',
        'tema': 'Inteligência Artificial',
        'participantes': []
    },
    {
        'codigo': 'EVT002',
        'nome': 'Workshop de Web Design',
        'data': '2025-08-01',
        'tema': 'Web',
        'participantes': []
    },
    {
        'codigo': 'EVT003',
        'nome': 'Cybersegurança para Iniciantes',
        'data': '2025-09-10',
        'tema': 'Segurança',
        'participantes': []
    }
]
ids_eventos = {e['codigo'] for e in eventos}


def adicionar_evento(codigo, nome, data, tema):
    global ids_eventos
    if codigo in ids_eventos:
        print("Evento com esse código já existe.")
        return None

    novo_evento = {
        'codigo': codigo,
        'nome': nome,
        'data': data,
        'tema': tema,
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
    for evento in eventos:
        print(
            f"Código: {evento['codigo']}, Nome: {evento['nome']}, Tema: {evento['tema']}, Data: {evento['data']}, Participantes: {evento['participantes']} \n")


def editar_evento(codigo, **kwargs):
    evento = consultar_evento(codigo)
    if not evento:
        print("Evento não encontrado.")
        return None

    for novo in ['nome', 'data', 'tema']:
        if novo in kwargs and kwargs[novo]:
            evento[novo] = kwargs[novo]

    print(f"Evento {codigo} atualizado com sucesso.")
    return evento


def remover_evento(codigo):
    global eventos, ids_eventos
    evento = next((e for e in eventos if e['codigo'] == codigo), None)
    if not evento:
        print("Evento não encontrado.")
        return None

    [p['eventos_inscritos'].remove(
        codigo) for p in participantes if codigo in p['eventos_inscritos']]
    eventos = [e for e in eventos if e['codigo'] != codigo]
    if codigo in ids_eventos:
        ids_eventos.discard(codigo)
    print(f"Evento {codigo} removido com sucesso.")
