from src.preprocessing import load_data
from src.features import create_features
from src.model import train_model

print("Loading data...")
df = load_data()

print("Creating features...")
df = create_features(df)

print("Training model...")
train_model(df)

print("✅ DONE")