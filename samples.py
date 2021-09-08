# Code to strip HTML formatting from a dataframe column
df['column'] = df['column'].apply(lambda x: re.sub('<[^<]+?>', '', x))

# Collapse columns to fill null values
df.ffill(1).iloc[:,-1]

# Create a target feature column
df.loc[df['Status'] == 'Yes', 'Target'] = 1
df.loc[df['Status'] == 'No', 'Target'] = 0

# Drop excess columns
df.drop(columns = ['Column A', 'Column W'])
