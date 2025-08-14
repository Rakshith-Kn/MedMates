import streamlit as st
import requests
from pydantic import BaseModel

API_URL = "http://127.0.0.1:8000/prescribe"  # FastAPI backend

class PrescriptionRequest(BaseModel):
    patient_info: str
    symptoms: str
    context: str = None

def main():
    st.title("💊 AI Medical Prescription Assistant")

    st.markdown(
        """
        Enter the patient's information and symptoms to receive a suggested AI-generated prescription.

        **Note:** This tool is for demonstration purposes only. Always consult a qualified medical professional.
        """
    )

    patient_info = st.text_area("🧑‍⚕️ Patient Information", placeholder="e.g., 45-year-old male, diabetic")
    symptoms = st.text_area("🩺 Symptoms", placeholder="e.g., fever, sore throat, fatigue")
    context = st.text_area("📝 Additional Context (optional)", placeholder="e.g., previous medication reactions")

    if st.button("Generate Prescription"):
        if not patient_info.strip() or not symptoms.strip():
            st.error("⚠️ Please enter both patient information and symptoms.")
        else:
            payload = PrescriptionRequest(
                patient_info=patient_info,
                symptoms=symptoms,
                context=context or None
            ).dict()

            try:
                response = requests.post(API_URL, json=payload)
                response.raise_for_status()
                prescription = response.json().get("prescription", "")

                st.subheader("🧾 Suggested Prescription:")
                st.text_area("Prescription", prescription, height=200)
            except requests.exceptions.RequestException as e:
                st.error(f"🚨 Error contacting backend: {e}")
            except Exception as e:
                st.error(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()
