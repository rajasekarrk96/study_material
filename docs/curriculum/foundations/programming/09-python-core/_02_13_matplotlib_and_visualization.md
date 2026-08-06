---
id: "02_13_03"
title: "Matplotlib and Visualization"
course: "Python"
module: 13
module_title: "Scientific Python"
lesson: 3
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["matplotlib", "pyplot", "figure", "axes", "plot", "scatter", "bar", "hist", "subplot", "seaborn", "plotly", "savefig", "style"]
prerequisites: []
lab_required: true
---

# Matplotlib and Visualization


## Matplotlib Basics

```python
import matplotlib.pyplot as plt
import numpy as np

# Line plot
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(x, y, color="blue", linewidth=2, label="sin(x)")
ax.plot(x, np.cos(x), "r--", linewidth=1.5, label="cos(x)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Sine and Cosine")
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("plot.png", dpi=150)
plt.show()
```

## Common Plot Types

```python
# Scatter
ax.scatter(x, y, c=colors, s=sizes, alpha=0.6)

# Bar
ax.bar(categories, values, color="steelblue")
ax.barh(categories, values)   # horizontal

# Histogram
ax.hist(data, bins=30, density=True, alpha=0.7)

# Box plot
ax.boxplot([group1, group2, group3], labels=["A","B","C"])

# Pie
ax.pie(sizes, labels=labels, autopct="%1.1f%%")
```

## Subplots

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes[0, 0].plot(x, y)
axes[0, 1].scatter(x, y)
axes[1, 0].bar(cats, vals)
axes[1, 1].hist(data)
plt.tight_layout()
```

## Seaborn — Statistical Plots

```python
import seaborn as sns

# Distribution
sns.histplot(df["score"], kde=True)
sns.boxplot(x="department", y="salary", data=df)
sns.violinplot(x="category", y="value", data=df)

# Relationships
sns.scatterplot(x="age", y="salary", hue="department", data=df)
sns.lineplot(x="date", y="revenue", data=df)

# Correlation heatmap
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", vmin=-1, vmax=1)

# Pair plot
sns.pairplot(df, hue="category")
```

## Lab Exercise
1. Plot monthly sales trends with dual y-axes (revenue + units sold)
2. Create a correlation heatmap for a financial dataset using Seaborn
3. Build an interactive scatter plot using `plotly.express.scatter()`
