# NASA Solar Storm Games - Flask Edition

A collection of educational games about solar storms and space exploration, now running on Flask!

## 🎮 Games Included

1. **Solar Flare Escape** (`/`) - Break free from the Sun's gravitational pull during a massive solar flare
2. **ISS Magnetosphere Run** (`/iss`) - Protect the International Space Station by collecting comets and avoiding meteors
3. **Helicopter Emergency Landing** (`/heli`) - Navigate through solar storm effects and bird hazards to make an emergency landing

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone or download this repository**
   ```bash
   cd nasa
   ```

2. **Install Flask and dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask application**
   ```bash
   python app.py
   ```

4. **Open your browser and visit**
   ```
   http://localhost:5000
   ```

## 📁 Project Structure

```
nasa/
├── app.py                 # Flask application main file
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/            # HTML templates
│   ├── index.html       # Solar flare escape game
│   ├── iss.html         # ISS magnetosphere game
│   ├── heli.html        # Helicopter landing game
│   ├── 404.html         # Error page
│   └── 500.html         # Server error page
└── static/              # Static files
    └── resources/       # Game assets (audio, images)
        ├── *.mp3        # Audio files
        ├── *.ogg        # Audio files
        └── *.png        # Sprite images
```

## 🎯 Game Routes

- `/` - Solar Flare Escape (main game)
- `/iss` - ISS Magnetosphere Run
- `/heli` - Helicopter Emergency Landing

## 🔧 Development

### Running in Development Mode
The Flask app runs in debug mode by default, which includes:
- Auto-reload on file changes
- Detailed error messages
- Debug toolbar

### Configuration
The Flask app is configured to:
- Run on `0.0.0.0:5000` (accessible from network)
- Serve static files from `/static/` directory
- Use Jinja2 templates from `/templates/` directory

## 🎵 Audio Files

The games include immersive audio:
- Background music and ambient sounds
- Voice acting for dialogue sequences  
- Sound effects for interactions

Make sure your browser allows audio autoplay or click to enable audio when prompted.

## 🌟 Features

- **Educational Content**: Learn about solar storms, magnetosphere protection, and emergency procedures
- **Progressive Gameplay**: Three interconnected games that tell a complete story
- **Responsive Design**: Works on desktop and mobile browsers
- **Audio Integration**: Full voice acting and sound effects
- **Visual Effects**: Dynamic graphics and particle systems

## 🚨 Troubleshooting

### Common Issues

**Audio not playing:**
- Make sure your browser allows audio autoplay
- Click anywhere on the page to enable audio context
- Check browser console for audio loading errors

**Images not loading:**
- Ensure all files in `static/resources/` are present
- Check Flask console for 404 errors on static files

**Flask won't start:**
- Make sure you have Python 3.7+ installed
- Install dependencies: `pip install -r requirements.txt`
- Check that port 5000 is available

## 📝 License

This project is for educational purposes. All audio and visual assets are used with permission or under fair use.

## 🎓 Educational Value

These games teach:
- **Solar Physics**: How solar flares and coronal mass ejections work
- **Space Safety**: Emergency protocols for spacecraft and astronauts  
- **Magnetosphere Science**: How Earth's magnetic field protects us
- **Problem Solving**: Quick decision making under pressure