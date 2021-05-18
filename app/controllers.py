import torch
import pytorch_transformers
import numpy as np

import tensorflow
from keras import models
from keras.models import model_from_json

import os

from app import constants

class GrowPredict():
    tokenizer = None
    model = None
    token = None
    last_hidden_states = None

    def __init__(self):
        pretrained_weights = 'bert-base-uncased'
        tokenizer_class = pytorch_transformers.BertTokenizer
        self.tokenizer = tokenizer_class.from_pretrained(pretrained_weights)

        model_class = pytorch_transformers.BertModel
        self.bert_model = model_class.from_pretrained(pretrained_weights)

        #print(os.getcwd())
        with open(os.getcwd() + f'/data/model_pr4_{constants.MODEL_NUMBER}.json', 'r') as file:
            model_json = file.read()
        self.my_model = model_from_json(model_json)
        self.my_model.load_weights(os.getcwd() + f'/data/weights_pr4_{constants.MODEL_NUMBER}.h5')

    def set_text(self, text):
        self.token = self.tokenizer.encode(text, add_special_tokens=True)
        padded = np.array(self.get_padded())

        input_ids = torch.tensor([padded])  
        text_attention_mask = torch.tensor([np.where(padded != 0, 1, 0)])

        last_hidden_states = self.bert_model(input_ids, attention_mask=text_attention_mask)
        #print(last_hidden_states[0][:,0,:].numpy())
        with torch.no_grad():
            features = last_hidden_states[0][:,0,:].detach().numpy()
            self.prediction = self.my_model.predict(features)

    def get_token_lenght(self):
        return len(self.token)

    def get_padded(self):
        padded = self.token + [0]*(constants.TOKENS_MAX_LENGHT-self.get_token_lenght())
        return padded

    def get_prediction(self):
        if (self.prediction != None):
            return self.prediction[0][0]
        else:
            return 'Empty'

        