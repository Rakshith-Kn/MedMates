# MedMates
Medication errors cause millions of preventable injuries yearly. Our AI system uses IBM Watson, Hugging Face NLP and detect drug interactions, check age-specific dosages, and suggest safe alternatives—fast, accurate, and reliable for healthcare providers.


#📌 #Description

Medical Prescription is an AI-powered system designed to verify and analyze prescriptions for safety and accuracy.
It helps detect drug interactions, confirm correct dosages, and suggest safe alternative medications based on a patient’s age and drug details.
The project integrates IBM Watson AI and Hugging Face NLP models to process medical text efficiently.

🚀 #Features

✅ Drug interaction detection

✅ Dosage verification

✅ Alternative medicine suggestions

✅ User-friendly interface with Streamlit

✅ Fast and secure backend using FastAPI


🛠 # Tech Stack

Frontend: Streamlit

Backend: FastAPI

AI Models: IBM Watson, Hugging Face Transformers


Others: Python, Pandas, NLP techniques


# Install dependencies
pip install -r requirements.txt

💡 Usage

1. Run the backend:

uvicorn main:app --reload


2. Run the frontend:

streamlit run app.py


3. Upload a prescription or type drug details to check interactions and get suggestions.
