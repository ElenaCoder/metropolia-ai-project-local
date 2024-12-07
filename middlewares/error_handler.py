from flask import jsonify


def handle_errors(error):
    """Middleware to handle all uncaught exceptions."""
    response = {
        "error": str(error),
        "message": "An error occurred while processing your request.",
    }
    return jsonify(response), 500
