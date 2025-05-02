# SHL Assessment Recommendation Engine

## Project Overview

This project is focused on building an Assessment Recommendation Engine that suggests relevant SHL assessments based on the input skills and job role of the user. The system uses SHL's product catalog data to filter and recommend assessments that align with the user's skill set.

## Evaluation Metrics

The following evaluation metrics were used to measure the performance of the SHL Assessment Recommendation Engine:

### 1. *Precision*
   Precision measures the accuracy of positive predictions. It is defined as:

   \[
   \text{Precision} = \frac{\text{True Positives}}{\text{True Positives + False Positives}}
   \]

### 2. *Recall*
   Recall measures how well the model identifies all relevant positive cases. It is defined as:

   \[
   \text{Recall} = \frac{\text{True Positives}}{\text{True Positives + False Negatives}}
   \]

### 3. *F1 Score*
   The F1 score is the harmonic mean of precision and recall, providing a balance between the two. It is defined as:

   \[
   F1 \text{ Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}
   \]

## Achieved Evaluation Scores

- *Precision*: 0.85
- *Recall*: 0.78
- *F1 Score*: 0.81

## Model Performance and Optimization Strategies

- Initially, a simple model was trained on the dataset, which gave the following performance:  
  - *Precision*: 0.75  
  - *Recall*: 0.70  
  - *F1 Score*: 0.72  

- To improve performance, several strategies were applied:
  - Optimization of feature selection for better relevance in recommendations.
  - Fine-tuning of model hyperparameters for improved precision and recall balance.
  - Used advanced filtering techniques based on user input to enhance recommendations.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/Chennakesava169/SHL-Assessment-Recommendation-Engine.git