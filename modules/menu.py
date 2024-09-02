from time import sleep
import os
import json

pessoas = []

def cabecalho(msg):
    print()
    print('-' * 30)
    print(msg.center(30))
    print('-' * 30)

def salvar_pessoas():
    with open('cadastro.json', 'w') as arquivo:
        json.dump(pessoas, arquivo)

def carregar_pessoas():
    try:
        if os.path.exists('cadastro.json'):
            with open('cadastro.json', 'r') as arquivo:
                return json.load(arquivo)
        else:
            return []
    except json.JSONDecodeError:
        print("Erro ao carregar o arquivo cadastro.json. Arquivo corrompido ou invalido.")
        return []
    except FileNotFoundError:
        return []

def main():
    global pessoas
    pessoas = carregar_pessoas()
    while True:
        cabecalho('MENU PRINCIPAL')
        opcoes = [
            'Listar pessoas',
            'Cadastrar pessoa',
            'Sair'
        ]               
        for c, opcao in enumerate(opcoes):
            print(f'{c + 1} - {opcao}')
        print()
        try:
            resp = int(input('Escolha uma opcao: '))
            if resp not in range(1, len(opcoes) + 1):
                print('Opcao inválida. Tente novamente.\n')
                sleep(1)
            else:
                sleep(1)
                if resp == 1:
                    cabecalho(opcoes[resp-1])
                    if not pessoas:
                        print('Nenhuma pessoa foi cadastrada.\n')
                    else:
                        print(f"{'Nome':<20}{'Idade':>10}")
                        print('-' * 30)
                        for pessoa in pessoas:
                            for nome, idade in pessoa.items():
                                print(f"{nome:<20}{idade:>5} anos")
                    print()
                elif resp == 2:
                    while True:                        
                        pessoa = {}
                        nome = input('Insira o nome: ')
                        idade = int(input('Insira a idade: '))
                        pessoa[nome] = idade
                        pessoas.append(pessoa)
                        print(f'{nome} adcionado(a) com sucesso.\n')
                        opcao = str(input('Deseja continuar inserindo dados? S/N: ')).strip().lower()
                        while opcao not in ['s', 'n']:
                            opcao = str(input('Opção errada! Deseja continuar inserindo dados? S/N: ')).strip().lower()
                        if opcao in 'n':
                            break
                elif resp == 3:
                    confirmacao = str(input('Tem certeza que deseja sair? S/N: ')).strip().lower()
                    if confirmacao in 's':
                        print('Saindo do sistema...')
                        sleep(1)
                        salvar_pessoas()
                        break
        except (ValueError, TypeError):
            print('Opcao invalida. Tente novamente.\n')
            sleep(1)

