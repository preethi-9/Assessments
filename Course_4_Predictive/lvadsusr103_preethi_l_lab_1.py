# -*- coding: utf-8 -*-
"""LVADSUSR103_Preethi_L_lab_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10iqtHTDlvPP4FUjvN8uo39AjESTs7MSW
"""

#1
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,precision_score,recall_score

#a
data = pd.read_csv("/content/drive/MyDrive/winequality-red.csv")
# printing first 10 values
data.info()
data.head()

#checking for null values
data.isnull().sum()
data['fixed acidity'].sort_values()
data['fixed acidity'] = data['fixed acidity'].fillna(method='bfill')
data['volatile acidity'].sort_values()
data['volatile acidity'] = data['volatile acidity'].fillna(method='bfill')
data['residual sugar'].sort_values()
data['residual sugar'] = data['residual sugar'].fillna(method='bfill')
data['chlorides'].sort_values()
data['chlorides'] = data['chlorides'].fillna(method='bfill')
data['sulphates'].sort_values()
data['sulphates'] = data['sulphates'].fillna(method='bfill')
data['citric acid'].sort_values()
data['citric acid'] = data['citric acid'].fillna(method='bfill')
data['residual sugar'].sort_values()
data['residual sugar'] = data['residual sugar'].fillna(method='ffill')
data['free sulfur dioxide'].sort_values()
data['free sulfur dioxide'] = data['free sulfur dioxide'].fillna(method='bfill')
data.isnull().sum()

#outliers detection
Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
#InterQuartile Range
IQR = Q3 - Q1
threshold_value = 1.5
Outliers = (data < (Q1 - threshold_value * IQR)) | (data  > (Q3 + threshold_value * IQR))
data_file = data[~Outliers.any(axis=1)]
print("Outliers are : \n",Outliers,"\n")
print("Without outliers: \n",data_file)

data.head()

def map_quality(quality):
    if quality >= 3 and quality <= 6:
        return 0
    elif quality >= 7 and quality <= 8:
        return 1
    else:
        return None
data['quality'] = data['quality'].apply(map_quality)

data.head(10)

quality_dist = data['quality'].value_counts()
print("Wine quality distribution:")
print(quality_dist)

plt.figure(figsize=(8, 6))
quality_dist.plot(kind='bar', color='gray')
plt.title('Wine Quality Distribution')
plt.xlabel('Quality')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()

X = data.drop(columns=['quality'])
y = data['quality']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
smote = SMOTE(random_state = 42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

selected_features = X.columns

from sklearn.metrics import classification_report
rf_classifier = RandomForestClassifier(random_state=42)
rf_classifier.fit(X_train_resampled, y_train_resampled)
rf_predictions = rf_classifier.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_predictions)
print("Random Forest Classifier Accuracy:", rf_accuracy)
print("Random Forest Classifier Classification Report:")
print(classification_report(y_test, rf_predictions))