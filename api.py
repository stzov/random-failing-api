import os
import sys
import traceback
import random
import logging

from flask import Flask, jsonify, make_response

sys.path.append(os.path.dirname(__file__))

app = Flask(__name__)

logger = logging.getLogger('api')
logger.setLevel(logging.INFO)

@app.route("/get", methods=["get"])
def get_res():
    # Statistically more successes
    outcomes = [200, 200, 200, 502, 200, 503, 200, 200, 401, 200, 200]
    random_outcome = random.choice(outcomes)
    try:
        if random_outcome == 200:
            logger.info("Got 200")
            return jsonify({"status": "ok"})
        else:
            logger.error("Got " + str(random_outcome))
            return make_response(jsonify({}), random_outcome)
    except Exception:
        logger.error(traceback.format_exc())
        return make_response(jsonify({"status": "error"}), 500)
