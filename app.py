from flask import Flask, render_template, request, redirect, url_for
import os
from datetime import datetime

print("Starting app.py")  # Debugging statement

app = Flask(__name__)

@app.route('/', methods=['GET'])
def form():
    print("Rendering form.html")  # Debugging statement
    return render_template('form.html')

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        print("Processing form submission")  # Debugging statement

        # Retrieve form data
        name = request.form.get('name')
        age = request.form.get('age')
        sex = request.form.get('sex')
        hobby = request.form.get('hobby')

        # Combine the data into a formatted string
        data = f"Name: {name}\nAge: {age}\nSex: {sex}\nHobby: {hobby}\n"

        # Generate a unique filename using timestamp and microseconds
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        submissions_dir = 'submissions'
        if not os.path.exists(submissions_dir):
            os.makedirs(submissions_dir)
            print(f"Created directory: {submissions_dir}")  # Debugging statement
        filename = os.path.join(submissions_dir, f"submission_{timestamp}.txt")

        # Write the data to a text file
        try:
            with open(filename, 'w') as file:
                file.write(data)
            print(f"Data saved to {filename}")  # Debugging statement
        except IOError as e:
            print(f"An error occurred: {e}")  # Debugging statement
            return "An error occurred while saving your data."

        # Render the result page
        return render_template('result.html', name=name, age=age, sex=sex, hobby=hobby)
    else:
        print("Received GET request on /submit_form, redirecting to form")  # Debugging statement
        return redirect(url_for('form'))

if __name__ == '__main__':
    print("Running Flask app")  # Debugging statement
    app.run(debug=True)
