# Python

Les scripts Python utilisés ici utilisent les librairies `tqdm` et `requests`. Pour les installer, dans une console, on peut faire:

## 01 - Set Up

```sh
pip install tqdm requests

# ou
pip install -r requirements.txt
```

## 02 - Utilisation

Les scripts peuvent être utilisés directement en utilisant l'interface en ligne de commande:

```sh
python python-scripts/01_recuperation_du_statut_de_lapi.py --key-id '****'
```

L'aide est disponible si on utilise `-h`:
```sh
python python-scripts/01_recuperation_du_statut_de_lapi.py -h
```

## 03 - Description des scripts

- `01_recuperation_du_statut_de_lapi`: [ce script](/python-scripts/01_recuperation_du_statut_de_lapi.py) permet de récupérer le statut de l'API
- `02_recuperation_dune_decision`: [ce script](/python-scripts/02_recuperation_dune_decision.py) permet de récupérer une décision à partir de son identifiant
- `03_recherche_plein_texte`: [ce script](/python-scripts/03_recherche_plein_texte.py) permet de faire une recherche plein texte
- `04_recupetation_de_decisions_par_batch`: [ce script](/python-scripts/04_recupetation_de_decisions_par_batch.py) permet de récupérer un lot de décision
- `05_recuperation_des_statistiques_de_lapi`: [ce script](/python-scripts/05_recuperation_des_statistiques_de_lapi.py) permet de récupérer les statistiques de publication de l'API