from transformers import AutoModelForSequenceClassification, AutoTokenizer

MODEL_NAME = "cambridgeltl/sst_mobilebert-uncased"
# Download and save the pre-trained model
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
model.save_pretrained("./lambda/model")
# Download and save the tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
tokenizer.save_pretrained("./lambda/model")
print("Model and tokenizer downloaded successfully!")