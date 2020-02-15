from flask import Flask

#create an instance of the Flask class
app=Flask(__name__)

#then make a route with its corresponding view function
@app.route('/')
def hello():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True) # run the server in debug mode for development only.

    #it simplifies debugging