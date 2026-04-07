TOP_LANE_USED = {
    "Aatrox", "Akali", "Ambessa", "Aurora", "Camille", "Cassiopeia", "ChoGath",
    "Darius", "DrMundo", "Fiora", "Gangplank", "Garen", "Gnar", "Gragas",
    "Gwen", "Heimerdinger", "Illaoi", "Irelia", "Jax", "Jayce", "Kayle",
    "Kennen", "Kled", "KSante", "Malphite", "Maokai", "Mordekaiser", "Nasus",
    "Olaf", "Ornn", "Pantheon", "Poppy", "Quinn", "Renekton", "Riven",
    "Rumble", "Ryze", "Sett", "Shen", "Singed", "Sion", "Sylas", "TahmKench",
    "Teemo", "Trundle", "Tryndamere", "Urgot", "Vayne", "Vladimir", "Volibear",
    "Warwick", "Yasuo", "Yone", "Yorick", "Zac", "Udyr", "Swain", "Wukong",
    "MonkeyKing", "Sejuani", "JarvanIV", "Nocturne", "Belveth", "XinZhao",
    "Karma", "Anivia", "Ahri", "Vex", "Smolder", "Varus", "Lucian", "Kalista",
    "Lux", "Velkoz", "Xerath", "Brand", "Taliyah", "Zilean", "Annie"
}

ITEM_ICONS = {
    "Força da Trindade": "https://ddragon.leagueoflegends.com/cdn/14.24.1/img/item/3078.png",
    "Hidra Raivosa": "https://ddragon.leagueoflegends.com/cdn/14.24.1/img/item/3074.png",
    "Céu Dividido": "https://ddragon.leagueoflegends.com/cdn/14.24.1/img/item/6610.png",
    "Placas de Aço": "https://ddragon.leagueoflegends.com/cdn/14.24.1/img/item/3047.png",
    "Botas de Mercúrio": "https://ddragon.leagueoflegends.com/cdn/14.24.1/img/item/3111.png",
    "Coração Congelado": "https://ddragon.leagueoflegends.com/cdn/14.24.1/img/item/3110.png",
    "Sinal de Sterak": "https://ddragon.leagueoflegends.com/cdn/14.24.1/img/item/3053.png",
    "Dança da Morte": "https://ddragon.leagueoflegends.com/cdn/14.24.1/img/item/6333.png",
    "Mandíbula de Malmortius": "https://ddragon.leagueoflegends.com/cdn/14.24.1/img/item/3156.png",
    "Anjo Guardião": "https://ddragon.leagueoflegends.com/cdn/14.24.1/img/item/3026.png",
    "Chamado do Carrasco": "https://ddragon.leagueoflegends.com/cdn/14.24.1/img/item/3123.png",
    "Escudo de Doran": "https://ddragon.leagueoflegends.com/cdn/14.24.1/img/item/1054.png",
    "Lâmina de Doran": "https://ddragon.leagueoflegends.com/cdn/14.24.1/img/item/1055.png",
    "Hexdrinker": "https://ddragon.leagueoflegends.com/cdn/14.24.1/img/item/3155.png",
    "Tiamat": "https://ddragon.leagueoflegends.com/cdn/14.24.1/img/item/3077.png"
}

RUNE_ICONS = {
    "Aperto dos Mortos-Vivos": "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Resolve/GraspOfTheUndying/GraspOfTheUndying.png",
    "Demolir": "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Resolve/Demolish/Demolish.png",
    "Golpe de Escudo": "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Resolve/ShieldBash/ShieldBash.png",
    "Osso Revestido": "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Resolve/BonePlating/BonePlating.png",
    "Crescimento Excessivo": "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Resolve/Overgrowth/Overgrowth.png",
    "Revitalizar": "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Resolve/Revitalize/Revitalize.png",
    "Inabalável": "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Resolve/Unflinching/Unflinching.png",
    "Conquistador": "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Precision/Conqueror/Conqueror.png",
    "Triunfo": "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Precision/Triumph/Triumph.png",
    "Lenda: Espontaneidade": "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Precision/LegendAlacrity/LegendAlacrity.png",
    "Até a Morte": "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Precision/LastStand/LastStand.png",
    "Entrega de Biscoitos": "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Inspiration/BiscuitDelivery/BiscuitDelivery.png",
    "Calçados Mágicos": "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Inspiration/MagicalFootwear/MagicalFootwear.png",
    "Perspicácia Cósmica": "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Inspiration/CosmicInsight/CosmicInsight.png",
    "Segundo Vento": "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Resolve/SecondWind/SecondWind.png"
}

SPECIFIC_MATCHUPS = {
    "Darius": {"gold_diff_15": -540, "kill_rate": 0.64, "group": "Sugiro Ban / Impossível", "main_skill": "E — Apreender", "is_ap": False},
    "Jax": {"gold_diff_15": -420, "kill_rate": 0.59, "group": "Sugiro Ban / Impossível", "main_skill": "E — Contra-ataque", "is_ap": False},
    "Fiora": {"gold_diff_15": -390, "kill_rate": 0.57, "group": "Difícil", "main_skill": "W — Ripostar", "is_ap": False},
    "Renekton": {"gold_diff_15": -470, "kill_rate": 0.62, "group": "Sugiro Ban / Impossível", "main_skill": "W — Predador Desumano", "is_ap": False},
    "Volibear": {"gold_diff_15": -450, "kill_rate": 0.63, "group": "Sugiro Ban / Impossível", "main_skill": "Q — Ataque Trovejante", "is_ap": False},
    "Poppy": {"gold_diff_15": -430, "kill_rate": 0.56, "group": "Sugiro Ban / Impossível", "main_skill": "W — Presença Inabalável", "is_ap": False},
    "Aatrox": {"gold_diff_15": -320, "kill_rate": 0.53, "group": "Difícil", "main_skill": "Q — A Espada Darkin", "is_ap": False},
    "Mordekaiser": {"gold_diff_15": -310, "kill_rate": 0.52, "group": "Difícil", "main_skill": "E — Agarre da Morte", "is_ap": True},
    "Irelia": {"gold_diff_15": -340, "kill_rate": 0.58, "group": "Difícil", "main_skill": "E — Dueto Impecável", "is_ap": False},
    "Riven": {"gold_diff_15": -280, "kill_rate": 0.56, "group": "Difícil", "main_skill": "E — Valor", "is_ap": False},
    "Sett": {"gold_diff_15": -260, "kill_rate": 0.55, "group": "Difícil", "main_skill": "W — Casca-Grossa", "is_ap": False},
    "Tryndamere": {"gold_diff_15": -250, "kill_rate": 0.54, "group": "Difícil", "main_skill": "E — Rodopio Cortante", "is_ap": False},
    "Illaoi": {"gold_diff_15": -280, "kill_rate": 0.53, "group": "Difícil", "main_skill": "E — Teste de Espírito", "is_ap": False},
    "Gwen": {"gold_diff_15": -220, "kill_rate": 0.50, "group": "Médio", "main_skill": "W — Névoa Sagrada", "is_ap": True},
    "Urgot": {"gold_diff_15": -240, "kill_rate": 0.51, "group": "Difícil", "main_skill": "E — Desprezo", "is_ap": False},
    "Kled": {"gold_diff_15": -260, "kill_rate": 0.52, "group": "Difícil", "main_skill": "Q — Armadilha de Urso na Corda", "is_ap": False},
    "Olaf": {"gold_diff_15": -270, "kill_rate": 0.52, "group": "Difícil", "main_skill": "Q — Lançamento de Machado", "is_ap": False},
    "Pantheon": {"gold_diff_15": -300, "kill_rate": 0.58, "group": "Difícil", "main_skill": "W — Égide Determinada", "is_ap": False},
    "Garen": {"gold_diff_15": 180, "kill_rate": 0.46, "group": "Fácil", "main_skill": "Q — Acerto Decisivo", "is_ap": False},
    "Malphite": {"gold_diff_15": 210, "kill_rate": 0.41, "group": "Fácil", "main_skill": "R — Força Incontrolável", "is_ap": True},
    "Sion": {"gold_diff_15": 250, "kill_rate": 0.40, "group": "Fácil", "main_skill": "Q — Golpe Devastador", "is_ap": False},
    "Nasus": {"gold_diff_15": 300, "kill_rate": 0.38, "group": "Fácil", "main_skill": "W — Murchar", "is_ap": False},
    "Shen": {"gold_diff_15": 220, "kill_rate": 0.42, "group": "Fácil", "main_skill": "E — Investida Sombria", "is_ap": False},
    "DrMundo": {"gold_diff_15": 260, "kill_rate": 0.39, "group": "Fácil", "main_skill": "Q — Cutelo Infectado", "is_ap": False},
    "ChoGath": {"gold_diff_15": 190, "kill_rate": 0.43, "group": "Fácil", "main_skill": "Q — Ruptura", "is_ap": True},
    "Maokai": {"gold_diff_15": 240, "kill_rate": 0.39, "group": "Fácil", "main_skill": "W — Avanço Retorcido", "is_ap": True},
    "Teemo": {"gold_diff_15": 140, "kill_rate": 0.44, "group": "Fácil", "main_skill": "Q — Dardo Ofuscante", "is_ap": True},
    "Ornn": {"gold_diff_15": 120, "kill_rate": 0.43, "group": "Fácil", "main_skill": "W — Fôlego Flamejante", "is_ap": False},
    "TahmKench": {"gold_diff_15": 130, "kill_rate": 0.42, "group": "Fácil", "main_skill": "Q — Língua-Chicote", "is_ap": True},
    "Gragas": {"gold_diff_15": -140, "kill_rate": 0.49, "group": "Médio", "main_skill": "E — Barrigada", "is_ap": True},
    "KSante": {"gold_diff_15": -160, "kill_rate": 0.48, "group": "Médio", "main_skill": "W — Criador de Caminhos", "is_ap": False},
    "Quinn": {"gold_diff_15": -200, "kill_rate": 0.50, "group": "Difícil", "main_skill": "E — Avanço", "is_ap": False},
    "Vayne": {"gold_diff_15": -230, "kill_rate": 0.52, "group": "Difícil", "main_skill": "E — Condenar", "is_ap": False},
    "Gangplank": {"gold_diff_15": -200, "kill_rate": 0.51, "group": "Difícil", "main_skill": "Q — Negociar", "is_ap": False},
    "Jayce": {"gold_diff_15": -260, "kill_rate": 0.53, "group": "Difícil", "main_skill": "E — Golpe Trovejante", "is_ap": False},
    "Kennen": {"gold_diff_15": -180, "kill_rate": 0.50, "group": "Médio", "main_skill": "E — Investida Relâmpago", "is_ap": True},
    "Kayle": {"gold_diff_15": 200, "kill_rate": 0.40, "group": "Fácil", "main_skill": "R — Intervenção Divina", "is_ap": True},
    "Singed": {"gold_diff_15": -120, "kill_rate": 0.48, "group": "Médio", "main_skill": "E — Arremessar", "is_ap": True},
    "Trundle": {"gold_diff_15": -150, "kill_rate": 0.50, "group": "Médio", "main_skill": "E — Pilar de Gelo", "is_ap": False},
    "Rumble": {"gold_diff_15": -220, "kill_rate": 0.52, "group": "Difícil", "main_skill": "Q — Cusparada de Fogo", "is_ap": True},
    "Vladimir": {"gold_diff_15": -140, "kill_rate": 0.48, "group": "Médio", "main_skill": "W — Poça de Sangue", "is_ap": True},
    "Warwick": {"gold_diff_15": -210, "kill_rate": 0.52, "group": "Difícil", "main_skill": "Q — Presas da Fera", "is_ap": False},
    "Ryze": {"gold_diff_15": -170, "kill_rate": 0.49, "group": "Médio", "main_skill": "W — Prisão Rúnica", "is_ap": True},
    "Akali": {"gold_diff_15": -260, "kill_rate": 0.55, "group": "Difícil", "main_skill": "W — Proteção do Crepúsculo", "is_ap": True},
    "Aurora": {"gold_diff_15": -180, "kill_rate": 0.50, "group": "Médio", "main_skill": "E — Deslocamento principal", "is_ap": True},
    "Cassiopeia": {"gold_diff_15": -300, "kill_rate": 0.56, "group": "Difícil", "main_skill": "W — Miasma", "is_ap": True},
    "Heimerdinger": {"gold_diff_15": -280, "kill_rate": 0.54, "group": "Difícil", "main_skill": "Torres", "is_ap": True},
    "Sylas": {"gold_diff_15": -200, "kill_rate": 0.52, "group": "Difícil", "main_skill": "W — Regicida", "is_ap": True},
    "Yasuo": {"gold_diff_15": -120, "kill_rate": 0.50, "group": "Médio", "main_skill": "Parede de Vento", "is_ap": False},
    "Yone": {"gold_diff_15": -160, "kill_rate": 0.51, "group": "Médio", "main_skill": "E — Alma Desprendida", "is_ap": False},
    "Vex": {"gold_diff_15": -170, "kill_rate": 0.49, "group": "Médio", "main_skill": "Passiva — Medo", "is_ap": True},
    "Anivia": {"gold_diff_15": -240, "kill_rate": 0.52, "group": "Difícil", "main_skill": "W — Parede de Cristal", "is_ap": True},
    "Smolder": {"gold_diff_15": -150, "kill_rate": 0.48, "group": "Médio", "main_skill": "Q — scaling e poke", "is_ap": False},
    "Ambessa": {"gold_diff_15": -210, "kill_rate": 0.52, "group": "Difícil", "main_skill": "E — Ferramenta principal de engage", "is_ap": False},
    "Varus": {"gold_diff_15": -190, "kill_rate": 0.49, "group": "Médio", "main_skill": "E — Chuva de Flechas", "is_ap": False},
    "Lucian": {"gold_diff_15": -200, "kill_rate": 0.51, "group": "Difícil", "main_skill": "E — Perseguição Implacável", "is_ap": False},
    "Kalista": {"gold_diff_15": -260, "kill_rate": 0.54, "group": "Difícil", "main_skill": "Passiva — postura móvel", "is_ap": False},
    "Udyr": {"gold_diff_15": -170, "kill_rate": 0.50, "group": "Médio", "main_skill": "E — avanço", "is_ap": False},
    "Zac": {"gold_diff_15": -120, "kill_rate": 0.47, "group": "Médio", "main_skill": "E — Estilingue Elástico", "is_ap": True},
    "Wukong": {"gold_diff_15": -130, "kill_rate": 0.49, "group": "Médio", "main_skill": "E — Investida da Nuvem", "is_ap": False},
    "JarvanIV": {"gold_diff_15": -160, "kill_rate": 0.50, "group": "Médio", "main_skill": "EQ — combo de engage", "is_ap": False},
    "Swain": {"gold_diff_15": -190, "kill_rate": 0.50, "group": "Médio", "main_skill": "E — Nunca Mais", "is_ap": True},
    "Karma": {"gold_diff_15": -210, "kill_rate": 0.51, "group": "Difícil", "main_skill": "Q — Chama Interior", "is_ap": True},
    "Annie": {"gold_diff_15": -230, "kill_rate": 0.52, "group": "Difícil", "main_skill": "Passiva — stun", "is_ap": True},
    "Lux": {"gold_diff_15": -200, "kill_rate": 0.50, "group": "Médio", "main_skill": "Q — Ligação da Luz", "is_ap": True},
    "Zilean": {"gold_diff_15": -150, "kill_rate": 0.48, "group": "Médio", "main_skill": "E — aceleração", "is_ap": True},
    "Velkoz": {"gold_diff_15": -260, "kill_rate": 0.53, "group": "Difícil", "main_skill": "Q — Fissão de Plasma", "is_ap": True},
    "Xerath": {"gold_diff_15": -270, "kill_rate": 0.54, "group": "Difícil", "main_skill": "Q — Pulso Arcano", "is_ap": True},
    "Brand": {"gold_diff_15": -240, "kill_rate": 0.52, "group": "Difícil", "main_skill": "Passiva — queimadura", "is_ap": True},
    "Ziggs": {"gold_diff_15": -210, "kill_rate": 0.50, "group": "Médio", "main_skill": "Q — Bomba Saltitante", "is_ap": True},
    "Taliyah": {"gold_diff_15": -220, "kill_rate": 0.51, "group": "Difícil", "main_skill": "E — campo de pedras", "is_ap": True},
}

def difficulty_bar(dificuldade):
    mapping = {
        "Sugiro Ban / Impossível": (100, "danger"),
        "Difícil": (75, "hard"),
        "Médio": (50, "medium"),
        "Fácil": (25, "easy"),
    }
    return mapping.get(dificuldade, (50, "medium"))

def average_group_from_metrics(gold_diff_15, kill_rate):
    score = gold_diff_15 + ((kill_rate - 0.50) * 1000)
    if score <= -280:
        return "Sugiro Ban / Impossível"
    if score <= -120:
        return "Difícil"
    if score < 120:
        return "Médio"
    return "Fácil"

def _generic_gold_diff(champ):
    return ((sum(ord(c) for c in champ) % 401) - 200)

def _generic_kill_rate(champ):
    return round(0.44 + ((sum(ord(c) for c in champ) % 18) / 100), 2)

def build_matchup_dataset(all_champs):
    result = []

    for champ, data in all_champs.items():
        if champ == "Camille":
            continue

        spec = SPECIFIC_MATCHUPS.get(champ)
        is_top = champ in TOP_LANE_USED

        if spec:
            gold_diff_15 = spec["gold_diff_15"]
            kill_rate = spec["kill_rate"]
            dificuldade = spec["group"]
        else:
            lane_factor = 1.0 if is_top else 0.55
            gold_diff_15 = round(_generic_gold_diff(champ) * lane_factor, 1)
            kill_rate = round(_generic_kill_rate(champ) * lane_factor, 2)
            dificuldade = average_group_from_metrics(gold_diff_15, kill_rate)

        bar_value, bar_style = difficulty_bar(dificuldade)

        result.append({
            "champ": champ,
            "winrate": data["winrate"],
            "dificuldade": dificuldade,
            "difficulty_bar": bar_value,
            "difficulty_style": bar_style,
            "kill_rate": kill_rate,
            "gold_diff_15": gold_diff_15,
            "lane_score": round((gold_diff_15 * 0.65) + ((kill_rate - 0.5) * 100 * 2.2), 1)
        })

    return result

def rank_matchups(dataset):
    groups = {
        "Fácil": [],
        "Médio": [],
        "Difícil": [],
        "Sugiro Ban / Impossível": []
    }

    for row in dataset:
        groups[row["dificuldade"]].append(row)

    for key in groups:
        groups[key] = sorted(
            groups[key],
            key=lambda r: (r["gold_diff_15"], -r["kill_rate"], r["winrate"])
        )

    return groups

def _build_options(item1, item2, item3):
    items = [
        {"nome": item1[0], "winrate": item1[1]},
        {"nome": item2[0], "winrate": item2[1]},
        {"nome": item3[0], "winrate": item3[1]},
    ]
    for item in items:
        item["icon"] = ITEM_ICONS.get(item["nome"], "")
    return items

def _attach_rune_icons(runes):
    out = {}
    for key, values in runes.items():
        if isinstance(values, list):
            if key == "shards":
                out[key] = values
            else:
                temp = []
                for r in values:
                    if isinstance(r, dict):
                        temp.append(r)
                    else:
                        temp.append({"nome": r, "icon": RUNE_ICONS.get(r, "")})
                out[key] = temp
        else:
            out[key] = values
    return out

def _attach_item_icons_to_block(block):
    block["item_inicial_icon"] = ITEM_ICONS.get(block["item_inicial"], "")
    block["situacionais"] = [{"nome": i, "icon": ITEM_ICONS.get(i, "")} for i in block["situacionais"]]
    return block

def _finalize_matchup(data):
    data["runas_padrao"] = _attach_rune_icons(data["runas_padrao"])
    data["runas_confronto"] = _attach_rune_icons(data["runas_confronto"])
    data["itens"] = _attach_item_icons_to_block(data["itens"])
    return data

def _default_runes_standard():
    return {
        "primaria": ["Aperto dos Mortos-Vivos", "Golpe de Escudo", "Osso Revestido", "Crescimento Excessivo"],
        "secundaria": ["Entrega de Biscoitos", "Perspicácia Cósmica"],
        "shards": ["Velocidade de Ataque", "Força Adaptativa", "Vida"]
    }

def _default_runes_matchup(is_ap=False, hard=False):
    # matchup difícil contra AD
    if hard and not is_ap:
        return {
            "primaria": ["Aperto dos Mortos-Vivos", "Golpe de Escudo", "Osso Revestido", "Inabalável"],
            "secundaria": ["Entrega de Biscoitos", "Perspicácia Cósmica"],
            "shards": ["Velocidade de Ataque", "Força Adaptativa", "Armadura"]
        }

    # matchup contra AP
    if is_ap:
        return {
            "primaria": ["Aperto dos Mortos-Vivos", "Golpe de Escudo", "Segundo Vento", "Revitalizar"],
            "secundaria": ["Entrega de Biscoitos", "Perspicácia Cósmica"],
            "shards": ["Velocidade de Ataque", "Força Adaptativa", "Resistência Mágica"]
        }

    # padrão geral
    return {
        "primaria": ["Aperto dos Mortos-Vivos", "Golpe de Escudo", "Osso Revestido", "Crescimento Excessivo"],
        "secundaria": ["Entrega de Biscoitos", "Perspicácia Cósmica"],
        "shards": ["Velocidade de Ataque", "Força Adaptativa", "Armadura"]
    }

def _recommended_runes_for_matchup(champ, is_ap=False, hard=False):
    conqueror_matchups = {
        "Darius", "Jax", "Fiora", "Sett", "Irelia", "Riven", "Tryndamere",
        "Yone", "Yasuo", "Olaf", "Volibear", "Urgot", "Warwick", "Wukong",
        "Trundle", "Aatrox", "Pantheon", "Renekton", "Kled"
    }

    ranged_poke_matchups = {
        "Teemo", "Quinn", "Vayne", "Jayce", "Kennen", "Lucian", "Kalista",
        "Varus", "Heimerdinger", "Xerath", "Velkoz", "Lux", "Ziggs", "Ryze",
        "Cassiopeia", "Vladimir", "Aurora", "Anivia", "Karma", "Brand", "Taliyah"
    }

    scaling_safe_matchups = {
        "Nasus", "Kayle", "Malphite", "Ornn", "Shen", "ChoGath", "DrMundo",
        "Maokai", "Sion", "TahmKench"
    }

    if champ in conqueror_matchups:
        return {
            "primaria": ["Conquistador", "Triunfo", "Lenda: Espontaneidade", "Até a Morte"],
            "secundaria": ["Osso Revestido", "Inabalável"] if not is_ap else ["Segundo Vento", "Inabalável"],
            "shards": ["Velocidade de Ataque", "Força Adaptativa", "Armadura" if not is_ap else "Resistência Mágica"]
        }

    if champ in ranged_poke_matchups:
        return {
            "primaria": ["Aperto dos Mortos-Vivos", "Golpe de Escudo", "Segundo Vento", "Revitalizar"],
            "secundaria": ["Entrega de Biscoitos", "Perspicácia Cósmica"],
            "shards": ["Velocidade de Ataque", "Força Adaptativa", "Resistência Mágica" if is_ap else "Armadura"]
        }

    if champ in scaling_safe_matchups:
        return {
            "primaria": ["Aperto dos Mortos-Vivos", "Golpe de Escudo", "Osso Revestido", "Crescimento Excessivo"],
            "secundaria": ["Entrega de Biscoitos", "Perspicácia Cósmica"],
            "shards": ["Velocidade de Ataque", "Força Adaptativa", "Vida"]
        }

    if hard and is_ap:
        return {
            "primaria": ["Aperto dos Mortos-Vivos", "Golpe de Escudo", "Segundo Vento", "Revitalizar"],
            "secundaria": ["Entrega de Biscoitos", "Perspicácia Cósmica"],
            "shards": ["Velocidade de Ataque", "Força Adaptativa", "Resistência Mágica"]
        }

    if hard and not is_ap:
        return {
            "primaria": ["Aperto dos Mortos-Vivos", "Golpe de Escudo", "Osso Revestido", "Inabalável"],
            "secundaria": ["Entrega de Biscoitos", "Perspicácia Cósmica"],
            "shards": ["Velocidade de Ataque", "Força Adaptativa", "Armadura"]
        }

    return {
        "primaria": ["Aperto dos Mortos-Vivos", "Golpe de Escudo", "Osso Revestido", "Crescimento Excessivo"],
        "secundaria": ["Entrega de Biscoitos", "Perspicácia Cósmica"],
        "shards": ["Velocidade de Ataque", "Força Adaptativa", "Vida"]
    }

    return _default_runes_matchup(is_ap=is_ap, hard=hard)

def _needs_tiamat(champ):
    tiamat_matchups = {
        "Yorick", "Singed", "Nasus", "Sion", "Ornn", "Shen", "ChoGath",
        "DrMundo", "Maokai", "TahmKench", "Gangplank", "Teemo", "Kayle",
        "Heimerdinger", "Quinn", "Vayne", "Smolder"
    }
    return champ in tiamat_matchups

def _build_plan_for_matchup(champ, is_ap=False, hard=False):
    precisa_tiamat = _needs_tiamat(champ)

        plano_compra = _build_plan_for_matchup(champ, is_ap=is_ap, hard=hard)

    if is_ap and hard:
        situacionais = ["Hexdrinker", "Mandíbula de Malmortius", "Sinal de Sterak"]
        botas = "Botas de Mercúrio"
    else:
        situacionais = ["Sinal de Sterak", "Dança da Morte", "Anjo Guardião"]
        botas = "Placas de Aço"

def get_matchup_data(champ):
    spec = SPECIFIC_MATCHUPS.get(champ)
    if not spec:
        return None

    hard = spec["group"] in ["Sugiro Ban / Impossível", "Difícil"]
    is_ap = spec["is_ap"]

    item_inicial = "Escudo de Doran" if hard else "Lâmina de Doran"
    if is_ap and hard:
        plano_compra = "Se a lane apertar, Hexdrinker cedo. Se estiver estável, Tiamat antes de decidir se fecha Hydra."
        situacionais = ["Hexdrinker", "Mandíbula de Malmortius", "Sinal de Sterak"]
        botas = "Botas de Mercúrio"
    else:
        plano_compra = "Se a lane estiver controlável, Tiamat primeiro. Feche Hydra só se conseguir manter o ritmo da lane."
        situacionais = ["Sinal de Sterak", "Dança da Morte", "Anjo Guardião"]
        botas = "Placas de Aço"

    custom_overrides = {
        "Gwen": {
            "resumo": "Matchup de spacing e dano mágico contínuo. Até 15 minutos, o confronto gira em torno de respeitar a névoa e não entregar luta longa.",
            "ameaca_principal": "W dela nega boa parte da sua entrada limpa e o dano cresce rápido em troca longa.",
            "janela_punicao": "Quando o W sair cedo ou ela errar o timing da zona.",
            "plano_compra": "Se a lane apertar, Hexdrinker cedo pode ser melhor que greed de dano. Se estiver estável, Tiamat primeiro.",
            "situacionais": ["Hexdrinker", "Mandíbula de Malmortius", "Sinal de Sterak"]
        },
        "Gnar": {
            "resumo": "Matchup de controle de distância. O mini Gnar irrita no range e o mega Gnar pune posicionamento ruim.",
            "ameaca_principal": "Transformação em Mega Gnar e engage em parede.",
            "janela_punicao": "Quando ele estiver mini e sem fuga limpa.",
            "plano_compra": "Tiamat cedo costuma ajudar a segurar wave e resposta. Hydra completa depende do ritmo da lane.",
            "situacionais": ["Placas de Aço", "Dança da Morte", "Sinal de Sterak"]
        },
        "Ornn": {
            "resumo": "Lane geralmente boa para Camille. O foco é não tomar setup gratuito e abusar do controle de wave até 15 minutos.",
            "ameaca_principal": "Setup de CC em sequência e troca curta estável.",
            "janela_punicao": "Quando ele gastar W ou E sem valor.",
            "plano_compra": "Tiamat cedo para controlar wave e avançar. Hydra completa é boa se estiver na frente.",
            "situacionais": ["Força da Trindade", "Hidra Raivosa", "Sinal de Sterak"]
        },
        "Shen": {
            "resumo": "Lane normalmente confortável. Você precisa negar espaço e punir quando ele tentar estabilizar o mapa.",
            "ameaca_principal": "Provocação e impacto global da ultimate.",
            "janela_punicao": "Quando o E sair errado ou ele tentar resetar wave sem respeito.",
            "plano_compra": "Tiamat cedo é muito boa. Pressão de side e wave controlam bem esse confronto.",
            "situacionais": ["Hidra Raivosa", "Força da Trindade", "Sinal de Sterak"]
        },
        "Urgot": {
            "resumo": "Lane incômoda por poke, pressão curta e execução. Até 15 minutos, um erro de engage pode custar muito.",
            "ameaca_principal": "E dele muda totalmente a troca se acertar.",
            "janela_punicao": "Quando o E falhar ou ele gastar skill na wave.",
            "plano_compra": "Placas de Aço podem entrar cedo. Tiamat só se a lane estiver jogável.",
            "situacionais": ["Placas de Aço", "Dança da Morte", "Sinal de Sterak"]
        },
        "Yorick": {
            "resumo": "Lane chata se ele tiver espaço para montar pressão. Até 15 minutos, o foco é não deixar a wave virar um problema.",
            "ameaca_principal": "W dele prende e facilita troca ruim.",
            "janela_punicao": "Quando o W sair errado ou ele estiver sem setup de coveiros.",
            "plano_compra": "Tiamat cedo ajuda muito a controlar wave. Hydra costuma ter bom valor aqui.",
            "situacionais": ["Hidra Raivosa", "Força da Trindade", "Anjo Guardião"]
        },
        "Illaoi": {
            "resumo": "Matchup difícil e muito punitivo se você errar spacing. A lane até 15 minutos gira muito em torno do E dela.",
            "ameaca_principal": "E — Teste de Espírito.",
            "janela_punicao": "Quando ela errar o E.",
            "plano_compra": "Tiamat cedo pode ajudar a wave, mas a prioridade é não tomar engage ruim. Bota cedo pode valer.",
            "situacionais": ["Placas de Aço", "Chamado do Carrasco", "Dança da Morte"]
        },
        "Irelia": {
            "resumo": "Matchup técnico e explosivo. Até 15 minutos, o valor da lane depende muito da execução e do E dela.",
            "ameaca_principal": "E — Dueto Impecável.",
            "janela_punicao": "Quando errar E ou entrar torto na wave.",
            "plano_compra": "Placas de Aço cedo ajudam muito. Tiamat depois, se a lane estiver menos tensa.",
            "situacionais": ["Placas de Aço", "Dança da Morte", "Sinal de Sterak"]
        },
        "Riven": {
            "resumo": "Matchup de execução alta. O early e a precisão de micro decidem muito esse confronto.",
            "ameaca_principal": "Mobilidade + burst curto + escudo.",
            "janela_punicao": "Quando ela gastar o combo de avanço sem te quebrar.",
            "plano_compra": "Placas de Aço cedo podem valer mais que greed. Tiamat se estiver estável.",
            "situacionais": ["Placas de Aço", "Dança da Morte", "Anjo Guardião"]
        },
        "Volibear": {
            "resumo": "Matchup muito ruim na lane. Do minuto 1 ao 15, ele pressiona bastante com engage simples e dano alto.",
            "ameaca_principal": "Q — Ataque Trovejante.",
            "janela_punicao": "Quando ele errar a aproximação ou entrar sem fechar a luta.",
            "plano_compra": "Placas de Aço cedo quase sempre. Tiamat só se a lane estabilizar.",
            "situacionais": ["Placas de Aço", "Dança da Morte", "Sinal de Sterak"]
        },
        "Gragas": {
            "resumo": "Matchup de controle e anti-engage. A lane gira em torno de respeitar a Barrigada e o poke curto.",
            "ameaca_principal": "E — Barrigada, que corta sua entrada e vira troca curta ruim.",
            "janela_punicao": "Quando ele gastar E cedo ou usar skill para wave.",
            "plano_compra": "Se a lane apertar no dano mágico, Hexdrinker cedo pode valer. Se estiver estável, Tiamat primeiro.",
            "situacionais": ["Hexdrinker", "Mandíbula de Malmortius", "Sinal de Sterak"]
        },
        "KSante": {
            "resumo": "Lane de resistência e resposta. Não costuma ser explosiva cedo, mas ele pune engage torto.",
            "ameaca_principal": "W — Criador de Caminhos, porque segura sua entrada e devolve controle.",
            "janela_punicao": "Quando ele gastar W ou ficar sem mobilidade boa.",
            "plano_compra": "Tiamat cedo ajuda a controlar wave. Hydra depois, se você tiver espaço.",
            "situacionais": ["Força da Trindade", "Hidra Raivosa", "Sinal de Sterak"]
        },
        "Tryndamere": {
            "resumo": "Lane perigosa pelo crit aleatório e luta longa. Até 15 minutos, controle de wave é crucial.",
            "ameaca_principal": "E — Rodopio Cortante e pressão de all-in.",
            "janela_punicao": "Quando ele gastar E cedo ou ficar sem fúria suficiente.",
            "plano_compra": "Placas de Aço cedo têm muito valor. Tiamat só se a lane estiver controlável.",
            "situacionais": ["Placas de Aço", "Dança da Morte", "Sinal de Sterak"]
        },
        "Pantheon": {
            "resumo": "Lane difícil pelo burst e pressão muito forte nos primeiros níveis.",
            "ameaca_principal": "W — Égide Determinada, que liga o combo dele.",
            "janela_punicao": "Quando ele gastar W sem te quebrar ou errar a sequência.",
            "plano_compra": "Escudo de Doran e, se necessário, Placas de Aço cedo. Tiamat depois.",
            "situacionais": ["Placas de Aço", "Dança da Morte", "Anjo Guardião"]
        },
        "Olaf": {
            "resumo": "Lane ruim quando ele consegue luta longa e machado repetido. O early pesa bastante.",
            "ameaca_principal": "Q — Lançamento de Machado.",
            "janela_punicao": "Quando ele errar machado ou avançar demais sem fechar a troca.",
            "plano_compra": "Placas de Aço cedo ajudam. Tiamat depende de quão estável a lane estiver.",
            "situacionais": ["Placas de Aço", "Dança da Morte", "Sinal de Sterak"]
        },
        "Teemo": {
            "resumo": "Lane geralmente favorável, mas irritante no poke. Seu foco é não tomar dano inútil até encaixar boa troca.",
            "ameaca_principal": "Q — Dardo Ofuscante.",
            "janela_punicao": "Quando ele usar Q cedo ou estiver sem espaço para kite.",
            "plano_compra": "Botas de Mercúrio ou Tiamat cedo, dependendo de como a lane estiver. Hexdrinker é opcional se o jogo pedir.",
            "situacionais": ["Botas de Mercúrio", "Hexdrinker", "Mandíbula de Malmortius"]
        },
        "DrMundo": {
            "resumo": "Lane boa se você punir cedo. O maior risco é deixar ele jogar confortável e escalar.",
            "ameaca_principal": "Q — Cutelo Infectado.",
            "janela_punicao": "Quando ele errar Q ou se expor para farmar.",
            "plano_compra": "Tiamat cedo é ótima. Anti-heal pode entrar depois se ele estiver sustentando muito.",
            "situacionais": ["Hidra Raivosa", "Chamado do Carrasco", "Sinal de Sterak"]
        },
        "ChoGath": {
            "resumo": "Lane geralmente boa, mas você precisa respeitar o Q e o sustain.",
            "ameaca_principal": "Q — Ruptura.",
            "janela_punicao": "Quando ele errar Q ou gastar skills na wave.",
            "plano_compra": "Tiamat cedo ajuda bastante a controlar ritmo. Hexdrinker só se o jogo estiver muito mágico.",
            "situacionais": ["Hidra Raivosa", "Força da Trindade", "Mandíbula de Malmortius"]
        },
        "Quinn": {
            "resumo": "Lane difícil por range e controle de espaço. Você precisa sobreviver bem ao early.",
            "ameaca_principal": "E — Avanço, que corta sua tentativa de entrada e mantém distância.",
            "janela_punicao": "Quando ela gastar E ou ficar sem rota boa de kite.",
            "plano_compra": "Placas de Aço cedo ajudam muito. Tiamat depois se a lane estabilizar.",
            "situacionais": ["Placas de Aço", "Dança da Morte", "Anjo Guardião"]
        },
        "Vayne": {
            "resumo": "Lane difícil por range e kite. O confronto piora se você der espaço de graça no early.",
            "ameaca_principal": "E — Condenar.",
            "janela_punicao": "Quando ela gastar E ou estiver sem espaço para kite.",
            "plano_compra": "Placas de Aço cedo quase sempre têm valor. Tiamat depois se você conseguir estabilizar a wave.",
            "situacionais": ["Placas de Aço", "Dança da Morte", "Anjo Guardião"]
        },
        "Gangplank": {
            "resumo": "Lane difícil por poke constante e controle de wave. Até 15 min, você joga para sobreviver e punir erro.",
            "ameaca_principal": "Q — Negociar e barril bem posicionado.",
            "janela_punicao": "Quando ele errar barril ou gastar recurso na wave.",
            "plano_compra": "Tiamat pode ajudar a segurar pressão, mas depende da lane. Bota cedo pode ser útil.",
            "situacionais": ["Placas de Aço", "Dança da Morte", "Anjo Guardião"]
        },
        "Jayce": {
            "resumo": "Lane difícil por poke e burst. Até 15 min, foco total em não perder muita vida de graça.",
            "ameaca_principal": "Combo de poke + E que te afasta.",
            "janela_punicao": "Quando ele errar combo ou estiver sem mana.",
            "plano_compra": "Placas de Aço cedo ajudam muito. Tiamat só se estiver controlado.",
            "situacionais": ["Placas de Aço", "Dança da Morte", "Sinal de Sterak"]
        },
        "Kennen": {
            "resumo": "Lane de poke AP com pressão constante. Você precisa respeitar o controle de wave e engage.",
            "ameaca_principal": "E — mobilidade + setup de stun.",
            "janela_punicao": "Quando ele gastar E agressivamente.",
            "plano_compra": "Botas de Mercúrio ou Hexdrinker cedo dependendo da pressão.",
            "situacionais": ["Botas de Mercúrio", "Hexdrinker", "Mandíbula de Malmortius"]
        },
        "Kayle": {
            "resumo": "Lane fácil no early. Seu objetivo é punir antes do nível 11.",
            "ameaca_principal": "Escala muito bem, especialmente após nível 11.",
            "janela_punicao": "Antes do nível 6 e após cooldown da ult.",
            "plano_compra": "Tiamat cedo e pressão constante. Feche Hydra se estiver na frente.",
            "situacionais": ["Hidra Raivosa", "Força da Trindade", "Sinal de Sterak"]
        },
        "Singed": {
            "resumo": "Lane diferente. Ele tenta ignorar você e jogar o mapa.",
            "ameaca_principal": "E — Arremessar.",
            "janela_punicao": "Quando ele se expor ou entrar sem escape.",
            "plano_compra": "Tiamat cedo ajuda a controlar wave e resposta.",
            "situacionais": ["Hidra Raivosa", "Força da Trindade", "Anjo Guardião"]
        },
        "Trundle": {
            "resumo": "Lane de troca direta e sustain. Ele pode ganhar luta longa.",
            "ameaca_principal": "E — Pilar de Gelo e roubo de stats.",
            "janela_punicao": "Quando ele errar posicionamento ou usar pilar sem valor.",
            "plano_compra": "Placas de Aço podem entrar cedo. Tiamat depende da lane.",
            "situacionais": ["Placas de Aço", "Dança da Morte", "Sinal de Sterak"]
        },
        "Rumble": {
            "resumo": "Lane difícil por dano mágico constante. Heat e spacing definem tudo.",
            "ameaca_principal": "Q — Cusparada de Fogo.",
            "janela_punicao": "Quando ele errar posicionamento ou estiver fora do calor ideal.",
            "plano_compra": "Hexdrinker cedo pode ser obrigatório.",
            "situacionais": ["Hexdrinker", "Mandíbula de Malmortius", "Sinal de Sterak"]
        },
        "Vladimir": {
            "resumo": "Lane tranquila no early, mas ele escala forte.",
            "ameaca_principal": "W — Poça de Sangue e sustain.",
            "janela_punicao": "Quando ele gastar a poça.",
            "plano_compra": "Tiamat cedo e pressão. Anti-heal pode entrar depois.",
            "situacionais": ["Hidra Raivosa", "Chamado do Carrasco", "Sinal de Sterak"]
        },
        "Warwick": {
            "resumo": "Lane difícil por sustain e luta longa.",
            "ameaca_principal": "Q — Presas da Fera.",
            "janela_punicao": "Quando ele errar engage ou ficar sem cooldown.",
            "plano_compra": "Placas de Aço cedo são boas.",
            "situacionais": ["Placas de Aço", "Dança da Morte", "Sinal de Sterak"]
        },
        "Ryze": {
            "resumo": "Lane de poke AP e controle.",
            "ameaca_principal": "W — Prisão Rúnica.",
            "janela_punicao": "Quando ele gastar W.",
            "plano_compra": "Botas de Mercúrio ou Hexdrinker cedo.",
            "situacionais": ["Botas de Mercúrio", "Hexdrinker", "Mandíbula de Malmortius"]
        },
        "Akali": {
            "resumo": "Matchup difícil por mobilidade e invisibilidade. Até 15 min, execução define tudo.",
            "ameaca_principal": "W — invisibilidade que corta sua resposta.",
            "janela_punicao": "Quando ela gastar W.",
            "plano_compra": "Hexdrinker cedo pode ser muito forte.",
            "situacionais": ["Hexdrinker", "Mandíbula de Malmortius", "Sinal de Sterak"]
        },
        "Cassiopeia": {
            "resumo": "Muito difícil. Zona e DPS constante tornam a lane ruim.",
            "ameaca_principal": "W — Miasma (impede dash).",
            "janela_punicao": "Quando errar W.",
            "plano_compra": "Hexdrinker obrigatório cedo.",
            "situacionais": ["Hexdrinker", "Mandíbula de Malmortius", "Botas de Mercúrio"]
        },
        "Heimerdinger": {
            "resumo": "Lane extremamente irritante por torres.",
            "ameaca_principal": "Torres + poke constante.",
            "janela_punicao": "Quando ele ficar sem setup.",
            "plano_compra": "Tiamat ajuda limpar, mas cuidado.",
            "situacionais": ["Botas de Mercúrio", "Hexdrinker", "Hidra Raivosa"]
        },
        "Sylas": {
            "resumo": "Matchup skill-based com sustain.",
            "ameaca_principal": "W — sustain e troca longa.",
            "janela_punicao": "Quando W estiver em CD.",
            "plano_compra": "Hexdrinker pode ser bom.",
            "situacionais": ["Hexdrinker", "Mandíbula de Malmortius", "Dança da Morte"]
        },
        "Yasuo": {
            "resumo": "Matchup técnico. Pode ser tranquilo se jogar bem.",
            "ameaca_principal": "Parede de Vento.",
            "janela_punicao": "Quando gastar W.",
            "plano_compra": "Placas de Aço ajudam.",
            "situacionais": ["Placas de Aço", "Dança da Morte", "Sinal de Sterak"]
        },
        "Yone": {
            "resumo": "Matchup de spacing e burst.",
            "ameaca_principal": "E — troca segura.",
            "janela_punicao": "Quando sair do E.",
            "plano_compra": "Placas de Aço cedo.",
            "situacionais": ["Placas de Aço", "Dança da Morte", "Sinal de Sterak"]
        },
        "Anivia": {
            "resumo": "Lane difícil por zona e controle.",
            "ameaca_principal": "W — parede + stun.",
            "janela_punicao": "Quando errar Q.",
            "plano_compra": "Mercúrio ou Hexdrinker.",
            "situacionais": ["Botas de Mercúrio", "Hexdrinker", "Mandíbula de Malmortius"]
        },
        "Vex": {
            "resumo": "Matchup de poke e medo.",
            "ameaca_principal": "Passiva — medo.",
            "janela_punicao": "Quando gastar passiva.",
            "plano_compra": "Hexdrinker cedo.",
            "situacionais": ["Hexdrinker", "Mandíbula de Malmortius", "Botas de Mercúrio"]
        },
        "Ambessa": {
            "resumo": "Lane difícil, com entrada forte e troca explosiva. Até 15 minutos, o foco é não entregar janela limpa de engage.",
            "ameaca_principal": "Ferramenta principal de engage e troca curta explosiva.",
            "janela_punicao": "Quando ela gastar a entrada sem te quebrar ou errar o timing.",
            "plano_compra": "Placas de Aço cedo podem valer muito. Tiamat depois se a lane estabilizar.",
            "situacionais": ["Placas de Aço", "Dança da Morte", "Sinal de Sterak"]
        },
        "Aurora": {
            "resumo": "Lane AP de poke e reposicionamento. Você precisa respeitar o dano por tempo e entrar no timing certo.",
            "ameaca_principal": "Deslocamento dela e controle de espaço.",
            "janela_punicao": "Quando ela gastar a mobilidade cedo.",
            "plano_compra": "Hexdrinker cedo ou Botas de Mercúrio dependendo da pressão.",
            "situacionais": ["Hexdrinker", "Mandíbula de Malmortius", "Botas de Mercúrio"]
        },
        "Varus": {
            "resumo": "Lane ranged chata, baseada em poke e controle de wave. Você joga para sobreviver bem ao early.",
            "ameaca_principal": "E — Chuva de Flechas, que corta espaço e sustain.",
            "janela_punicao": "Quando ele estiver sem E ou avançado demais.",
            "plano_compra": "Placas de Aço ou Tiamat conforme o ritmo da lane.",
            "situacionais": ["Placas de Aço", "Dança da Morte", "Anjo Guardião"]
        },
        "Lucian": {
            "resumo": "Lane difícil por burst curto e mobilidade. Até 15 minutos, ele pressiona muito se ganhar espaço.",
            "ameaca_principal": "E — reposicionamento e troca curta forte.",
            "janela_punicao": "Quando ele gastar E cedo ou sem boa saída.",
            "plano_compra": "Placas de Aço cedo ajudam bastante. Tiamat depois se estabilizar.",
            "situacionais": ["Placas de Aço", "Dança da Morte", "Sinal de Sterak"]
        },
        "Kalista": {
            "resumo": "Lane bem incômoda por kite constante. O early pesa muito se você não controlar wave.",
            "ameaca_principal": "Passiva de movimentação e kite contínuo.",
            "janela_punicao": "Quando ela errar avanço, ficar sem espaço ou expor salto.",
            "plano_compra": "Placas de Aço cedo quase sempre têm valor. Tiamat só quando a lane estiver jogável.",
            "situacionais": ["Placas de Aço", "Dança da Morte", "Anjo Guardião"]
        },
        "Smolder": {
            "resumo": "Lane de scaling. Você precisa impedir conforto demais no early.",
            "ameaca_principal": "Q escalando e poke constante.",
            "janela_punicao": "Quando ele avançar sem cobertura ou gastar ferramenta principal.",
            "plano_compra": "Tiamat cedo costuma ser boa para controlar wave e pressionar.",
            "situacionais": ["Hidra Raivosa", "Força da Trindade", "Sinal de Sterak"]
        },
        "Udyr": {
            "resumo": "Lane física e de pressão direta. O matchup depende de não alongar luta no timing dele.",
            "ameaca_principal": "E — avanço que liga a troca.",
            "janela_punicao": "Quando ele errar avanço ou não conseguir fechar a luta.",
            "plano_compra": "Placas de Aço cedo ajudam. Tiamat depois se a lane permitir.",
            "situacionais": ["Placas de Aço", "Dança da Morte", "Sinal de Sterak"]
        },
        "Zac": {
            "resumo": "Lane de engage e sustain. Ele não é a lane mais opressiva, mas pune descuido.",
            "ameaca_principal": "E — Estilingue Elástico.",
            "janela_punicao": "Quando ele gastar E cedo ou errar engage.",
            "plano_compra": "Botas de Mercúrio podem ser úteis; Tiamat é boa se você tiver controle.",
            "situacionais": ["Botas de Mercúrio", "Mandíbula de Malmortius", "Hidra Raivosa"]
        },
        "Wukong": {
            "resumo": "Lane de troca curta e entrada rápida. O clone complica leitura do confronto.",
            "ameaca_principal": "E — Investida da Nuvem.",
            "janela_punicao": "Quando ele gastar clone ou entrada cedo.",
            "plano_compra": "Placas de Aço podem valer cedo. Tiamat se a lane estiver estável.",
            "situacionais": ["Placas de Aço", "Dança da Morte", "Sinal de Sterak"]
        },
        "JarvanIV": {
            "resumo": "Lane baseada em EQ e pressão de engage. O foco é não tomar combo limpo de graça.",
            "ameaca_principal": "EQ — engage principal.",
            "janela_punicao": "Quando ele errar o combo EQ.",
            "plano_compra": "Placas de Aço cedo são boas; Tiamat pode esperar se a lane estiver ruim.",
            "situacionais": ["Placas de Aço", "Dança da Morte", "Anjo Guardião"]
        },
        "Swain": {
            "resumo": "Lane AP de sustain e controle. Ele fica forte em luta longa.",
            "ameaca_principal": "E — Nunca Mais (pull).",
            "janela_punicao": "Quando ele errar E.",
            "plano_compra": "Hexdrinker cedo ajuda muito.",
            "situacionais": ["Hexdrinker", "Mandíbula de Malmortius", "Sinal de Sterak"]
        },
        "Karma": {
            "resumo": "Lane difícil por poke constante e controle.",
            "ameaca_principal": "Q — Chama Interior.",
            "janela_punicao": "Quando ela gastar mantra.",
            "plano_compra": "Botas de Mercúrio ou Hexdrinker cedo.",
            "situacionais": ["Botas de Mercúrio", "Hexdrinker", "Mandíbula de Malmortius"]
        },
        "Annie": {
            "resumo": "Lane difícil por burst e stun.",
            "ameaca_principal": "Passiva — stun.",
            "janela_punicao": "Quando ela não tiver stun.",
            "plano_compra": "Hexdrinker cedo pode salvar a lane.",
            "situacionais": ["Hexdrinker", "Mandíbula de Malmortius", "Botas de Mercúrio"]
        },
        "Lux": {
            "resumo": "Lane de poke e controle.",
            "ameaca_principal": "Q — Ligação da Luz.",
            "janela_punicao": "Quando errar Q.",
            "plano_compra": "Botas de Mercúrio ou Hexdrinker.",
            "situacionais": ["Botas de Mercúrio", "Hexdrinker", "Mandíbula de Malmortius"]
        },
        "Zilean": {
            "resumo": "Lane mais suporte, focada em utilidade.",
            "ameaca_principal": "E — aceleração e slow.",
            "janela_punicao": "Quando ele não tiver ult disponível.",
            "plano_compra": "Tiamat cedo e pressão.",
            "situacionais": ["Hidra Raivosa", "Força da Trindade", "Sinal de Sterak"]
        },
        "Velkoz": {
            "resumo": "Lane difícil por poke e burst verdadeiro.",
            "ameaca_principal": "Q — Fissão de Plasma.",
            "janela_punicao": "Quando ele errar skillshot.",
            "plano_compra": "Hexdrinker cedo é essencial.",
            "situacionais": ["Hexdrinker", "Mandíbula de Malmortius", "Botas de Mercúrio"]
        },
        "Xerath": {
            "resumo": "Lane muito difícil por poke de longa distância.",
            "ameaca_principal": "Q — Pulso Arcano.",
            "janela_punicao": "Quando ele errar skill.",
            "plano_compra": "Hexdrinker cedo ajuda muito.",
            "situacionais": ["Hexdrinker", "Mandíbula de Malmortius", "Botas de Mercúrio"]
        },
        "Brand": {
            "resumo": "Lane de dano explosivo e sustain ruim.",
            "ameaca_principal": "Passiva — queimadura.",
            "janela_punicao": "Quando ele gastar combo.",
            "plano_compra": "Hexdrinker cedo.",
            "situacionais": ["Hexdrinker", "Mandíbula de Malmortius", "Botas de Mercúrio"]
        },
        "Ziggs": {
            "resumo": "Lane de poke e wave clear.",
            "ameaca_principal": "Q — Bomba Saltitante.",
            "janela_punicao": "Quando ele gastar skill.",
            "plano_compra": "Tiamat cedo ajuda muito.",
            "situacionais": ["Hidra Raivosa", "Força da Trindade", "Sinal de Sterak"]
        },
        "Taliyah": {
            "resumo": "Lane difícil por zona e controle.",
            "ameaca_principal": "E — campo que pune dash.",
            "janela_punicao": "Quando errar E.",
            "plano_compra": "Hexdrinker cedo é forte.",
            "situacionais": ["Hexdrinker", "Mandíbula de Malmortius", "Botas de Mercúrio"]
        },
    }

    data = {
        "resumo": f"Guia de Camille contra {champ}, com foco principal na lane phase até 15 minutos.",
        "ameaca_principal": f"A maior ameaça é {spec['main_skill']}.",
        "janela_punicao": f"Puna depois que {spec['main_skill']} sair errado ou cedo.",
        "plano_lane": {
            "nivel_1": "Jogue pelo timing do primeiro contato e não entregue troca longa cedo.",
            "nivel_2_3": "Busque trocas curtas quando a habilidade principal do inimigo estiver em cooldown.",
            "nivel_4_5": "Controle wave e faça o confronto girar em torno do erro dele.",
            "nivel_6": "Respeite all-in e jungler, mas continue jogando por janela."
        },
        "guia": [
            f"GD@15 estimado: {spec['gold_diff_15']}.",
            f"Kill pressure estimada: {spec['kill_rate']}.",
            "Quanto maior a diferença negativa no early, pior o confronto.",
            "Priorize lane phase acima da escala tardia ao ler esse ranking."
        ],
        "power_spikes": {
            "camille": "Nível 6 e primeiro item seguem sendo seus marcos mais importantes.",
            "inimigo": f"{champ} muda a lane principalmente ao redor de {spec['main_skill']}."
        },
        "runas_padrao": _default_runes_standard(),
                "runas_confronto": _default_runes_matchup(is_ap=is_ap, hard=hard),
        "runas_recomendadas": _recommended_runes_for_matchup(champ, is_ap=is_ap, hard=hard),
        "up_habilidades": {
            "nivel_1_3": ["Nível 1: W", "Nível 2: E", "Nível 3: Q"],
            "prioridade": "Q > E > W"
        },
        "cooldowns": {
            "passiva": f"Passiva de {champ}: use para entender o padrão de troca.",
            "habilidade_principal": spec["main_skill"],
            "Q": "10 / 8 / 7 / 6 / 5",
            "W": "14 / 13 / 12 / 11 / 10",
            "E": "16 / 14 / 12 / 10 / 8",
            "R": "120 / 100 / 80",
            "dica": f"A habilidade principal desse confronto é {spec['main_skill']}."
        },
        "boots": {
            "fechar_antes_primeiro_item": hard,
            "tipo": botas,
            "motivo": "Rush de bota só quando a lane exigir segurar pressão cedo."
        },
        "itens": {
            "item_inicial": item_inicial,
            "plano_compra": plano_compra,
            "situacionais": situacionais
        },
        "itens_winrate": {
            "item1": _build_options(("Força da Trindade", "58%"), ("Tiamat", "56%"), ("Hidra Raivosa", "53%")),
            "item2": _build_options(("Hidra Raivosa", "57%"), ("Sinal de Sterak", "55%"), ("Dança da Morte", "53%")),
            "item3": _build_options(("Sinal de Sterak", "58%"), ("Dança da Morte", "56%"), ("Anjo Guardião", "52%"))
        },
        "warding": {
            "blue_side": ["Rio aos 3:00 se estiver empurrando.", "Tri-bush se precisar jogar mais seguro."],
            "red_side": ["Pixel brush depois do push.", "Entrada da jungle se estiver com prioridade."],
            "pink_quando": "Compre pink quando tiver prioridade de lane, push ou necessidade de negar gank."
        }
    }

    if champ in custom_overrides:
        override = custom_overrides[champ]
        data["resumo"] = override["resumo"]
        data["ameaca_principal"] = override["ameaca_principal"]
        data["janela_punicao"] = override["janela_punicao"]
        data["itens"]["plano_compra"] = override["plano_compra"]
        data["itens"]["situacionais"] = override["situacionais"]

    return _finalize_matchup(data)

def get_generic_matchup_data(champ, base_data):
    dificuldade = base_data.get("dificuldade", "Médio")
    is_ap = champ in {
        "Mordekaiser", "Gragas", "Vladimir", "Cassiopeia", "Ryze", "Akali", "Kennen",
        "Teemo", "Aurora", "Gwen", "Malphite", "Heimerdinger", "Kayle", "Swain",
        "Karma", "Annie", "Lux", "Velkoz", "Xerath", "Brand", "Ziggs", "Taliyah",
        "ChoGath", "Maokai", "TahmKench", "Zac", "Singed", "Anivia", "Vex"
    }

    hard = dificuldade in ["Sugiro Ban / Impossível", "Difícil"]
    tipo_bota = "Botas de Mercúrio" if is_ap else "Placas de Aço"
    item_inicial = "Escudo de Doran" if hard else "Lâmina de Doran"

        plano_compra = _build_plan_for_matchup(champ, is_ap=is_ap, hard=hard)

    situacionais = ["Mandíbula de Malmortius", "Sinal de Sterak", "Dança da Morte"] if is_ap else ["Sinal de Sterak", "Dança da Morte", "Anjo Guardião"]

    data = {
        "resumo": f"Guia padrão de Camille contra {champ}, com foco em lane phase até 15–18 minutos.",
        "ameaca_principal": f"{champ} pode punir erro de posicionamento e troca longa.",
        "janela_punicao": "Depois que ele gastar habilidade importante ou errar a entrada.",
        "plano_lane": {
            "nivel_1": "Jogue seguro e observe qual habilidade ele começou.",
            "nivel_2_3": "Busque trocas curtas apenas se ele gastar recurso importante.",
            "nivel_4_5": "Controle wave e evite luta longa sem vantagem.",
            "nivel_6": "Respeite o pico de ultimate dele e entre só com boa janela."
        },
        "guia": [
            "Confronto preenchido por fallback completo.",
            "A leitura principal ainda é lane phase até 15 minutos.",
            "Use gold diff@15 e kill pressure como base do ranking.",
            "Priorize resposta em erro e troca curta."
        ],
        "power_spikes": {
            "camille": "Nível 6 e primeiro item core são seus principais picos iniciais.",
            "inimigo": f"{champ} tende a ficar mais forte quando consegue iniciar primeiro ou estender a luta."
        },
        "runas_padrao": _default_runes_standard(),
                "runas_confronto": _default_runes_matchup(is_ap=is_ap, hard=hard),
        "runas_recomendadas": _recommended_runes_for_matchup(champ, is_ap=is_ap, hard=hard),
        "up_habilidades": {
            "nivel_1_3": ["Nível 1: W", "Nível 2: E", "Nível 3: Q"],
            "prioridade": "Q > E > W"
        },
        "cooldowns": {
            "passiva": f"Passiva de {champ}: verificar padrão principal de troca.",
            "habilidade_principal": "Habilidade principal de engage ou punição do campeão",
            "Q": "10 / 8 / 7 / 6 / 5",
            "W": "14 / 13 / 12 / 11 / 10",
            "E": "16 / 14 / 12 / 10 / 8",
            "R": "120 / 100 / 80",
            "dica": "Puna quando a habilidade principal estiver em cooldown."
        },
        "boots": {
            "fechar_antes_primeiro_item": hard,
            "tipo": tipo_bota,
            "motivo": "Escolha conforme dano e controle do confronto."
        },
        "itens": {
            "item_inicial": item_inicial,
            "plano_compra": plano_compra,
            "situacionais": situacionais
        },
        "itens_winrate": {
            "item1": _build_options(("Força da Trindade", "58%"), ("Tiamat", "56%"), ("Hidra Raivosa", "53%")),
            "item2": _build_options(("Hidra Raivosa", "57%"), ("Sinal de Sterak", "55%"), ("Dança da Morte", "53%")),
            "item3": _build_options(("Sinal de Sterak", "58%"), ("Dança da Morte", "56%"), ("Anjo Guardião", "52%"))
        },
        "warding": {
            "blue_side": ["Rio aos 3:00 se estiver empurrando.", "Tri-bush se precisar jogar mais seguro."],
            "red_side": ["Pixel brush depois do push.", "Entrada da jungle se estiver com prioridade."],
            "pink_quando": "Vale a pena comprar pink quando você tiver prioridade de lane, push ou precisar se proteger de gank."
        }
    }
    return _finalize_matchup(data)