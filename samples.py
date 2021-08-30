# Code to strip HTML formatting from a dataframe column
df['column'] = df['column'].apply(lambda x: re.sub('<[^<]+?>', '', x))
