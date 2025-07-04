import clear
from participantes import adicionar_participante, listar_participantes, editar_participante, remover_participante
from eventos import adicionar_evento, listar_eventos, editar_evento, remover_evento
from inscricao import inscrever
from relatorio import estatisticas, top_eventos, participantes_mais_ativos, eventos_com_poucos_participantes, participantes_sem_evento, eventos_sem_participante


def opcao(limite):
    while True:
        try:
            op = int(input("Digite a opção desejada: "))
            if 0 <= op <= limite:
                return op
            else:
                print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")


def menu_principal():
    while True:
        clear.clear()
        print('\n  MENU PRINCIPAL \n')
        print("1 - Participantes")
        print("2 - Eventos")
        print("3 - Inscrição")
        print("4 - Relatórios")
        print("0 - Sair")
        op = opcao(4)

        if op == 1:
            menu_participantes()

        elif op == 2:
            menu_eventos()

        elif op == 3:
            menu_inscricao()

        elif op == 4:
            menu_relatorios()

        elif op == 0:
            print("Saindo do sistema...")

            return exit()

        else:
            print("Opção inválida!")
            input("Pressione Enter para continuar...")


def menu_participantes():
    while True:
        clear.clear()
        print('\n MENU PARTICIPANTES \n')
        print("1 - Adicionar participante")
        print("2 - Listar participantes")
        print("3 - Editar participante")
        print("4 - Remover participante")
        print("0 - Voltar")
        op = opcao(4)

        if op == 1:
            id_participante = input("ID: ")
            nome = input("Nome: ")
            email = input("Email: ")
            preferencia_tematica = input("Preferência temática (opcional): ")
            adicionar_participante(id_participante, nome,
                                   email, preferencia_tematica or None)

        elif op == 2:
            listar_participantes()

        elif op == 3:
            id_participante = input("ID do participante: ")
            novo_nome = input("Novo nome (ou Enter para manter): ")
            novo_email = input("Novo email (ou Enter para manter): ")
            novo_preferencia = input(
                "Nova preferência temática (ou Enter para manter): ")
            editar_participante(id_participante, nome=novo_nome or None,
                                email=novo_email or None, preferencia_tematica=novo_preferencia or None)

        elif op == 4:
            id_participante = input("ID do participante a remover: ")
            remover_participante(id_participante)

        elif op == 0:
            break
        input("\n Pressione Enter para continuar...")


def menu_eventos():
    while True:
        clear.clear()
        print('\n  MENU EVENTOS \n')
        print("1 - Adicionar evento")
        print("2 - Listar eventos")
        print("3 - Editar evento")
        print("4 - Remover evento")
        print("0 - Voltar")
        op = opcao(4)

        if op == 1:
            codigo = input("Código do evento: ")
            nome = input("Nome do evento: ")
            data = input("Data do evento: ")
            tema = input("Tema do evento: ")
            adicionar_evento(codigo, nome, data, tema)
        elif op == 2:
            listar_eventos()
        elif op == 3:
            codigo = input("Código do evento: ")
            novo_nome = input("Novo nome (ou Enter para manter): ")
            nova_data = input("Nova data (ou Enter para manter): ")
            novo_tema = input("Novo tema (ou Enter para manter): ")

            editar_evento(codigo, nome=novo_nome or None,
                          data=nova_data or None, tema=novo_tema or None)
        elif op == 4:
            codigo = input("Código do evento a remover: ")
            remover_evento(codigo)
        elif op == 0:
            break
        input("\nPressione Enter para continuar...")


def menu_inscricao():
    while True:
        clear.clear()
        print('\n  MENU INSCRIÇÃO \n')
        id_participante = input("ID do participante: ")
        codigo_evento = input("Código do evento: ")

        if inscrever(id_participante, codigo_evento):
            print("Inscrição realizada com sucesso.")
        else:
            print("Falha na inscrição.")

        op = input("\nDeseja inscrever outro? (s/n): ").lower()
        if op == 'n':
            break
        elif op != 's':
            print("Opção inválida, voltando ao menu principal.")
            break


def menu_relatorios():
    while True:
        clear.clear()
        print('\n  MENU RELATÓRIOS \n')
        print("1 - Estatísticas gerais")
        print("2 - Top eventos mais cheios")
        print("3 - Participantes mais ativos")
        print("4 - Eventos com poucos menos de 2 participantes")
        print("5 - Participantes sem evento")
        print("6 - eventos sem Participantes")
        print("0 - Voltar")
        op = opcao(6)

        if op == 1:
            estatisticas()
        elif op == 2:
            top_eventos()
        elif op == 3:
            participantes_mais_ativos()
        elif op == 4:
            eventos_com_poucos_participantes()
        elif op == 5:
            participantes_sem_evento()
        elif op == 6:
            eventos_sem_participante()
        elif op == 0:
            break
        else:
            print("Opção inválida!")
        input("\nPressione Enter para continuar...")
