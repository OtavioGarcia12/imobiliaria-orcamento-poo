import csv

class Imovel:
    def __init__(self, tipo):
        self.tipo = tipo
        self.valor = 0

    def calcular(self, quartos, garagem, vagas, possui_crianca):
        if self.tipo == "apartamento":
            self.valor = 700
            if quartos == 2:
                self.valor += 200
            if garagem:
                self.valor += 300
            if not possui_crianca:
                self.valor *= 0.95

        elif self.tipo == "casa":
            self.valor = 900
            if quartos == 2:
                self.valor += 250
            if garagem:
                self.valor += 300

        elif self.tipo == "estudio":
            self.valor = 1200
            if vagas >= 2:
                self.valor += 250
                if vagas > 2:
                    self.valor += (vagas - 2) * 60

        return self.valor

    def gerar_csv(self):
        with open("orcamento.csv", "w", newline="") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(["Parcela", "Valor"])
            for i in range(1, 13):
                writer.writerow([i, self.valor])


# ===== PROGRAMA PRINCIPAL =====

print("=== ORÇAMENTO IMOBILIÁRIA R.M ===")

tipo = input("Tipo (apartamento/casa/estudio): ").lower()

quartos = 1
garagem = False
vagas = 0
possui_crianca = True

if tipo in ["apartamento", "casa"]:
    quartos = int(input("Quartos (1 ou 2): "))
    garagem = input("Garagem? (s/n): ").lower() == "s"

if tipo == "apartamento":
    possui_crianca = input("Possui criança? (s/n): ").lower() == "s"

if tipo == "estudio":
    vagas = int(input("Quantidade de vagas: "))

imovel = Imovel(tipo)
valor = imovel.calcular(quartos, garagem, vagas, possui_crianca)

print(f"\nValor mensal: R$ {valor:.2f}")
print("Contrato: R$ 2000 (até 5x de R$ 400.00)")

imovel.gerar_csv()
print("Arquivo orcamento.csv gerado.")
