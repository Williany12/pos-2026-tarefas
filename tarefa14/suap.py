import requests
from getpass import getpass

api_url = "https://suap.ifrn.edu.br/api/"

user = input("user: ")
password = getpass()

data = {"username":user,"password":password}

response = requests.post(api_url+"token/pair", json=data)
token = response.json()["access"]
print(response.json())


headers = {
    "Authorization": f'Bearer {token}'
}

print(headers)
ano = input("Digite o ano: ")
periodo = input("Digite o período: ")
url = api_url+f"ensino/meu-boletim/{ano}/{periodo}/"
print(url)
response = requests.get(url, headers=headers)

disciplinas = response.json()["results"]
print()
print(f'{"Disciplina":<80} | {"N1":^5} | {"N2":^5} | {"N3":^5} | {"N4":^5}')
print("-" * 115)

for disciplina in disciplinas:
    print(
        f'{disciplina["disciplina"]:<80} |'
        f'{str(disciplina["nota_etapa_1"]["nota"]):^6} |'
        f'{str(disciplina["nota_etapa_2"]["nota"]):^6} |'
        f'{str(disciplina["nota_etapa_3"]["nota"]):^6} |'
        f'{str(disciplina["nota_etapa_4"]["nota"]):^6} |'
    )
