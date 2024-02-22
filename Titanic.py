# Import necessary libraries
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the dataset
titanic_data = pd.read_csv('train.csv')

# Preprocess the data
titanic_data = titanic_data.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1) # Drop irrelevant columns
titanic_data = pd.get_dummies(titanic_data, columns=['Sex', 'Embarked']) # One-hot encode categorical columns
titanic_data['Age'] = titanic_data['Age'].fillna(titanic_data['Age'].median()) # Fill missing age values with the median age
titanic_data['Fare'] = titanic_data['Fare'].fillna(titanic_data['Fare'].median()) # Fill missing fare values with the median fare

# Split the data into training and testing sets
X = titanic_data.drop(['Survived'], axis=1) # Extract features (all columns except 'Survived')
y = titanic_data['Survived'] # Extract target variable ('Survived' column)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # Split the data into training and testing sets

# Train a Random Forest classifier on the training data
rfc = RandomForestClassifier(n_estimators=100, random_state=42) # Instantiate a Random Forest classifier with 100 trees
rfc.fit(X_train, y_train) # Fit the classifier to the training data

# Predict the survival outcomes for the testing data
y_pred = rfc.predict(X_test) # Predict the target variable ('Survived') for the testing data

# Evaluate the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred) # Calculate the accuracy of the classifier
print('Accuracy:', accuracy) # Print the accuracy score