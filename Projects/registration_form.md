Sure, let's implement each file step by step.

1. **`app/models.py`**: Define the database models using SQLAlchemy.

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.Enum('male', 'female', 'other'))
    country = db.Column(db.String(100))

    def __repr__(self):
        return f'<User {self.first_name} {self.last_name}>'
```

2. **`app/service.py`**: Implement the service layer logic for processing user registration data.

```python
from app.models import db, User

def register_user(first_name, last_name, email, password, age, gender, country):
    new_user = User(first_name=first_name, last_name=last_name, email=email, password=password,
                    age=age, gender=gender, country=country)
    db.session.add(new_user)
    db.session.commit()
```

3. **`app/views.py`**: Define the API endpoints using Flask's Blueprint.

```python
from flask import Blueprint, render_template, request, redirect, url_for
from app.service import register_user

bp = Blueprint('app', __name__)

@bp.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        age = request.form['age']
        gender = request.form['gender']
        country = request.form['country']
        # Basic validation (you can add more validation logic here)
        if not (first_name and last_name and email and password):
            return render_template('register.html', error='All fields are required.')
        # Call service layer to register user
        register_user(first_name, last_name, email, password, age, gender, country)
        return redirect(url_for('app.register'))  # Redirect to registration page after successful registration

    return render_template('register.html', error=None)
```

4. **`app/__init__.py`**: Initialize the Flask application and configure SQLAlchemy.

```python
from flask import Flask
from app.models import db
from app.views import bp as app_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Change to your MySQL database URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.register_blueprint(app_bp)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app
```

5. **`app.py`**: Entry point for the Flask application.

```python
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
```

6. **`templates/register.html`**: HTML template for the registration form.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registration Form</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <div class="container">
        <h1>Registration Form</h1>
        {% if error %}
        <p class="error">{{ error }}</p>
        {% endif %}
        <form method="post">
            <label for="first_name">First Name:</label><br>
            <input type="text" id="first_name" name="first_name"><br>
            
            <label for="last_name">Last Name:</label><br>
            <input type="text" id="last_name" name="last_name"><br>
            
            <label for="email">Email:</label><br>
            <input type="email" id="email" name="email"><br>
            
            <label for="password">Password:</label><br>
            <input type="password" id="password" name="password"><br>
            
            <label for="age">Age:</label><br>
            <input type="number" id="age" name="age" min="18"><br>
            
            <label for="gender">Gender:</label><br>
            <select id="gender" name="gender">
                <option value="male">Male</option>
                <option value="female">Female</option>
                <option value="other">Other</option>
            </select><br>
            
            <label for="country">Country:</label><br>
            <input type="text" id="country" name="country"><br>
            
            <input type="submit" value="Submit">
        </form>
    </div>
</body>
</html>
```

7. **`config.ini`**: MySQL configuration file.

```ini
[mysql]
host = 127.0.0.1
port = 3306
database = your_database_name
user = your_mysql_username
password = your_mysql_password
```

Ensure that you replace placeholders like `your_database_name`, `your_mysql_username`, and `your_mysql_password` with your actual MySQL database credentials.

With this implementation, the registration form (`templates/register.html`) will submit the data to the `register` endpoint (`app/views.py`). The view function will then call the `register_user` function in the service layer (`app/service.py`), which will insert the user data into the database using the models defined in `app/models.py`.
