import pandas as pd

data = {
    'Call ID': [1, 2, 3, 4, 5],
    'Agent': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob'],
    'Duration (minutes)': [5, 10, 7, 12, 8],
    'Customer Satisfaction': [4, 5, 3, 5, 4],
    'Call Type': ['Inquiry', 'Complaint', 'Inquiry', 'Sales', 'Complaint']
}

df = pd.DataFrame(data)

print(df.head(3))
print(df['Agent'])
print(df['Duration (minutes)'])
print(df['Duration (minutes)'].mean())
print(df['Duration (minutes)'].max())
