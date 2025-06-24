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