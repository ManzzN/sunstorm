from flask import Flask, render_template, send_from_directory, redirect, url_for
import os

app = Flask(__name__)

# Configure static folder for resources
app.config['STATIC_FOLDER'] = 'static'

@app.route('/')
@app.route('/index.html')
def index():
    """Solar flare escape game - main entry point"""
    return render_template('index.html')

@app.route('/iss')
@app.route('/iss.html')
def iss_game():
    """ISS magnetosphere survival game"""
    return render_template('iss.html')

@app.route('/heli')
@app.route('/heli.html')
def helicopter_game():
    """Helicopter emergency landing game"""
    return render_template('heli.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    """Serve static files (resources, audio, images)"""
    return send_from_directory('static', filename)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Check if templates and static directories exist
    if not os.path.exists('templates'):
        os.makedirs('templates')
        print('Created templates directory')
    if not os.path.exists('static'):
        os.makedirs('static')
        print('Created static directory')
    if not os.path.exists('static/resources'):
        os.makedirs('static/resources')
        print('Created static/resources directory')
    
    # List available templates
    templates = [f for f in os.listdir('templates') if f.endswith('.html')]
    print(f'Available templates: {templates}')
    
    print('Starting Flask server at http://localhost:5000')
    print('Game routes:')
    print('  / or /index.html - Solar Flare Escape')
    print('  /iss or /iss.html - ISS Magnetosphere Run') 
    print('  /heli or /heli.html - Helicopter Landing')
    
    # Run Flask development server
    app.run(debug=True, host='0.0.0.0', port=5000)