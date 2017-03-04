# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 15:00:30 2017

@author: odin
"""

#==============================================================================
#Pandas read_csv dtype leading zeros#
#pd.read_csv('filename.csv', dtype={'leading_zero_column_name': object})
df=pd.read_excel(file_name,encoding='gbk',converters={'PO Line Number': lambda x: str(x)})
#==============================================================================

#==============================================================================
# Saving a DataFrame to a Python dictionary
dictionary = df.to_dict()
#==============================================================================


#==============================================================================
# dataframe to list#
#==============================================================================
df = pd.DataFrame({'a':[1,3,5,7,4,5,6,4,7,8,9],
                   'b':[3,5,6,2,4,6,7,8,7,8,9]})
df['a'].values.tolist()
df.values.tolist()
df['a'].tolist()
df['a'].drop_duplicates().values.tolist()
list(set(df['a']))

#==============================================================================
# List unique values
df.name.unique()
#==============================================================================


#==============================================================================
# Create a Dataframe
df = pd.DataFrame(np.random.randn(4, 5), columns=['A', 'B', 'C', 'D', 'E'])
#          A         B         C         D         E
#0  0.673092  0.230338 -0.171681  0.312303 -0.184813
#1 -0.504482 -0.344286 -0.050845 -0.811277 -0.298181
#2  0.542788  0.207708  0.651379 -0.656214  0.507595
#3 -0.249410  0.131549 -2.198480 -0.437407  1.628228

#Calculate the sum of each column of data and add it as a new column to the end
df['Col_sum'] = df.apply(lambda x: x.sum(), axis=1)

#Calculate the sum of each row of data and add it as a new line to the end
df.loc['Row_sum'] = df.apply(lambda x: x.sum())
#                A         B         C         D         E   Col_sum
#0        0.673092  0.230338 -0.171681  0.312303 -0.184813  0.859238
#1       -0.504482 -0.344286 -0.050845 -0.811277 -0.298181 -2.009071
#2        0.542788  0.207708  0.651379 -0.656214  0.507595  1.253256
#3       -0.249410  0.131549 -2.198480 -0.437407  1.628228 -1.125520
#Row_sum  0.461987  0.225310 -1.769627 -1.592595  1.652828 -1.022097
#==============================================================================


#==============================================================================
#Batch read the file, when the larger the data, the more optimized upgrade
now=datetime.datetime.now()
table_test=pd.read_sql_table("inventory_pipeline_temp",engine_df,chunksize=10000)
chunks=[]
for i in table_test:
    chunks.append(i)
df=pd.concat(chunks,ignore_index=True)        
result=datetime.datetime.now()
print(str(result-now))
#==============================================================================


#==============================================================================
df.info()
#View the data type and memory usage#
#==============================================================================

#==============================================================================
# round 2
#method 1
df['A']=df['A'].map('{:,.0f}'.format)
#method 2
df[['A','B']]=np.round([['A','B']].decimals=2)
df[['A','B']]=df[['A','B']].apply(lambda x:pd.Series.round(x,2))
#method 3
df.round(2)
##
df1=df.round({'A':2,'B':3})#not change the original table
#==============================================================================

#==============================================================================
# Remove duplicate data (do not change the original table, if the two are the same, then leave the first pen)
data = pd.DataFrame({'k1': ['one'] * 3 + ['two'] * 4,
                  'k2': [1, 1, 2, 3, 3, 4, 4]})
#To determine whether the line is repeat line
data.duplicated()#return boolean
#Remove duplicate rows
data.drop_duplicates()
#Delete the duplicate value for the specified column
data.drop_duplicates(['k1'])
data.drop_duplicates(['k1'],keep='last')#The same value retains the last one
#==============================================================================

#==============================================================================
# replace
#==============================================================================
df['A'] = df['A'].str.replace(',','.')

# Match string #
df['A'].str.contains('s')
