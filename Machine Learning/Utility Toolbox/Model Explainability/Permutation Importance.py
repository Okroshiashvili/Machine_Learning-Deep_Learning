


"""
One of the most basic question we ask while building model is what features
have the biggest impact on model accuracy? or what features are the most important?

This is well known concept in data science community.

Here, we focus on "Permutation Importance". So, how it works?

"Permutation Importance is calculated after the model has been fitted.
So, our model do not change. The main question we ask here is the the following:
If I randomly shuffle a single column of the validation data, leaving the
target and all other columns in place, how would it affect the accuracy of
predictions in that now-shuffled data?

If after random shuffle of one column deteriorates the model accuracy the most,
the most important feature it is.

"""


"""
Data link:
    https://www.kaggle.com/mathan/fifa-2018-match-statistics#FIFA%202018%20Statistics.csv

"""



import eli5
import numpy as np
import pandas as pd
from eli5.sklearn import PermutationImportance
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv('FIFA 2018 Statistics.csv')


y = (df['Man of the Match'] == 'Yes')

feature_names = [i for i in df.columns if df[i].dtype in [np.int64]]

X = df[feature_names]


X_train, X_val, y_train, y_val = train_test_split(X,y, random_state=1)


model = RandomForestClassifier(random_state = 0).fit(X_train, y_train)


# To calculate and show importance we need "eli5" library

permutations = PermutationImportance(model,random_state=1).fit(X_val,y_val)

eli5.show_weights(permutations, feature_names=X_val.columns.tolist())
