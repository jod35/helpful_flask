from flask import Flask,render_template #this method is used to render templates

app=Flask(__name__)

#fake in memory database containing post data

posts=[
   {
      'author':"Harry Porter",
      'date_posted':"Sat 15 Feb 2020",
      'title':"A day in Portland",
      'content':"Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempora voluptate, quis quae iure, hic accusamus culpa minima nam non eius praesentium earum veniam molestias sed delectus eum odit tenetur voluptatem."
   },
   {
      'author':"John Doe",
      'date_posted':"Sat 15 Feb 2020",
      'title':"How was Valentine?",
      'content':"Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempora voluptate, quis quae iure, hic accusamus culpa minima nam non eius praesentium earum veniam molestias sed delectus eum odit tenetur voluptatem."
   },
   {
      'author':"Jane Doe",
      'date_posted':"Sat 15 Feb 2020",
      'title':"One African survived coronavirus",
      'content':"Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempora voluptate, quis quae iure, hic accusamus culpa minima nam non eius praesentium earum veniam molestias sed delectus eum odit tenetur voluptatem."
   },

]

@app.route('/')
def index():

   return render_template('index.html',posts=posts)

@app.route('/about')
def about():
   return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)