from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Open and read the JSON file
file_path = 'blog_db/blog.json'
with open(file_path, 'r') as file:
    blog_posts = json.load(file)


def save_to_json_file(file):
    with open(file, 'w') as file_obj:
        json.dump(blog_posts, file_obj, indent=4)


@app.route('/')
def index():
    # add code here to fetch the job posts from a file
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        # Extract post data
        title = request.form.get('title')
        author = request.form.get('author')
        content = request.form.get('content')

        # update blog and storage
        max_id = max(post['id'] for post in blog_posts)
        new_id = max_id + 1

        # create new blog post
        new_post = {'id': new_id, 'author': author, 'title': title, 'content': content}
        blog_posts.append(new_post)
        # update json file
        save_to_json_file(file_path)

        return redirect(url_for('index'))
    return render_template('add_post.html')


@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    global blog_posts

    # Remove the post from the in-memory list
    blog_posts = [post for post in blog_posts if post['id'] != post_id]

    # Update the JSON file
    save_to_json_file(file_path)

    # Redirect to the index page
    return redirect(url_for('index'))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update_post(post_id):
    # define the post logic
    global blog_posts
    if request.method == 'POST':
        # Fetch the updated form fields
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')
        for post in blog_posts:
            if post['id'] == post_id:
                post['author'] = author
                post['title'] = title
                post['content'] = content
        # Update the post in the JSON file
        save_to_json_file(file_path)
        # Redirect back to index
        return redirect(url_for('index'))

    # Else, it's a GET request
    else:
        post = next(post for post in blog_posts if post['id'] == post_id)
    # So display the update.html page
    return render_template('update.html', post=post)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
