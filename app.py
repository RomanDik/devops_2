import http.server
import socketserver

PORT = 8181

class SimpleHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        html_content = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>DevOps Lab #1</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; }
                .container { max-width: 800px; margin: 0 auto; }
                .success { color: green; font-weight: bold; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>DevOps Laboratory Work #1</h1>
                <p><strong>Student:</strong> dik</p>
                <p class="success">Successfully deployed via GitHub Webhooks! final try again 2!</p>
                <p>This page updates automatically when you push to GitHub.</p>
                <p><strong>Webhook URL:</strong> http://webhook.dik.course.prafdin.ru</p>
                <p><strong>App URL:</strong> http://app.dik.course.prafdin.ru</p>
            </div>
        </body>
        </html>
        '''
        
        self.wfile.write(html_content.encode())

with socketserver.TCPServer(("", PORT), SimpleHandler) as httpd:
    print(f"Server running on port {PORT}")
    httpd.serve_forever()