# GenAi prompt engineering lab

def create_prompt(role, task, audience, constraints):
    
    prompt = f"""
    
    Role: {role}
    Task: {task}
    Target Audience: {audience}
    Instructions: {constraints}
    Generate a clear and useful response 
    """
    
    return prompt

# Example 1

prompt1 = create_prompt(
    role="Data Scientist",
    task="Analyze the sales data for the last quarter and provide insights.",
    audience="Company executives",
    constraints="Focus on key trends, anomalies, and actionable recommendations."
)

# Example 2

prompt2 = create_prompt(
    role="Software Engineer",
    task="Develop a new feature for the mobile application that allows users to track their fitness goals.",
    audience="users of the mobile application", 
    constraints="Ensure the feature is user-friendly, integrates with existing functionalities, and follows best practices for mobile app development."
)

print("Prompt 1:\n", prompt1)
print("\nPrompt 2:\n", prompt2)

# basic token - count appx 

def estimate_token_count(prompt):
    # This is a rough estimate; actual token count may vary based on the model's tokenizer
    return len(prompt.split())

print("Token count for Prompt 1:", estimate_token_count(prompt1))
print("Token count for Prompt 2:", estimate_token_count(prompt2))