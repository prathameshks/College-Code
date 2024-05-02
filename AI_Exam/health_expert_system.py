def select_diseases(symptoms):
    diseases = {
        "Allergies": ['sneezing', 'blocked nose', 'watery eyes', 'red eyes', 'coughing', 'red rash'],
        "Asthma": ['wheezing', 'shortness of breath', 'tight chest'],
        "Head Tumor": ['severe headaches', 'seizures', 'mental changes', 'vision problem'],
        "Chronic Pain": ['diabetes', 'arthritis', 'back pain'],
        "Dehydration": ['feeling thirsty', 'dry mouth', 'tiredness', 'strong smelling urine'],
        "Food Poisoning": ['nausea', 'vomiting', 'weakness', 'loss of appetite', 'aching muscles', 'chills','sneezing']
    }

    # Convert all disease symptoms to lower case for case insensitive matching
    diseases = {disease: [symptom.lower() for symptom in symptoms_list] for disease, symptoms_list in diseases.items()}

    matching_diseases = []
    
    # AND based expert system 
    for disease, disease_symptoms in diseases.items():
        flag = True
        for sym in symptoms:
            if sym not in disease_symptoms:
                flag = False
        if flag:
            matching_diseases.append(disease)
                
    # OR based expert system
    # for disease, disease_symptoms in diseases.items():
    #     if any(symptom in disease_symptoms for symptom in symptoms):
    #         matching_diseases.append(disease)


    return matching_diseases


# Prompt the user to enter symptoms
symptoms_input = input("Enter your symptoms (separated by commas): ")

# Check if user entered any symptoms
if not symptoms_input.strip():
    print("No symptoms were entered. Please try again.")
else:
    # Convert symptoms to lower case and remove leading/trailing spaces
    symptoms = [symptom.strip().lower() for symptom in symptoms_input.split(',')]

    # Select the diseases based on symptoms
    diagnosed_diseases = select_diseases(symptoms)

    # Print the diagnosed diseases or an error message if no match found
    if diagnosed_diseases:
        print("You may have the following disease(s):")
        for disease in diagnosed_diseases:
            print("- " + disease)
    else:
        print("Unable to diagnose any disease based on the given symptoms.")
