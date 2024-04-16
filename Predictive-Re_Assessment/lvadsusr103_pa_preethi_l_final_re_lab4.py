# -*- coding: utf-8 -*-
"""LVADSUSR103_PA_Preethi_L_FINAL_RE_lab4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bjmGzcIXee3N5H1kNNvxSJkMxra8g1Y0
"""

#4
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.metrics import silhouette_score
from sklearn.impute import SimpleImputer
from sklearn.ensemble import IsolationForest
from sklearn.svm import SVC
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from xgboost import XGBClassifier
from xgboost import XGBRegressor
from sklearn.metrics import accuracy_score,f1_score,mean_absolute_error,mean_squared_error,r2_score,classification_report,confusion_matrix

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv("/content/drive/MyDrive/anomaly_train.csv")
df

# Handle missing values
df.fillna(0, inplace=True)

#Feature Engineering (if needed)
# No specific feature engineering is mentioned in the description

#statistics
df.describe()

# Visualization
sns.pairplot(df)
plt.show()

# Identify categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
# Initialize LabelEncoder
label_encoder = LabelEncoder()
for col in categorical_cols:
    df[col] = label_encoder.fit_transform(df[col])

X = df.drop(['Time'], axis=1)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# Anomaly Detection using Isolation Forest
outlier_detector = IsolationForest(contamination=0.05, random_state=42)
outliers = outlier_detector.fit_predict(X_scaled)

df['anomaly_flag'] = np.where(outliers == -1, 'Anomaly', 'Normal')

# Further Investigation
# Further actions can be decided based on the 'anomaly_flag'

# Print flagged anomalies for further investigation
print("Flagged Anomalies:")
print(df[df['anomaly_flag'] == 'Anomaly'])