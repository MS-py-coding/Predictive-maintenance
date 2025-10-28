import json
import joblib
import numpy as np
import os

def init():
    global model
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'predictive_maintenance_model.pkl')
    model = joblib.load(model_path)

def run(raw_data):
    try:
        data = np.array(json.loads(raw_data)['data'])
        preds = model.predict(data)
        return json.dumps({"predictions": preds.tolist()})
    except Exception as e:
        return json.dumps({"error": str(e)})