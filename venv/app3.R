# Title     : TODO
# Objective : TODO
# Created by: nisha
# Created on: 14-07-2019

data = read.csv('data.csv')

#data$Exp <- factor(data$Exp)
#data$Salary <- factor(data$Salary)

lm_ = lm(data$Salary ~ data$Exp, data)
#print(lm_)


plot(data$Exp, data$Salary)
#r.squared(lm_)
print(25792 + 9450*4.0)