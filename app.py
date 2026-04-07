from flask import Flask, render_template, request, Response
from services.riot_api import get_champions, get_camille_home_data
from services.analysis import (
    build_matchup_dataset,
    get_matchup_data,
    get_generic_matchup_data,
    rank_matchups
)
from services.skins import get_camille_skins_data

app = Flask(__name__)

ALL_CHAMPS = get_champions()
MATCHUP_DATASET = build_matchup_dataset(ALL_CHAMPS)

TOP_LANE_PRIORITY = [
    "Aatrox", "Darius", "Renekton", "Jax", "Fiora", "Camille", "Sett", "Mordekaiser",
    "Garen", "Nasus", "Malphite", "Ornn", "Shen", "Irelia", "Riven", "Volibear",
    "Urgot", "Illaoi", "K'Sante", "KSante", "Gnar", "Jayce", "Gangplank", "Tryndamere",
    "Pantheon", "Olaf", "Poppy", "Gwen", "Gragas", "DrMundo", "ChoGath", "Teemo",
    "Kennen", "Kayle", "Singed", "Trundle", "Warwick", "Yorick", "Vayne", "Quinn",
    "Lucian", "Kalista", "Varus", "Smolder", "Ryze", "Vladimir", "Cassiopeia",
    "Akali", "Sylas", "Heimerdinger", "Anivia", "Swain", "Karma", "Lux", "Annie",
    "Vex", "Xerath", "Velkoz", "Brand", "Taliyah", "Zilean", "Aurora", "Ambessa",
    "JarvanIV", "Wukong", "Udyr", "Zac"
]

TOP_LANE_INDEX = {name: i for i, name in enumerate(TOP_LANE_PRIORITY)}

GROUP_ORDER = [
    "Sugiro Ban / Impossível",
    "Difícil",
    "Médio",
    "Fácil"
]

def sort_rows_by_top_presence(rows):
    return sorted(
        rows,
        key=lambda r: (
            TOP_LANE_INDEX.get(r["champ"], 9999),
            r["champ"]
        )
    )

@app.route("/")
def home():
    camille = get_camille_home_data()
    return render_template("index.html", camille=camille)

@app.route("/matchups")
def matchups():
    q = request.args.get("q", "").strip().lower()

    ranked = rank_matchups(MATCHUP_DATASET)

    ordered_ranked = {}
    for group_name in GROUP_ORDER:
        rows = ranked.get(group_name, [])
        rows = sort_rows_by_top_presence(rows)

        if q:
            rows = [row for row in rows if q in row["champ"].lower()]

        ordered_ranked[group_name] = rows

    champions = sorted([c for c in ALL_CHAMPS.keys() if c != "Camille"])

    return render_template(
        "matchups.html",
        ranked=ordered_ranked,
        champions=champions,
        busca=q
    )

@app.route("/matchup/<champ>")
def matchup(champ):
    base = ALL_CHAMPS.get(champ)
    if not base:
        return "Campeão não encontrado."

    detailed = get_matchup_data(champ)
    if detailed is None:
        detailed = get_generic_matchup_data(champ, base)

    return render_template(
        "matchup.html",
        champ=champ,
        data=base,
        matchup=detailed
    )

@app.route("/skins")
def skins():
    skins_data = get_camille_skins_data()
    return render_template("skins.html", skins=skins_data)

@app.route("/download/<champ>")
def download_guide(champ):
    base = ALL_CHAMPS.get(champ)
    if not base:
        return "Campeão não encontrado."

    detailed = get_matchup_data(champ)
    if detailed is None:
        detailed = get_generic_matchup_data(champ, base)

    text = []
    text.append(f"Camille vs {champ}")
    text.append(f"Winrate: {base['winrate']}%")
    text.append(f"Dificuldade: {base['dificuldade']}")
    text.append("")
    text.append("1. INFORMAÇÕES")
    text.append(f"Ameaça principal: {detailed['ameaca_principal']}")
    text.append(f"Janela de punição: {detailed['janela_punicao']}")
    text.append("")
    text.append("2. RUNAS PADRÃO")
    text.append("Primária:")
    text.extend([r["nome"] if isinstance(r, dict) else r for r in detailed["runas_padrao"]["primaria"]])
    text.append("Secundária:")
    text.extend([r["nome"] if isinstance(r, dict) else r for r in detailed["runas_padrao"]["secundaria"]])
    text.append("Shards:")
    text.extend(detailed["runas_padrao"]["shards"])
    text.append("")
    text.append("2.1 RUNAS MAIS VITORIOSAS")
    text.append("Primária:")
    text.extend([r["nome"] if isinstance(r, dict) else r for r in detailed["runas_confronto"]["primaria"]])
    text.append("Secundária:")
    text.extend([r["nome"] if isinstance(r, dict) else r for r in detailed["runas_confronto"]["secundaria"]])
    text.append("Shards:")
    text.extend(detailed["runas_confronto"]["shards"])
    text.append("")
    text.append("2.2 RUNA RECOMENDADA PARA A MATCHUP")
    text.append("Primária:")
    text.extend([r["nome"] if isinstance(r, dict) else r for r in detailed["runas_recomendadas"]["primaria"]])
    text.append("Secundária:")
    text.extend([r["nome"] if isinstance(r, dict) else r for r in detailed["runas_recomendadas"]["secundaria"]])
    text.append("Shards:")
    text.extend(detailed["runas_recomendadas"]["shards"])
    text.append("")
    text.append("3. UP DE HABILIDADE")
    text.extend(detailed["up_habilidades"]["nivel_1_3"])
    text.append(f"Prioridade: {detailed['up_habilidades']['prioridade']}")
    text.append("")
    text.append("4. CD DO INIMIGO")
    text.append(f"Passiva: {detailed['cooldowns']['passiva']}")
    text.append(f"Habilidade principal: {detailed['cooldowns']['habilidade_principal']}")
    text.append(f"Q: {detailed['cooldowns']['Q']}")
    text.append(f"W: {detailed['cooldowns']['W']}")
    text.append(f"E: {detailed['cooldowns']['E']}")
    text.append(f"R: {detailed['cooldowns']['R']}")
    text.append("")
    text.append("5. BOTAS")
    text.append(f"Tipo: {detailed['boots']['tipo']}")
    text.append(f"Fechar antes do 1º item: {'Sim' if detailed['boots']['fechar_antes_primeiro_item'] else 'Não'}")
    text.append("")
    text.append("6. ITENS")
    text.append(f"Item inicial: {detailed['itens']['item_inicial']}")
    text.append(f"Plano de compra: {detailed['itens']['plano_compra']}")
    text.append("Situacionais:")
    for item in detailed["itens"]["situacionais"]:
        if isinstance(item, dict):
            text.append(item["nome"])
        else:
            text.append(item)
    text.append("")
    text.append("7. WARD")
    text.append(f"Pink quando: {detailed['warding']['pink_quando']}")
    text.append("")
    text.append("GUIA DA LANE")
    text.append(f"Nível 1: {detailed['plano_lane']['nivel_1']}")
    text.append(f"Nível 2-3: {detailed['plano_lane']['nivel_2_3']}")
    text.append(f"Nível 4-5: {detailed['plano_lane']['nivel_4_5']}")
    text.append(f"Nível 6: {detailed['plano_lane']['nivel_6']}")

    filename = f"camille_vs_{champ.lower()}.txt"
    content = "\n".join(text)

    return Response(
        content,
        mimetype="text/plain",
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )

if __name__ == "__main__":
    app.run(debug=True)