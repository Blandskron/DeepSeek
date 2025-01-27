from transformers import AutoModelForCausalLM, AutoTokenizer

# Especifica el nombre del modelo en Hugging Face
model_name = "deepseek-ai/DeepSeek-R1"

# Cargar el modelo y el tokenizador
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Codificar la entrada
input_text = input("Ingrese el texto de entrada: ")
input_ids = tokenizer.encode(input_text, return_tensors="pt")

# Generar texto
output = model.generate(input_ids, max_length=50, num_return_sequences=1)

# Decodificar la salida
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)