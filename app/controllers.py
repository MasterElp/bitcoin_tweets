import torch
import pytorch_transformers

from app import constants

class BertModelClassificate():
    def __init__(self, text):
        self.pretrained_weights = 'bert-base-uncased'
        tokenizer_class = pytorch_transformers.BertTokenizer
        tokenizer = tokenizer_class.from_pretrained(self.pretrained_weights)
        self.token = tokenizer.encode(text, add_special_tokens=True)

    def init_model(self):
        model_class = pytorch_transformers.BertModel
        model = model_class.from_pretrained(self.pretrained_weights)

    def get_token_lenght(self):
        return len(self.token)


    def get_token(self):
        padded = self.token + [0]*(constants.TOKENS_MAX_LENGHT-self.get_token_lenght())
        return 'Text is : {} '.format(padded)

        