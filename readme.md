# ROLEX Flask Web Application

## Project Overview

ROLEX is a multi-page responsive web application developed using Flask (Python). The project represents a luxury watch brand website and demonstrates core full-stack web development concepts including routing, template rendering, form handling, and admin panel integration.

The application uses Flask for backend development and Bootstrap for frontend design.

---

## Features

### Web Pages

* Home page with hero section and image carousel
* About page with brand information
* Services page showcasing offerings
* Gallery page displaying product collection
* Contact page with form interface
* Login page with authentication system (demo)
* Registration page for user signup (demo)

---

### Authentication System

* User registration form handling
* User login with validation logic
* Redirect to home page after successful login
* Logout functionality (if implemented)
* Session-based flow (if enabled)

Note: Authentication is demo-based unless connected to a database.

---

### Admin Panel (Flask-Admin)

The project includes an admin panel built using Flask-Admin.

Features:

* Admin dashboard interface
* View and manage application data
* Basic CRUD operations (Create, Read, Update, Delete)
* Temporary data storage support (depending on configuration)

The admin panel is used for managing users and application-related data in a structured interface similar to Django admin.

---

## Technologies Used

### Backend

* Python 3
* Flask
* Flask-Admin

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* Bootstrap Icons

---

## Project Structure

```text
ROLEX-Flask-Project/
│
├── app.py
│
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── services.html
│   ├── gallery.html
│   ├── contact.html
│   ├── login.html
│   ├── register.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── images/
│       ├── 1.jpg
│       ├── 2.jpg
│       ├── 3.jpg
│
└── README.md
```

---

## Installation Instructions

### 1. Install Python

Ensure Python 3.x is installed.

```bash
python --version
```

---

### 2. Install Dependencies

```bash
pip install flask-admin
```

---

### 3. Run the Application

```bash
python app.py
```

---

### 4. Open in Browser

```
http://127.0.0.1:5000/
```

---

## Demo Login Credentials

Username:

```
admin
```

Password:

```
1234
```

---

## How the Project Works

* Flask handles routing using `@app.route`
* HTML templates are stored in the templates folder
* Static assets are stored in the static folder
* Forms use POST method for login and registration
* Flask-Admin provides an admin dashboard for data management
* Temporary storage is used unless a database is connected

---

## Limitations

* No full database integration (if not configured)
* Data may be temporary depending on setup
* Authentication is basic/demo-based
* Security features like hashing may not be implemented

---

## Future Improvements

* Integration with SQLite/MySQL database
* Secure authentication with password hashing
* Session-based login/logout system
* Enhanced admin dashboard customization
* Contact form backend storage
* Role-based access control (user/admin separation)

---

## Conclusion

This project demonstrates a complete Flask-based web application with frontend pages, authentication flow, and an admin panel using Flask-Admin. It serves as a practical implementation of full-stack web development concepts for learning purposes.

---

## License

This project is created for educational purposes only.


