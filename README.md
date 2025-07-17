# DiseasePredictor

**DiseasePredictor** is a Python-based application that predicts diseases based on input symptoms and provides medication recommendations. It uses machine learning techniques, specifically a decision tree classifier, to predict diseases from a set of common symptoms. The model also recommends appropriate medications for the predicted disease.

## Features

- **Symptom-based Disease Prediction**: Input symptoms are used to predict a possible disease.
- **Medication Recommendations**: Based on the predicted disease, the application provides general medication recommendations.
- **Simple Command-Line Interface**: The tool uses a straightforward CLI, where users input their symptoms, and it outputs the predicted disease and recommended medications.

## Supported Diseases

- **Common Cold**
- **Influenza**
- **Allergy**
- **COVID-19**

## Technologies Used

- **Python** (Programming Language)
- **scikit-learn** (For the Decision Tree Classifier)
- **NumPy** (For data manipulation)
- **MultiLabelBinarizer** (For encoding symptoms)

## Requirements

To run this project, you need Python 3.x.

## Setup and Installation

Follow these steps to set up the project using the provided virtual environment:

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/dhruvgupta3389/DiseasePredictor.git
cd DiseasePredictor
```
### 2. Install Requirements
You can install the required libraries using pip:
``` 
pip install -r requirements.txt
```
### 3.Run the Application:
```
python module.py
```
### 3.Input Symptoms:
The application will prompt you to enter your symptoms separated by commas. For example:
```
Enter your symptoms separated by commas: fever, cough, fatigue
```
### 4.Get the Result:
The application will predict the disease based on the symptoms and suggest a list of recommended medications. Example output:
```
Predicted Disease: Common Cold
Medication Recommendations:
- Rest
- Stay hydrated
- Over-the-counter cold medicine
```
## Example
Here’s an example of how the program works:
```
Enter your symptoms separated by commas: fever, cough, shortness of breath
Predicted Disease: COVID-19
Medication Recommendations:
- Isolate yourself
- Seek medical attention
- Follow health guidelines
```
