'''
The intent of this code is to learn how to use ML to predict house prices. I should be able to go line by line and figure out
what each line does. Apply it to a dataset of my choice and ask Chat GPT for questions.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load Dataset (Replace with actual dataset path or API call)
df = pd.read_csv('real_estate_data.csv')  # Replace with actual dataset

# Display first few rows
display(df.head())

# Data Preprocessing
numerical_features = ['square_feet', 'bedrooms', 'bathrooms', 'year_built']
categorical_features = ['city', 'property_type']


def preprocess_data(df):
    # Handling missing values
    df = df.dropna()

    # Splitting data into features and target
    X = df[numerical_features + categorical_features]
    y = df['price']

    # Preprocessing pipeline
    num_transformer = StandardScaler()
    cat_transformer = OneHotEncoder(handle_unknown='ignore')

    preprocessor = ColumnTransformer([
        ('num', num_transformer, numerical_features),
        ('cat', cat_transformer, categorical_features)
    ])

    return X, y, preprocessor


X, y, preprocessor = preprocess_data(df)

# Splitting Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Model Evaluation
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
print(f'RMSE: {rmse}, R² Score: {r2}')

# Visualization
plt.figure(figsize=(6, 4))
sns.scatterplot(x=y_test, y=y_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted Prices")
plt.show()
