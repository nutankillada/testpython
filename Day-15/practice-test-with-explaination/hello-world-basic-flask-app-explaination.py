## **Flask Code Explanation (For Absolute Beginners)**  
'''
This Python script creates a **simple web server** using **Flask**, a lightweight web framework. Let's break it down **word by word** and **line by line**, assuming you have **never used Flask before**.  
===================================================================================================
'''


## **🔹 Step 1: Import Flask**  
from flask import Flask
'''
- `from flask` → We are using the **Flask** library, which is a tool to build web applications in Python.
- `import Flask` → We are importing the `Flask` class from the `flask` module.
💡 **Think of `Flask` as a mini web server** that can handle requests and send responses.
'''


## **🔹 Step 2: Create a Flask Application**
app = Flask(__name__)
print(__name__)
'''
- `app = Flask(__name__)` → We are **creating an instance (object)** of the Flask class and assigning it to the variable `app`.  
- `Flask(__name__)` → This tells Flask that this script is the **main program**.  
- `__name__` → This is a **special Python variable** that holds the **name of the current module**.
💡 **Think of this as creating a basic app that Flask will run.**

🔸 Why is __name__ used?
- If you run this file directly, __name__ will be "__main__".
- If this file is imported as a module, __name__ will be the name of the module.
- Flask uses this to determine the root path of your application.

🔸 How does it work?
- print(__name__)           # If this file is run directly, prints "__main__"
- app = Flask(__name__)     # Creates the Flask app
✅ Flask now knows that this file is the main application and can use it to handle web requests.
'''


## **🔹 Step 3: Define a Route (URL Handling)**
'''
- `@app.route('/')` → This is a **decorator** that tells Flask:  
  🛣️ **"When someone visits the homepage (`/`), run the function below!"**
- `'/'` → This is the **root URL** (homepage of your website).  
  - Example: `http://localhost:5000/`
💡 **Think of this as setting up a signpost that says: "If someone visits `/`, show them something!"**
'''
@app.route('/')


## **🔹 Step 4: Create a Function That Runs When the URL Is Accessed**
def hello_world():
    return 'Hello, World!..yayy..'
'''
- `def hello_world():` → This is a **function** that runs when someone visits the `'/'` URL.
- `return 'Hello, World!..yayy..'` → This sends **text** (`'Hello, World!..yayy..'`) back to the user's web browser.
💡 **Think of this as writing the message you want to show on your webpage.**
'''

@app.route('/main')
def main_page():
    return 'Hello, This is the main page of your web page'

@app.route('/category1')
def category1():
    return 'Category-1'

@app.route('/category2')
def category2():
    return 'Category-2'


## **🔹 Step 5: Run the Flask Web Server**
#if __name__ == '__main__':
#    app.run("0.0.0.0")
app.run("0.0.0.0")
'''
1. **`if __name__ == '__main__':`**  
   - This ensures that the script runs **only if executed directly** (not when imported into another file).  
2. **`app.run("0.0.0.0")`**  
   - `app.run()` → This **starts** the Flask web server.
   - `"0.0.0.0"` → This allows the app to be accessible **from any device on your network**.
   - By default, Flask runs on **port 5000** (i.e., `http://localhost:5000`).
💡 **Think of this as pressing the "START" button to launch your website!**
'''


## **📌 What Happens When You Run This Code?**
'''
1. Flask **starts a web server**.
2. When you open `http://localhost:5000/` in your browser:
   - Flask sees that **you visited `/` (the homepage)**.
   - It runs `hello_world()`, which **returns** `'Hello, World!..yayy..'`.
   - The browser **displays** `'Hello, World!..yayy..'` as a webpage.
'''


## **🚀 Recap (Simplified)**
'''
| Code | What It Does |
|------|-------------|
| `from flask import Flask` | Imports Flask library |
| `app = Flask(__name__)` | Creates a Flask app |
| `@app.route('/')` | Handles the homepage URL (`/`) |
| `def hello_world(): return 'Hello, World!..yayy..'` | Displays a message |
| `if __name__ == '__main__': app.run("0.0.0.0")` | Runs the Flask web server |
'''