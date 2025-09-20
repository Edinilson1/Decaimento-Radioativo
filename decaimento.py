from InquirerPy import inquirer
import json
import time

tempo = ["0.001x", "0.01x", "0.1x", "1x", "10x", "100x", "1000x", "10000x", "100000x", "1000000x", "10000000x", "100000000x", "1000000000x"]

with open("isotopos_radioativos.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

nomes_isotopos = [elemento["isótopo"] for elemento in dados]

choice = inquirer.select(
    message="Selecione um elemento:",
    choices=nomes_isotopos,
).execute()

isotopo = next((item for item in dados if item["isótopo"] == choice), None)

if isotopo:
    hl = isotopo['meia_vida_segundos']
else:
    print("Erro")

timemultiplier = inquirer.select(
    message="Selecione o tempo da simulação:",
    choices=tempo,
    default=tempo[3]
).execute()

timemultiplier = float(timemultiplier.replace("x", ""))

novohl = hl/timemultiplier

massa = float(input("Digite a massa do elemento em Quilos: "))

intervalo = 0.1
tempoacumulado = 0

start = time.time()

while massa > 0.001:
    print(f"\r{massa}", end="", flush=True)



    time.sleep(intervalo)
    tempoacumulado += intervalo
    temporeal = time.time() - start

    if tempoacumulado > novohl:
        massa /= 2
        tempoacumulado = 0

print()
print(f"{isotopo['isótopo']} com meia vida de {isotopo["meia_vida_segundos"]} segundos com tempo de simulação {timemultiplier}, demorou {temporeal:.2f} segundos para decair abaixo de 0.001 quilos")