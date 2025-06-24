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
    
    
def consultar_participante(id_participante):
    for participante in participantes:
        if participante['id'] == id_participante:
            return participante
    return None

def listar_participantes():
    if not participantes:
        print("Nenhum participante cadastrado.")
    else:
        for participante in participantes:
            print(f"ID: {participante['id']}, Nome: {participante['nome']}, Email: {participante['email']}, Eventos: {len(participante['eventos_inscritos'])}")