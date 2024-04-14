from functools import wraps
from flask import request, jsonify
from app.models.User import User
import jwt
from flask import current_app as app

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "x-access-tokens" in request.headers:
            token = request.headers["x-access-tokens"]
        if not token:
            return jsonify({"message": "Token is missing!"}), 401
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            current_user = User.query.filter_by(id=data["id"]).first()
        except:
            return jsonify({"message": "Token is invalid!"}), 401
        return f(current_user, *args, **kwargs)

    return decorated
