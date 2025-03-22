from transformers import pipeline

# Load a Hugging Face model for text generation
generator = pipeline('text-generation', model='gpt2')

def generate_excuse(prompt="I can't attend because"):
    # Generate a funny excuse
    response = generator(prompt, max_length=50, num_return_sequences=1)
    return response[0]['generated_text']
