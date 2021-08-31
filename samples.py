# Code to strip HTML formatting from a dataframe column
df['column'] = df['column'].apply(lambda x: re.sub('<[^<]+?>', '', x))

# Collapse columns to fill null values
df.ffill(1).iloc[:,-1]
