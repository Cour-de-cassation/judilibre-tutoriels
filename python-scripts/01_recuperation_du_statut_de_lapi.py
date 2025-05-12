import requests


def get_api_status(
    url: str,
    key: str,
) -> str:
    response = requests.get(
        url=f"{url}/healthcheck",
        headers={"KeyId": key},
    )
    response.raise_for_status()

    return response.json()["status"]


if __name__ == "__main__":
    from argparse import ArgumentParser

    argument_parser = ArgumentParser(
        description="Script permettant de récupérer le statut de l'API JUDILIBRE",
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
    arguments = argument_parser.parse_args()

    key_id = arguments.key_id
    url = arguments.url

    api_status = get_api_status(
        url=url,
        key=key_id,
    )

    print(api_status)
