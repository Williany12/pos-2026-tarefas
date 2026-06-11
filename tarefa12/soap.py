import requests
from xml.dom.minidom import parseString

url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

op = input("Digite 1 para o código telefônico, 2 para a capital do país ou 3 para ver a bandeira do país: ")

if op == '1':
    operacao = "CountryIntPhoneCode"
elif op == '2':
    operacao = "CapitalCity"
elif op == '3':
    operacao = "CountryFlag"
else:
    print("Digite um número válido!")

country_code = input("Digite o código do país: ").upper()

payload = f"""<?xml version="1.0" encoding="utf-8"?>
            <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/\">
            <soap:Body>
                <{operacao} xmlns="http://www.oorsprong.org/websamples.countryinfo">
                    <sCountryISOCode>{country_code}</sCountryISOCode>
                </{operacao}>
            </soap:Body>
        </soap:Envelope>"""

#headers
headers = {
	'Content-Type': 'text/xml; charset=utf-8'
}
# request POST
response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
print(response)

if response.status_code == 200:
    if op == '1':
        print("O código telefônico do país é: " + parseString(response.text).documentElement.getElementsByTagName("m:CountryIntPhoneCodeResult")[0].firstChild.nodeValue)

    if op =='2':
        print("A capital do país é: " + parseString(response.text).documentElement.getElementsByTagName("m:CapitalCityResult")[0].firstChild.nodeValue)

    if op == '3':
        print("A bandeira do país é:" + parseString(response.text).documentElement.getElementsByTagName("m:CountryFlagResult")[0].firstChild.nodeValue)
