# Sign Language Recognition App

A Django web application that uses deep learning to recognize American Sign Language (ASL) letters from images.

## Features

- Upload images of hand signs for ASL letters
- AI-powered recognition of 24 ASL letters (A-Y, excluding J and Z which require motion)
- Modern, responsive UI built with Bootstrap 5
- Confidence score for predictions
- Ability to try multiple images

## Prerequisites

- Python 3.9+
- pip (Python package manager)
- Virtual environment tool (recommended)

## Installation

Follow these steps to run the application locally:

### 1. Clone the Repository

```bash
git clone git@github.com:FREDERICO23/sign-langauge-detection.git
cd sign-language-detection
```

### 2. Create and Activate Virtual Environment

```bash
# Using venv (built-in to Python)
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

Or use Pipenv:

```bash
pip install pipenv
pipenv shell
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

or with Pipenv:

```bash
pipenv install
```

### 5. Configure Environment Variables

Create a `.env` file in the project root directory:

```bash
# .env
DEBUG=True
DATABASE_URL=postgresql://username:password@localhost:5432/sign_language
```

### 6. Create Database Tables

```bash
python manage.py migrate
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Using the Application

1. Open the application in your web browser
2. Click on the upload area or drag and drop an image of a hand sign
3. Click "Recognize Sign" to process the image
![img](https://i.imgur.com/WX3PZ3l.png)
4. View the prediction result and confidence score
![img](https://i.imgur.com/7o0GeAB.png)

