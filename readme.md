# Django Project Template

## Description

+ Reformats <code>settings.py</code> as a python module with local environment variables.
+ Sets template, static, and media urls.
+ Includes home screen application.

## Requirements

- django
- django-environ

## Usage

- In a directory:
    - <code>py -m venv venv</code>
    - <code>.\venv\bin\activate</code>
    - <code>pip install django</code>
    - <code>django-admin startproject --template [template_url] [project_name] .</code>
    - <code>pip install -r requirements.txt</code>
    - create <code>.env</code> with:
        - <code>DEBUG=True</code>
        - <code>SECRET_KEY=some_string</code>
        - <code>DATABASE_URL=sqlite:///db.sqlite3</code>

## To do

- Migrate code to repo
- Update Views to use viewsets
- Implement django-rest-framework
