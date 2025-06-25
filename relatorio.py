from eventos import eventos
from participantes import participantes


def estatisticas():
    total_inscricoes = sum(len(evento['participantes']) for evento in eventos)
    media = total_inscricoes / len(eventos)

    if not eventos:
        print("Sem eventos cadastrados.")
        return

    print("\n=== ESTATÍSTICAS BÁSICAS ===")
    print(f"- Eventos: {len(eventos)}")
    print(f"- Participantes: {len(participantes)}")
    print(f"- Inscrições: {total_inscricoes}")
    print(f"- Média por evento: {media:.1f}")


def top_eventos(qtd=3):
    print(f"\n=== TOP {qtd} EVENTOS MAIS CHEIOS ===")
    mais_cheios = sorted(eventos, key=lambda e: len(e['participantes']), reverse=True)[:qtd]
    for e in mais_cheios:
        print(f"  {e['nome']} ({len(e['participantes'])} inscritos)")


def participantes_mais_ativos(qtd=3):
    print(f"\n=== TOP {qtd} PARTICIPANTES MAIS ATIVOS ===\n")
    mais_ativos = sorted(participantes, key=lambda p: len(p['eventos_inscritos']), reverse=True)[:qtd]
    for p in mais_ativos:
        print(f"  {p['nome']} ({len(p['eventos_inscritos'])} eventos)")


def eventos_com_poucos_participantes():
    poucos = [e for e in eventos if len(e['participantes']) < 3]
    if poucos:
        print("\n=== EVENTOS COM <3 PARTICIPANTES ===")
        for e in poucos:
            print(f"  {e['nome']} (Código {e['codigo']})")


def participantes_sem_evento(qtd=3):
    sem_evento = [p for p in participantes if not p['eventos_inscritos']]
    if sem_evento:
        print(f"\n=== PARTICIPANTES SEM INSCRIÇÃO (mostrando até {qtd}) ===")
        for p in sem_evento[:qtd]:
            print(f"  {p['nome']} (ID {p['id']})")