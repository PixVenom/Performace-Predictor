import pandas as pd
import numpy as np
import random

# Set seed for reproducibility
random.seed(99)
np.random.seed(99)

def generate_student_data_v2(num_records=1000):
    data = {
        "school": np.random.choice(["AB", "CD"], size=num_records),
        "gender": np.random.choice(["Male", "Female", "Other"], size=num_records),
        "age": np.random.randint(14, 21, size=num_records),
        "residence": np.random.choice(["Urban", "Suburban", "Rural"], size=num_records),
        "parental_education": np.random.choice(["None", "Primary", "Secondary", "Higher", "PhD"], size=num_records),
        "family_income": np.random.randint(2000, 20000, size=num_records),
        "studytime": np.random.randint(1, 5, size=num_records),
        "failures": np.random.randint(0, 4, size=num_records),
        "internet_access": np.random.choice(["yes", "no"], size=num_records),
        "part_time_job": np.random.choice(["yes", "no"], size=num_records),
        "extracurriculars": np.random.choice(["yes", "no"], size=num_records),
        "mobile_addiction": np.random.choice(["low", "moderate", "high"], size=num_records),
        "screen_time": np.random.uniform(1, 12, size=num_records).round(1),
        "sleep_hours": np.random.uniform(4, 10, size=num_records).round(1),
        "mental_health_score": np.random.randint(1, 11, size=num_records),  # 1 to 10 scale
        "attendance_rate": np.random.uniform(60, 100, size=num_records).round(2),
        "parental_support": np.random.choice(["yes", "no"], size=num_records),
        "travel_time": np.random.randint(1, 5, size=num_records),
        "peer_influence": np.random.choice(["low", "medium", "high"], size=num_records),
    }

    # Generate grades
    data["G1"] = np.random.randint(0, 21, size=num_records)
    data["G2"] = np.random.randint(0, 21, size=num_records)

    # G3 is weighted more toward G1 now
    data["G3"] = np.clip(
        (0.6 * data["G1"] + 0.3 * data["G2"] + np.random.normal(0, 2, size=num_records)).astype(int),
        0, 20
    )

    df = pd.DataFrame(data)
    return df

# Generate and save
df_v2 = generate_student_data_v2(1000)
df_v2.to_csv("student_mat_v2.csv", index=False)
print("✅ New student dataset saved as 'student_mat_v2.csv'")