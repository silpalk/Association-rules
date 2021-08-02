# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules
#loading the data set
books=pd.read_csv(r"C:\Users\Amarnadh Tadi\Desktop\datascience\assign6\book.csv")
# showing the data 
books.head()
books.columns
books.isnull().sum()## no null values

##item frequencies can be caluculated by  Counter class

from collections import Counter
item_frequencies=Counter(books)

##to obtain frequent_itemsets by apriori algorithm


frequent_itemsets=apriori(books,min_support=0.012,max_len=4,use_colnames=True)

##sorting of frequent itemsets by support value
frequent_itemsets.sort_values('support',ascending=False,inplace=True)
# barplot of top 10 
import matplotlib.pyplot as plt

%matplotlib inline
plt.bar(x=list(range(0,11)),height=frequent_itemsets.support[0:11],color='rgmyk')
plt.xlabel("item_sets")
plt.ylabel("support")

##framing association rules
rules=association_rules(frequent_itemsets,metric="lift",min_threshold=1)
rules.sort_values('lift',ascending=False,inplace=True)
rules.head(10)

##associate rules for movies data set


import pandas as pd
import matplotlib.pyplot as plt

movies=pd.read_csv(r"C:\Users\Amarnadh Tadi\Desktop\datascience\assign6\my_movies.csv")
#data preprocessing
##Dropping of columns
movies1=movies.iloc[: ,5:15]
movies1.columns
movies1.head()
movies1.isnull().sum()

####to obtain frequent_itemsets by apriori algorithm from mlxtend
from mlxtend.frequent_patterns import apriori, association_rules
frequent_itemsets=apriori(movies1,min_support=0.012,max_len=4,use_colnames=True)
##sorting of frequent itemsets by support value
frequent_itemsets.sort_values('support',ascending=False,inplace=True)
%matplotlib inline
##barplot for 10 values
plt.bar(x=list(range(0,11)),height=frequent_itemsets.support[0:11],color='rgmyk')
plt.xlabel("item_sets")
plt.ylabel("support")
##framing of associate rules
rules=association_rules(frequent_itemsets,metric="lift",min_threshold=1)
##sorting of rules by lift values
rules.sort_values('lift',ascending=False,inplace=True)
rules.head()

 
###phone data associate rules
import pandas as pd
import matplotlib.pyplot as plt

phonedata=pd.read_csv(r"C:\Users\Amarnadh Tadi\Desktop\datascience\assign6\myphonedata.csv")
#data preprocessing
##Dropping of columns
phonedata1=phonedata.iloc[: ,3:9]
phonedata1.columns
phonedata1.head()
phonedata1.isnull().sum()

####to obtain frequent_itemsets by apriori algorithm from mlxtend
from mlxtend.frequent_patterns import apriori, association_rules
frequent_itemsets=apriori(phonedata1,min_support=0.012,max_len=3,use_colnames=True)
##sorting of frequent itemsets by support value
frequent_itemsets.sort_values('support',ascending=False,inplace=True)
%matplotlib inline
##barplot for 10 values
plt.bar(x=list(range(0,11)),height=frequent_itemsets.support[0:11],color='rgmyk')
plt.xlabel("item_sets")
plt.ylabel("support")
##framing of associate rules
rules=association_rules(frequent_itemsets,metric="lift",min_threshold=1)
##sorting of rules by lift values
rules.sort_values('lift',ascending=False,inplace=True)
rules.head()

##association rules for transaction data set
import pandas as pd
import matplotlib.pyplot as plt
retail_transaction=pd.read_csv(r"C:\Users\Amarnadh Tadi\Desktop\datascience\assign6\transactions_retail1.csv",header=None)
##data preprocessing

retail_transaction.isnull().sum()
##dropping last column data
retail_transaction1=retail_transaction.iloc[:557042,:5]
retail_transaction1.columns
##imputing nan values
retail_transaction1.fillna( value=0, axis=1, inplace=True)
retail_transaction1.isnull().sum()
retail_transaction1=retail_transaction.iloc[:557042,:5]
retail_transaction1.columns

##
from mlxtend.preprocessing import TransactionEncoder
y=retail_transaction1.to_numpy()

te = TransactionEncoder()
te_ary = te.fit_transform(y.astype(int))
retail_new=pd.DataFrame(te_ary,columns=te.columns_)#te.columns_List of unique names in the Y input list of lists
retail_new.head()

####to obtain frequent_itemsets by apriori algorithm from mlxtend
from mlxtend.frequent_patterns import apriori, association_rules
frequent_itemsets=apriori(retail_new,min_support=0.012,max_len=5,use_colnames=True)
##sorting of frequenting items by support values
frequent_itemsets.sort_values('support',ascending=False,inplace=True)
%matplotlib inline
#barplot for 10 values
plt.bar(x=list(range(0,11)),height=frequent_itemsets.support[0:11],color='rgmyk')
plt.xlabel("item_sets")
plt.ylabel("support")
##framing of associate rules
rules=association_rules(frequent_itemsets,metric="lift",min_threshold=1)
##sorting of rules by lift values
rules.sort_values('lift',ascending=False,inplace=True)
rules.head()
