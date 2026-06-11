import zeep

# define a URL do WSDL
wsdl_url = "http://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"

# inicializa o cliente zeep
client = zeep.Client(wsdl=wsdl_url)

# define o código do país para BR
numero = input("Digite o número que deseja converter: ")

# faz a chamada do serviço
result = client.service.NumberToWords(
	ubiNum=numero
)
# imprime o resultado
print(f"{result}")