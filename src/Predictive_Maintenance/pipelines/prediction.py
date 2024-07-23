import pickle


class Prediction:
    def __init__(self):
        with open("artifacts/scaler.pkl","rb") as f:
                self.scaler = pickle.load(f)
        with open("artifacts/model.pkl","rb") as f:
                self.model = pickle.load(f)
    def predict(self,type_value, rpm, torque, tool_wear, air_temp, process_temp):
        #preporocessing 
        if type_value == 'Low':
            type_value = int(0)
        elif type_value == 'Medium':    
                type_value = int(1)
        elif type_value == 'High':    
                type_value = int(2)

        type_value = float(type_value)   

        #scaling
        scaled_input = self.scaler.transform([[rpm, torque, tool_wear, air_temp, process_temp]])
        rpm, torque, tool_wear, air_temp, process_temp = scaled_input[0]
        
        #prediction
        prediction = self.model.predict([[type_value, rpm, torque, tool_wear, air_temp, process_temp]])
        if prediction[0] == 0:
                result = 'No Failure'
        elif prediction[0] == 1:
                result = 'Machine Failure'            
        return result
