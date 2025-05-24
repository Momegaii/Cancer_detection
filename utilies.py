def load_model(model_path):
    import joblib
    return joblib.load(model_path)

def preprocess_input(input_data, scaler):
    return scaler.transform(input_data)