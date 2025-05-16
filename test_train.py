
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


df = pd.read_csv("milk_quality.csv")


df.columns = df.columns.str.strip()


k = 3
model = KMeans(n_clusters=k, random_state=42)
df['quality_group'] = model.fit_predict(df[['pH', 'temperature']])


print("\nClustered data with quality groups:\n", df)


cluster_summary = df.groupby('quality_group').agg({'pH': ['mean', 'std'], 'temperature': ['mean', 'std']})
print("\nCluster summary (mean and std of pH and temperature):\n", cluster_summary)


cluster_labels = {0: 'Fresh', 1: 'Spoiled', 2: 'Borderline'}  # Example assignment


df['quality_label'] = df['quality_group'].map(cluster_labels)


df.to_csv("milk_with_quality_group_and_label.csv", index=False)
print("\nSaved clustered data with labels to 'milk_with_quality_group_and_label.csv'.")


overall_quality = df['quality_label'].mode()[0]
print("\nOverall milk quality based on most frequent cluster label:", overall_quality)


plt.figure(figsize=(8, 6))
scatter = plt.scatter(df['pH'], df['temperature'], c=df['quality_group'], cmap='viridis', s=100)
plt.xlabel('pH')
plt.ylabel('Temperature (°C)')
plt.title('Milk Quality Clustering')
plt.colorbar(label='Cluster (Quality Group)')


for i, txt in enumerate(df['quality_label']):
    plt.annotate(txt, (df['pH'][i], df['temperature'][i]), fontsize=8, color='black')

plt.grid(True)
plt.show()
