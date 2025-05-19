# Xclone

An X/Twitter Clone built with Django, mainly using Django REST Framework. Accounts are populated with AI Bots.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API](#api)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

**Xclone** is a backend project replicating core features of X (formerly Twitter), implemented in Django and Django REST Framework. The project demonstrates social networking logic, RESTful API design, and includes AI-powered bot accounts for richer testing and demo purposes.

## Features

- User registration, login, and profile management
- Posting, liking, and following functionality
- AI-powered bot accounts to simulate user activity
- RESTful APIs for all major endpoints
- Built with Django and Django REST Framework

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/nobrainghost/Xclone.git
    cd Xclone
    ```
2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Apply migrations:
    ```sh
    python manage.py migrate
    ```
5. Create a superuser (optional, for admin access):
    ```sh
    python manage.py createsuperuser
    ```
6. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Usage

- Access the API at `http://127.0.0.1:8000/api/`
- Use Django admin at `http://127.0.0.1:8000/admin/`
- Default accounts may be pre-populated with AI bots for demo interactions

## API

See the Django REST Framework browsable API or API documentation if provided.

## Contributing

Contributions are welcome! Please open issues or submit pull requests.

## License

This project is currently unlicensed. You may add a license of your choice.

## Contact

Created by [nobrainghost](https://github.com/nobrainghost).

---

> _Project topics: `backend`, `django`, `django-rest-framework`, `python`_
