import pandas as pd

# Load the dataset
file_path = "training_solutions_rev1.csv"
df = pd.read_csv(file_path)

# Define classification function
def classify_galaxy(row):
    elliptical_prob = row['Class1.1'] + row['Class1.2'] + row['Class1.3']
    spiral_prob = row['Class2.1'] + row['Class3.1'] + row['Class3.2'] + row['Class4.1'] + row['Class4.2']
    irregular_prob = row['Class2.2'] + row['Class5.3'] + row['Class5.4'] + row['Class5.1'] + row['Class5.2']
    
    if max(elliptical_prob, spiral_prob, irregular_prob) == elliptical_prob:
        return "Elliptical"
    elif max(elliptical_prob, spiral_prob, irregular_prob) == spiral_prob:
        return "Spiral"
    else:
        return "Irregular"

# Apply classification
df['Morphology'] = df.apply(classify_galaxy, axis=1)

# Save the results
df[['GalaxyID', 'Morphology']].to_csv("galaxy_classification.csv", index=False)

print("Classification completed. File saved as 'galaxy_classification.csv'.")
