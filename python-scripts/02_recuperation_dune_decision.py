import requests
import os
import json


def get_decision(
    key: str,
    url: str,
    decision_id: str,
) -> dict:
    response = requests.get(
        url=f"{url}/decision",
        headers={"KeyId": key},
        params={
            "id": decision_id,
        },
    )
    response.raise_for_status()

    return response.json()


if __name__ == "__main__":
    from argparse import ArgumentParser

    argument_parser = ArgumentParser(
        description="Script permettant de récupérer une décision de justice depuis l'API JUDILIBRE à partir de son identifiant",
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
        "-id",
        "--decision-id",
        help="ID of the decision to get",
        default="667e51a56430c94f3afa7d0e",
    )
    arguments = argument_parser.parse_args()

    key_id = arguments.key_id
    url = arguments.url
    output_folder = arguments.output_folder
    decision_id = arguments.decision_id

    try:
        os.stat(output_folder)
    except FileNotFoundError:
        os.mkdir(output_folder)

    decision_data = get_decision(
        key=key_id,
        url=url,
        decision_id=decision_id,
    )

    with open(
        os.path.join(f"decision_{decision_id}.json"),
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(decision_data, file)
