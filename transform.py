"""
Transform de data, of bitcoin, and clean the data, on import the fields: Name and price
args: price_dolar: Actual price of Peso Argentino, with respect to dolar
"""

import pandas as pd

def transform(price_dolar):
    """
    Transform the data of the source and save this in the target csv
    """
    path_target = "./target/Precio_Bitcoin_ARS.csv"
    path_source = "./target/Precio_Bitcoin.csv"
    
    df = pd.read_csv(path_source)

    df["Price_ARS"] = df["Price"] * price_dolar

    df = df.drop(["Price"], axis=1)
    
    df.to_csv(path_target, index=False)