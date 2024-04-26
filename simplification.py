from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

# Load the pre-trained T5 model and tokenizer
tokenizer = T5Tokenizer.from_pretrained('t5-base')
model = T5ForConditionalGeneration.from_pretrained('t5-base')

def simplify_text(preprocessed_text):
    # Tokenize the input text
    inputs = tokenizer.encode("simplify: " + preprocessed_text, return_tensors="pt", max_length=512, truncation=True)
    
    # Generate simplified text using the T5 model
    with torch.no_grad():
        outputs = model.generate(inputs, max_length=150, num_beams=4, early_stopping=True)
    
    # Decode the generated output
    simplified_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Convert simplified text into bullet points
    bullet_points = "\n".join(["- " + point for point in simplified_text.split(".")])
    
    return bullet_points
