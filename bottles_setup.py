class Bottles:
    def __init__(self):
        self.name = ""
        self.defesa = 0
        self.pneu = 0
        self.controle = 0
        self.largada = 0
        self.manutencao = 0
        self.pitstop = 0
        self.ultrapassagem = 0
        self.energia = 0
        self.velocidade = 0

    def imprimir(self):
        atributos = vars(self)  # Obtém um dicionário dos atributos da instância
        for atributo, valor in atributos.items():
            if valor != 0:
                print(f"{atributo}: {valor}")
        print()