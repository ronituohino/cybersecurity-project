# cybersecurity-project

This is a project application for
[Cyber Security Base 2022](https://cybersecuritybase.mooc.fi/).

This application has security issues built into it, and a report which details
how to exploit and fix them.

Built using [Django](https://www.djangoproject.com/).

## Installation

Create a `secret_key.env` file in the root. Type in a secret key, which Django
uses for cryptographic signing.

## Commands

#### Start the server in development/production mode

```
python3 manage.py runserver
```

To change between development and production, switch the `DEBUG` boolean in
`cybersecurity/settings.py`
