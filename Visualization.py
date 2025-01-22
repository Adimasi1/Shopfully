# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 14:55:00 2025

@author: andre
"""
import pandas as pd
import matplotlib.pyplot as plt

# Function to load data
def load_data(file_path):
    df = pd.read_csv(file_path, delimiter=";", skipinitialspace=True)
    df.columns = df.columns.str.strip()  # Clean column names
    return df

# Function to process data
def process_ctr_data(df):
    ctr_summary = df.groupby(["order_month", "order_type"]).agg(
        total_clicks=("total_clicks", "sum"),
        total_visualizations=("total_visualizations", "sum")
    ).reset_index()
    ctr_summary["CTR"] = ctr_summary["total_clicks"] / ctr_summary["total_visualizations"]
    return ctr_summary

# Function to create visualization
def plot_ctr_chart(ctr_summary):
    ctr_pivot = ctr_summary.pivot(index="order_month", columns="order_type", values="CTR")
    ctr_pivot.plot(kind="bar", figsize=(8, 5))

    plt.xlabel("Month")
    plt.ylabel("Average CTR")
    plt.title("Average CTR per Month per Order Type")
    plt.xticks(ticks=[0, 1], labels=["October", "November"], rotation=0)
    plt.legend(title="Order Type")
    plt.show()

# Run the previous steps - the summary is from random data, replace it if needed
file_url = "https://raw.githubusercontent.com/Adimasi1/Shopfully/main/summary.csv"
df = load_data(file_url)
ctr_summary = process_ctr_data(df)
plot_ctr_chart(ctr_summary)
