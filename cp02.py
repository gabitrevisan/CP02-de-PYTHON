# Por Eduardo Andrade (RM99758), Gabriel Doms (RM98630), Gabriela Trevisan (RM99500), Leonardo Correia (RM550413) e Rafael Franck (RM550875)
# Turma ESPY

# Apresentação e boas-vindas
print('Bem-vindo à Vinheria Agnello')
print('Atualmente, nossas opções de menu de acesso interno são:')
print('1. Compra de Suprimentos')
print('2. Controle de Estoque')
# Seleção de menus (Compra de Suprimentos (1) ou Controle de Estoque (2))
menu = int(input('Selecione qual menu deseja acessar: '))

match menu:
# Caso seja selecionado o menu (1)
    case 1:
        print('')
        print('Você acessou a página de Compra de Suprimentos!')
# Mostrar a quantidade de vinhos que existe no estoque
        print('O nosso estoque do dia é esse:')
        print('1 - Porto Burton’s Ruby (100 garrafas disponíveis)')
        print('2 - Frisante Mosketto White (111 garrafas disponíveis)')
        print('3 - Rosé Marqués de Casa Concha (202 garrafas disponíveis)')
        print('4 - Chardonnay Benjamin Nieto (77 garrafas disponíveis)')
        print('5 - Sauvignon Blanc (34 garrafas disponíveis)')
# Informar o lugar do qual será comprado (Nome + CNPJ + Endereço)
        nome_empresa = input('Por favor, informe o nome da empresa vendedora: ')
        cnpj_empresa = int(input('Informe o CNPJ da empresa vendedora (APENAS NÚMEROS): '))
        endereco_empresa = input('Digite o endereço da empresa vendedora: ')
# Perguntar endereço de entrega
        endereco_entrega = input('Informe o endereço de entrega: ')
# Apresentar possibilidades de compra
        print('')
        print('Esses são os vinhos disponíveis para a compra, e seus respectivos valores')
        print('1 - Porto Burtons Ruby (R$65.00)')
        print('2 - Frisante Mosketto White (R$ 80,00)')
        print('3 - Rosé Marqués de Casa Concha (R$ 125,00)')
        print('4 - Chardonnay Benjamin Nieto (R$ 69,00)')
        print('5 - Sauvignon Blanc (R$ 22,00)')

        preco_vinhos = [65.0, 80.0, 125.0, 69.0, 22.0]  
        quantidade_vinhos = [0, 0, 0, 0, 0]
        total_compra = 0.0
# Questionar qual vinho está sendo comprado
        while True:
            opcao = input('Digite o número do vinho que deseja comprar (ou "pronto" para finalizar a compra): ')
            if opcao.lower() == 'pronto':
                break
            elif not opcao.isnumeric() or int(opcao) < 1 or int(opcao) > 5:
                print('Opção inválida, por favor digite novamente.')
            else:
                quantidade = int(input('Digite a quantidade de garrafas: '))
                quantidade_vinhos[int(opcao)-1] += quantidade
                total_compra += preco_vinhos[int(opcao)-1] * quantidade
# Informar a data de entrega e valor do frete
        if total_compra < 20.0:
            print('Você não adicionou nenhuma garrafa de vinho no carrinho.')
        else:
            print(f'Valor total da compra: R${total_compra:.2f}')
            if total_compra > 200.0:
                print('Frete grátis!')
                print('Sua compra será entregue em até 11 dias úteis.')
            else:
                frete = 22.0
                total_compra += frete
                print(f'Valor do frete: R${frete:.2f}')
                print(f'Valor total com frete: R${total_compra:.2f}')
                print('Sua compra será entregue em até 11 dias úteis.')
# Informar a quantidade de vinhos que está sendo comprada
            print(f'Você adicionou ao carrinho de compras {sum(quantidade_vinhos)} garrafas de vinho. Isso deu um valor de R${total_compra:.2f}.')
            confirmacao = int(input('Deseja confirmar a compra de reposição de estoque? Digite "1" para "Sim" e "0" para "Não": '))
            if confirmacao < 1:
                print('Sua compra não foi confirmada.')
# Finalizar a Compra de Suprimentos
            else:
                print(f'Você comprou {sum(quantidade_vinhos)} garrafas de vinho, no valor total de R${total_compra:.2f}, na empresa {(nome_empresa)}.')
                print(f'Seus vinhos serão entregues no endereço: {endereco_entrega}')

# Caso seja selecionado o menu (2)
    case 2:
        print('')
        print('Você acessou a página de Controle de Estoque!')
# Exibir sub-menu (Informar vendas realizadas no dia (A), Informar compras de suprimentos realizadas no dia (B) ou Mostrar o Estoque Inicial (C))
        print('Nesta seção possuímos 3 sub-menus; são eles:')
        print('A. Informar vendas realizadas no dia')
        print('B. Informar compra de suprimentos realizadas no dia')
        print('C. Mostrar o estoque inicial')
        print('')
        while True:
            sub_menu = input('Por favor, informe qual sub-menu deseja acessar: ')
# Caso seja escolhido o sub-menu (A)
            if sub_menu == 'A' or sub_menu == "a":
                print('Você escolheu o sub-menu A - Informar vendas realizadas no dia')
# Informar qual vinho foi vendido naquele dia
                print('')
                print('Esses são os possíveis vinhos vendidos e seus respectivos códigos')
                print('Porto Burtons Ruby (Código = 1)')
                print('Frisante Mosketto White (Código = 2)')
                print('Rosé Marqués de Casa Concha (Código = 3)')
                print('Chardonnay Benjamin Nieto (Código = 4)')
                print('Sauvignon Blanc (Código = 5)')
                print('')
                while True:
                    vinho_vendido = input('Informe o código do vinho vendido (ou "pronto" para finalizar o processo): ')
                    if vinho_vendido.lower() == 'pronto':
                        break
                    elif not vinho_vendido.isnumeric() or int(vinho_vendido) < 1 or int(vinho_vendido) > 5:
                        print('Opção inválida, por favor digite novamente.')
# Informar a quantidade do vinho vendido naquele dia
                    else:
                        quantidade_vinhovendido = int(input('Informe a quantidade do vinho vendido (APENAS NÚMEROS): '))
# Apresentar dados do cliente (nome, telefone, endereço e CPF)
                        nome_cliente = input('Qual é do nome do cliente que comprou o vinho?: ')
                        telefone_cliente = int(input('Informe o telefone-celular do cliente (APENAS NÚMEROS): '))
                        cpf_cliente = int(input('Informe o CPF do cliente (APENAS NÚMEROS): '))
# Confirmar informações
                        print(f'Você adicionou que foram vendidas {quantidade_vinhovendido} garrafas de vinho do vinho {vinho_vendido} para o o cliente {nome_cliente}.')
                        confirmacao_vinhovendido = int(input('Deseja confirmar essa informação? Digite "1" para "Sim" e "0" para "Não": '))
                        if confirmacao_vinhovendido < 1:
                            print('As informações não foram atualizadas.')
                            break
                        else:
                            print('As informações foram atualizadas com sucesso!')
                            break
# Caso seja escolhido o sub-menu (B)
            elif sub_menu == 'B' or sub_menu == "b":
                print('Você escolheu o sub-menu B - Informar compra de suprimentos realizadas no dia')
# Informar qual vinho foi comprado naquele dia
                print('')
                print('Esses são os possíveis vinhos comprados e seus respectivos códigos')
                print('Porto Burtons Ruby (Código = 1)')
                print('Frisante Mosketto White (Código = 2)')
                print('Rosé Marqués de Casa Concha (Código = 3)')
                print('Chardonnay Benjamin Nieto (Código = 4)')
                print('Sauvignon Blanc (Código = 5)')
                print('')
                while True:
                    vinho_comprado = input('Informe o código do vinho comprado (ou "pronto" para finalizar o processo): ')
                    if vinho_comprado.lower() == 'pronto':
                        break
                    elif not vinho_comprado.isnumeric() or int(vinho_comprado) < 1 or int(vinho_comprado) > 5:
                        print('Opção inválida, por favor digite novamente.')
# Informar qa quantidade do vinho comprado naquele dia
                    else:
                        quantidade_vinhocomprado = int(input('Informe a quantidade do vinho vendido (APENAS NÚMEROS): '))
# Apresentar nome e CNPJ da empresa vendedora
                        nome_empresavendedora = input('Qual é do nome da empresa que vendeu o vinho?: ')
                        cnpj_empresavendedora = int(input('Informe o CNPJ da empresa que vendeu o vinho (APENAS NÚMEROS): '))
# Confirmar informações
                        print(f'Você adicionou que foram compradas {quantidade_vinhocomprado} garrafas de vinho do vinho {vinho_comprado} da empresa {nome_empresavendedora}.')
                        confirmacao_vinhocomprado = int(input('Deseja confirmar essa informação? Digite "1" para "Sim" e "0" para "Não": '))
                        if confirmacao_vinhocomprado < 1:
                            print('As informações não foram atualizadas.')
                            break
                        else:
                            print('As informações foram atualizadas com sucesso!')
                            break
# Caso seja escolhido o sub-menu C
            elif sub_menu == 'C' or sub_menu == "c":
                print('Você escolheu o sub-menu C - Mostrar o estoque inicial')
                print('')
                print('No início do dia, este era nosso estoque:')
                print('1 - Porto Burton’s Ruby (100 garrafas disponíveis)')
                print('2 - Frisante Mosketto White (111 garrafas disponíveis)')
                print('3 - Rosé Marqués de Casa Concha (202 garrafas disponíveis)')
                print('4 - Chardonnay Benjamin Nieto (77 garrafas disponíveis)')
                print('5 - Sauvignon Blanc (34 garrafas disponíveis)')
                break
# Caso seja escolhido um sub-menu inexistente 
            else:
                print('Opção inválida. Por favor, escolha uma opção válida (A, B ou C)')
            break

# Caso seja selecionado um menu inexistente
    case _:
        print('Opção inexistente!')