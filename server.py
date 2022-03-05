from flask import Flask
app = Flask(__name__)

ip = input()
user_port = input()

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(host=ip, port=user_port)
