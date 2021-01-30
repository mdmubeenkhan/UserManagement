from flask import Flask, jsonify

class User:
    def login():
        user = {
            "id": "",
            "password": ""
        }
        return jsonify(user), 200


