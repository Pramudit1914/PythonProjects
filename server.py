import http.server
import socketserver
import json
import os
from Fnaf4 import FNAFEngine

PORT = 8000
game_instance = None

class FNAFHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        global game_instance
        
        if self.path == '/api/start':
            game_instance = FNAFEngine()
            response = {
                "status": "alive",
                "time": game_instance.time,
                "action_amount": game_instance.action_amount,
                "messages": [
                    "You are awoken in a dark room, you have no idea where you are or how you got there.",
                    "Its almost like a nightmare. But you somehow have deja vu, but you know you have never been here.",
                    "Your heart is pounding and it cant be stopped. You tell yourself you're okay. Its too bad your doors cant be locked, to keep whatevers there away...",
                    "................. Good luck.",
                    "HOW 2 PLAY: To approach to the left door, press the Left arrow key, Right arrow key for right door, for Closet, click the upwards arrow key. Press the down key to check the bed behind you.",
                    "Survive until 6 AM! Each action progresses the time."
                ],
                "random_probability1": game_instance.random_probability1,
                "random_probability2": game_instance.random_probability2,
                "random_probability22": game_instance.random_probability22,
                "closet_state": game_instance.closet_state
            }
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode('utf-8'))
            
        elif self.path == '/api/action':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
                action = data.get('action')
            except Exception as e:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Invalid JSON")
                return
                
            if not game_instance:
                game_instance = FNAFEngine()
                
            result = game_instance.execute_action(action)
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
            self.end_headers()
            self.wfile.write(json.dumps(result).encode('utf-8'))
            
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

    # Override log_message to print cleaner messages in terminal
    def log_message(self, format, *args):
        print(f"[Server] {self.address_string()} - - [{self.log_date_time_string()}] {format%args}")

def run_server():
    # Make sure we serve from the directory of this server file
    server_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(server_dir)
    
    # Allow address reuse to prevent "address already in use" errors during rapid restarts
    socketserver.TCPServer.allow_reuse_address = True
    
    with socketserver.TCPServer(("", PORT), FNAFHTTPRequestHandler) as httpd:
        print("==================================================")
        print(f" FNAF 4 Web Game Server running at:")
        print(f" http://localhost:{PORT}")
        print(" Press Ctrl+C to stop the server")
        print("==================================================")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped. Goodbye!")

if __name__ == "__main__":
    run_server()
