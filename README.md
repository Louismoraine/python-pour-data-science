Python pour la Data Science
*Projet de programmation réalisé dans le cadre du cours Python pour la Data Science de 2e année*

Vous arrive-t-il d'ouvrir le frigo et de voir les quelques aliments qu'il serait temps d'utiliser mais que, faute d'inspiration, vous n'arrivez pas à utiliser?  
Alors ce projet est fait pour vous!  
L'objectif est de vous proposer des recettes vous permettant d'utiliser les ingrédients qui traînent dans votre frigo plutôt que de les gâcher. Le programme vous renverra la recette la moins calorique vous permettant d'utiliser ces ingrédients!


# Etape 1 - Obtention des données sur les calories et statistiques descriptives

- **Données Ciqual de l'ANSES** obtenues sur data.gouv.
Nous avons importé la bases de données concernant la composition nutritionnelle de plus de 3000 aliments. Les informations apportées par cette base de données concernent par exemple l'apport calorique, en fibre, sucres, sel ou encore l'apport en différentes vitamines par 100 grammes d'aliment.

L'import et le nettoyage de ces données se fait à l'aide du module lecture_ciqual.py. Ce module contient la fonction lecture_excel() renvoyant trois dataframes df_calories, df_svm et df.
- df : Contient les données des ingrédients uniquement : les plats composés tels que salades composées, crudités, soupes, pizzas, tartes et sandwichs ont été supprimés. Seules les variables quantitatives suivantes ont été conservées : Calories, Protéines et Glucides.

- df_svm : Obtenu après supression des valeurs manquantes et conversion des variables quantitatives en numérique. Ce dataframe permettra d'effectuer les statistiques descriptives.

- df_calories : Restriction de df aux deux colonnes Nom et Calories, ce dataframe permettra de calculer le nombre de calories d'une recette.

Le notebook données.ipynb présente des statistiques descriptives en faisant appel à la fonction lecture_excel du module lecture_ciqual.py. Les principaux résultats obtenus sont les suivants :

- Les groupes ayant le plus d'ingrédients sont dans l'ordre 'Viandes, Œufs, Poissons Et Assimilés', 'Fruits, Légumes, Légumineuses Et Oléagineux' et 'Produits Laitiers Et Assimilés'.

- Les catégories qui sont en moyenne les plus caloriques sont, sans grande surprise, les matières grasses, huiles & graisses végétales, suivies par d'autres graisses, les graines et les chocolats. Les catégories les moins caloriques en moyenne sont les fruits, les légumes et les mollusques.

- Les viandes, œufs et poissons ont davantage de protéines.

- Les produits céréaliers et les produits sucrés ont davantage de glucides.


# Etape 1 - Obtention des données

- **Données Ciqual de l'ANSES** obtenues sur data.gouv.
Nous avons importé la base de données concernant la composition nutritionnelle de plus de 3000 aliments. Les informations apportées par cette base de données concernent par exemple l'apport calorique, en fibre, sucres, sel ou encore l'apport en différentes vitamines par 100 grammes d'aliment.

L'import de ces données se fait à l'aide du module lecture_ciqual.py. Ce module contient la fonction lecture_excel() renvoyant trois dataframes df_calories, df_svm et df.
    - df : Contient les données des ingrédients uniquement : les plats composés tels que salades composées, crudités, soupes, pizzas, tartes et sandwichs ont été supprimés. Seules les variables quantitatives suivantes ont été conservées : Calories, Protéines et Glucides.
    - df_svm : Obtenu après supression des valeurs manquantes et conversion des variables quantitatives en numérique. Ce dataframe permettra d'effectuer les statistiques descriptives
    - df_calories : Restriction de df aux deux colonnes Nom et Calories, ce dataframe permettra de calculer le nombre de calories d'une recette.

- **Scrapping sur Marmiton**.
Nous avons comparé les sites de recettes français les plus importants afin de choisir le mieux adapté à notre projet. 
Nous avons donc étudié la structure de Marmiton, Cuisine AZ et 750g.
    Cuisine AZ avait comme avantage de montrer à la fois la note, le temps nécessaire, la difficulté, le niveau de prix et les ingrédients nécessaires sur la page de recherche - donc sans avoir à cliquer sur la recette. L'inconvénient de ce site est qu'il semble que lorsque l'on met deux ingrédients dans la barre de recherche, on ne nous propose que des recettes dont le nom contient les deux ingrédients. Cela limite les possibilités; si on cherche carottes+aubergines on ne verra pas la recette de lasagnes aux aubergines même si celle-ci contient des carottes...

Un des premiers obstacles a été les cookies. Le site propose de les accepter ou bien de s'abonner.

Dans le dossier scraper se trouvent deux fichiers:

    - *installation_chrome.ipynb* : dont l'exécution permet d'installer Chrome ainsi que le webdriver nécessaires au scraping.
    - *scraper_marmiton_selenium.py* : contient le scraper, ce scraper prend en argument deux ingrédients proposés par l'utilisateur ainsi qu'un entier naturel n et renvoie n recettes utilisant les deux ingrédients proposés. 


# Etape 2 - Statistiques descriptives

Les statistiques descriptives s'appuient sur le dataframe df_svm issu du jeu de données Ciqual. Le notebook données.ipynb résume ces statistiques descriptives en faisant appel à la fonction lecture_excel du module lecture_ciqual.py permettant l'import et le nettoyage des données.

Les principaux résultats obtenus sont les suivants :

    - Les groupes ayant le plus d'ingrédients sont dans l'ordre 'Viandes, Œufs, Poissons Et Assimilés', 'Fruits, Légumes, Légumineuses Et Oléagineux' et 'Produits Laitiers Et Assimilés'.
    - Les catégories qui sont en moyenne les plus caloriques sont, sans grande surprise, les matières grasses, huiles & graisses végétales, suivies par d'autres graisses, les graines et les chocolats. Les catégories les moins caloriques en moyenne sont les fruits, les légumes et les mollusques.
    - Les viandes, œufs et poissons ont davantage de protéines.
    - Les produits céréaliers et les produits sucrés ont davantage de glucides.


# Etape 3 - Recherche de la recette la moins calorique

Un problème important est que le nom des ingrédients dans la base de données Ciqual ne correspond pas toujours aux noms qu'ils sont dans les recettes du site Marmiton. Pour résoudre ce problème nous avons utilisé le package rapidfuzz permettant de calculer la distance entre des mots. Ainsi, pour déterminer les calories d'un ingrédient, nous cherchons l'ingrédient de la table Ciqual ayant le nom le plus proche à l'aide de la fonction ingredient_le_plus_proche du module ingredient_fuzzy.py.

Un autre problème important est la gestion des unités puisque la quantité associée à un ingrédient n'est pas toujours exprimée en grammes : la quantité est parfois exprimée en cl, ml, pincées (sel ou poivre), cuillères à soupe, cuillères à café ou gousses (ail). Pour résoudre ce problème, nous avons construit la fonction conversion du module conversions.py prenant en arguments un ingrédient, une quantité, une unité et renvoyant l'ingrédient avec une quantité exprimée en grammes.


# Etape 4 - Modélisation :