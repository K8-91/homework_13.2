from flask import Flask, request, render_template, redirect, url_for
from forms import TodoForm
from models import todos


app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"


@app.route("/todos/", methods=["GET", "POST"])
def todos_list():
    form = TodoForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            values =[]
            for value in form.data.values():
                values.append(value)
            how_many = len(values)
            todos.insert((values)[:how_many-1])
        return redirect(url_for("todos_list"))
    return render_template("todos.html", form=form, todos=todos.show_all(), error=error)


@app.route("/todos/edit/<int:todo_id>/", methods=["GET", "POST"])
def todo_edit(todo_id):
    todo = todos.show_one(todo_id-1)
    form = TodoForm(data=todo)
    if request.method == "POST":
        if form.validate_on_submit():
            values = []
            for value in form.data.values():
                values.append(value)
            how_many = len(values)
        todos.update(todo_id-1, (values[:how_many - 1]))
        return redirect(url_for("todos_list"))
    return render_template("todo_id.html", form=form, todo_id=todo_id)


@app.route("/todos/<int:id>/", methods=["DELETE"])
def todos_delete(id):
    result = todos.delete(id)
    return result


if __name__ == "__main__":
    app.run(debug=True)