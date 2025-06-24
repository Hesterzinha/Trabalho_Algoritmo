from eventos import consultar_evento
participantes = []
ids_participantes = set()


def adicionar_participante(id_participante, nome, email):
    if id_participante in ids_participantes:
        print(f"ID '{id_participante}' já está em uso.")
        return None

    novo_participante = {
        'id': id_participante,
        'nome': nome,
        'email': email,
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
    if not participantes:
        print("Nenhum participante cadastrado.")
    else:
        for participante in participantes:
            print(f"ID: {participante['id']}, Nome: {participante['nome']}, Email: {participante['email']}, Eventos: {len(participante['eventos_inscritos'])}")
            
            
def editar_participante(id_participante, novo_nome=None, novo_email=None):
    participante = consultar_participante(id_participante)
    if not participante:
        print(f"Participante com ID {id_participante} não encontrado.")
        return None
    
    if novo_nome:
        participante['nome'] = novo_nome
    if novo_email:
        participante['email'] = novo_email
        
    print(f"Participante {id_participante} atualizado com sucesso.")
    return participante


def remover_participante(id_participante):
    global participantes
    participantes = [participante for participante in participantes if participante['id'] != id_participante]
    ids_participantes.discard(id_participante)
    
    
def inscrever_evento(id_participante, codigo_evento):
    participante = consultar_participante(id_participante)
    evento = consultar_evento(codigo_evento)
    
    if not participante or not evento:
        return False

    if codigo_evento in participante['eventos_inscritos']:
        print("Participante já está inscrito neste evento.")
        return False

    participante['eventos_inscritos'].append(codigo_evento)
    evento['participantes'].append(id_participante)
    return True