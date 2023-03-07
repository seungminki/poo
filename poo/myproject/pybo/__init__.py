# set FLASK_APP=pybo
# set FLASK_DEBUG=true


from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def page_not_found(e):
  return render_template('404.html'), 404

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_error_handler(404, page_not_found)

     # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # 블루프린트
    from .views import main_views
    app.register_blueprint(main_views.bp)


    return app

# db.session.rollback() 커밋 이전에 취소 가능