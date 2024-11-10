# Classe Heroi para representar um herói no jogo
class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        # Definindo o ataque baseado no tipo do herói
        if self.tipo == "mago":
            ataque = "magia"
        elif self.tipo == "guerreiro":
            ataque = "espada"
        elif self.tipo == "monge":
            ataque = "artes marciais"
        elif self.tipo == "ninja":
            ataque = "shuriken"
        else:
            ataque = "ataque desconhecido"

        print(f"O {self.tipo} atacou usando {ataque}")

# Exemplo de uso da classe Heroi
if __name__ == "__main__":
    nome = input("Digite o nome do herói: ")
    idade = int(input("Digite a idade do herói: "))
    tipo = input("Digite o tipo do herói (mago, guerreiro, monge, ninja): ").lower()

    # Criando o herói com base nas informações fornecidas
    heroi = Heroi(nome, idade, tipo)

    # Realizando o ataque do herói
    heroi.atacar()
