import litellm

response = litellm.completion(
    model="llama3",
    messages=[{"role": "user", "content": "Hello"}],
    api_base="http://localhost:11434/v1",  # Ollama default API URL
    custom_llm_provider="ollama"  # Specify Ollama as the provider
)

print(response)
