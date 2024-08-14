""""For  Downloading Datasets for training Language models."""
from datasets import load_dataset

# Load a dataset from Hugging Face
dataset = load_dataset('ag_news')

# Access the training set
train_dataset = dataset['train']

print(train_dataset[0])

for i in range(10):
    print(train_dataset[i])