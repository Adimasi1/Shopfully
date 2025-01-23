# Shopfully
Test Case

**Process Overview**
To complete this task, I followed a structured approach involving data extraction, processing, and visualization.

**1️ Creating and Preparing the Dataset**
Since no initial dataset was provided, I generated synthetic data using Python (Random_data.py).
The dataset was structured to match the expected format.
The final dataset was saved as a CSV file (summary.csv) for further processing.

**2️ Importing Data into MySQL**
The dataset (orders_kpi.csv) was imported into a MySQL database.
A table (orders_kpi) was created to store the data, ensuring that all relevant fields were available.

**3️ Extracting Relevant Data Using SQL**
I wrote and executed an SQL query (SQL_Andrea.sql) to extract and summarize the CTR per order type and month for the specific client (customer_id = 123).
The extracted data was exported as a CSV file (orders_kpi_summary.csv) for further analysis.

**4️ Analyzing and Visualizing the Data in Python**
The extracted data (orders_kpi_summary.csv) was loaded into Python for further processing (Visualization.py).
The script follows a modular approach, making it scalable and reusable
I used Pandas to clean and aggregate the data, ensuring the CTR was calculated correctly.
A pivot table was created to compare CTR trends for the two order types.
Finally, a bar chart was generated to visualize the CTR trends across October and November.
The final bar chart was saved as an image (bar_chart.png), showcasing the CTR trends per month and order type.
