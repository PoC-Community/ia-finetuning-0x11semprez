from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load tokenizer and model
model_name = 'gpt2'

tokenizer = AutoTokenizer.from_pretrained("openai-community/gpt2")
model = AutoModelForCausalLM.from_pretrained("openai-community/gpt2", dtype=torch.float16, device_map="auto", attn_implementation="sdpa")

# Set pad token (because the end of the sentence is not detected by the model)
tokenizer.pad_token =

print(f"✅ Model '{model_name}' loaded successfully!")
print(f"Model has {model.num_parameters():,} parameters")

