import pandas as pd
import plotly.express as px
import numpy as np
import re

def get_data():

    # Read data
    df = pd.read_csv("dataset.csv")

    # Any further data preprocessing can go here
    time_list = df['Time'].tolist()
    hour_list = [re.findall('([0-9]+)\:[0-9]+', i) for i in time_list]
    df['Hour'] = hour_list
    df['Hour'] = df['Hour'].str[0]

    # Redefine rows with unknown values
    df = df.replace(['?', -1, np.nan], 100000000)

    df = df.astype('str')

    return df
