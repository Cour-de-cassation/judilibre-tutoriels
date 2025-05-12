import requests
import os
import json


def get_decisions_by_batch(
    key: str,
    url: str,
    params: dict={},
) -> dict:

    batch_number = 0
    next_batch = True

    decisions = []

    params = {
        **params,
        "batch_size": 25,
    } 

    decisions = []

    while next_batch is True:
        params["batch"] = batch_number

        response = requests.get(
            url=f"{url}/export",
            headers={"KeyId": key},
            params=params,
        )

        # vérification de la réponse
        response.raise_for_status()

        decisions.extend(response.json()["results"])

        # on vérifie si il y a d'autres résultats
        if response.json().get("next_batch") is None:
            next_batch = False

        # on prend le batch suivant
        batch_number += 1

    return decisions


if __name__ == "__main__":
    from argparse import ArgumentParser

    argument_parser = ArgumentParser(
        description="Script permettant de récupérer un lot de décisions depuis l'API JUDILIBRE",
    )

    argument_parser.add_argument(
        "-k",
        "--key-id",
        help="Clef de l'API JUDILIBRE",
    )
    argument_parser.add_argument(
        "-u",
        "--url",
        help="URL de l'API JUDILIBRE",
        default="https://api.piste.gouv.fr/cassation/judilibre/v1.0",
    )
    argument_parser.add_argument(
        "-o",
        "--output-folder",
        help="Folder in which to save decisions",
        default="./data",
    )
    argument_parser.add_argument(
        "-p",
        "--parameters",
        help="Paramètres de recherche de décisions au format JSON",
        default='{"jurisdiction": "cc"}',
    )
    arguments = argument_parser.parse_args()

    key_id = arguments.key_id
    url = arguments.url
    output_folder = arguments.output_folder
    parameters = arguments.parameters


    try:
        os.stat(output_folder)
    except FileNotFoundError:
        os.mkdir(output_folder)
    
    params = json.loads(parameters)

    decisions = get_decisions_by_batch(
        key=key_id,
        url=url,
        params=params,
    )
    for decision_data in decisions:

        with open(
            os.path.join(f"decision_{decision_data['id']}.json"),
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(decision_data, file)
