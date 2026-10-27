from flask import Flask, request, jsonify
from motor_testing import forward, backward, turn_left, turn_right, stop

app = Flask(__name__)

COMMANDS = {
    "forward": forward,
    "backward": backward,
    "left": turn_left,
    "right": turn_right,
    "stop": stop,
}

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Robot Control</title>
        <style>
            body { font-family: Arial; text-align: center; background: #111; color: white; }
            button {
                width: 120px; height: 70px; font-size: 20px;
                margin: 8px; border-radius: 12px; border: none;
                background: #2b7cff; color: white;
            }
            #stop { background: #d93025; width: 260px; }
        </style>
    </head>
    <body>
        <h1>Raspberry Pi Robot</h1>

        <div>
            <button onclick="send('forward')">FORWARD</button>
        </div>

        <div>
            <button onclick="send('left')">LEFT</button>
            <button onclick="send('stop')">STOP</button>
            <button onclick="send('right')">RIGHT</button>
        </div>

        <div>
            <button onclick="send('backward')">BACKWARD</button>
        </div>

        <div>
            <button id="stop" onclick="send('stop')">EMERGENCY STOP</button>
        </div>

        <script>
            async function send(cmd) {
                await fetch('/control', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({command: cmd})
                });
            }

            // Safety: stop the robot if the browser/tab closes
            window.addEventListener('beforeunload', () => send('stop'));
        </script>
    </body>
    </html>
    """

@app.route("/control", methods=["POST"])
def control():
    data = request.get_json()
    command = data.get("command")

    if command not in COMMANDS:
        return jsonify({"status": "error", "message": "Unknown command"}), 400

    COMMANDS[command]()
    return jsonify({"status": "ok", "command": command})

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=5000)
    finally:
        stop()