import requests
import os
import json


def get_stats(
    key: str,
    url: str,
    keys: list[str],
    date_start: str | None = None,
    date_end: str | None = None,
) -> dict:
    
    params = {
        "keys": keys,
    }

    if date_start is not None:
        params["date_start"] = date_start
    if date_end is not None:
        params["date_end"] = date_end

    response = requests.get(
        url=f"{url}/stats",
        headers={"KeyId": key},
        params=params,
    )
    response.raise_for_status()

    return response.json()["results"]


if __name__ == "__main__":
    from argparse import ArgumentParser

    argument_parser = ArgumentParser(
        description="Script permettant de récupérer les statistiques de l'API JUDILIBRE",
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
        "--date-start",
        help="Date minimale des décisions",
        default=None,
    )
    argument_parser.add_argument(
        "--date-end",
        help="Date maximale des décisions",
        default=None,
    )
    argument_parser.add_argument(
        "--keys",
        help="Clefs d'agrégation séparées par des virgules (ex: 'month,jurisdiction')",
        default="month",
    )

    arguments = argument_parser.parse_args()

    key_id = arguments.key_id
    url = arguments.url
    output_folder = arguments.output_folder
    date_start = arguments.date_start
    date_end = arguments.date_end
    keys = arguments.keys.split(",")

    try:
        os.stat(output_folder)
    except FileNotFoundError:
        os.mkdir(output_folder)

    stats = get_stats(
        key=key_id,
        url=url,
        date_start=date_start,
        date_end=date_end,
        keys=keys,
    )

    with open(
        os.path.join(f"stats_aggregated_by_{'-'.join(keys)}.json"),
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(stats, file)
