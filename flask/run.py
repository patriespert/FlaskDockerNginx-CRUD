from core import create_app

class Config:
    DEBUG = True

app = create_app(Config)

if __name__ == '__main__':
    app.run(host='0.0.0.0')