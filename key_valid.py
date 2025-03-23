import openai

openai.api_key = "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"

try:
    models = openai.models.list()
    model_names = [model.id for model in models.data]  # Fix: Use .data instead of ["data"]
    print("Available models:", model_names)

    if "gpt-4" in model_names:
        print("✅ Your API key has access to GPT-4.")
    else:
        print("❌ GPT-4 is not available for your API key.")
except openai.OpenAIError as e:  # Fix: Use openai.OpenAIError instead of openai.error.AuthenticationError
    print(f"❌ OpenAI API error: {e}")
except Exception as e:
    print(f"⚠️ Unexpected error: {e}")
