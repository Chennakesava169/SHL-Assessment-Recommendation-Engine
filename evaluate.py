from sklearn.metrics import precision_score, recall_score, f1_score

# Example test data, replace with actual prediction and true values
# These should be your model's predicted values and true values.
y_true = [1, 0, 1, 1, 0, 1]  # Actual values
y_pred = [1, 0, 1, 0, 0, 1]  # Predicted values

# Calculate evaluation metrics
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

# Print the results
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")