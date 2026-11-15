# Mini RAG Retrieval Demo
# Retrieval baseline using IF-IDF and cosine similarity

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. sample knowledge base
documents = [
    {
        "id": "DOC1",
        "text": "To reset a forgotten password, use password reset link on login page"
    },
    {
        "id": "DOC2",
        "text": "Employees receive 18 paid leaves every year"
    },
    {
        "id": "DOC3",
        "text": "Submit expense reimbursement receipts within 30 days of purchase"
    },
    {
        "id": "DOC4",
        "text": "Remote work requests must be approved by reporting manager"
    },
    {
        "id": "DOC5",
        "text": "Never share otp passwords or account credentials with anyone"
    }
]

# 2. convert documents to TF-IDF vectors

texts = [doc["text"] for doc in documents]

vectorizer = TfidfVectorizer(stop_words='english')
document_vectors = vectorizer.fit_transform(texts)

# 3. retrieve relevant documents

def retrieve_documents(query, top_k=2):
    
    # Convert query to TF-IDF vector
    query_vector = vectorizer.transform([query])
    
    # Compute cosine similarity between query and document vectors
    similarities = cosine_similarity(query_vector, document_vectors).flatten()

    ranked_indices = similarities.argsort()[::-1]

    results = []

    for index in ranked_indices[:top_k]:
        if similarities[index] > 0:
            results.append({
                "id": documents[index]["id"],
                "text": documents[index]["text"],
                "similarity": similarities[index]
            })

        if len(results) == top_k:
            break

    return results

# 4. Prepare a prompt for an LLM
def build_rag_prompt(query, retrieved_docs):

    context = "\n".join(
        doc["text"] for doc in retrieved_docs
    )

    prompt = f"""
Answer the question using only the context below.

If the answer is not available in the context,
say that you do not have enough information.

Context:
{context}

Question:
{query}

Answer:
"""

    return prompt


# 5. Test the RAG retrieval process
user_query = "I forgot my password. How can I log in again?"

retrieved = retrieve_documents(user_query, top_k=2)

print("USER QUESTION:")
print(user_query)

print("\nRETRIEVED DOCUMENTS:")

for doc in retrieved:
    print(f"\nDocument: {doc['id']}")
    print(f"Similarity: {doc['similarity']:.3f}")
    print(doc["text"])

# 6. Generate the final LLM input prompt
final_prompt = build_rag_prompt(user_query, retrieved)

print("\nPROMPT TO SEND TO AN LLM:")
print(final_prompt)
