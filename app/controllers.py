import torch
import pytorch_transformers
import numpy as np

from app import constants

class BertModelEmbendibg():
    tokenizer = None
    model = None
    token = None
    last_hidden_states = None

    def __init__(self):
        pretrained_weights = 'bert-base-uncased'
        tokenizer_class = pytorch_transformers.BertTokenizer
        self.tokenizer = tokenizer_class.from_pretrained(pretrained_weights)
        model_class = pytorch_transformers.BertModel
        self.model = model_class.from_pretrained(pretrained_weights)

    def set_text(self, text):
        self.token = self.tokenizer.encode(text, add_special_tokens=True)
        padded = np.array(self.get_padded())
        input_ids = torch.tensor([padded])  
        text_attention_mask = torch.tensor([np.where(padded != 0, 1, 0)])
        print(input_ids)
        print(text_attention_mask)
        self.last_hidden_states = self.model(input_ids, attention_mask=text_attention_mask)

    def get_token_lenght(self):
        return len(self.token)

    def get_padded(self):
        padded = self.token + [0]*(constants.TOKENS_MAX_LENGHT-self.get_token_lenght())
        return padded

    def get_last_hidden_layers(self):
        if (self.last_hidden_states != None):
            return 'Text is : {} '.format(self.last_hidden_states)
        else:
            return 'Text empty'

        