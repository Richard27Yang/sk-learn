# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

"""
Please note, this code is only for python 3+. If you are using python 2+, please modify the code accordingly.
"""
from __future__ import print_function
from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
X = iris.data
y = iris.target

# test train split #
#==============================================================================
# X_train, X_test,y_train,y_test=train_test_split(X,y,random_state=4)
# knn = KNeighborsClassifier(n_neighbors=5)
# knn.fit(X_train,y_train)
# print(knn.score(X_test,y_test))
# 
#==============================================================================

from sklearn.cross_validation import cross_val_score
#==============================================================================
# knn = KNeighborsClassifier(n_neighbors=5)
# scores = cross_val_score(knn,X,y,cv=5,scoring='accuracy')
# print(scores.mean())
#==============================================================================
# this is cross_val_score #

import matplotlib.pyplot as plt
k_range  = range(1,31)
k_scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
##    loss = -cross_val_score(knn, X, y, cv=10, scoring='mean_squared_error') # for regression
    scores = cross_val_score(knn,X,y,cv=10,scoring='accuracy')
    k_scores.append(scores.mean())

plt.plot(k_range,k_scores)
plt.xlabel('Values of K for KNN')
plt.ylabel('Cross-validation Accuracy')
plt.show()
    
# this is how to use cross_val_score to choose model and configs #














