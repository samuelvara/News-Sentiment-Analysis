import utils
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import tensorflow as tf

PATH = 'cardiffnlp/twitter-roberta-base-sentiment-latest'

TOKENIZER = AutoTokenizer.from_pretrained(PATH)
MODEL = AutoModelForSequenceClassification.from_pretrained(PATH)

def classify(s):
    s = utils.process_sent(s)
    inputs = TOKENIZER(s, return_tensors="pt", max_length=50, truncation=True)

    with torch.no_grad():
        logits = MODEL(**inputs).logits

    predicted_class_id = logits.argmax().item()
    return MODEL.config.id2label[predicted_class_id], tf.nn.softmax(utils.normalize(logits[0].tolist())).numpy()

if __name__ == '__main__':
    pass
    # scores = utils.normalize(logits[0].tolist())
    # scores = tf.nn.softmax(scores).numpy()
    # print(scores)
    # utils.gradient_bar([['Good', scores]])





