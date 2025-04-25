import pandas as pd

data = {
    'Call ID': [1, 2, 3, 4, 5],
    'Agent': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob'],
    'Duration (minutes)': [5, 10, 7, 12, 8],
    'Customer Satisfaction': [4, 5, 3, 5, 4],
    'Call Type': ['Inquiry', 'Complaint', 'Inquiry', 'Sales', 'Complaint']
}


df = pd.DataFrame(data)

while ['Agent'] == 'Alice':

    alice_calls = df[df['Agent'] == 'Alice']
    print(alice_calls)

call_type_satisfaction = df.groupby('Call Type')['Customer Satisfaction'].mean()
print(call_type_satisfaction)

df['Cost'] = df['Duration (minutes)'] * 2
print(df)

sorted_df = df.sort_values(by='Duration (minutes)', ascending=False)
print(sorted_df)

agent_duration = df.groupby('Agent')['Duration (minutes)'].mean()
print(agent_duration)

print(df.head(3))
print(df['Agent'])