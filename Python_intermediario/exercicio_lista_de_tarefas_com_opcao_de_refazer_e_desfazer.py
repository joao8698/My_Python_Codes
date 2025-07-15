# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import os
import json

def adicionar(tarefa ,lista):
    lista.append(tarefa)

def listar(lista):
    if not lista:
        print()
        print('Nada para listar')
        print()
        return
    print()
    print(*lista, sep='\n')
    print()

def desfazer(desfazer, lista):
    if not lista:
        print()
        print('Nada para desfazer')
        print()
        return
    tarefa = lista.pop()
    salvar(lista, CAMINHO_ARQUIVO)
    desfazer.append(tarefa)

def refazer(desfazer, lista):
    if not desfazer:
        print()
        print('Nada para refazer')
        print()
        return
    tarefa = desfazer.pop()
    lista.append(tarefa)
    salvar(lista, CAMINHO_ARQUIVO)

def ler(lista, caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo nao existe!')
        salvar(lista, caminho_arquivo)
        return []
    except json.JSONDecodeError:
        print('Arquivo corrompido ou vazio. Reiniciando...')
        salvar([], caminho_arquivo)
        return []

def salvar(lista, caminho_arquivo):
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(lista, arquivo, indent=2, ensure_ascii=False)

CAMINHO_ARQUIVO = 'banco_de_tarefas.json'
lista_de_tarefas = ler([], CAMINHO_ARQUIVO)
desfazer_var = []

while True:
    user_input = input('Comandos (listar, desfazer, refazer, sair)\nDigite uma tarefa ou comando: ').strip().lower()
    print()

    comandos = {
        'listar': lambda: listar(lista_de_tarefas),
        'desfazer': lambda: desfazer(desfazer_var, lista_de_tarefas),
        'refazer': lambda: refazer(desfazer_var, lista_de_tarefas),
    }

    if user_input == 'sair':
        print('Saindo....')
        exit()
    elif user_input in comandos:
        comandos[user_input]()  # Chama o comando correspondente
    elif user_input == '':
        print('Voce nao digitou nenhuma tarefa!')
    else:
        adicionar(user_input, lista_de_tarefas)
        salvar(lista_de_tarefas, CAMINHO_ARQUIVO)
        desfazer_var.clear()  # Limpa histórico de desfazer ao adicionar nova tarefa


    # if user_input == 'listar':
    #     listar(lista_de_tarefas)
    #     continue
    # elif user_input == 'desfazer':
    #     desfazer(desfazer_var, lista_de_tarefas)
    #     continue
    # elif user_input == 'refazer':
    #     refazer(desfazer_var, lista_de_tarefas)
    #     continue
    # elif user_input == 'sair':
    #     exit()
    # else:
    #     if user_input == '':
    #         print('Voce nao digitou nenhuma tarefa!')
    #         continue
    #     else:
    #         lista_de_tarefas.append(user_input)