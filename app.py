from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulando um banco de dados de usuários
users = [
    {'id': 1, 'name': 'Alice'},
    {'id': 2, 'name': 'Bob'}
]

posts = [
    {'id': 1, 'author': 'Alice', 'title': 'Primeiro Post', 'content': 'Este é o conteúdo do primeiro post'},
    {'id': 2, 'author': 'Bob', 'title': 'Segundo Post', 'content': 'Este é o conteúdo do segundo post'}
]

# CRUD de usuários
@app.route('/api/users', methods=['GET'])
def get_users():
    sorted_users = sorted(users, key=lambda x: x['name'])
    return jsonify(sorted_users), 200

@app.route('/api/users', methods=['POST'])
def create_user():
    new_user = request.get_json()
    # Validação de dados - garantindo que o novo usuário tenha um nome
    if 'name' not in new_user:
        return jsonify({'error': 'Missing name parameter'}), 400
    new_user['id'] = len(users) + 1
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user is not None:
        return jsonify(user), 200
    else:
        return jsonify({'message': 'User not found'}), 404

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user['id'] != user_id]
    return jsonify({'message': 'User deleted'}), 204

# Modificando o endpoint para incluir o nome do autor
@app.route('/api/posts', methods=['GET'])
def get_posts():
    for post in posts:
        author = next((user['name'] for user in users if user['name'] == post['author']), None)
        post['author'] = author
    sorted_posts = sorted(posts, key=lambda x: x['author'])
    return jsonify(sorted_posts), 200

@app.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if post is not None:
        return jsonify(post), 200
    else:
        return jsonify({'message': 'Post not found'}), 404

@app.route('/api/posts', methods=['POST'])
def create_post():
    new_post = request.get_json()
    # Validação de dados - garantindo que o novo post tenha um autor, título e conteúdo
    if 'author' not in new_post or 'title' not in new_post or 'content' not in new_post:
        return jsonify({'error': 'Missing author, title, or content parameter'}), 400
    new_post['id'] = len(posts) + 1
    posts.append(new_post)
    return jsonify(new_post), 201

@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if post is not None:
        data = request.get_json()
        post.update(data)
        return jsonify(post), 200
    else:
        return jsonify({'message': 'Post not found'}), 404

@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    global posts
    posts = [post for post in posts if post['id'] != post_id]
    return jsonify({'message': 'Post deleted'}), 204

if __name__ == '__main__':
    app.run(debug=True)
