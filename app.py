from flask import Flask, render_template, request
import random
import string

# Create Flask app
app = Flask(__name__)

# Define password generator function
def generate_password(length, uppercase, lowercase, numbers, symbols):
    # Create a list of characters based on the user input
    characters = []
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation
    
    # Check if the list is not empty
    if characters:
        # Generate a random password with the given length and characters
        password = "".join(random.choices(characters, k=length))
        return password
    else:
        # Return an empty string if the list is empty
        return ""

# Define home route
@app.route("/")
def home():
    # Render the home page template
    return render_template("home.html")

# Define generate route
@app.route("/generate", methods=["POST"])
def generate():
    # Get the user input from the form
    length = int(request.form.get("length"))
    uppercase = request.form.get("uppercase") == "on"
    lowercase = request.form.get("lowercase") == "on"
    numbers = request.form.get("numbers") == "on"
    symbols = request.form.get("symbols") == "on"

    # Generate a password using the user input
    password = generate_password(length, uppercase, lowercase, numbers, symbols)

    # Render the generate page template with the password
    return render_template("generate.html", password=password)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)