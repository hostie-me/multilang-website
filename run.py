from server import app
import routes

if __name__ == '__main__':
    app.run(port=5050, debug=True, threaded=True)