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
