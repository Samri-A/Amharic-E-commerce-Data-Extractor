from transformers import Trainer , AutoTokenizer , TrainingArguments , DataCollatorForTokenClassification , DataCollatorWithPadding , AutoModelForTokenClassification
import pandas as pd
from datasets import Dataset 
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.preprocessing import LabelEncoder
import evaluate
import random

class FinetuneNER:
    def __init__(self, model_name, label_list, test_size=0.1):
        self.model_name = model_name
        self.label_list = label_list
        self.num_labels = len(label_list)
        self.label_to_id = {label: i for i, label in enumerate(label_list)}
        self.id_to_label = {i: label for i, label in enumerate(label_list)}
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
        self.metric = evaluate.load("seqeval")
        self.data_collator = DataCollatorForTokenClassification(tokenizer=self.tokenizer)

    def tokenize_and_align_labels(self, examples):
        tokenized_inputs = self.tokenizer(
            examples["tokens"],
            truncation=True,
            padding="max_length",
            max_length=128,
            is_split_into_words=True,
        )
        labels = []
        for i, label in enumerate(examples["ner_tags"]):
            word_ids = tokenized_inputs.word_ids(batch_index=i)
            previous_word_idx = None
            label_ids = []
            for word_idx in word_ids:
                if word_idx is None:
                    label_ids.append(-100)
                elif word_idx != previous_word_idx:
                    label_ids.append(label[word_idx])
                else:
                    label_ids.append(-100)
                previous_word_idx = word_idx
            labels.append(label_ids)
        tokenized_inputs["labels"] = labels
        return tokenized_inputs 
    def compute_metrics(self, eval_pred):
        logits, labels = eval_pred
        predictions = np.argmax(logits, axis=2)
        true_predictions = [
            [self.id_to_label[p] for (p, l) in zip(pred, label) if l != -100]
            for pred, label in zip(predictions, labels)
        ]
        true_labels = [
            [self.id_to_label[l] for (p, l) in zip(pred, label) if l != -100]
            for pred, label in zip(predictions, labels)
        ]
        return self.metric.compute(predictions=true_predictions, references=true_labels)


    def train(self, train_dataset, test_dataset, epochs=3, batch_size=8):
        model = AutoModelForTokenClassification.from_pretrained(
            self.model_name,
            num_labels=self.num_labels,
            id2label=self.id_to_label,
            label2id=self.label_to_id
        )

        training_args = TrainingArguments(
            output_dir="./models",
            per_device_train_batch_size=batch_size,
            per_device_eval_batch_size=batch_size,
            report_to="none",
            num_train_epochs=epochs,
            learning_rate=1e-5,
            weight_decay=0.01,
            save_strategy="epoch",
            logging_strategy="epoch",
           
        )

        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=test_dataset,
            tokenizer=self.tokenizer,
            data_collator=self.data_collator,
            compute_metrics=self.compute_metrics,
        )

        trainer.train()
        return trainer
