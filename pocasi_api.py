#Zjistete maximální denní teplotu.
#Vytvořte funkce, která vám umožní pohybovat se v jednotlivých informacích.
#To znamená, že každá informace bude mít vlastní funkci
#Api klíč vložte do samostatného souboru auth.py a naimportujte ho do hlavního scripti api.py
#Vytvořte if __name__ == "main":
#Z příkazové řádky zadávejte Mesto a zkratku zeme.
#                                                  mesto, znacka  klic pro autorizaci
# 'http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=d7fbd888f435c075cdd7d5a28ed0c899'
import os
import json


def save_api_key(url: str) -> None:
    key = url.split("APPID=")[1]
    with open("auth.py", "w") as f:
        f.write(key)


def get_api_key() -> str:
    try:
        with open("auth.py", "r") as f:
            key = f.readline()
            return key
    except:
        print("Nenalezen API key!")
        exit()


def read_actual_data(key: str):
    pass


def main():
    # if not os.path.exists("auth.py"):
    #    save_api_key('http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=d7fbd888f435c075cdd7d5a28ed0c899')

    read_actual_data(get_api_key())


if __name__ == "__main__":
    main()
