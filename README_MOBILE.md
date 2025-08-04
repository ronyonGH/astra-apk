# 📱 Astra Mobile - Lightweight AI Assistant

A mobile-optimized version of Astra AI Assistant designed specifically for low-end smartphones. Built with performance and battery life in mind.

## 🚀 Features

### Core Features
- **🤖 Lightweight AI**: Offline-first AI assistant
- **🔋 Battery Optimized**: Minimal battery usage
- **💾 Low Memory**: Uses less than 50MB RAM
- **⚡ Fast Startup**: Starts in under 2 seconds
- **📡 Offline Operation**: Works without internet
- **📱 Mobile UI**: Touch-friendly interface

### AI Capabilities
- **🧮 Math Calculations**: Simple arithmetic operations
- **⏰ Time & Date**: Current time and date
- **📝 Chat History**: Persistent conversation history
- **🔍 Smart Responses**: Context-aware replies
- **📋 Commands**: Built-in command system

### Mobile Optimizations
- **🎨 Dark Theme**: Easy on the eyes
- **📱 Touch Friendly**: Large buttons and text
- **🔄 Smooth Scrolling**: Optimized chat interface
- **⚙️ Settings Screen**: App configuration
- **📊 Status Display**: Real-time app status

## 📋 Requirements

### Minimum Requirements
- **Python**: 3.6 or higher
- **Kivy**: 2.1.0 or higher
- **RAM**: 50MB available
- **Storage**: 10MB free space

### Optional Dependencies
- **requests**: For future online features
- **psutil**: For system monitoring

## 🛠️ Installation

### Quick Install
```bash
# Clone or download the mobile files
# Install requirements
pip install -r mobile_requirements.txt

# Run the app
python mobile_launcher.py
```

### Manual Install
```bash
# Install Kivy
pip install kivy>=2.1.0

# Run directly
python astra_mobile.py
```

## 🚀 Usage

### Starting the App
```bash
# Using launcher (recommended)
python mobile_launcher.py

# Direct launch
python astra_mobile.py

# With help
python mobile_launcher.py --help
```

### Basic Commands
- **Hello**: Get a greeting
- **What time is it?**: Current time
- **Calculate 15 + 23**: Math operations
- **Help**: Show help information
- **/status**: App status
- **/clear**: Clear chat

### Mobile Commands
- **/help**: Show all commands
- **/time**: Current time
- **/date**: Current date
- **/status**: App status
- **/clear**: Clear chat
- **/battery**: Battery info
- **/memory**: Memory usage
- **/offline**: Offline status

## 📱 Building for Mobile

### Android Build
```bash
# Install buildozer
pip install buildozer

# Build Android APK
python mobile_build.py android
```

### iOS Build
```bash
# Install kivy-ios
pip install kivy-ios

# Build iOS app
python mobile_build.py ios
```

### Desktop Build
```bash
# Install pyinstaller
pip install pyinstaller

# Build desktop executable
python mobile_build.py desktop
```

### All Platforms
```bash
# Build for all platforms
python mobile_build.py all
```

## 🏗️ Architecture

### File Structure
```
astra_mobile/
├── astra_mobile.py          # Main mobile app
├── mobile_launcher.py       # Launcher script
├── mobile_requirements.txt  # Lightweight requirements
├── mobile_build.py          # Build script
├── README_MOBILE.md         # This file
└── astra_mobile_package/    # Mobile package
```

### Key Components
- **AstraMobileApp**: Main application class
- **MobileChatScreen**: Chat interface
- **MobileSettingsScreen**: Settings interface
- **process_mobile_query()**: Query processor
- **OFFLINE_RESPONSES**: Response database

### Performance Optimizations
- **Minimal Imports**: Only essential modules
- **Lightweight UI**: Simple, fast interface
- **Offline AI**: No heavy models
- **Memory Management**: Efficient resource usage
- **Battery Optimization**: Minimal CPU usage

## 🔧 Configuration

### Mobile Settings
- **Battery Saver**: Enabled by default
- **Low Memory Mode**: Enabled by default
- **Offline Mode**: Primary operation mode
- **Dark Theme**: Default interface

### Performance Tuning
```python
# In astra_mobile.py
MOBILE_MODE = True
LOW_MEMORY_MODE = True
BATTERY_SAVER = True
```

## 📊 Performance Metrics

### Memory Usage
- **Startup**: ~20MB
- **Running**: ~30-50MB
- **Peak**: <100MB

### Battery Impact
- **Idle**: Minimal
- **Active**: Low
- **Background**: None

### Startup Time
- **Cold Start**: <2 seconds
- **Warm Start**: <1 second
- **Hot Start**: <0.5 seconds

## 🐛 Troubleshooting

### Common Issues

#### App Won't Start
```bash
# Check Python version
python --version

# Check Kivy installation
python -c "import kivy; print('Kivy OK')"

# Reinstall requirements
pip install -r mobile_requirements.txt
```

#### Performance Issues
- Close other apps
- Restart the device
- Check available memory
- Update to latest version

#### Build Issues
```bash
# Android build fails
pip install buildozer
buildozer init

# iOS build fails
pip install kivy-ios
kivy-ios --version

# Desktop build fails
pip install pyinstaller
pyinstaller --version
```

### Error Messages

#### "Kivy not available"
```bash
pip install kivy>=2.1.0
```

#### "Module not found"
```bash
pip install -r mobile_requirements.txt
```

#### "Build failed"
- Check build tools installation
- Ensure sufficient disk space
- Verify platform-specific requirements

## 🔄 Updates

### Version History
- **v1.0.0**: Initial mobile release
  - Basic AI functionality
  - Mobile-optimized UI
  - Offline operation
  - Battery optimization

### Upcoming Features
- **Online Mode**: Optional internet features
- **Voice Input**: Speech recognition
- **Custom Themes**: Multiple UI themes
- **Data Export**: Chat history export
- **Widgets**: Home screen widgets

## 🤝 Contributing

### Development Setup
```bash
# Clone repository
git clone <repository-url>

# Install development requirements
pip install -r mobile_requirements.txt

# Run in development mode
python mobile_launcher.py
```

### Code Style
- Follow PEP 8
- Use descriptive variable names
- Add docstrings to functions
- Keep functions small and focused

### Testing
```bash
# Run basic tests
python -c "import astra_mobile; print('Import OK')"

# Test launcher
python mobile_launcher.py --help

# Test build
python mobile_build.py package
```

## 📄 License

This project is part of the Astra AI Assistant project. See the main project for license information.

## 🆘 Support

### Getting Help
1. Check this README
2. Look at error messages
3. Try the troubleshooting section
4. Check the main Astra project

### Reporting Issues
- Include error messages
- Specify your platform
- Describe the steps to reproduce
- Include system information

### Feature Requests
- Check if it's already planned
- Consider mobile constraints
- Focus on lightweight solutions
- Prioritize offline functionality

## 🎯 Roadmap

### Short Term (v1.1)
- [ ] Voice input support
- [ ] Custom themes
- [ ] Data export
- [ ] Widget support

### Medium Term (v1.2)
- [ ] Online mode
- [ ] Cloud sync
- [ ] Advanced AI features
- [ ] Plugin system

### Long Term (v2.0)
- [ ] Full AI capabilities
- [ ] Multi-language support
- [ ] Advanced customization
- [ ] Enterprise features

---

**Astra Mobile** - Lightweight AI for Mobile Devices 🚀

*Optimized for performance, designed for simplicity.* 