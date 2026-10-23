# Task 1: Structured LLM Prompt Pipeline & JSON Extractor

## Overview

This project extracts structured information from invoice text using Google's Gemini AI model. The extracted information is validated using Pydantic and returned in JSON format.

## Features

* Uses Google Gemini API for information extraction.
* Uses a parameterized prompt template.
* Extracts invoice details into structured JSON.
* Validates extracted data using Pydantic.
* Uses `null` for missing information.
* Rejects negative invoice amounts.
* Rejects empty invoice input.

## Extracted Fields

* Invoice Number
* Customer Name
* Invoice Date
* Total Amount
* Currency
* Payment Status

## Requirements

* Python
* Google Gemini API key

## Installation

1. Create and activate a Python virtual environment.

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project directory and add your Gemini API key:

   ```text
   GEMINI_API_KEY=your_api_key_here
   ```

   Replace `your_api_key_here` with your own API key. Do not upload the `.env` file to GitHub.

## Run the Project

```bash
python main.py
```

## Run Validation Tests

```bash
python test_validation.py
python test_empty.py
```

## Technologies Used

* Python
* Google Gemini API
* Pydantic
* python-dotenv
