import pandas as pd
import sqlite3

data_base_file = sqlite3.connect('path_to_data_base_file.db')
excel_file = pd.read_excel('path_to_excel_file.xlsx', sheet_name=None)
for table, data_frame in excel_file.items():
    data_frame.to_sql(table, data_base_file)
