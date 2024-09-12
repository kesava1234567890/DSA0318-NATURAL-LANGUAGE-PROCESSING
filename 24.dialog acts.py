from transformers import pipeline
dialog_act_classifier = pipeline("text-classification", model="mrm8488/t5-base-finetuned-samsum-dialog-summary")

def classify_dialog_acts(dialog):
    dialog_acts = []
    
    
    utterances = dialog.split("\n")  
    
    for utterance in utterances:
        if utterance.strip():
            result = dialog_act_classifier(utterance.strip())
            dialog_acts.append({"utterance": utterance, "dialog_act": result[0]['label']})
    
    return dialog_acts
dialog = """
Person A: Hello, how are you?
Person B: I'm good, thanks! How about you?
Person A: I'm doing well. Did you complete the report?
Person B: Not yet, but I will finish it by tomorrow.
Person A: Great! Let me know if you need any help.
"""

dialog_acts = classify_dialog_acts(dialog)
for act in dialog_acts:
    print(f"Utterance: {act['utterance']} \nDialog Act: {act['dialog_act']}\n")
