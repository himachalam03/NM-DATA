import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

np.random.seed(42)

start_date = "2025-04-01 00:00:00"
end_date = "2025-04-30 23:00:00"
date_range = pd.date_range(start=start_date, end=end_date, freq='H')

def simulate_usage(hour):
    if 0 <= hour < 6:
        return np.random.uniform(0.2, 0.5)
    elif 6 <= hour < 9:
        return np.random.uniform(1.0, 2.0)
    elif 9 <= hour < 17:
        return np.random.uniform(0.5, 1.5)
    elif 17 <= hour < 21:
        return np.random.uniform(2.0, 3.5)
    else:
        return np.random.uniform(0.5, 1.0)

usage_data = [simulate_usage(ts.hour) for ts in date_range]

df = pd.DataFrame({
    'Timestamp': date_range,
    'Energy_kWh': usage_data
})
df['hour'] = df['Timestamp'].dt.hour
df['day'] = df['Timestamp'].dt.date

hourly_avg = df.groupby('hour')['Energy_kWh'].mean().reset_index()
top_hours = hourly_avg.sort_values(by='Energy_kWh', ascending=False).head(3)

plt.figure(figsize=(12, 6))
sns.lineplot(data=hourly_avg, x='hour', y='Energy_kWh', marker='o')
plt.axhline(y=top_hours['Energy_kWh'].min(), color='r', linestyle='--', label='Peak Threshold')
plt.title("Average Hourly Energy Consumption (April 2025)")
plt.xlabel("Hour of Day")
plt.ylabel("Energy (kWh)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

def generate_recommendations(peak_hours):
    recommendations = []
    for hour in peak_hours['hour']:
        recommendations.append(f"Reduce energy usage during {hour}:00 by shifting activities to off-peak hours or using efficient appliances.")
    return recommendations

recommendations = generate_recommendations(top_hours)
print("\nEnergy Optimisation Recommendations:")
for tip in recommendations:
    print(f"- {tip}")
