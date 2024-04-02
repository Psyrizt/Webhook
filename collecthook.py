from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Define the HTTP request handler class
class WebhookHandler(BaseHTTPRequestHandler):
    # Handle POST requests
    def do_POST(self):
        # Check if the request path is '/webhook'
        if self.path == '/webhook':
            # Get the content length
            content_length = int(self.headers['Content-Length'])
            # Read the POST data
            post_data = self.rfile.read(content_length)
            # Parse JSON data
            system_info = json.loads(post_data.decode('utf-8'))
            # Print received system information
            print('Received system information:')
            print(system_info)
            # Send response
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(bytes('Data received successfully', 'utf-8'))
        else:
            # If path is not '/webhook', send 404 response
            self.send_error(404, 'Not Found')

# Define the server address and port
server_address = ('', 8080)

# Create an HTTP server with the defined request handler
httpd = HTTPServer(server_address, WebhookHandler)

# Start the HTTP server
print('Server running on port 8080')
httpd.serve_forever()
