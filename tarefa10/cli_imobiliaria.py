import json


with open("imobiliaria.json", "r",encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

imoveis = dados["imobiliaria"]["imoveis"]

for i in range(len(imoveis)):
    print(i + 1, "-", imoveis[i]["descricao"])


op = int(input("Digite o número do imóvel: "))

imovel = imoveis[op - 1]

print("\nDESCRIÇÃO:", imovel["descricao"])

print("\nPROPRIETÁRIO:")
print("Nome:", imovel["proprietario"].get("nome"))
print("Telefone:", imovel["proprietario"].get("telefone"))
print("Email:", imovel["proprietario"].get("email"))

print("\nENDEREÇO:")
print("Rua:", imovel["endereco"].get("rua"))
print("Número:", imovel["endereco"].get("numero"))
print("Bairro:", imovel["endereco"].get("bairro"))
print("Cidade:", imovel["endereco"].get("cidade"))

print("\nCARACTERÍSTICAS:")
print("Tamanho:", imovel["caracteristicas"].get("tamanho"),"m²")
print("Quartos:", imovel["caracteristicas"].get("numQuartos"))
print("Banheiros:", imovel["caracteristicas"].get("numBanheiros"))

print("\nVALOR:", imovel["valor"])