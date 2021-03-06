# -*- coding: utf-8 -*-
"""Chatbot_Tinder.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TYSRLQn1T3I82stJgZ-TVth5FmEYN4TR
"""

#!pip install transformers
#!pip3 install git+https://github.com/ptrstn/deepl-translate

import deepl
from deepl import *

def translate_ger_eng(input):
  output = deepl.translate(source_language="german", target_language="english", text=input, formality_tone="informal") #formal, informal möglich
  return output

def translate_eng_ger(input):
  output = deepl.translate(source_language="english", target_language="german", text=input, formality_tone="informal") #formal, informal möglich
  return output

#print(translate_ger_eng("Handtücher sind cool."))
#print(translate_eng_ger("towels are cool."))

#import all necessary models

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "microsoft/DialoGPT-large"
#model_name = "microsoft/DialoGPT-medium"
#model_name = "microsoft/DialoGPT-small"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def getResponse(text, chat_history_ids = []):
	text = translate_ger_eng(text)
	input_ids = tokenizer.encode(text + tokenizer.eos_token, return_tensors="pt")
	bot_input_ids = torch.cat([chat_history_ids, input_ids], dim=-1) if len(chat_history_ids) > 0 else input_ids
	chat_history_ids_list = model.generate(
        bot_input_ids,
        max_length=1000,
        do_sample=True,
        top_p=0.95,
        top_k=50,
        temperature=0.75,
        num_return_sequences=1,
        pad_token_id=tokenizer.eos_token_id
    )
	output = tokenizer.decode(chat_history_ids_list[0][bot_input_ids.shape[-1]:], skip_special_tokens=True)
	output = translate_eng_ger(output)
	return output

from api import BumbleAPI
import time
import random
session = ""

api = BumbleAPI(session)

for user in api.getConversationQueue():
    # get last message from Chat
    try:
        messages = api.getChat(user.id).messages
    except:
        continue
    if messages[-1].fromID == user.id and len(messages) > 0:
        # last message was not from chatbot
        response = getResponse(messages[-1].text)
        print(user.name + " - " + str(messages[-1].text) + " - " + str(response))
        api.sendMessage(user.id, response)
        time.sleep(random.uniform(10,20))