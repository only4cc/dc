from flask import Flask
import socket
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
  
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Flask en un contenedor Docker! ' +str(ip_address)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
