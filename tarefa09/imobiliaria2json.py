from xml.dom.minidom import parse
import json

dom = parse("imobiliaria.xml")
imobiliaria = dom.documentElement

imoveis = imobiliaria.getElementsByTagName('imovel')

dados = []

for i in imoveis:
    prop = i.getElementsByTagName("proprietario")[0]
    end = i.getElementsByTagName("endereco")[0]
    car = i.getElementsByTagName("caracteristicas")[0]

    telefones = []
    for t in prop.getElementsByTagName("telefone"):
        telefones.append(t.firstChild.data)

    email = None
    if prop.getElementsByTagName("email"):
        email = prop.getElementsByTagName("email")[0].firstChild.data

    numero = None
    if end.getElementsByTagName("número"):
        numero = end.getElementsByTagName("número")[0].firstChild.data

    item = {
        "descricao": i.getElementsByTagName("descricao")[0].firstChild.data,
        "proprietario": {
            "nome": prop.getElementsByTagName("nome")[0].firstChild.data,
            "telefones": telefones,
            "email": email
        },
        "endereco": {
            "rua": end.getElementsByTagName("rua")[0].firstChild.data,
            "bairro": end.getElementsByTagName("bairro")[0].firstChild.data,
            "cidade": end.getElementsByTagName("cidade")[0].firstChild.data,
            "numero": numero
        },
        "caracteristicas": {
            "tamanho": car.getElementsByTagName("tamanho")[0].firstChild.data,
            "quartos": car.getElementsByTagName("numQuartos")[0].firstChild.data,
            "banheiros": car.getElementsByTagName("numBanheiros")[0].firstChild.data
        },
        "valor": i.getElementsByTagName("valor")[0].firstChild.data
    }

    dados.append(item)

with open("imobiliaria.json", "w",encoding="utf-8") as f:
    json.dump(dados, f, indent=4)