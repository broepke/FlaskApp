from click import core
from flaskr import create_app
from flaskr import db

core._verify_python3_env = lambda: None

app = create_app()
with app.app_context():
    db.init_db_command()
