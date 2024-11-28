class PostHandler:
    def __init__(self, data_handler):
        self.data_handler = data_handler

    def add_post(self, post):
        data = self.data_handler.load_data()
        data.append(post)
        self.data_handler.save_data(data)
        return {"message": "Post added successfully!"}

    def get_posts(self):
        return self.data_handler.load_data()
