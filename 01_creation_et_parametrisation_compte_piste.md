# Création et paramétrisation d'un compte PISTE pour l'utilisation de Judilibre

## Prérequis

Pour créer un compte PISTE, il suffit d'une adresse e-mail.

## Création d'un compte PISTE

Pour créer un compte PISTE, rendez-vous sur le site de [PISTE](https://piste.gouv.fr):

![Accueil du site PISTE](/images/piste-accueil.png)

Cliquez sur `Créer un compte` et remplissez le formulaire avec: 

- votre nom
- votre adresse e-mail
- un mot de passe
- en acceptant les Conditions Générales d'Utilisation
- en acceptant ou refusant les communications optionnelles
- en remplissant le CAPTCHA

![Page de création de compte PISTE](/images/piste-inscription.png)

On peut ensuite cliquer sur `S'inscrire`. Un mail de confirmation est envoyé à l'adresse proposée. Il suffit de cliquer sur le lien `Activez votre compte`.

![Mail de confirmation de création du compte](/images/piste-confirmation.png)

Le compte est à présent créé et activé. 


## Paramétrisation du compte pour l'utilisation de Judilibre

Une fois le compte créé, il faut le paramétrer pour utiliser l'API Judilibre.

### Première connexion

Commencez par vous connecter à votre compte:

![Page de connexion à PISTE](/images/piste-connexion.png).

PISTE devrait alors vous demandez d'accepter les CGU. Pour continuer, il faudra accepter ces conditions.

![Modal d'acceptation des conditions](/images/piste-conditions.png)

On est alors redirigé la page d'accueil de PISTE:

![Page d'accueil du compte PISTE](/images/piste-connecte.png).

### Consentement aux conditions d'utilisation de Judilibre

Pour utiliser une API via PISTE, il nous faut accepter les conditions générales d'utilisation spécifique à l'API.

Dans la bar de navigation, cliquez sur `API > Consentement CGU API`.

![Page de consentement aux CGU des API](/images/piste-mes-consentements.png)


Il faut ensuite sélectionner les APIs que l'on souhaite utiliser. On pourra s'aider de la barre de recherche pour trouver Judilibre. Il faut ensuite cochez les lignes qui correspondent à Judilibre puis cliquer sur `Valider mes choix CGU`.

![Page de consentement aux CGU des API avec recherche de Judilibre](/images/piste-mes-consentements-judilibre.png).

### Modification de l'application

Maintenant que les conditions de Judilibre ont été acceptées, on doit modifier nos applications pour les autoriser à utiliser Judilibre.

Cliquez sur le lien `Applications` dans la barre de navigation:

![Page d'accueil des applications PISTE](/images/piste-mes-applications.png)

Sélectionnez votre application:

![Page de présentation de l'application PISTE](/images/piste-mon-application.png)

Cliquez sur le bouton `Modifier l'application`:

![Page de modification de l'application](/images/piste-mon-application-modification.png)

Dans la liste des applications, sélectionnez `JUDILIBRE` puis cliquez sur `Appliquer les modifications`.

## Notes sur la sécurité

Vos identifiants, et en particulier vos clefs d'API, sont privés et ne devraient pas être partagés. Si vos clefs sont diffusées, vous pouvez retourner sur l'onglet de modification de votre application (`Applications` puis `Modifier l'application`), choisir l'onglet `Authentification` et générer de nouvelles clefs et supprimer les anciennes:

![Page de modificaiton des clefs de l'application ](/images/piste-mon-application-authentification.png)

## Notes sur la Sandbox

Les décisions sont publiées sur l'environnement de production. Si la Sandbox est régulièrement mise à jour, elle peut avoir du retard. 

> Les droits de l'application créée automatiquement lors de l'inscription ne sont pas suffisants pour utiliser l'API en production. Une API qui a les droits pour la sandbox n'aura pas nécessairement les droits pour la production.

Pour avoir les droits de consommation de l'API de production, il faut recréer une application, accepter les conditions générales d'utilisation de l'API en production, puis dans l'onglet modification de l'application, on sélectionne JUDILIBRE (production), puis on clique sur `Appliquer les modifications`.

![Page de modification de l'API avec les droits pour JUDILIBRE acceptés](/images/piste-application-modification-judilibre-prod.png)

