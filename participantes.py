participantes = [
    {
        'id': 'P001',
        'nome': 'Alice Silva',
        'email': 'alice@gmail.com',
        'preferencia_tematica': 'Tecnologia, IA',
        'eventos_inscritos': []
    },
    {
        'id': 'P002',
        'nome': 'Bruno Costa',
        'email': 'bruno.costa@hotmail.com',
        'preferencia_tematica': 'Programação, Desenvolvimento Web',
        'eventos_inscritos': []
    },
    {
        'id': 'P003',
        'nome': 'Carla Mendes',
        'email': 'carla.m@gmail.com',
        'preferencia_tematica': 'Design, UX/UI',
        'eventos_inscritos': []
    }
]
ids_participantes = {p['id'] for p in participantes}


def adicionar_participante(id_participante, nome, email, preferencia_tematica=None):
    if id_participante in ids_participantes:
        print(f"ID '{id_participante}' já está em uso.")
        return None

    novo_participante = {
        'id': id_participante,
        'nome': nome,
        'email': email,
        'preferencia_tematica': preferencia_tematica,
        'eventos_inscritos': []
    }
    participantes.append(novo_participante)
    print(f"Participante {nome} adicionado com sucesso.")
    ids_participantes.add(id_participante)


def consultar_participante(id_participante):
    for participante in participantes:
        if participante['id'] == id_participante:
            return participante
    return None


def listar_participantes():
    print('\n Lista de Participantes:\n')
    for participante in participantes:
        print(
            f"ID: {participante['id']}, Nome: {participante['nome']}, Email: {participante['email']}, Preferência Temática: {participante['preferencia_tematica']} , Inscritos no(s) eventos: {participante['eventos_inscritos']}")


def editar_participante(id_participante, **kwargs):
    participante = consultar_participante(id_participante)
    if not participante:
        print(f"Participante com ID {id_participante} não encontrado.")
        return None

    for novo in ['nome', 'email', 'preferencia_tematica']:
        if novo in kwargs and kwargs[novo]:
            participante[novo] = kwargs[novo]

    print(f"Participante {id_participante} atualizado com sucesso.")
    return participante


def remover_participante(id_participante):
    from eventos import eventos
    global participantes

    for evento in eventos:
        if id_participante in evento['participantes']:
            evento['participantes'].remove(id_participante)
    participantes = [
        participante for participante in participantes if participante['id'] != id_participante]
    ids_participantes.discard(id_participante)
    print(f"Participante {id_participante} removido com sucesso.")
