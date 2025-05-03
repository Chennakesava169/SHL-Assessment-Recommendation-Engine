# recommendation_engine.py

def recommend_assessment(user_input):
    # Simple rule-based recommendation logic
    if "data" in user_input.lower():
        return ["Data Science Assessment"]
    elif "code" in user_input.lower():
        return ["Coding Skills Assessment"]
    else:
        return ["General Cognitive Assessment"]