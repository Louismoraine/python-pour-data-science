import geopandas as gpd
import contextily as ctx
import matplotlib.pyplot as plt

from cartiflette import carti_download

communes_borders = carti_download(
    crs=4326,
    values=["75", "92", "93", "94"],
    borders="COMMUNE",
    vectorfile_format="geojson",
    filter_by="DEPARTEMENT",
    source="EXPRESS-COG-CARTO-TERRITOIRE",
    year=2022,
)
communes_borders.sample(3)
communes_borders.crs
communes_borders = communes_borders.to_crs(2154)
communes_92 = communes_borders.loc[communes_borders["INSEE_DEP"]=="92"]
communes_92.crs
communes_92.plot()

#Projet

#Boxplots
from matplotlib.ticker import MaxNLocator

# Création du graphique 
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))  

# Boxplot
ax = sns.boxplot(y='Groupe', x='Calories', data=df_svm, palette="Set3", hue = 'Groupe', legend = False)

# Calculer les moyennes par catégorie
mean_values = df_svm.groupby('Groupe')['Calories'].mean().reset_index()

# Ajouter des croix pour les moyennes
ax.scatter(mean_values['Calories'], mean_values['Groupe'], 
           color='lightcoral', marker='X', s=75, label='Moyenne', zorder = 3)

# Ajout des étiquettes et du titre
plt.title("Distribution de Calories selon le groupe d'ingredients", fontsize=14,fontweight='bold')
plt.xlabel('Calories (kcal/100g)', fontsize=10)
plt.ylabel('')
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=10))

# Faire pivoter les étiquettes de l'axe des x si nécessaire
plt.yticks(rotation=0, ha='right', fontsize = 10)
plt.grid(True)
plt.legend()
# Ajuster l'affichage pour éviter les chevauchements
plt.tight_layout()

# Afficher le graphique
plt.show()