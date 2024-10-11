
from flask import Flask, jsonify, request
from pymongo import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)


uri = "mongodb+srv://venkatasugunadithya:fmHpAuSLcnkI4BUM@cluster0.zvndb.mongodb.net/mydb?retryWrites=true&w=majority&appName=Cluster0"


client = MongoClient(uri, server_api=ServerApi('1'))

# Test connection
try:
    client.admin.command('ping')
    print("Successfully connected to MongoDB Atlas!")
except Exception as e:
    print("Connection error:", e)

db = client.mydb

tasks_collection = db.tasks


@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = list(tasks_collection.find({}, {'_id': 0}))  # Exclude MongoDB's default _id field
    return jsonify(tasks)


@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json
    tasks_collection.insert_one(task)
    return jsonify({"message": "Task added successfully!"}), 201


@app.route('/tasks/<string:task_name>', methods=['PUT'])
def update_task(task_name):
    updated_task = request.json
    result = tasks_collection.update_one({"name": task_name}, {"$set": updated_task})
    if result.matched_count == 0:
        return jsonify({"error": "Task not found"}), 404
    return jsonify({"message": "Task updated successfully!"})


@app.route('/tasks/<string:task_name>', methods=['DELETE'])
def delete_task(task_name):
    result = tasks_collection.delete_one({"name": task_name})
    if result.deleted_count == 0:
        return jsonify({"error": "Task not found"}), 404
    return jsonify({"message": "Task deleted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
