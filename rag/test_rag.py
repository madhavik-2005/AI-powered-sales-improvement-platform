from vector_store import create_vector_store


vs = create_vector_store("knowledge_base.txt")

query = "How should a sales rep handle price objections?"
docs = vs.similarity_search(query, k=2)

for d in docs:
    print(d.page_content)
