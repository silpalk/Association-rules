###Association rules for boks data


install.packages("arules")
library(arules)# Used for building association rules i.e. apriori algorithm
rm(list = ls())
books <-read.csv(file.choose())
inspect(books[1:5])


class(books)
summary(books)
arules <- apriori(books, parameter = list(support=0.7, confidence = 0.8, maxlen = 6))

arules
# Viewing rules based on lift value
inspect(head(sort(arules, by = "lift"))) # to view we use inspect 

# Overal quality 
head(quality(arules))


library("arulesViz") # for visualizing rules

# Different Ways of Visualizing Rules
plot(arules)

windows()
plot(arules, method = "grouped")
plot(arules[1:10], method = "graph") # for good visualization try plotting only few rules


write(arules, file = "a_rules1.csv", sep = ",")

getwd()
###############################################################################

##Association rules for movies data


library(readr)
my_movies<-read.transactions(file.choose())
my_movies <-my_movies[1:11,6:15]
summary(my_movies)
inspect(my_movies)
library("arules")
# Building rules using apriori algorithm
arules <- apriori(my_movies, parameter = list(support = 0.002, confidence = 0.75, minlen = 2))
arules
# Viewing rules based on lift value
inspect(head(sort(arules, by = "lift"))) # to view we use inspect 

# Overal quality 
head(quality(arules))

# install.packages("arueslViz")
library("arulesViz") # for visualizing rules

# Different Ways of Visualizing Rules
plot(arules)

windows()
plot(arules, method = "grouped")
plot(arules[1:10], method = "graph") # for good visualization try plotting only few rules

################################################################################
##Association rules framing for phone data

library(readr)
phone_data<-read.transactions(file.choose())
phone_data <-phone_data[1:11,4:9]
summary(phone_data)
library("arules")
inspect(phone_data)

# Building rules using apriori algorithm
arules <- apriori(phone_data, parameter = list(support = 0.0012, confidence = 0.75, minlen = 4))
arules
# Viewing rules based on lift value
inspect(head(sort(arules, by = "lift"))) # to view we use inspect 

# Overal quality 
head(quality(arules))

# install.packages("arueslViz")
library("arulesViz") # for visualizing rules

# Different Ways of Visualizing Rules
plot(arules)

windows()
plot(arules, method = "grouped")
plot(arules[1:10], method = "graph") # for good visualization try plotting only few rules

##################################################################################
##Association rules for retail transactions data

library(arules)
retail <- read.transactions("C://Users//Amarnadh Tadi//Desktop//datascience//assign6//transactions_retail1.csv", sep = ",")
summary(retail)
# showing only top 5 transactions
inspect(retail[1:5])
# retail is in transactions format
class(retail)
# Building rules using apriori algorithm
# Keep changing support and confidence values to obtain different rules
arules <- apriori(retail, parameter = list(support = 0.001, confidence = 0.75, minlen = 2))
arules
# Viewing rules based on lift value
inspect(head(sort(arules, by = "lift"))) # to view we use inspect 

# Overal quality 
head(quality(arules))

# install.packages("arueslViz")
library("arulesViz") # for visualizing rules

# Different Ways of Visualizing Rules
plot(arules)

windows()
plot(arules, method = "grouped")
plot(arules[1:10], method = "graph") # for good visualization try plotting only few rules

#############################################################################
##Association rules for groceries data

data("Groceries") # loading the Groceries Data
?Groceries

inspect(Groceries[1:5]) # showing only top 10 transactions
class(Groceries) # Groceries is in transactions format

summary(Groceries)

# making rules using apriori algorithm 
# Keep changing support and confidence values to obtain different rules

# Building rules using apriori algorithm
arules <- apriori(Groceries, parameter = list(support = 0.001, confidence = 0.75, minlen = 2))
arules

# Viewing rules based on lift value
inspect(head(sort(arules, by = "lift"))) # to view we use inspect 

# Overal quality 
head(quality(arules))

# install.packages("arueslViz")
library("arulesViz") # for visualizing rules

# Different Ways of Visualizing Rules
plot(arules)

windows()
plot(arules, method = "grouped")
plot(arules[1:10], method = "graph") # for good visualization try plotting only few rules
