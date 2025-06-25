from eventos import eventos
from participantes import participantes


def estatisticas_basicas():
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


