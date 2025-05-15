# R

Les scripts R ont ici été traduits à partir de Python avec une intelligence artificielle.

## 01 - Set Up

Pour les utiliser, on doit installer les librairies `httr`, `jsonlite`, `progress`, `optparse`: dans une console R

```r
install.packages(c("httr", "jsonlite", "progress", "optparse"))
```

## 02 - Utilisation

Pour le lancer, dans une console, on peut faire:

```sh
Rscript r-scripts/get-all-tj-decsisions.r --key-id '****'

```

## 03 - Description des scripts

- `get-all-tj-decisions.r`: [ce script](/r-scripts/get-all-tj-decsisions.r) permet de récupérer toutes les décisions des tribunaux judiciaires publiées depuis la mise en Open Data des TJs.