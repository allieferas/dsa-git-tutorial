import pandas as pd
import numpy as np

def clean_tree_data(df):
    columns_to_keep = [
        'Stormwater Gallons Saved',
        'CO2 Avoided (in lbs.)',
        'kWh Saved',
        'Therms Saved',
        'Pollutants Saved (in lbs.)',
        'Property Benefits ($)'
        'Site ID'
        #changing some stuff because there is some stuff to be changed
    ]
    df = df[columns_to_keep].dropna().reset_index(drop=True)
    df = df.loc[np.all(df>0,axis=1)].reset_index(drop=True) #on the assumption that zeros are missing data. whateverrrr
    return df