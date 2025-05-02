# Import the AssessmentRecommender class
from assessment_recommender import AssessmentRecommender

# Create an instance of AssessmentRecommender with your catalog CSV path
recommender = AssessmentRecommender("catalog.csv")  # Update this path

# Test the recommendation method
skills = ["Python", "Data Analysis", "Machine Learning"]  # Example skills
job_role = "Data Scientist"  # Example job role

# Get the recommendations
recommendations = recommender.recommend_assessments(skills, job_role)

# Print the recommendations
print(recommendations)