
# Translator

Welcome to the Translator repository! This project focuses on building and training a translation model using deep learning techniques. The model is designed to translate between English and Russian. This repository contains all the necessary code, data, and resources required to train, evaluate, and use the translation model.

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Training](#training)
- [Evaluation](#evaluation)
  
## Project Overview

This project aims to create a machine translation model capable of translating between English and Russian. The model is based on Transformer architecture, which is widely used for natural language processing tasks. The project includes data preprocessing scripts, model training code, and evaluation metrics.

## Installation

To get started with the project, you'll need to clone the repository and install the necessary dependencies. 

### Clone the Repository

```bash
git clone https://github.com/turman17/translator.git
cd translator
```

### Create a Virtual Environment

It's recommended to create a virtual environment to manage dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Note

Ensure that your environment supports the necessary libraries, such as TensorFlow and PyTorch, as they are required for model training and inference.

## Usage

This repository contains scripts and notebooks to preprocess data, train the model, and perform translations.

### Preprocessing Data

Use the `cleaner.py` script to clean and preprocess your data:

```bash
python cleaner.py
```

### Training the Model

The training process is managed by the `Transformer Trainer Notebook.ipynb`. You can open this notebook in your favorite environment (e.g., Jupyter Notebook, Google Colab) and run the cells to train the model.

### Translating Text

Once the model is trained, you can use the `transformer.py` script to translate text from English to Russian and vice versa:

```bash
python transformer.py --text "Your text here" --source-lang "en" --target-lang "ru"
```

## Data

The data used for training the translation model includes large datasets that have been preprocessed for this task. The main datasets are stored in the `Lang/` directory, including:

- `English.en`: English text data
- `Russian.ru`: Russian text data
- `output_eng.eng`: Preprocessed English data
- `output_ru.ru`: Preprocessed Russian data

### Note

Due to the large size of these files, they are not included in the repository. You will need to download or generate these datasets before running the training process.

## Training

The model is trained using the Transformer architecture, and the training process is handled within the `Transformer Trainer Notebook.ipynb`. This notebook guides you through the training steps, including data loading, model setup, training loop, and evaluation.

### Model Checkpoints

Model checkpoints are saved during training, allowing you to resume training or use the checkpoints for inference.

## Evaluation

Evaluation metrics such as BLEU score can be calculated using the evaluation scripts provided. The evaluation results help in understanding the model's performance and areas of improvement.
