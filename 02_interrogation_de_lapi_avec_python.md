# Interrogation de l'API avec Python

Dans ce document, nous décrivons comment interroger l'API avec Python. On trouvera des exemples de script dans le dossiers `python-scripts`. Les scripts sont des exemples d'utilisation des endpoints suivants:

- [01_recuperation_du_statut_de_lapi.py](/python-scripts/01_recuperation_du_statut_de_lapi.py): `GET /healthcheck`
- [02_recuperation_dune_decision.py](/python-scripts/02_recuperation_dune_decision.py): `GET /decision`
- [03_recherche_plein_texte.py](/python-scripts/03_recherche_plein_texte.py): `GET /search`
- [04_recupetation_de_decisions_par_batch.py](/python-scripts/04_recupetation_de_decisions_par_batch.py): `GET /export`
- [05_recuperation_des_statistiques_de_lapi.py](python-scripts/05_recuperation_des_statistiques_de_lapi.py): `GET /stats`

On peut les modifier de manière à les faire correspondre à ses besoins. La documentation de l'API se trouve au format OpenAPI/Swagger [ici](https://github.com/Cour-de-cassation/judilibre-search/blob/dev/public/JUDILIBRE-public.json).

## 00 - Paramétrage

Pour ce tutoriel, nous allons utiliser la librairie `requests` qui est plus simple à manipuler que les librairies natives de Python:

```python
import requests
```

Dans la suite, nous aurons besoin de la clef d'API de votre application ainsi que de l'URL de l'API en  production:

```python
JUDILIBRE_API_URL = "https://api.piste.gouv.fr/cassation/judilibre/v1.0"
JUDILIBRE_API_KEY = "***"
```

Pour interroger l'API, on spécifie la clef d'API dans le header `KeyId`:
```python
headers = {
    "KeyId": JUDILIBRE_API_KEY,
}

```

## 01 - Récupération du statut de l'API

Pour vérifier le statut de l'API, on peut utiliser le endpoint `GET /healthcheck`. Si l'API fonctionne et que les identifiants sont bons, l'API doit retourner `{"status": "disponible"}`. Ce script permet de le faire directement.

```python
response = requests.get(
    url=f"{JUDILIBRE_API_URL}/decision",
    headers=headers,
)

# vérification de la réponse
response.raise_for_status()

# récupération du statut de l'API
status = response.json()["status"]
```


## 02 - Récupération d'une decision par son identifiant

On peut récupèrer les décisions en utilisant le endpoint `GET /decision` et en spécifiant l'ID de la décision. Un script complet est disponible [ici](/python/02_recuperation_dune_decision.py). Les identifiants sont trouvables dans les URLs des décisions sur le site de la Cour de cassation:

![URL d'une décision sur le site de la Cour de cassation](/images/identifiant-decision.png)

```python
# identifiant de la décision
DECISION_ID = "667e51a56430c94f3afa7d0e"

# récupération de la décision
response = requests.get(
    url=f"{JUDILIBRE_API_URL}/decision",
    headers=headers,
    params={"id": DECISION_ID},
)

# vérification de la réponse
response.raise_for_status()

# récupération des données de la décision
decision = response.json()

```

## 03 - Recherche plein texte dans les décisions

Pour faire une recherche en plein texte, il faut utiliser le endpoint `GET /search`. On spécifiera les termes de recherche en utilisant le paramètre `query`. On peut aussi spécifier le type de recherche avec `operator` qui peut prendre les valeurs suivantes:

- `or`: retourne les décisions qui correspondent à un ou plusieurs des mots de la chaîne de caractères
- `and`: retourne les décisions qui correspondent à tous les mots dans la chaîne de caractères
- `exact`: retourne les décisions qui correpondent exactement à la chaîne de caractères

L'API ne permet pas de retourner plus de 10 000 résultats pour un même jeu de paramètres. Pour une même requête, on ne peut pas retourner plus de 25 décisions à la fois. Pour celà, il faut spécifier le paramètre `page_size` qui donnera le nombre de décisions retournées à la fois. Pour paginer,on utilisera le paramètre `page`. 

Les résultats ne sont pas exactement les décisions mais des versions réduites de celles-ci et sont contenues dans le paramètre `results` de la réponse. Si il n'y a pas plus de résultats, le paramètres `next_batch` de la réponse sera nul. On peut aussi spécifier d'autres paramètres. Pour une documentation plus complête, on peut aller voir le [repo de l'API](https://github.com/Cour-de-cassation/judilibre-search/blob/dev/public/JUDILIBRE-public.json).

```python
PAGE_SIZE = 25
QUERY = "Hello World"

page_number = 0
next_batch = True

decisions = []

params = {
    "query": QUERY,
    "page_size": PAGE_SIZE,
    # on peut définir d'autres paramètres ici
} 

decisions = []

while next_batch is True:
    params["page"] = page_number

    response = requests.get(
        url=f"{JUDILIBRE_API_URL}/search",
        headers=headers,
        params=params,
    )

    # vérification de la réponse
    response.raise_for_status()

    decisions.extend(response.json()["results"])

    # on vérifie si il y a d'autres résultats
    if response.json().get("next_batch") is None:
        next_batch = False

    # on prend la page suivante
    page_number += 1
```

## 04 - Récupération de lots de décisions

Pour récupérer des décisions sans spécifier de termes de recherche, on peut utiliser le endpoint `GET /export`. Ce endpoint permet de récupérer jusqu'à 10 000 décisions. Il fonctionne de manière similaire à `GET /search` sans le paramètre `query` et avec les paramètres `batch` et `batch_size` à la place de `page` et `page_size`. De plus, ce chemin retourne les décisions en entier.




```python
BATCH_SIZE = 1_000

batch_number = 0
next_batch = True

decisions = []

params = {
    "batch_size": PAGE_SIZE,
    # on peut définir d'autres paramètres ici
} 

decisions = []

while next_batch is True:
    params["batch"] = batch_number

    response = requests.get(
        url=f"{JUDILIBRE_API_URL}/export",
        headers=headers,
        params=params,
    )

    # vérification de la réponse
    response.raise_for_status()

    decisions.extend(response.json()["results"])

    # on vérifie si il y a d'autres résultats
    if response.json().get("next_batch") is None:
        next_batch = False

    # on prend la page suivante
    batch_number += 1
```

# 05 - Récupération de statistisques de l'API

Pour récupérer des nombres de décisions selon certains critères, on peut utiliser le endpoint `GET /stats`. Il faut spécifier certains filtres ainsi que des clefs d'agrégation. Par exemple, on peut spécifier `date_start` (date minimale), `date_end` (date maximale), `locations` (juridictions), `jurisdiction` (niveau d'instance), `selection` (booléen limitant les résultats aux décisions présentant un intérêt particulier). 
Les clefs d'agrégation peuvent être une liste de valeurs parmis les suivantes:     

- `jurisdiction`
- `source`
- `location`
- `year`
- `month`
- `chamber`
- `formation`
- `solution`
- `type`
- `nac`
- `themes`
- `publication`

Les résultats sont contenus dans la clef `results` de la réponse. On y retrouve:
- `aggregated_data`: nombre de décisions par valeur de l'ensemble des clefs d'agrégation
- `min_decision_date`: date de la décision la plus ancienne
- `max_decision_date`: date de la décision la plus récente
- `total_decisions`: nombre total de décision correspondant aux filtres

```python
AGGREGATION_KEYS = ["month", "jurisdiction"]
DATE_START = "2020-01-01"
DATE_END = "2025-12-31"

params = {
    "date_start": DATE_START,
    "date_end": DATE_END,
    "keys": AGGREGATION_KEYS,
}

response = requests.get(
    url=f"{JUDILIBRE_API_URL}/stats",
    headers=headers,
    params=params,
)

# vérification de la réponse
response.raise_for_status()

# récupération des données
data = response.json()["results"]

```