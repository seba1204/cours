# Projet PIM

## Recommandations

### Ne pas encombrer le serveur SVN avec des fichiers inutiles

**Ne pas pousser sur SVN les gros exemples.**

Vous pouvez les avoir dans votre copie locale mais il ne faut pas les mettre
sur SVN car vous n'avez pas à les modifier, qu'on peut les retrouver
facilement sur Moodle et qu'ils vont inutilement occuper beaucoup de place sur
le serveurs SVN. Il y a pas loin de 100 équipes !.

De la même façon, on ne met pas les exécutables ni aucun fichier résultat de
la compilation.

Si vous le faites, outre la place gaspillée sur le serveur, vous allez avoir
de nombreux conflits car SVN ne saura pas faire la fusion des fichiers objets
ou exécutables !

### Pousser régulièrement vos modifications

Vous devez pousser régulièrement vos modifications. Définissez de petits
objectifs (écrire un sous-programme, tester un sous-programme, améliorer un
algorithmique, etc.) et dès qu'il est atteint vous pousser vos modifications
sur le serveurs SVN.

Faites aussi des `svn update` régulièrement pour limiter les conflits et
communiquez avec votre coéquipier !

## Organisation du dépôt SVN

- `src/` : pour les sources de votre projet (fichiers .adb, ads, etc.)
- `livrables/` : les fichiers qui sont demandés dans le sujet. Attention à
respecter les noms. Certains sont déjà là. Il suffit de les remplacer.
- `docs/` : c'est ici que vous pouvez mettre les fichiers qui vous permettent
d'obtenir le rapport (par exemple fichier LaTeX, markdown, etc.)

## Autres informations

### TODO

- [ ] Passer la précision du type `T_Double` du module `Helpers` en générique.
- [ ] Meilleure gestion des erreurs (si possible l'exporter du pagerank.adb)
- [x] Créer les fichiers dans le dossier d'où vient le `.net`
- [ ] Ajouter un logger avec une option -v
- [ ] Ajouter un dossier obj vide dans l'archive à rendre
