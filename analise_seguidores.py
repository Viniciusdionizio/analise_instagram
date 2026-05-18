import json


def carregar_usuarios(arquivo, chave=None):
    """
    Lê o arquivo JSON exportado do Instagram e retorna um conjunto de nomes de usuários.
    Compatível com followers_1.json e following.json (com 'title').
    """
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"[ERRO] Problema ao abrir ou ler {arquivo}")
        return set()

    # se o arquivo tiver uma chave principal (como 'relationships_following')
    if chave and isinstance(data, dict):
        data = data.get(chave, [])

    usuarios = set()

    # percorre a lista de itens
    for item in data:
        if not isinstance(item, dict):
            continue

        # followers_1.json - nomes estão dentro de string_list_data
        if "string_list_data" in item and not item.get("title"):
            for entry in item["string_list_data"]:
                if isinstance(entry, dict) and "value" in entry:
                    usuarios.add(entry["value"])

        # following.json - nomes estão em 'title'
        elif "title" in item and item["title"]:
            usuarios.add(item["title"])

    return usuarios


def analisar_instagram():
    seguidores = carregar_usuarios("followers_1.json")
    seguidos = carregar_usuarios("following.json", "relationships_following")

    nao_retornaram = seguidos - seguidores
    nao_retornei = seguidores - seguidos

    resultado = {
        "Seguidores": sorted(seguidores),
        "Seguidos": sorted(seguidos),
        "Nao_retornaram": sorted(nao_retornaram),
        "Nao_retornei": sorted(nao_retornei),
        "Quantidades": {
            "Seguidores": len(seguidores),
            "Seguidos": len(seguidos),
            "Nao_retornaram": len(nao_retornaram),
            "Nao_retornei": len(nao_retornei),
        },
    }

    print("\n📊 Resumo:")
    for chave, valor in resultado["Quantidades"].items():
        print(f"{chave}: {valor}")

    with open("analise_instagram.json", "w", encoding="utf-8") as f:
        json.dump(resultado, f, ensure_ascii=False, indent=2)

    print("\n✅ Arquivo 'analise_instagram.json' gerado com sucesso!")


if __name__ == "__main__":
    analisar_instagram()
