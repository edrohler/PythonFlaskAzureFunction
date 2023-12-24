from flask_restx import Resource, Namespace
import logging
ns = Namespace("api", description="Api endpoints", version=1.0)

@ns.route("/ping")
class Ping(Resource):
    def get(self):
        logging.info("Ping endpoint was called.")
        return {"message": "pong"}