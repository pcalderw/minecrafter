from app import app

from config import init
init(app)

if __name__ == '__main__':
    app.run('0.0.0.0', 5433, debug=True)