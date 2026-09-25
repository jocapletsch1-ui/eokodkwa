jogadores = []
gols = []


def requisitarDados():
    print("=== Bem-vindo ao Sistema de Cadastro ===")
    nome = input("Digite o nome do jogador: ")

    while True:
        try:
            quantidadeGols = int(input(f"Digite a quantidade de gols do {nome}"))
            break
        except ValueError:
            print("Por favor digite um número válido")

    jogadores.append(nome)
    gols.append(quantidadeGols)

    return nome, quantidadeGols

def calcularTotalGols(gols):
    if not gols:
        return 0
    
    quantidadeTotal = sum(gols)
    return quantidadeTotal

def calcularMediaGols():
    quantidadeJogadores = len(jogadores)
    quantidadeGols = len(gols)
    mediaTotal = quantidadeGols / quantidadeJogadores

    if quantidadeJogadores == 0:
        return 0

    if quantidadeGols > mediaTotal:
        print("Este jogador marcou mais que a média")
    return quantidadeJogadores, quantidadeGols
def encontrarArtilheiro(quantidadeGols):
    artilheiro = max(quantidadeGols)

    return artilheiro

def mostrarRelatorio(artilheiro):