from faker import Faker
import pandas as pd
import random

fake = Faker()

def generate_patient_record():
    """Generates one synthetic patient record for FQHC clinics. 
       Returns a dict representing the patient."""
    
    age = random.randint(40, 85)
    pack_years = random.randint(0,60)
    quit_years = random.choice([None, random.randint(0,20)]) # None means current smoker
    
    # Comorbidities simulation
    comorbidities = random.sample(
        ["COPD", "Diabetes", "Hypertension", "None"],
        k=1
    )[0]
    
    # Generate unstructured clinical note
    if quit_years is None:
        smoking_note = f"Patient has {pack_years} pack-year smoking history and currently smokes."
    else:
        smoking_note = f"Patient has a {pack_years} pack-year smoking history and quit {quit_years} years ago."
        
    note = f"{smoking_note} Past medical history includes {comorbidities}."
    
    return {
        "name": fake.name(),
        "age": age,
        "pack_years": pack_years,
        "quit_years": quit_years,
        "comorbidities": comorbidities,
        "note": note
    }
    
def generate_dataset(n=100):
    data = [generate_patient_record() for _ in range(n)]
    df = pd.DataFrame(data)
    df.to_csv("../data/raw/synthetic_patients.csv", index=False)
    print(f"Generated {n} patient records -> ../data/raw/synthetic_patients.csv")
    
if __name__ == "__main__":
    generate_dataset(150)