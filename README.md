# Blogging Website

This is a simple blogging website built using the Django framework. The website allows users to register, log in, create, edit, and delete blog posts, and view posts created by other users.

## Features

- **User Authentication**: Users can register, log in, and log out.
- **Profile Verification**: User profiles must be verified to post blogs.
- **CRUD Operations**: Users can create, read, update, and delete blog posts.
- **Responsive Design**: The website is responsive and works on various devices.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/niharikakuchhal/Blogging.git
   cd Blogging

2. Create and activate a virtual environment:
   ```bash
   python -m venv myenv
   myenv\Scripts\activate

3. Apply migrations:
   ```bash
   python manage.py migrate

4. Create a superuser:
   ```bash
   python manage.py createsuperuser

5. Run the development server:
   ```bash
   python manage.py runserver

6. Access the website:
Open your browser and go to http://127.0.0.1:8000/.

## Usage
- **Register**: Create a new account.
- **Log In**: Access your account.
- **Create Post**: Add new blog posts.
- **Edit Post**: Update your existing posts.
- **Delete Post**: Remove unwanted posts.
- **View Posts**: Browse posts from all users.


