#!/usr/bin/env python3
"""
Social Media Analytics Dashboard
Flask server running on port 8080
"""

import os
import json
from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
from fetch_stats import update_analytics

load_dotenv()

app = Flask(__name__)
PORT = int(os.getenv('FLASK_PORT', 8080))

def load_analytics():
    """Load analytics data from JSON file"""
    try:
        with open('analytics.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "instagram": {"followers": 0, "profile_views": 0, "posts": []},
            "twitter": {"followers": 0, "tweets": []},
            "history": []
        }

@app.route('/')
def dashboard():
    """Main dashboard page"""
    data = load_analytics()
    return render_template('dashboard.html', data=data)

@app.route('/api/analytics')
def get_analytics():
    """API endpoint to get analytics data"""
    data = load_analytics()
    return jsonify(data)

@app.route('/fetch')
def fetch():
    """Fetch and update analytics"""
    try:
        data = update_analytics()
        return jsonify({
            "success": True,
            "message": "Analytics updated successfully!",
            "data": data
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error: {str(e)}"
        }), 500

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 Social Media Analytics Dashboard")
    print("="*60)
    print(f"📍 Server: http://localhost:{PORT}")
    print(f"📍 Dashboard: http://localhost:{PORT}/")
    print(f"📍 Fetch Analytics: http://localhost:{PORT}/fetch")
    print("="*60)
    print("Press CTRL+C to stop the server")
    print("="*60 + "\n")
    
    app.run(host='0.0.0.0', port=PORT, debug=True)
