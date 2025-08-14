from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME", "ibm-granite/granite-3.3-2b-instruct")
HF_API_KEY = os.getenv("HF_API_KEY")
MAX_TOKENS = int(os.getenv("MAX_TOKENS", 100))

# Load tokenizer and model with Hugging Face API key
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, token=HF_API_KEY)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, token=HF_API_KEY)
model.eval()

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

def generate_prescription(prompt: str, max_new_tokens=MAX_TOKENS) -> str:
    messages = [{"role": "user", "content": prompt}]
    
    inputs = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        tokenize=True,
        return_dict=True,
        return_tensors="pt",
    ).to(device)

    outputs = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        temperature=0.7,
    )

    generated = tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:])
    return generated.strip()
