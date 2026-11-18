
# Multi-Agent ML Project Review System
# Demonstrates specialised agents and orchestration

# Sample values for demonstration only.
# These are NOT measured results from the user's project.

sample_dataset = {
    "total_rows": 1000,
    "missing_values": 12,
    "duplicate_rows": 3
}

sample_model = {
    "accuracy": 0.80,
    "precision": 0.76,
    "recall": 0.68,
    "f1_score": 0.72
}


# AGENT 1: Data Quality Agent
def data_quality_agent(dataset):

    print("\n[Data Quality Agent] Analysing dataset...")

    missing = dataset["missing_values"]
    duplicates = dataset["duplicate_rows"]

    if missing > 0 or duplicates > 0:
        status = "needs_preprocessing"
    else:
        status = "clean"

    return {
        "missing_values": missing,
        "duplicate_rows": duplicates,
        "status": status
    }


# AGENT 2: Model Evaluation Agent
def model_evaluation_agent(metrics):

    print("\n[Model Evaluation Agent] Evaluating model...")

    accuracy = metrics["accuracy"]
    precision = metrics["precision"]
    recall = metrics["recall"]
    f1 = metrics["f1_score"]

    observations = []

    if recall < 0.75:
        observations.append(
            "Recall is relatively low. Investigate false negatives."
        )

    if f1 < 0.75:
        observations.append(
            "Consider improving the balance between precision and recall."
        )

    if accuracy >= 0.80:
        observations.append(
            "Accuracy is 80% or higher in this sample."
        )

    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1_score": f1,
        "observations": observations
    }


# AGENT 3: Recommendation Agent
def recommendation_agent(data_report, model_report):

    print("\n[Recommendation Agent] Preparing suggestions...")

    recommendations = []

    if data_report["status"] != "clean":
        recommendations.append(
            "Investigate missing values and duplicate records."
        )

    if model_report["recall"] < 0.75:
        recommendations.append(
            "Analyse false negatives and consider class balancing."
        )

    if model_report["f1_score"] < 0.75:
        recommendations.append(
            "Compare models using F1-score and other suitable metrics."
        )

    if not recommendations:
        recommendations.append(
            "Continue monitoring model performance."
        )

    return recommendations


# ORCHESTRATOR
def run_multi_agent_review():

    print("=" * 45)
    print("MULTI-AGENT ML REVIEW SYSTEM")
    print("=" * 45)

    # Step 1: Data agent
    data_report = data_quality_agent(sample_dataset)

    # Step 2: Evaluation agent
    model_report = model_evaluation_agent(sample_model)

    # Step 3: Recommendation agent
    recommendations = recommendation_agent(
        data_report,
        model_report
    )

    # Step 4: Combine agent outputs
    final_report = {
        "data_quality": data_report,
        "model_evaluation": model_report,
        "recommendations": recommendations
    }

    return final_report


# MAIN EXECUTION
if __name__ == "__main__":

    report = run_multi_agent_review()

    print("\nFINAL CONSOLIDATED REPORT")

    print("\nData Quality:")
    print(report["data_quality"])

    print("\nModel Evaluation:")
    print(report["model_evaluation"])

    print("\nRecommendations:")

    for recommendation in report["recommendations"]:
        print("-", recommendation)
