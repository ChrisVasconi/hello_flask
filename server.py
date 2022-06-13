
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
app.secret_key = "secret"


list_todos = [{
    "todo": "Learn templates in flask",
    "status": "In progress"
},
    {
        "todo": "Learn templates in flask",
        "status": "In progress"
},
    {
        "todo": "Learn templates in flask",
        "status": "In progress"
}
]


@app.route("chris")
def hello_from_flask():
    return "Hello class! This is coming from your first server"


@app.route("/goodbye")
def goodbye_from_flask():
    return "Good bye class!"


@app.route("/num/<int:num>")
def print_number(num):
    print("Number sent from the URL:", num)
    return f"Your number is + {num}"


@app.route("/")
@app.route("/todos")
def fet_all_todos():
    if "num_of_visits" in session:
        session["num_of_visits"] += 1
    else:
        session["num_of_visits"] = 1
        
    return render_template( "index.html", first_name = "Alexander", list_todos = list_todos)
    
@app.route("/todo/new", methods = ['POST'] )
def create_todo():
    pass
# Theres also "GET"-display route "POST" and ""


if __name__ == "__main__":
    app.run(debug=True)


"http://127.0.0.1:5000"



# Display routes and action routes
# GET - read and display
# URL of the route to display all: the name of the list or dictionary we are about to display
# ex. "/todos"
#     "/users"

# function: get_all_todos()

# URL of the route to display one: the name of the list in singular that we are about to display followed by the id
# ex. "/todos/<int:id>"
# ex. "/users/<int:id>"

# Function: get_todo_by_id ( id )

# post - create
# URL of the route to create something new: name of list in singular that we are about to create followed by the keyword /new
# ex. "/todo/new"
# ex. "/user/new"

# function: create_todo()

# PUT - update
# URL of the route to update something already existing: the name of the list in singular that we are about to update followed by the id, followed by the keyword/update /Edit
# example: "/todo/<int:id>update"
# ex. ""

# Function: update_todo_by_id( id )

# DELETE - 
# URL of the route to delete something already existing: the name of the list in singular that we are about to delete followed by the id, followed by the keyword/delete /Edit
# example: "/todo/<int:id>delete"