import os
import joblib

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier


def train_model(df):

    num = [
        'sizeusd','executionprice','fee',
        'size_price_ratio','fee_ratio',
        'hour','day','prev_pnl','rolling_pnl'
    ]

    cat = ['side','direction','classification']

    X = df[num + cat]
    y = df['target']

    num_pipe = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])

    cat_pipe = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    preprocessor = ColumnTransformer([
        ('num', num_pipe, num),
        ('cat', cat_pipe, cat)
    ])

    model = Pipeline([
        ('prep', preprocessor),
        ('model', RandomForestClassifier())
    ])

    model.fit(X, y)

    # Save model
    base_dir = os.path.dirname(os.path.dirname(__file__))
    model_dir = os.path.join(base_dir, "models")
    os.makedirs(model_dir, exist_ok=True)

    model_path = os.path.join(model_dir, "model.pkl")
    joblib.dump(model, model_path)

    print("Model saved at:", model_path)

    return model