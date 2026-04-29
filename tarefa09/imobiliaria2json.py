from xml.dom.minidom import parse
import json

dom = parse("imobiliaria.xml")
imobiliaria = dom.documentElement

imoveis = imobiliaria.getElementsByTagName('imovel')