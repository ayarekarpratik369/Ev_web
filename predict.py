import pandas as pd
import pickle

# Fault label map
fault_map = {
    0: "Normal",
    1: "Battery_Overheat",
    2: "Battery_Undervoltage",
    3: "Motor_Overload",
    4: "Coolant_Failure",
    5: "Fire_Risk",
    6: "Cell_Imbalance"
}

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("top10_features.pkl", "rb") as f:
    top10_features = pickle.load(f)



def predict_fault(user_input: dict):
    input_df = pd.DataFrame([user_input])[top10_features]
    prediction = model.predict(input_df)[0]

    return {
        "label": int(prediction),
        "fault": fault_map[prediction]
    }