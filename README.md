# Amharic E-commerce Data Extractor

## Overview
The **Amharic E-commerce Data Extractor** is a project designed to scrape and preprocess e-commerce data from Amharic Telegram channels. This tool aims to facilitate the extraction of relevant product information and make it available for further analysis and research.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features
- Scrapes e-commerce data from Amharic Telegram channels.
- Preprocesses the extracted data into a structured format.
- Supports output in CoNLL format for labeled data.
- Includes Jupyter Notebooks for easy experimentation and modification.

## Installation
To get started with the Amharic E-commerce Data Extractor, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Samri-A/Amharic-E-commerce-Data-Extractor.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd Amharic-E-commerce-Data-Extractor
   ```

3. **Install the required dependencies:**
   Make sure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To use the data extractor, you can run the provided scripts in the `scripts` folder. For example:
```bash
python scripts/extract_data.py
```
Make sure to modify any parameters as necessary to suit your specific needs.

## Project Structure
```
Amharic-E-commerce-Data-Extractor/
│
├── .github/
│   └── workflows/         # GitHub Actions workflows
├── .vscode/               # Visual Studio Code settings
├── notebooks/             # Jupyter Notebooks for experimentation
├── scripts/               # Python scripts for data extraction
├── src/                   # Source code for the extractor
├── tests/                 # Unit tests for the project
├── .gitignore             # Git ignore file
├── README.md              # Project documentation
├── product_data.CoNLL     # Labeled data in CoNLL format
└── requirements.txt       # Required Python packages
```

## Contributing
Contributions are welcome! If you would like to contribute to the project, please fork the repository and submit a pull request. Make sure to follow the coding standards and include tests for any new features.
