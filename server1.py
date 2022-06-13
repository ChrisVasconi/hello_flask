from flask import Flask  # Import Flask to allow us to create our app
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


# import statements=, maybe some other routes
@app.route('/success')
def success():
    return "success"

# app.run(debug=True) should be the very last statement!


# for a route '/hello/____' anything after '/hello/', get passed as a variable 'name'
# @app.route('/hello/<name>')
# def hello(name):
#     print(name)
#     return "Hello, " + name


@app.route('/dojo')
def dojo():
    return "Dojo!"


@app.route('/flask')
def flask():
    return "Hi Flask!"


@app.route('/michael')
def michael():
    return "Hi Michael!"


@app.route('/john')
def john():
    return "Hi John!"


# @app.route('/hello/<hello>')
# def __init__(hello):
#     result = (hello + " ") * 35
#     return result


# @app.route('/bye/<bye>')
# def __init__(bye):
#     farewell = (bye + " ") * 80
#     return farewell

@app.route('/dogs/<dogs>')
def __init__(dogs):
    product = (dogs + " ") * 99
    return product


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
