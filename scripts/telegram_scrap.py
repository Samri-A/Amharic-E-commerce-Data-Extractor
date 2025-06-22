from dotenv import load_dotenv
import os
from telethon.sync import TelegramClient
import json
from telethon.sync import TelegramClient
import json
import pandas as pd
from transformers import AutoTokenizer , pipelines, AutoModelForMaskedLM
from etnltk import Amharic
from etnltk.common.preprocessing  import (
  remove_emojis,
  remove_digits,
  remove_english_chars
)
from etnltk.common.ethiopic import remove_ethiopic_punctuation
from etnltk.lang.am import clean_amharic
from etnltk.tokenize.am import word_tokenize

load_dotenv()

class scrap_process:
    def __init__(self):
        self.api_id = os.getenv("api_id")
        self.api_hash = os.getenv("api_hash")
        self.phone_num = os.getenv("phone_num")
        self.session_name = os.getenv("session_name")
        self.client = TelegramClient(self.session_name  , self.api_id ,self.api_hash)

    async def scraping_message(chat_name , limit):
        await self.client.start()
        chat_info = await self.client.get_entity(chat_name)
        messages = await self.client.get_messages(entity=chat_info ,limit= limit)
        return ({"message": messages , "Channel_info": chat_info })

    def to_df(scrpped_results):
         msg_result = [ msg.to_dict() for msg in scrpped_results["message"]]
         outputpath = "scrapped.json"
         with open ( outputpath , "w") as file:
           json.dump(msg_result, file, default=str, ensure_ascii=False)
         df = pd.read_json(outputpath)
         return df

    def preprocess(text):

        custom_pipeline = [
        remove_emojis,
        #remove_english_chars,
        remove_ethiopic_punctuation
        ]
        cleaned = clean_amharic(text, keep_abbrev=False, pipeline=custom_pipeline)
        #tokenized = word_tokenize(cleaned)
        return cleaned
    
    