from app import create_app
import os


app = create_app(os.getenv('ENVIRONMENT') or 'Development')

if __name__ == '__main__':
    app.run()