import streamlit as st

# Apply background color using a more general selector
st.markdown(
    """
    <style>
    /* Apply background color to the entire page */
    .stApp {
        background-color: #f4bbff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.title("Dashboard")
option = st.sidebar.radio("Select Category", ["Home", "Prediction", "About"])

if option == 'Home':
    st.title("Heart Disease Prediction System")
    image_path = "th (1).jpeg"
    st.image(image_path, use_column_width=True)
    st.markdown("""
    Welcome to the Heart Disease Prediction System!  

    Our mission is to help identify Heart diseases efficiently. 

    ### How It Works?
                
      1.***Enter Your Information:*** Fill in details such as age, gender, cholesterol level, and blood pressure on the webpage.
                
      2.***Submit Your Data***: Click the "Submit" button to send your information for analysis.

      3.***AI Analysis:*** Our system processes your data using advanced AI to assess your risk of heart disease.

      4.***Get Results:*** Instantly view your prediction result along with helpful recommendations based on the analysis
    """)

elif option == 'About':
    st.header("About")
    st.markdown("""
    -***Number of Records***: Over 1000 patient records.
                
    -***Types of Data***: The dataset includes a range of medical attributes such as age, gender, cholesterol levels, blood pressure, and more.
                
    -***Data Sources***: Records were collected from medical clinics, health surveys, and trusted medical databases.
                
    -***Diversity***: The dataset encompasses a wide variety of patient profiles, including different ages, genders, and health conditions, to ensure accurate predictions for all users.
                
    -***Annotations***: Each record is meticulously reviewed and annotated by medical professionals to provide reliable training data for the AI model.
    """)

elif option == 'Prediction':
    
    age = st.number_input("Age", min_value=1, max_value=100, value=25)
    Sex= st.number_input("Sex (1 for male and 0 for Female)", min_value=0, max_value=1, value=1)
    bp = st.number_input("Resting Blood Pressure", min_value=50, max_value=200, value=120)
    cholesterol = st.number_input("Cholesterol", min_value=100, max_value=800, value=200)
    Chest_pain_type = st.number_input("Chest_pain_type", min_value=1, max_value=4, value=1)
    max_hr = st.number_input("Maximum Heart Rate", min_value=50, max_value=200, value=100)
    FBS_over_120 = st.number_input("Fasting Blood Sugar ", min_value=0, max_value=10, value=5)
    EKG_results = st.number_input("EKG_results", min_value=0, max_value=2, value=0)
    Exercise_angina = st.text_input("Exercise_angina", value='No')
    ST_depression = st.number_input("ST_depression", min_value=0.0, max_value=10.0, value=2.5)
    Slope_of_ST = st.number_input("Slope_of_ST", min_value=0, max_value=5, value=1)
    Number_of_vessels_fluro = st.number_input("MNumber_of_vessels_fluro", min_value=0, max_value=10, value=3)
    Thallium = st.number_input("Thallium", min_value=0, max_value=10, value=5)
    
    

    if st.button('Predict'):
        import pandas as pd
        from sklearn.model_selection import train_test_split
        from sklearn.preprocessing import StandardScaler,LabelEncoder
        from sklearn.linear_model import LogisticRegression
        from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

        # Load your dataset
        df = pd.read_csv("Heart_Disease_Prediction.csv")

        le=LabelEncoder()
        df['Heart Disease']=le.fit_transform(df['Heart Disease'])
    

        # Features and target
        X = df.drop(columns='Heart Disease')
        y = df['Heart Disease']

        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Scale the features
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        # Initialize and fit the logistic regression model
        model = LogisticRegression()
        model.fit(X_train_scaled, y_train)

        # Get prediction probabilities
        y_pred_proba = model.predict_proba(X_test_scaled)

        # Set a custom threshold
        threshold = 0.60 # You can adjust this value

        # Make predictions based on the custom threshold
        y_pred_custom = (y_pred_proba[:, 1] >= threshold).astype(int)

    
        
        if Exercise_angina=='Yes':
                  Exercise_angina=1
        else:
                  Exercise_angina=0
        def predict_heart_disease():
                  		
        # Create DataFrame from user input
            user_data = pd.DataFrame({
            'Age': [age],
            'Sex':[Sex],
            'Chest pain type' :[Chest_pain_type],
            'BP': [bp],
            'Cholesterol': [cholesterol],
            'FBS over 120' :[FBS_over_120],
            'EKG results' :[EKG_results],
            'Max HR': [max_hr],
            'Exercise angina' :[Exercise_angina],
            'ST depression': [ST_depression],
            'Slope of ST' :[Slope_of_ST],
            'Number of vessels fluro' :[Number_of_vessels_fluro],
            'Thallium':[Thallium]
    })

    # Scale the user data
            user_data_scaled = scaler.transform(user_data)

    # Get prediction probability for the user input
            user_pred_proba = model.predict_proba(user_data_scaled)[0, 1]

    # Make prediction based on the custom threshold
            prediction = 1 if user_pred_proba >= threshold else 0
            st.write(f"**Prediction: {' ⚠️ Warning: You may be at risk of heart disease' if prediction == 1 else '🎉Great! You have no signs of heart disease'}**")
            st.write(f"**Probability of Heart Disease: {user_pred_proba:.2f}**")

# Call the function to get user input and predict
        predict_heart_disease()

      
       


