import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

np.random.seed(42)

start_date = "2025-04-01"
end_date = "2025-04-30 23:00:00"
date_range = pd.date_range(start=start_date, end=end_date, freq='H')

def simulate_usage(hour):
    if 0 <= hour < 6:
        return np.random.uniform(0.2, 0.5)
    elif 6 <= hour < 12:
        return np.random.uniform(0.5, 1.2)
    elif 12 <= hour < 18:
        return np.random.uniform(1.0, 2.5)
    elif 18 <= hour < 22:
        return np.random.uniform(2.0, 3.5)
    else:
        return np.random.uniform(0.5, 1.0)

usage_data = [simulate_usage(ts.hour) for ts in date_range]

df = pd.DataFrame({
    'Timestamp': date_range,
    'Energy_kWh': usage_data
})
df['Hour'] = df['Timestamp'].dt.hour
df['Day'] = df['Timestamp'].dt.date

hourly_avg = df.groupby('Hour')['Energy_kWh'].mean().reset_index()
top_hours = hourly_avg.sort_values(by='Energy_kWh', ascending=False).head(3)

plt.figure(figsize=(12, 6))
sns.lineplot(data=hourly_avg, x='Hour', y='Energy_kWh', marker='o')
plt.axhline(y=top_hours['Energy_kWh'].min(), color='r', linestyle='--', label='Peak Threshold')
plt.title('Average Hourly Energy Consumption')
plt.xlabel('Hour of Day')
plt.ylabel('Average Energy (kWh)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

def generate_recommendations(df, peak_hours):
    tips = []
    for hour in peak_hours['Hour']:
        tips.append(f"Reduce energy usage during {hour}:00 by shifting activities to off-peak hours or using efficient appliances.")
    return tips

recommendations = generate_recommendations(df, top_hours)

print("\nEnergy Optimization Recommendations:")
for tip in recommendations:
    print(f"- {tip}")
