from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import MultiLabelBinarizer
import numpy as np

class DiseasePredictor:
    def __init__(self):
        self.symptoms = []
        self.diseases = ['Common Cold', 'Influenza', 'Allergy', 'COVID-19']
        self.medication_recommendations = {
            'Common Cold': ['Rest', 'Stay hydrated', 'Over-the-counter cold medicine'],
            'Influenza': ['Antiviral medication', 'Rest', 'Stay hydrated'],
            'Allergy': ['Antihistamines', 'Avoid allergens', 'Nasal decongestants'],
            'COVID-19': ['Isolate yourself', 'Seek medical attention', 'Follow health guidelines']
        }
        self.mlb = MultiLabelBinarizer()
        self.model = self.train_model()

    def train_model(self):
        X_train = [
            ['fever', 'cough', ''],
            ['fever', 'cough', 'fatigue'],
            ['cough', 'sneezing', 'runny nose'],
            ['fever', 'cough', 'shortness of breath']
        ]
        y_train = ['Common Cold', 'Common Cold', 'Allergy', 'COVID-19']
        X_train = self.mlb.fit_transform(X_train)
        model = DecisionTreeClassifier()
        model.fit(X_train, y_train)
        return model

    def get_input_symptoms(self):
        self.symptoms = input("Enter your symptoms separated by commas: ").strip().lower().split(',')

    def predict_disease(self):
        X_test = np.array([self.symptoms])
        X_test = self.mlb.transform(X_test)
        prediction = self.model.predict(X_test)
        return prediction[0] if prediction else None

    def recommend_medication(self, disease):
        if disease in self.medication_recommendations:
            return self.medication_recommendations[disease]
        else:
            return []

    def run(self):
        try:
            self.get_input_symptoms()
            disease = self.predict_disease()
            if disease:
                print("Predicted Disease:", disease)
                recommendations = self.recommend_medication(disease)
                if recommendations:
                    print("Medication Recommendations:")
                    for med in recommendations:
                        print("-", med)
                else:
                    print("No medication recommendations available for this disease.")
            else:
                print("Unable to predict disease based on provided symptoms.")
        except Exception as e:
            print("Error:", e)

# Testing
if __name__ == "__main__":
    predictor = DiseasePredictor()
    predictor.run()
