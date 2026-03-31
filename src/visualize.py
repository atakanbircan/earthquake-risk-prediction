import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

from src.train import train_model


def plot_earthquake_map(data_path: str):
    df = pd.read_csv(data_path)

    gdf = gpd.GeoDataFrame(
        df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude)
    )

    url = "https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip"
    world = gpd.read_file(url)
    turkey = world[world.NAME == "Turkey"]

    fig, ax = plt.subplots(figsize=(10, 6))
    turkey.plot(ax=ax, color='lightgrey')

    gdf.plot(ax=ax, markersize=df['Magnitude'] ** 2,
             column='Magnitude', cmap='Reds', legend=True, alpha=0.6)

    plt.show()


import os

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(current_dir, "..", "data", "earthquake_data.csv")

    plot_earthquake_map(data_file)