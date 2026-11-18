# Simple AI Agent Simulation
# Demonstrates planning, tool selection and action execution

# Tool 1: Calculator
def calculator(numbers):

    if not numbers:
        return "No numbers provided"

    average = sum(numbers) / len(numbers)

    return average


# Tool 2: Find highest score
def find_highest(numbers):

    if not numbers:
        return "No numbers provided"

    return max(numbers)


# Agent: Understands the task and selects a tool
def ai_agent(task, numbers):

    print("\nAgent received task:", task)

    task = task.lower()

    # Planning and tool selection
    if "average" in task:

        print("Agent decision: Use calculator tool")

        result = calculator(numbers)

        return f"Average marks: {result:.2f}"

    elif "highest" in task or "maximum" in task:

        print("Agent decision: Use highest-score tool")

        result = find_highest(numbers)

        return f"Highest marks: {result}"

    else:

        return "Agent cannot handle this task."


# Sample student data
student_marks = [78, 85, 92, 67, 88]

# Execute agent
task = "Find the average marks"

response = ai_agent(task, student_marks)

print("\nFinal Agent Response:")
print(response)
