import secrets

from flask import Flask
from flask_smorest import Api
from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint
from flask_jwt_extended import JWTManager

app=Flask(__name__)


app.config["PROPOGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Store Rest Api"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

app.config["JWT_SECRET_KEY"] = "267147144780067525750554488564863946480"
jwt = JWTManager(app)

api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)
