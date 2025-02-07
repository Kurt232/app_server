from flask import Flask, request, jsonify
from src.routes.upload_routes import upload_bp
from src.routes.gpt_routes import gpt_bp
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Set a secret key for session management

def create_app():
    
    # Register blueprints
    app.register_blueprint(upload_bp)
    app.register_blueprint(gpt_bp)
    
    # Ensure uploads directory exists
    os.makedirs('uploads', exist_ok=True)

    return app

# for uploading the userID
# @app.route('/set_user', methods=['POST'])
# def set_user():
#     user_id = request.json.get('user_id')
#     if user_id:
#         session['user_id'] = user_id
#         return jsonify({"status": "success", "message": f"User ID set successfully: {session.get('user_id')}"}), 200
#     return jsonify({"status": "error", "message": "User ID is required"}), 400

# @app.route('/get_user', methods=['GET'])
# def get_user():
#     user_id = session.get('user_id')
#     if user_id:
#         return jsonify({"status": "success", "user_id": user_id}), 200
#     return jsonify({"status": "error", "message": "No user ID set"}), 404

@app.route('/get_intervention', methods=['POST'])
def get_intervention():
    user_id =  request.json.get("user_id")
    file_path = 'test.txt'
    try:
        # Read the contents of the file
        with open(file_path, 'r') as f:
            intervention_text = f.read()
        
        # Return the intervention text in JSON format
        return jsonify({
            "status": "success",
            "intervention": intervention_text
        }), 200
    except FileNotFoundError:
        return jsonify({"status": "error", "message": "File not found"}), 404
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/get_summary', methods=['POST'])
def get_summary():
    user_id = request.json.get("user_id")
    if user_id:
        return jsonify({"status": "success", 
                        "summaryA": "this is a dummy summary A.",
                        "summaryB": "this is a dummy summary B."
                        }), 200
    else: 
        return jsonify({"status": "error", "message": "unsuccessful"}), 400

@app.route('/send_summary_feedback', methods= ["POST"])
def send_summary_feedback():
    try: 
        user_id =  request.json.get("user_id")
        summaryA = request.json.get("summaryA")
        summaryB = request.json.get("summaryB")
        chosen =  request.json.get("chosen")
        feedbackRating = request.json.get("feedbackRating")
        userSummary =  request.json.get("userSummary")

        return jsonify({"status": "success", "message": "successful"}), 200
    except:
        return jsonify({"status": "error", "message": "unsuccessful"}), 400

@app.route('/send_weekly_survey', methods= ["POST"])
def send_weekly_survey():
    try: 
        user_id =  request.json.get("user_id")
        phq4 = request.json.get("phq4")
        pss4 = request.json.get("pss4")
        panas = request.json.get("panas")

        return jsonify({"status": "success", "message": "successful"}), 200
    except:
        return jsonify({"status": "error", "message": "unsuccessful"}), 400

@app.route("/upload", methods=['POST'])
def upload():
    user_id = request.json.get("user_id")
    csv_content = request.json.get("csv_content")
    if user_id and csv_content: 
        file_path = f"uploads/{user_id}.csv"
        # Open the file in append mode and write the csv_content
        with open(file_path, 'a') as file:
            file.write(csv_content + '\n')  # Adding a newline for better formatting
        return jsonify({"status": "success", "user_id": user_id, "csv_content": csv_content}), 200
    else: 
        return jsonify({"status": "error", "message": "unsuccessful"}), 400

if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0")
