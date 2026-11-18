# Structured Tool Calling Agent
# Simulates the architecture used by LLM tool-calling applications.

# Sample student database
students = {
    "asha": [78, 85, 92],
    "rahul": [65, 72, 80],
    "neha": [90, 95, 88]
}


# TOOL 1: Calculate average
def calculate_average(numbers):

    if not numbers:
        raise ValueError("Numbers cannot be empty.")

    if not all(isinstance(n, (int, float)) for n in numbers):
        raise ValueError("All values must be numeric.")

    return sum(numbers) / len(numbers)


# TOOL 2: Find highest score
def find_highest(numbers):

    if not numbers:
        raise ValueError("Numbers cannot be empty.")

    return max(numbers)


# TOOL 3: Retrieve student marks
def get_student_marks(student_name):

    name = student_name.lower()

    if name not in students:
        raise ValueError("Student not found.")

    return students[name]


# TOOL REGISTRY
# Only registered tools can be executed.
tools = {
    "calculate_average": calculate_average,
    "find_highest": find_highest,
    "get_student_marks": get_student_marks
}


# SIMULATED LLM PLANNER
# A real LLM would produce this structured tool call.
def mock_llm_planner(user_request):

    request = user_request.lower()

    if "average" in request:

        return {
            "tool_name": "calculate_average",
            "arguments": {
                "numbers": [78, 85, 92]
            }
        }

    elif "highest" in request:

        return {
            "tool_name": "find_highest",
            "arguments": {
                "numbers": [78, 85, 92]
            }
        }

    elif "asha" in request and "marks" in request:

        return {
            "tool_name": "get_student_marks",
            "arguments": {
                "student_name": "asha"
            }
        }

    return None


# TOOL EXECUTOR
def execute_tool(tool_call):

    if not isinstance(tool_call, dict):
        raise ValueError("Invalid tool call.")

    tool_name = tool_call.get("tool_name")
    arguments = tool_call.get("arguments")

    if tool_name not in tools:
        raise ValueError("Tool is not permitted.")

    if not isinstance(arguments, dict):
        raise ValueError("Tool arguments must be a dictionary.")

    selected_tool = tools[tool_name]

    return selected_tool(**arguments)


# AGENT
def run_agent(user_request):

    print("\nUser:", user_request)

    try:
        # 1. Ask the planner to select a tool
        tool_call = mock_llm_planner(user_request)

        if tool_call is None:
            return "I cannot handle this request."

        print("\nStructured tool call:")
        print(tool_call)

        # 2. Execute the selected tool
        result = execute_tool(tool_call)

        # 3. Observe the result
        print("\nTool result:")
        print(result)

        # 4. Return the response
        return f"Task completed successfully. Result: {result}"

    except (ValueError, TypeError) as error:
        return f"Task failed: {error}"


# TEST THE AGENT
if __name__ == "__main__":

    response = run_agent("Calculate the average marks")

    print("\nFinal response:")
    print(response)
