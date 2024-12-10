import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Lire le fichier Excel
def lecture_excel():
    df = pd.read_excel('https://ciqual.anses.fr/cms/sites/default/files/inline-files/Table%20Ciqual%202020_FR_2020%2007%2007.xls')


    # Sélection des variables : noms, calories, sucres, fibres alimentaires, protéines, gludices, lipides
    df = df.loc[:,["alim_grp_nom_fr","alim_ssgrp_nom_fr","alim_ssssgrp_nom_fr","alim_nom_fr","Energie, Règlement UE N° 1169/2011 (kcal/100 g)","Sucres (g/100 g)","Fibres alimentaires (g/100 g)","Protéines, N x 6.25 (g/100 g)","Glucides (g/100 g)","Lipides (g/100 g)"]]

    # Renommer les variables
    df = df.rename(columns={'alim_grp_nom_fr': 'Groupe', 'alim_ssgrp_nom_fr':'Sous-groupe', 'alim_ssssgrp_nom_fr':'Sous-sous-groupe', 'alim_nom_fr':'Nom', 'Energie, Règlement UE N° 1169/2011 (kcal/100 g)': 'Calories', 'Sucres (g/100 g)' : 'Sucres', 'Fibres alimentaires (g/100 g)' : 'Fibres', 'Protéines, N x 6.25 (g/100 g)' : 'Protéines', 'Glucides (g/100 g)' : 'Glucides', 'Lipides (g/100 g)' : 'Lipides'})

    # Calories
    categ_a_supprimer=['salades composées et crudités', 'soupes', 'plats composés',
    'pizzas, tartes et crêpes salées', 'sandwichs',
    'feuilletées et autres entrées',
    'pains et assimilés', 'biscuits apéritifs', 
    'autres produits à base de viande', 
    'produits à base de poissons et produits de la mer', 
    'substitus de produits carnés', 
    'crèmes et spécialités à base de crème', 'eaux', 'boissons sans alcool',
    'confiseries non chocolatées',
    'confitures et assimilés', 'viennoiseries', 'biscuits sucrés',
    'céréales de petit-déjeuner', 'barres céréalières',
    'gâteaux et pâtisseries', '-', 'glaces', 'sorbets', 'desserts glacés',
    'huiles de poissons',
    'aides culinaires', 
    'denrées destinées à une alimentation particulière',
    'aides culinaires et ingrédients pour végétariens', 'ingrédients divers',
    'laits et boissons infantiles', 'petits pots salés et plats infantiles',
    'desserts infantiles', 'céréales et biscuits infantiles']
    df_calories = df[~df['Sous-groupe'].isin(categ_a_supprimer)]
    df_calories = df_calories.loc[:,["Nom","Calories"]]

    # Noms des Groupes et Sous-groupes en majuscule
    df['Groupe'] = df['Groupe'].str.title()
    df['Sous-groupe'] = df['Sous-groupe'].str.title()

    # Elimination des plats composés
    df = df[~df["Groupe"].isin(['Entrées Et Plats Composés','Glaces Et Sorbets','Aliments Infantiles'])]

    # Supression des valeurs manquantes
    df_svm = df.replace(to_replace=r'^<.*', value=np.nan, regex=True)
    df_svm = df_svm.dropna()
    for i in range(6):
        df_svm = df_svm[df_svm.iloc[:,i+4] != '-']
        df_svm = df_svm[df_svm.iloc[:,i+4] != 'traces']

    # Conversion en numéique 
    for i in range(6):
        df_svm.iloc[:,i+4] = pd.to_numeric(df_svm.iloc[:,i+4].str.replace(',', '.', regex=False))

    # Calories
    df_calories = df_calories.replace(to_replace=r'^<.*', value=np.nan, regex=True)
    df_calories = df_calories.dropna()
    df_calories = df_calories[df_calories["Calories"] != '-']
    df_calories = df_calories[df_calories["Calories"] != 'traces']
    df_calories["Calories"] = pd.to_numeric(df_calories["Calories"].str.replace(',', '.', regex=False))

    return df_calories,df_svm




