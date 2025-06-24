participantes = []
ids_participantes = set()

def adicionar_participante(id_participante, nome, email):
    if id_participante in ids_participantes:
        print(f"ID '{id_participante}' já está em uso. Escolha outro.")
        return None

    novo_participante = {
        'id': id_participante,
        'nome': nome,
        'email': email,
        'eventos_inscritos': []
    }
    participantes.append(novo_participante)
    ids_participantes.add(id_participante)
