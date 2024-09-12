from transformers import MarianMTModel, MarianTokenizer

def translate_en_to_fr(text):
    model_name = 'Helsinki-NLP/opus-mt-en-fr'
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    inputs = tokenizer(text, return_tensors="pt", padding=True)
    translated = model.generate(**inputs)
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)

    return translated_text
english_text = "Machine translation is an exciting field of natural language processing."
french_translation = translate_en_to_fr(english_text)
print(f"Original (English): {english_text}")
print(f"Translation (French): {french_translation}")
