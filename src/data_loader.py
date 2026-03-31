import pandas as pd


def load_and_preprocess_data(filepath: str):
    df = pd.read_csv(filepath)

    df = df[['Latitude', 'Longitude', 'Depth', 'Magnitude', 'Date']]
    df = df.dropna()

    df['Date'] = pd.to_datetime(df['Date'], format='mixed', dayfirst=True)
    df['year'] = df['Date'].dt.year
    df['month'] = df['Date'].dt.month

    X = df[['Latitude', 'Longitude', 'Depth']]
    y = df['Magnitude']

    return X, y