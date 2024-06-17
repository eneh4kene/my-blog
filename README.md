# Blog Platform

## Overview

This project is a simple Blog Platform built with Flask, a lightweight Python web framework. The platform allows users to create, read, update, and delete blog posts. 
The posts are stored in a JSON file, making it easy to manage without the need for a full-fledged database.

## Features

- **View Blog Posts**: Display all blog posts on the homepage.
- **Add New Post**: Create a new blog post with a title, author, and content.
- **Update Post**: Edit an existing blog post.
- **Delete Post**: Remove a blog post from the list.
- **Persistent Storage**: Blog posts are stored in a JSON file (`blog_db/blog.json`), ensuring data is preserved between server restarts.

## Requirements

- Python 3.x
- Flask
- JSON

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/blog-platform.git
   cd blog-platform
   ```

2. **Create a virtual environment and activate it**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application**:
   ```bash
   python main.py
   ```

5. **Open your browser and navigate to** `http://127.0.0.1:5000`

## Usage

### View All Posts

Navigate to the home page to see a list of all blog posts.

### Add a New Post

1. Click on the "Add Post" link.
2. Fill out the form with the post's title, author, and content.
3. Submit the form to add the post to the blog.

### Update a Post

1. Click the "Edit" button next to the post you want to update.
2. Modify the title, author, or content.
3. Submit the form to update the post.

### Delete a Post

1. Click the "Delete" button next to the post you want to remove.
2. Confirm the deletion to remove the post from the blog.

## File Structure

```
blog-platform/
├── blog_db/
│   └── blog.json          # JSON file storing the blog posts
├── templates/
│   ├── index.html         # Home page template
│   ├── add_post.html      # Template for adding a new post
│   └── update_post.html   # Template for updating a post
├── main.py                # Main Flask application file
├── requirements.txt       # Required Python packages
└── README.md              # Project README file
```

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any changes you would like to make.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

This README should provide a clear and concise overview of your project, making it easy for others to understand and contribute to it.
