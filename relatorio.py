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

