from datasets import load_dataset
import pandas as pd
import os


dataset = load_dataset("FiscalNote/billsum")


os.makedirs("billsum_dataset", exist_ok=True)


dataset["train"].to_pandas().to_csv("billsum_dataset/train.csv", index=False)
dataset["test"].to_pandas().to_csv("billsum_dataset/test.csv", index=False)
dataset["ca_test"].to_pandas().to_csv("billsum_dataset/ca_test.csv", index=False)
