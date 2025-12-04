
# Repro script for Phase 4 plots (matplotlib)
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import numpy as np

df = pd.read_csv('/mnt/data/phase4_outputs/clean_data_phase4.csv')
df['Purchase_Date'] = pd.to_datetime(df['Purchase_Date'], errors='coerce')
df['Final_Price(Rs.)'] = pd.to_numeric(df['Final_Price(Rs.)'], errors='coerce')
df['Price (Rs.)'] = pd.to_numeric(df['Price (Rs.)'], errors='coerce')
df['Discount (%)'] = pd.to_numeric(df['Discount (%)'], errors='coerce')

# Time series
ts = df.set_index('Purchase_Date').resample('D')['Final_Price(Rs.)'].sum().fillna(0)
plt.figure(figsize=(10,4))
plt.plot(ts.index, ts.values)
plt.xlabel('Date'); plt.ylabel('Daily Revenue (Final_Price Rs.)'); plt.title('Time Series - Daily Revenue (Final Price)')
plt.tight_layout(); plt.savefig('time_series_daily_revenue.png'); plt.close()
