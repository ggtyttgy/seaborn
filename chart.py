import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Seaborn style for professional appearance
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic data for support efficiency analysis
np.random.seed(42)
departments = ["Tech Support", "Customer Service", "Billing", "Sales"]
data = {
    "Department": np.random.choice(departments, 400),
    "Resolution_Time": np.concatenate([
        np.random.normal(30, 5, 100),   # Tech Support
        np.random.normal(45, 7, 100),   # Customer Service
        np.random.normal(25, 4, 100),   # Billing
        np.random.normal(35, 6, 100),   # Sales
    ])
}

df = pd.DataFrame(data)

# Create violin plot
plt.figure(figsize=(8, 8))  # 8 inches * 64 dpi = 512 pixels
sns.violinplot(
    x="Department",
    y="Resolution_Time",
    data=df,
    palette="Set2",
    inner="quartile"
)

# Titles and labels
plt.title("Resolution Time Distribution by Department", fontsize=16, weight="bold")
plt.xlabel("Department", fontsize=14)
plt.ylabel("Resolution Time (minutes)", fontsize=14)

# Save plot with exact 512x512 pixels
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
