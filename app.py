from flask import Flask, jsonify, request

app = Flask(__name__)

# Зразок даних (як база даних)
data_store = [
    {"id": 1, "name": "Елемент 1", "description": "Це перший елемент"},
    {"id": 2, "name": "Елемент 2", "description": "Це другий елемент"}
]

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API працює!"})

@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(data_store)

@app.route("/data/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((item for item in data_store if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Елемент не знайдено"}), 404
    return jsonify(item)

@app.route("/data", methods=["POST"])
def create_data():
    new_data = request.get_json()
    if not new_data or "name" not in new_data or "description" not in new_data:
        return jsonify({"error": "Недостатньо даних"}), 400
    
    new_id = max(item["id"] for item in data_store) + 1
    new_item = {
        "id": new_id,
        "name": new_data["name"],
        "description": new_data["description"]
    }
    data_store.append(new_item)
    return jsonify(new_item), 201

@app.route("/data/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    updated_data = request.get_json()
    item = next((item for item in data_store if item["id"] == item_id), None)
    
    if item is None:
        return jsonify({"error": "Елемент не знайдено"}), 404
    
    item["name"] = updated_data.get("name", item["name"])
    item["description"] = updated_data.get("description", item["description"])
    return jsonify(item)

@app.route("/data/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global data_store
    data_store = [item for item in data_store if item["id"] != item_id]
    return jsonify({"message": "Елемент видалено"}), 204

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
