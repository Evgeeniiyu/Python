from flask import Flask, jsonify, request

app = Flask(__name__)

# Зразок даних (наприклад, як база даних)
data_store = [
    {"id": 1, "name": "Елемент 1", "description": "Це перший елемент"},
    {"id": 2, "name": "Елемент 2", "description": "Це другий елемент"}
]

# Маршрут для перевірки роботи API
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API працює!"})

# Маршрут для отримання всіх елементів (GET)
@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(data_store)

# Маршрут для отримання конкретного елемента за його ID
@app.route("/data/<int:item_id>", methods=["GET"])
def get_item(item_id):
    # Пошук елемента за ID
    item = next((item for item in data_store if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Елемент не знайдено"}), 404
    return jsonify(item)

# Маршрут для створення нового елемента (POST)
@app.route("/data", methods=["POST"])
def create_data():
    # Отримання JSON даних з запиту
    new_data = request.get_json()
    
    # Перевірка наявності обов’язкових полів
    if not new_data or "name" not in new_data or "description" not in new_data:
        return jsonify({"error": "Недостатньо даних"}), 400
    
    # Додавання нового елемента до data_store
    new_id = max(item["id"] for item in data_store) + 1
    new_item = {
        "id": new_id,
        "name": new_data["name"],
        "description": new_data["description"]
    }
    data_store.append(new_item)
    return jsonify(new_item), 201

# Маршрут для оновлення існуючого елемента (PUT)
@app.route("/data/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    updated_data = request.get_json()
    item = next((item for item in data_store if item["id"] == item_id), None)
    
    if item is None:
        return jsonify({"error": "Елемент не знайдено"}), 404
    
    # Оновлення даних елемента
    item["name"] = updated_data.get("name", item["name"])
    item["description"] = updated_data.get("description", item["description"])
    return jsonify(item)

# Маршрут для видалення існуючого елемента (DELETE)
@app.route("/data/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global data_store
    data_store = [item for item in data_store if item["id"] != item_id]
    return jsonify({"message": "Елемент видалено"}), 204

# Запуск сервера
if __name__ == "__main__":
    app.run(debug=True)
