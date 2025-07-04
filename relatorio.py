from eventos import eventos
from participantes import participantes


def estatisticas():
    total_inscricoes = sum(len(evento['participantes']) for evento in eventos)
    media = total_inscricoes / len(eventos)

    if not eventos:
        print("Sem eventos cadastrados.")
        return

    print("\n ESTATÍSTICAS BÁSICAS \n")
    print(f"- Eventos: {len(eventos)}")
    print(f"- Participantes: {len(participantes)}")
    print(f"- Inscrições: {total_inscricoes}")
    print(f"- Média por evento: {media:.1f}")


def top_eventos():
    print(f"\n TOP EVENTOS MAIS CHEIOS \n")
    mais_cheios = sorted([e for e in eventos if e['participantes']],
                         key=lambda e: len(e['participantes']), reverse=True)
    if not mais_cheios:
        return print("Nenhum evento com participantes inscritos.")
    for e in mais_cheios:
        print(f" {e['nome']} ({len(e['participantes'])} inscritos)")


def participantes_mais_ativos():
    print(f"\n TOP PARTICIPANTES MAIS ATIVOS \n")
    mais_ativos = sorted([p for p in participantes if p['eventos_inscritos']],
                         key=lambda p: len(p['eventos_inscritos']), reverse=True)
    if not mais_ativos:
        return print("Nenhum participante inscrito nos eventos.")
    for p in mais_ativos:
        print(f"  {p['nome']} ({len(p['eventos_inscritos'])} eventos)")


def eventos_com_poucos_participantes():
    poucos = [e for e in eventos if len(e['participantes']) < 2]
    if poucos:
        print("\n EVENTOS COM MENOS DE 2 PARTICIPANTES \n")
        for e in poucos:
            print(
                f"  {e['nome']} (Código {e['codigo']}) com {len(e['participantes'])} inscritos")


def participantes_sem_evento():
    sem_evento = [p for p in participantes if not p['eventos_inscritos']]
    if not sem_evento:
        return print("\nTodos os participantes estão inscritos em pelo menos um evento.")
    elif sem_evento:
        print("\n PARTICIPANTES SEM INSCRIÇÃO \n")
        for p in sem_evento:
            print(f"  {p['nome']} (ID {p['id']})")


def eventos_sem_participante():
    sem_participantes = [e for e in eventos if not e['participantes']]
    if not sem_participantes:
        return print("\nTodos os eventos possuem pelo menos um participante inscrito.")
    elif sem_participantes:
        print("\n EVENTOS SEM INSCRIÇÃO \n")
        for e in sem_participantes:
            print(f" Id: {e['codigo']}, Nome: {e['nome']}")
