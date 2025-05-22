import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt

np.random.seed(42)
n_samples = 500
temperature = np.random.normal(loc=22, scale=3, size=n_samples)
occupancy = np.random.randint(0, 50, size=n_samples)
time_of_day = np.random.randint(0, 24, size=n_samples)
hvac_usage = 2.5 * occupancy + 1.2 * (25 - temperature) + 0.5 * time_of_day + np.random.normal(0, 5, size=n_samples)

df = pd.DataFrame({
    'Temperature': temperature,
    'Occupancy': occupancy,
    'TimeOfDay': time_of_day,
    'EnergyConsumption': hvac_usage
})

X = df[['Temperature', 'Occupancy', 'TimeOfDay']]
y = df['EnergyConsumption']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error: {mae:.2f} kWh")
print(f"R^2 Score: {r2:.2f}")

plt.figure(figsize=(10, 5))
plt.scatter(y_test, y_pred, alpha=0.6, color='teal')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel("Actual Energy Consumption (kWh)")
plt.ylabel("Predicted Energy Consumption (kWh)")
plt.title("Actual vs Predicted Energy Usage")
plt.tight_layout()
plt.show()
