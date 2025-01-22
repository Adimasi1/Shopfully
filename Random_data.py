# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 23:31:16 2025

@author: andre
"""
# Generate random data for the task
import pandas as pd
import numpy as np

np.random.seed(42)

data = {
    "order_number": np.arange(1, 51),
    "order_type": np.random.choice([1, 2], size=50),
    "order_month": np.random.choice([10, 11], size=50),  # Only October and November
    "order_year": 2024,  # Only 2024
    "customer_id": 123,  # Only customer 123
    "customer_type": np.random.choice(["premium", "standard"], size=50),
    "customer_country": np.random.choice(["Italy", "Poland", "Germany"], size=50),
    "store_id": np.random.randint(100, 200, size=50),
}

# Ensure visualizations are always greater than clicks
clicks = np.random.randint(0, 10000, size=50)
visualizations = clicks + np.random.randint(500, 50000, size=50)  # Ensure visualizations > clicks

data["clicks"] = clicks
data["visualizations"] = visualizations

orders_kpi_df = pd.DataFrame(data)

# Save the DataFrame as a CSV file
# csv_file_path = "C:/Users/andre/OneDrive/Desktop/Database/orders_kpi.csv"
# orders_kpi_df.to_csv(csv_file_path, index=False)
