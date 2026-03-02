import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Load dataset
def load_data(filepath):
    data = pd.read_csv(filepath)
    return data

# Preprocess the dataset
def preprocess_data(data):
    # Example preprocessing: Fill missing values and select features
    data.fillna(method='ffill', inplace=True)
    features = data[['temperature', 'humidity', 'wind_speed']]  # example features
    labels = data['heat_stress']  # target variable
    return features, labels

# Train the Random Forest model
def train_model(features, labels):
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model, X_test, y_test

# Evaluate the model
def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    report = classification_report(y_test, predictions)
    print(report)

# Save the model
def save_model(model, filename):
    joblib.dump(model, filename)

if __name__ == "__main__":
    # Example usage
    data = load_data('heat_stress_data.csv')  # replace with your dataset path
    features, labels = preprocess_data(data)
    model, X_test, y_test = train_model(features, labels)
    evaluate_model(model, X_test, y_test)
    save_model(model, 'heat_stress_model.pkl')
