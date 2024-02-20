from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Initialize variables
symptoms = []
diseases = {
    frozenset(['fever', 'cough', 'headache']): 'Common Cold',
    frozenset(['fever', 'rash', 'joint pain']): 'Dengue Fever',
    frozenset(['nausea', 'vomiting', 'diarrhea']): 'Gastroenteritis',
    frozenset(['fatigue', 'muscle aches', 'sore throat']): 'Influenza',
    frozenset(['fever', 'chills', 'sweating']): 'Malaria',
    frozenset(['cough', 'chest pain', 'shortness of breath']): 'Pneumonia',
    frozenset(['abdominal pain', 'bloating', 'constipation']): 'Irritable Bowel Syndrome',
    frozenset(['chest pain', 'shortness of breath', 'sweating']): 'Heart Attack',
    frozenset(['joint pain', 'stiffness', 'swelling']): 'Arthritis',
    frozenset(['fatigue', 'weight gain', 'cold intolerance']): 'Hypothyroidism',
    frozenset(['fatigue', 'weight loss', 'heat intolerance']): 'Hyperthyroidism',
    frozenset(['thirst', 'frequent urination', 'hunger']): 'Diabetes',
    frozenset(['headache', 'nausea', 'sensitivity to light']): 'Migraine',
    frozenset(['runny nose', 'sneezing', 'itchy eyes']): 'Allergic Rhinitis',
    frozenset(['coughing', 'wheezing', 'shortness of breath']): 'Asthma',
    frozenset(['redness', 'itching', 'dryness']): 'Eczema',
    frozenset(['redness', 'swelling', 'pain']): 'Cellulitis',
    frozenset(['painful urination', 'cloudy urine', 'lower back pain']): 'Urinary Tract Infection',
    frozenset(['fever', 'abdominal pain', 'loss of appetite']):'Appendicitis',
    frozenset(['yellowing of skin and eyes','dark urine','abdominal pain']):'Hepatitis A',
    frozenset(['muscle weakness','double vision','drooping eyelids']):'Myasthenia Gravis',
    frozenset(['tremors','stiffness','slow movement']):'Parkinsons Disease',
    frozenset(['numbness','tingling','muscle weakness']):'Multiple Sclerosis',
    frozenset(['memory loss','confusion','mood changes']):'Alzheimers Disease',
    frozenset(['abdominal pain', 'bloating', 'diarrhea']): 'Crohns Disease',
    frozenset(['abdominal pain', 'bloating', 'constipation']): 'Ulcerative Colitis',
    frozenset(['chest pain', 'shortness of breath', 'dizziness']): 'Angina',
    frozenset(['chest pain', 'shortness of breath', 'irregular heartbeat']): 'Atrial Fibrillation',
    frozenset(['joint pain', 'stiffness', 'swelling']): 'Osteoarthritis',
    frozenset(['joint pain', 'stiffness', 'swelling']): 'Rheumatoid Arthritis',
    frozenset(['fatigue', 'hair loss', 'cold intolerance']): 'Anemia',
    frozenset(['fatigue', 'weight loss', 'increased appetite']): 'Graves Disease',
    frozenset(['thirst', 'frequent urination', 'blurred vision']): 'Type 1 Diabetes',
    frozenset(['thirst', 'frequent urination', 'numbness in hands or feet']):'Type 2 Diabetes',
    frozenset(['headache', 'nausea', 'sensitivity to sound']):'Cluster Headaches',
    frozenset(['runny nose','congestion','postnasal drip']):'Sinusitis',
    frozenset(['coughing','wheezing','chest tightness']):'Chronic Obstructive Pulmonary Disease (COPD)',
    frozenset(['redness','swelling','oozing']):'Impetigo',
    frozenset(['redness','swelling','warmth']):'Deep Vein Thrombosis (DVT)',
    frozenset(['painful urination','blood in urine','pelvic pain']):'Bladder Cancer',
    frozenset(['fever','abdominal pain','bloating']):'Diverticulitis',
    frozenset(['yellowing of skin and eyes','abdominal pain','dark urine']):'Hepatitis B',
    frozenset(['muscle weakness','difficulty swallowing','slurred speech']):'Amyotrophic Lateral Sclerosis (ALS)',
    frozenset(['tremors','rigidity','bradykinesia']):'Parkinsons Disease'

}
all_symptoms = set(symptom for disease in diseases for symptom in disease)
greeted = False

# Define routes
@app.route('/')
def index():
    # Render the index page
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    global greeted
    data = request.get_json()
    message = data['message'].lower()
    
    if len(symptoms) == 0:
        # Add the first symptom to the list
        symptoms.append(message)
        # Prompt the user for their second symptom
        response = "Please enter your second symptom:"
          
    elif message not in all_symptoms:
        # Handle unrecognized symptoms
        response = "I'm sorry, but that doesn't seem to be a recognized symptom. Please enter a valid symptom:"
        
    elif len(symptoms) == 1:
        # Add the second symptom to the list
        symptoms.append(message)
        # Prompt the user for their third symptom
        response = "Please enter your third symptom:"
            
    elif len(symptoms) == 2:
        # Add the third symptom to the list
        symptoms.append(message)
        # Suggest a possible disease based on the user's symptoms
        disease = diseases.get(frozenset(symptoms),None)
        if disease:
            response = f"Based on the symptoms you have provided, it is possible that you may have {disease}. It is recommended that you visit a healthcare professional for proper diagnosis and treatment."
        else:
            response = "I'm sorry, but I couldn't find a matching disease based on the symptoms you provided."
    
    return jsonify({'response': response})


@app.route('/initiate_conversation')
def initiate_conversation():
    global greeted
    greeted = True
    response = "Hello! I am a healthcare chatbot. I can suggest possible diseases based on the symptoms you provide. \n\n Please enter your first symptom:"
    response = response.replace('\n', '<br>')
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run()
