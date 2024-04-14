import datetime
from flask import make_response
import jwt
from werkzeug.security import generate_password_hash, check_password_hash

from app.dtos.auth import AuthLoginDTO, AuthRegisterDTO
from app.models.User import User
from app import db, app
import sys

class AuthController:
        
      def register(self, user:AuthRegisterDTO):
        if not user["email"] or not user["password"]:
            return {
                    "err": "email and password are required",
                    "code": 400
                }

        existing_user = User.query.filter_by(email=user["email"]).first()
        if existing_user:
            return {
                    "err": "User already exists",
                    "code": 400
                }
        user["password"] = generate_password_hash(user["password"])
        print(user)
        new_user = User(email=user["email"],password=user["password"],name=user["name"],lastname=user["lastname"],document=user["document"])
        db.session.add(new_user)
        db.session.commit()

        return {"message": "User registered successfully"}
      
      def login(self, login:AuthLoginDTO):
        if not login or not login.get("email") or not login.get("password"):
            return {
                    "err": "Could not verify",
                    "code":"401",
                    "message":"'WWW-Authenticate': 'Basic realm='Login required!'"
                    }

        user = User.query.filter_by(email=login.get("email")).first()
 
        if not user or not check_password_hash(user.password,login["password"]):
            return {
                    "err": "Could not verify",
                    "code":"401",
                    "message":"'WWW-Authenticate': 'Basic realm='Login required!'"
                    }
        token = jwt.encode(
            {
                "id": user.id,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
            },
            app.config["SECRET_KEY"],
        )
        print("pan")

        
        return {"token": token, "user": user.email}