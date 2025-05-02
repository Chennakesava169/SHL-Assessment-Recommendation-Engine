import pandas as pd

class AssessmentRecommender:
    def __init__(self, catalog_path):
        """
        Initializes the AssessmentRecommender class with a CSV file.
        
        :param catalog_path: str - The path to the catalog CSV file.
        """
        self.catalog_path = catalog_path
        
        try:
            # Try reading the catalog CSV file
            self.catalog_data = pd.read_csv(catalog_path)
        except Exception as e:
            # If reading fails, print the error message and set catalog_data to None
            print(f"Error reading CSV file: {e}")
            self.catalog_data = None  # In case of error, make it None

    def recommend_assessments(self, skills, job_role):
        """
        Recommends assessments based on skills and job role.

        :param skills: List of skills the user has.
        :param job_role: The job role for which recommendations are to be made.
        
        :return: List of recommended assessments.
        """
        # Check if catalog_data is loaded correctly
        if self.catalog_data is None:
            return {"error": "Catalog data could not be loaded."}
        
        # Filter assessments based on job role
        relevant_assessments = self.catalog_data[self.catalog_data['job_role'] == job_role]
        
        if relevant_assessments.empty:
            return {"message": "No assessments found for this job role."}
        
        # Here, you could add logic to filter based on skills
        # For now, let's assume we return the first 3 relevant assessments
        recommended = relevant_assessments.head(3)['assessment_name'].tolist()

        return {"recommendations": recommended}