from flask import Flask, send_file
import os

app = Flask(__name__)


def create_default_index():
    os.makedirs('src', exist_ok=True)
    with open('src/index.html', 'w') as f:
        f.write('''<!DOCTYPE html>
<html>
<head><title>Flask Server</title></head>
<body>
    <h1>Hello from Flask!</h1>
    <p>Serving /src/index.html</p>
</body>
</html>''')


@app.route('/')
def serve_index():
    file_path = 'src/index.html'

    if not os.path.exists(file_path):
        create_default_index()

    return send_file(file_path)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)