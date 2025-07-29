import pandas as pd
import numpy as np
import random

random.seed(42)
np.random.seed(42)

def generate_student_data(num_records=1000):
    data = {
        "school": np.random.choice(["GP", "MS"], size=num_records),
        "sex": np.random.choice(["F", "M"], size=num_records),
        "age": np.random.randint(15, 22, size=num_records),
        "address": np.random.choice(["U", "R"], size=num_records),
        "famsize": np.random.choice(["LE3", "GT3"], size=num_records),
        "Pstatus": np.random.choice(["T", "A"], size=num_records),
        "Medu": np.random.randint(0, 5, size=num_records),
        "Fedu": np.random.randint(0, 5, size=num_records),
        "Mjob": np.random.choice(["teacher", "health", "services", "at_home", "other"], size=num_records),
        "Fjob": np.random.choice(["teacher", "health", "services", "at_home", "other"], size=num_records),
        "reason": np.random.choice(["home", "reputation", "course", "other"], size=num_records),
        "guardian": np.random.choice(["mother", "father", "other"], size=num_records),
        "studytime": np.random.randint(1, 5, size=num_records),
        "failures": np.random.randint(0, 4, size=num_records),
        "schoolsup": np.random.choice(["yes", "no"], size=num_records),
        "famsup": np.random.choice(["yes", "no"], size=num_records),
        "paid": np.random.choice(["yes", "no"], size=num_records),
        "activities": np.random.choice(["yes", "no"], size=num_records),
        "nursery": np.random.choice(["yes", "no"], size=num_records),
        "higher": np.random.choice(["yes", "no"], size=num_records),
        "internet": np.random.choice(["yes", "no"], size=num_records),
        "romantic": np.random.choice(["yes", "no"], size=num_records),
        "famrel": np.random.randint(1, 6, size=num_records),
        "freetime": np.random.randint(1, 6, size=num_records),
        "goout": np.random.randint(1, 6, size=num_records),
        "Dalc": np.random.randint(1, 6, size=num_records),
        "Walc": np.random.randint(1, 6, size=num_records),
        "health": np.random.randint(1, 6, size=num_records),
        "absences": np.random.randint(0, 31, size=num_records),
    }

    data["G1"] = np.random.randint(0, 21, size=num_records)
    data["G2"] = np.random.randint(0, 21, size=num_records)
    data["G3"] = np.clip(
        (0.3 * data["G1"] + 0.5 * data["G2"] + np.random.normal(0, 2, size=num_records)).astype(int),
        0, 20
    )

    df = pd.DataFrame(data)
    return df

df = generate_student_data(1000)
df.to_csv("student_mat.csv", index=False)
print("✅ Sample student dataset saved as 'student_mat.csv'")