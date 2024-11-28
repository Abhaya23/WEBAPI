from flask import Flask, request, jsonify
from handlers.post_handler import PostHandler
from handlers.data_handler import DataHandler

app = Flask(__name__)

data_handler = DataHandler()
post_handler = PostHandler(data_handler)

# API endpoint to add a post
@app.route('/api/posts', methods=['POST'])
def add_post():
    post = request.json
    if not post or "content" not in post:
        return jsonify({"error": "Invalid post"}), 400
    return jsonify(post_handler.add_post(post))

# API endpoint to get all posts
@app.route('/api/posts', methods=['GET'])
def get_posts():
    return jsonify(post_handler.get_posts())

if __name__ == '__main__':
    app.run(debug=True)
