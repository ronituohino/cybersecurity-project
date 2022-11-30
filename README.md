# cybersecurity-project

This is a project application for
[Cyber Security Base 2022](https://cybersecuritybase.mooc.fi/).

This application has security issues built into it, and a report which describes
the vulnerabilities and how fix them.

The idea behind the app "Instacare", is that users can contact a user named
"alice" to help with whatever problems they have in terms of healthcare.

Built using [Django](https://www.djangoproject.com/).

## Installation

Create a `secret_key.env` file in the root. Type in a secret key, which Django
uses for cryptographic signing.

## Commands

#### Start the server in development mode

```
python3 manage.py runserver
```
