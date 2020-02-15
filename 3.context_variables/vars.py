from flask import Flask
app=Flask(__name__)

peoplet=[
    {'name':"Ssali JOnathan"},
    {'name':"Julian Calor"},
    {'name':"Greet Calor"}
]

@app.route('/<string:name>') #we pass a name as a string
def hello(name): #pass it in the view function as an arguement
    return "<h1>Hello {}</h1>".format(name)#has to say hello to the name passed with the URLs



if __name__ == "__main__":
    app.run()
