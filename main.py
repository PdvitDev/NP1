import os
import platform
import random

#apenas para estetica
def limpar_terminal():
    sistema = platform.system()

    if sistema == "Windows":
        os.system('cls')

    else:
        os.system('clear')

def quiz(perguntas):
    pontuacao = 0
    #percorre perguntas
    random.shuffle(perguntas)

    for pergunta in perguntas:
        print(pergunta["pergunta"])

        #percorre os dicts dentro de perguntas

        for i, alternativa in enumerate(pergunta["alternativas"]):
            print(f"{i + 1}. {alternativa}")#mostra e formata as alternativas
        resposta_usuario = int(input("Sua resposta (digite o numero): "))

        #verificacao da resposta do usuario
        if resposta_usuario == pergunta["resposta_correta"]:
            limpar_terminal()
            print("Resposta correta!")
            pontuacao += 1
        else:
            limpar_terminal()
            print("Resposta incorreta!")

    print(f"Voce acertou {pontuacao} de {len(perguntas)} perguntas!")

def main():
    #list onde dentro de cada index tem um dict
    perguntas = [{
        "pergunta" : "Qual operador lógico em Python é usado para negar uma condição?",
        "alternativas" :["and", "or", "not"], #list
        "resposta_correta": 3,
    },
    {
        "pergunta" : "Qual das seguintes estruturas de controle de fluxo é usada para repetir um bloco de código várias vezes em Python?",
        "alternativas" :["if", "for", "else"],
        "resposta_correta": 2,
    },
    {
        "pergunta" : "Qual o nome do tipo de dado que respresenta numeros inteiros?",
        "alternativas" :["int", "float", "string"],
        "resposta_correta": 1,
    },
    {
        "pergunta" : "Qual tipo de dado que um float armazena?",
        "alternativas" :["caracteres", "listas ordenadas", "numeros flutuantes"],
        "resposta_correta": 3,
    },
    {
        "pergunta" : "Como se declara uma variavel em python?",
        "alternativas" :["var a = 1", "a == 1", "a = 1"],
        "resposta_correta": 3,
    },
    ]

    quiz(perguntas)
main()
