from flask import Flask, render_template, request, jsonify, session
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'discord_clone_secret_key'

# Données en mémoire (simulation)
servers = ["Accueil", "Gaming", "Musique", "Dev", "Anime"]
messages = {
    "general": [
        {"author": "Alice", "content": "Salut tout le monde !", "time": "14:32"},
        {"author": "Bob", "content": "Ça va ?", "time": "14:33"}
    ]
}
friends = ["Alice", "Bob", "Charlie", "Eva", "Lucas"]

@app.route('/')
def home():
    return render_template('index.html', servers=servers, friends=friends)

@app.route('/server/<server_name>')
def server(server_name):
    return render_template('chat.html', 
                         server_name=server_name,
                         channel="général",
                         messages=messages.get("general", []))

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    author = data.get('author', 'Vous')
    content = data.get('content')
    channel = data.get('channel', 'general')
    
    if content:
        if channel not in messages:
            messages[channel] = []
        messages[channel].append({
            "author": author,
            "content": content,
            "time": datetime.now().strftime("%H:%M")
        })
        return jsonify({"success": True, "message": messages[channel][-1]})
    return jsonify({"success": False})

@app.route('/friends')
def friends_page():
    return render_template('friends.html', friends=friends)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
