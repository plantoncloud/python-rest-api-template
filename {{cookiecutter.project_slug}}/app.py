from flask import Flask, jsonify, request

app = Flask(__name__)

# This is an in-memory store for the purposes of this example.
# You would typically use a database like MySQL or MongoDB in a real app.
todos = [
    {
        'id': 1,
        'task': 'Learn Python',
        'completed': False
    },
    {
        'id': 2,
        'task': 'Learn Flask',
        'completed': False
    }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next(filter(lambda t: t['id'] == todo_id, todos), None)
    if todo:
        return jsonify(todo)
    else:
        return 'Todo not found', 404

@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    task = data['task']
    if not task or len(task) < 3:
        return 'Task must be at least 3 characters long', 400
    todo = {
        'id': todos[-1]['id'] + 1,
        'task': task,
        'completed': False
    }
    todos.append(todo)
    return jsonify(todo), 201

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next(filter(lambda t: t['id'] == todo_id, todos), None)
    if not todo:
        return 'Todo not found', 404
    data = request.get_json()
    task = data['task']
    if not task or len(task) < 3:
        return 'Task must be at least 3 characters long', 400
    todo['task'] = task
    return jsonify(todo)

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = next(filter(lambda t: t['id'] == todo_id, todos), None)
    if not todo:
        return 'Todo not found', 404
    todos.remove(todo)
    return jsonify(todo)

if __name__ == '__main__':
    app.run(debug=True)
