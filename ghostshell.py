"""GhostShell: a local, offline haunted terminal. A ghost (open-weight model via Ollama) whispers about each command you run."""
import json, subprocess, sys, urllib.request

MODEL = "llama3.2:1b"  # any open-weight model pulled in Ollama
SYSTEM = ("You are a melancholy ghost haunting this terminal. In one short, eerie sentence, "
          "whisper commentary about the shell command and its output. Never give real instructions.")

def whisper(cmd, out, model=None):
    body = json.dumps({"model": model or MODEL, "stream": False, "messages": [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": f"Command: {cmd}\nOutput: {out[:500]}"}]}).encode()
    req = urllib.request.Request("http://localhost:11434/api/chat", body, {"Content-Type": "application/json"})
    try:
        return json.load(urllib.request.urlopen(req, timeout=60))["message"]["content"].strip()
    except Exception as e:
        return f"(the spirit is silent: {e})"

def serve(port=8000):
    import os
    from http.server import BaseHTTPRequestHandler, HTTPServer
    root = os.path.dirname(os.path.abspath(__file__))

    class H(BaseHTTPRequestHandler):
        def _send(self, code, ctype, data):
            self.send_response(code)
            self.send_header("Content-Type", ctype)
            self.end_headers()
            self.wfile.write(data)

        def do_GET(self):
            path = {"/": "index.html", "/assets/figma.css": "assets/figma.css"}.get(self.path)
            if not path:
                return self._send(404, "text/plain", b"not found")
            ctype = "text/css" if path.endswith(".css") else "text/html; charset=utf-8"
            self._send(200, ctype, open(os.path.join(root, path), "rb").read())

        def do_POST(self):
            # Browsers can't send application/json cross-origin without a preflight, which we never grant.
            if self.path != "/api/run" or self.headers.get("Content-Type") != "application/json":
                return self._send(400, "text/plain", b"bad request")
            req = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))))
            cmd = req.get("command", "")
            p = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
            out = (p.stdout + p.stderr).rstrip()
            res = {"output": out, "whisper": whisper(cmd, out, req.get("model"))}
            self._send(200, "application/json", json.dumps(res).encode())

    print(f"GhostShell UI on http://127.0.0.1:{port}")
    HTTPServer(("127.0.0.1", port), H).serve_forever()

def main():
    if "--web" in sys.argv:
        return serve()
    print("GhostShell - type commands, 'exit' to leave.")
    while True:
        cmd = input("\N{GHOST} $ ").strip()
        if cmd in ("exit", "quit"):
            break
        if not cmd:
            continue
        p = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        out = p.stdout + p.stderr
        print(out, end="")
        print(f"\x1b[35m  ~ {whisper(cmd, out)}\x1b[0m")

if __name__ == "__main__":
    sys.exit(main())
