import pandas as pd

df = pd.DataFrame()

df.iloc[:1,:]  # only first row (index 0)
df.loc[:1,:]  # first row and second row

# Access a single value for a row/column pair by integer position.
df.iat[1, 2]

df.sort_index(axis=1, ascending=False)

df.to_numpy()

df.copy()
df_new = df  # changes will be in two dataframes.

df.nlargest(n, columns, keep='first')
df.nsmallest(n, columns, keep='all')

df.isin([1, 2, 3])

df.iterrows()
# get each index and row | for i,value in df.iloc[:5,:].iterrows():

df.isna()
df.isnull()
df.notna()

# rename column
df.rename(columns={'skip_2': 'skip_2_first_half'}, inplace=True)

# duplicates
df.drop_duplicates(subset=None, keep='first', inplace=False)
df.duplicated(subset=None, keep='first')

# insert rows
df.append(df2, ignore_index=True)

# summary
df.agg({'Outside': ['sum', 'count']})
df.groupby(by=['CompanyId'], as_index=False).sum()

# compare datetime
df[df['Date'] > '2018-03-19']


time_range = pd.date_range(start='2-01-2019', end='3-01-2019', freq='H')

# get %m %Y
# python datetime strptime

# pd.concat
# https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
pd.concat([df1, df2, df3, df4])

# merge df with df_summary on some columns
pd.merge(df, df_tail, on=['tail'], how='left')
