import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('weather_data.csv')

# Line Chart - Temperature
plt.figure(figsize=(10, 5))
plt.plot(data['Day'], data['Temperature'], marker='o', color='red', label='Temperature (°C)')
plt.title('Temperature Over the Week')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Bar Chart - Humidity
plt.figure(figsize=(10, 5))
plt.bar(data['Day'], data['Humidity'], color='skyblue', label='Humidity (%)')
plt.title('Humidity Over the Week')
plt.xlabel('Day')
plt.ylabel('Humidity (%)')
plt.legend()
plt.tight_layout()
plt.show()

# Pie Chart - Wind Speed Contribution
plt.figure(figsize=(7, 7))
plt.pie(data['WindSpeed'], labels=data['Day'], autopct='%1.1f%%', startangle=140)
plt.title('Wind Speed Contribution Throughout the Week')
plt.tight_layout()
plt.show()
