import pandas as pd

df = pd.read_csv("sample_human_gait.csv")
print(df.head())

left_knee = df[(df['leg'] == 1) & (df['joint'] == 'knee')]

import matplotlib.pyplot as plt

# Filter for left leg, 1st replication
hip = df[(df['leg'] == 1) & (df['joint'] == 'hip') & (df['replication'] == 1)]
knee = df[(df['leg'] == 1) & (df['joint'] == 'knee') & (df['replication'] == 1)]

plt.plot(hip['angle'].values, knee['angle'].values)
plt.xlabel("Hip Angle (°)")
plt.ylabel("Knee Angle (°)")
plt.title("Cyclogram - Left Leg (Replication 1)")
plt.grid()
plt.show()
