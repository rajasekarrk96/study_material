---
id: "02_13_02"
title: "Pandas Fundamentals"
course: "Python"
module: 13
module_title: "Scientific Python"
lesson: 2
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["pandas", "DataFrame", "Series", "read-csv", "groupby", "merge", "pivot", "apply", "fillna", "dropna", "loc", "iloc", "datetime"]
prerequisites: []
lab_required: true
---

# Pandas Fundamentals


## Pandas Basics

```python
import pandas as pd

# Series — 1D labeled array
s = pd.Series([1, 2, 3], index=["a", "b", "c"])

# DataFrame — 2D labeled table
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "score": [85.5, 92.0, 78.5]
})

# Loading data
df = pd.read_csv("data.csv")
df = pd.read_excel("data.xlsx", sheet_name="Sheet1")
df = pd.read_json("data.json")
```

## Selection and Filtering

```python
df["name"]           # column as Series
df[["name","age"]]   # multiple columns as DataFrame

# loc — label-based
df.loc[0]             # row by index label
df.loc[0:2, "name":"age"]   # rows 0-2, cols name to age

# iloc — integer position
df.iloc[0]            # first row
df.iloc[0:3, 0:2]     # first 3 rows, first 2 cols

# Boolean filtering
df[df["age"] > 28]
df[(df["age"] > 25) & (df["score"] >= 80)]
df.query("age > 25 and score >= 80")
```

## Essential Operations

```python
df.info()            # dtypes, null counts
df.describe()        # statistics
df.shape             # (rows, cols)
df.dtypes            # column types
df.head(5)           # first 5 rows
df.tail(5)           # last 5 rows

# Sorting
df.sort_values("score", ascending=False)
df.sort_values(["age", "score"])

# Missing values
df.isnull().sum()           # count nulls per column
df.dropna()                 # drop rows with any null
df.fillna(0)                # fill nulls with 0
df.fillna(df.mean())        # fill with column means

# Rename columns
df.rename(columns={"name": "full_name"})

# Apply function
df["score_grade"] = df["score"].apply(
    lambda x: "A" if x >= 90 else "B" if x >= 75 else "C"
)
```

## GroupBy

```python
# Split → Apply → Combine
grouped = df.groupby("department")
grouped["salary"].mean()      # mean salary per department
grouped["salary"].agg(["mean", "max", "count"])

grouped.apply(lambda g: g.nlargest(3, "salary"))  # top 3 per group
```

## Merge and Join

```python
# merge (SQL-style join)
merged = pd.merge(orders, customers,
                  left_on="customer_id", right_on="id",
                  how="left")

# concat (stack DataFrames)
all_data = pd.concat([df1, df2, df3], ignore_index=True)
```

## Lab Exercise
1. Load a sales CSV, compute monthly revenue grouped by product category
2. Merge two DataFrames (orders + products) and calculate average order value
3. Find and fill missing values: numerical with mean, categorical with mode
