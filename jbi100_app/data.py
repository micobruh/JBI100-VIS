import datetime
import re

import numpy as np
import pandas as pd


def get_data():
    # Set low_mamory=False to inhibit error message
    # when the server is booting up
    # low_memory = False

    # Read data
    return process_data(read_data("dataset.csv"))


def read_data(filename):
    return pd.read_csv(filename)


# Any further data preprocessing can go here
def process_data(df):
    time_list = df['Time'].tolist()
    hour_list = [re.findall('([0-9]+)\:[0-9]+', i) for i in time_list]
    df['Hour'] = hour_list
    df['Hour'] = df['Hour'].str[0]

    # Redefine rows with unknown values
    df = df.replace(['?', -1, np.nan], 100000000)
    df = df.astype('str')

    return df


def update_date(start_date, end_date):
    start_date_date = datetime.date.fromisoformat(start_date)
    end_date_date = datetime.date.fromisoformat(end_date)

    start_date_datetime = datetime.datetime.combine(start_date_date, datetime.datetime.min.time())
    end_date_datetime = datetime.datetime.combine(end_date_date, datetime.datetime.min.time())

    min_date = start_date_datetime.timestamp()
    max_date = end_date_datetime.timestamp()

    # Read data again
    df = process_data(read_data("dataset.csv"))

    date_list = df['Date'].tolist()
    i = 0
    for entry in date_list:
        row_date = entry.split("/")
        entry_date = datetime.datetime(int(row_date[2]), int(row_date[1]), int(row_date[0]), 0, 0, 0).timestamp()
        if entry_date < min_date or entry_date > max_date:
            df.drop(i, inplace=True)
        i += 1
    df = df.astype('str')

    return df
