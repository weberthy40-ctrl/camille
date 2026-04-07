import requests

DDRAGON_VERSION = "14.24.1"

def classificar_dificuldade(champ):
    ban = {"Darius", "Jax", "Renekton", "Volibear", "Poppy"}
    dificil = {
        "Fiora", "Aatrox", "Mordekaiser", "Irelia", "Riven", "Sett",
        "Tryndamere", "Illaoi", "Urgot", "Pantheon", "Jayce", "Gangplank",
        "Cassiopeia", "Heimerdinger", "Quinn", "Vayne", "Lucian", "Kalista",
        "Velkoz", "Xerath", "Brand", "Taliyah"
    }
    facil = {
        "Garen", "Malphite", "Sion", "Nasus", "Shen", "DrMundo",
        "ChoGath", "Maokai", "Teemo", "Ornn", "TahmKench", "Kayle"
    }

    if champ in ban:
        return "Sugiro Ban / Impossível"
    if champ in dificil:
        return "Difícil"
    if champ in facil:
        return "Fácil"
    return "Médio"

def fake_winrate(champ):
    base = 48 + (sum(ord(c) for c in champ) % 7)
    if classificar_dificuldade(champ) == "Sugiro Ban / Impossível":
        base -= 2
    elif classificar_dificuldade(champ) == "Fácil":
        base += 2
    return round(base, 1)

def get_champions():
    url = f"https://ddragon.leagueoflegends.com/cdn/{DDRAGON_VERSION}/data/pt_BR/champion.json"
    response = requests.get(url, timeout=20)
    response.raise_for_status()
    data = response.json()["data"]

    champs = {}
    for champ_name in data.keys():
        if champ_name == "Camille":
            continue

        champs[champ_name] = {
            "winrate": fake_winrate(champ_name),
            "dificuldade": classificar_dificuldade(champ_name)
        }

    return champs

def get_camille_home_data():
    return {
        "historia": (
            "Camille é a principal inteligência do clã Ferros, uma agente de elite de Piltover "
            "que trocou partes do próprio corpo por aprimoramentos hextec. Precisa, fria e "
            "cirúrgica, domina lutas através de mobilidade, controle de tempo e execução."
        ),
        "habilidades": {
            "P": {
                "nome": "Defesas Adaptativas",
                "descricao": "Ao atacar um campeão, Camille ganha um escudo baseado no tipo de dano do alvo.",
                "cds": "20 / 16 / 12 (níveis 1 / 7 / 13)"
            },
            "Q": {
                "nome": "Protocolo de Precisão",
                "descricao": "Reforça o próximo ataque. Pode ser usada duas vezes. A segunda causa muito mais dano e pode virar dano verdadeiro.",
                "cds": "9 / 8.25 / 7.5 / 6.75 / 6"
            },
            "W": {
                "nome": "Varredura Tática",
                "descricao": "Camille varre a área em cone, causa mais dano na parte externa, aplica lentidão e cura.",
                "cds": "17 / 15.5 / 14 / 12.5 / 11"
            },
            "E": {
                "nome": "Disparo de Gancho",
                "descricao": "Camille se prende à parede e depois salta, podendo atordoar e ganhar velocidade de ataque.",
                "cds": "16 / 14.5 / 13 / 11.5 / 10"
            },
            "R": {
                "nome": "Ultimato Hextec",
                "descricao": "Prende o alvo em uma zona fechada e cria janela forte de all-in.",
                "cds": "140 / 115 / 90"
            }
        },
        "ordem_up_grid": {
            "Q": [1, 4, 5, 7, 9],
            "W": [3, 14, 15, 17, 18],
            "E": [2, 8, 10, 12, 13],
            "R": [6, 11, 16]
        }
    }