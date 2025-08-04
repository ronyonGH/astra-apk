# 📱 Astra Mobile APK Build Guide

Complete guide to build Astra Mobile into a fully functional Android APK using Buildozer.

## 🚀 Quick Start

### 1. Install Buildozer
```bash
pip install buildozer
```

### 2. Build APK
```bash
python build_apk.py
```

### 3. Install APK
- Transfer APK from `bin/` directory to Android device
- Enable "Install from unknown sources"
- Tap APK to install
- Launch Astra Mobile from app drawer

## 📋 Prerequisites

### System Requirements
- **OS**: Linux (recommended) or macOS
- **Python**: 3.6 or higher
- **RAM**: 4GB+ recommended
- **Storage**: 2GB+ free space
- **Internet**: Required for downloads

### Required Files
```
astra_mobile.py          # Main mobile app
mobile_main.py           # APK entry point
buildozer.spec           # Buildozer configuration
android_permissions.py   # Android permissions
build_apk.py            # Build script
```

## 🔧 Detailed Build Process

### Step 1: System Setup

#### Linux (Ubuntu/Debian)
```bash
# Install system dependencies
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

# Install Android SDK dependencies
sudo apt install -y libltdl-dev libffi-dev libssl-dev
```

#### macOS
```bash
# Install Homebrew if not installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install dependencies
brew install python3
brew install openjdk@8
brew install autoconf automake libtool pkg-config
```

### Step 2: Python Environment
```bash
# Create virtual environment
python3 -m venv astra_mobile_env
source astra_mobile_env/bin/activate  # Linux/macOS
# or
astra_mobile_env\Scripts\activate     # Windows

# Install Buildozer
pip install buildozer
```

### Step 3: Build Configuration

The `buildozer.spec` file is already configured with:
- **App Info**: Title, package name, version
- **Requirements**: Python3, Kivy, Requests
- **Android Settings**: API 28+, permissions, architecture
- **Build Settings**: Gradle dependencies, AAR files

### Step 4: Build APK

#### Automatic Build
```bash
# Run the build script
python build_apk.py
```

#### Manual Build
```bash
# Initialize Buildozer (if needed)
buildozer init

# Build debug APK
buildozer android debug

# Build release APK (signed)
buildozer android release
```

## 📱 APK Features

### Android Permissions
- **INTERNET**: For future online features
- **WRITE_EXTERNAL_STORAGE**: Save chat history
- **READ_EXTERNAL_STORAGE**: Read saved data

### App Configuration
- **Target API**: 28 (Android 9.0+)
- **Min API**: 21 (Android 5.0+)
- **Architecture**: armeabi-v7a, arm64-v8a
- **Orientation**: Portrait
- **Theme**: NoTitleBar (fullscreen)

### Build Settings
- **Gradle Dependencies**: WebKit for future features
- **AAR Files**: AndroidX libraries
- **Logging**: Level 2 (detailed)
- **Warnings**: Enabled

## 🔍 Troubleshooting

### Common Issues

#### 1. Buildozer Not Found
```bash
# Install Buildozer
pip install buildozer

# Check installation
buildozer --version
```

#### 2. Java Not Found
```bash
# Install OpenJDK
sudo apt install openjdk-8-jdk  # Ubuntu/Debian
brew install openjdk@8          # macOS

# Set JAVA_HOME
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
```

#### 3. Android SDK Issues
```bash
# Buildozer will download SDK automatically
# If manual setup needed:
export ANDROID_HOME=$HOME/.buildozer/android/platform/android-sdk
export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools
```

#### 4. Permission Denied
```bash
# Fix permissions
chmod +x build_apk.py
chmod +x mobile_main.py

# Clean and rebuild
buildozer clean
buildozer android debug
```

#### 5. Memory Issues
```bash
# Increase swap space (Linux)
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

### Build Errors

#### "SDK not found"
```bash
# Clean and rebuild
buildozer clean
buildozer android debug
```

#### "Gradle build failed"
```bash
# Check Java version
java -version

# Update Gradle wrapper
buildozer android clean
buildozer android debug
```

#### "Permission denied"
```bash
# Fix file permissions
chmod +x *.py
chmod +x buildozer.spec
```

## 📊 Build Output

### Successful Build
```
✅ APK build successful!
📦 APK files found:
   • astramobile-1.0.0-debug.apk (15.2 MB)
✅ Copied to bin/astramobile-1.0.0-debug.apk
```

### File Locations
- **APK**: `bin/astramobile-1.0.0-debug.apk`
- **Build Logs**: `.buildozer/logs/`
- **Cache**: `.buildozer/android/platform/`

## 📱 Installation Guide

### On Android Device

1. **Enable Unknown Sources**
   - Go to Settings → Security
   - Enable "Unknown sources"

2. **Transfer APK**
   - Copy APK from `bin/` to device
   - Use USB, email, or cloud storage

3. **Install APK**
   - Tap APK file
   - Follow installation prompts
   - Grant permissions when asked

4. **Launch App**
   - Find "Astra Mobile" in app drawer
   - Tap to launch
   - Grant permissions if prompted

### Testing Installation

1. **Basic Functionality**
   - App launches without errors
   - Chat interface loads
   - Can send messages
   - Receives responses

2. **Permissions**
   - Internet access works
   - Storage access granted
   - No permission errors

3. **Performance**
   - Fast startup (<5 seconds)
   - Smooth UI interactions
   - No crashes or freezes

## 🔧 Advanced Configuration

### Customizing buildozer.spec

#### App Information
```ini
title = Your App Name
package.name = yourpackagename
package.domain = com.yourcompany.app
version = 1.0.0
```

#### Requirements
```ini
requirements = python3,kivy>=2.1.0,requests>=2.28.0,your_package
```

#### Android Settings
```ini
android.api = 30
android.minapi = 21
android.arch = armeabi-v7a,arm64-v8a,x86
android.permissions = INTERNET,CAMERA,MICROPHONE
```

#### Build Options
```ini
android.release_artifact = apk
android.debug = True
android.allow_backup = True
```

### Signing APK

#### Debug Signing (Automatic)
```bash
buildozer android debug
```

#### Release Signing
```bash
# Create keystore
keytool -genkey -v -keystore my-release-key.keystore -alias alias_name -keyalg RSA -keysize 2048 -validity 10000

# Configure buildozer.spec
android.keystore = my-release-key.keystore
android.keyalias = alias_name

# Build release APK
buildozer android release
```

## 📈 Performance Optimization

### APK Size Reduction
```ini
# In buildozer.spec
android.arch = armeabi-v7a  # Single architecture
source.exclude_patterns = *.pyc,*.pyo,__pycache__
android.allow_backup = False
```

### Build Speed
```bash
# Use multiple cores
export ANDROID_NDK_HOME=$HOME/.buildozer/android/platform/android-ndk
export ANDROID_SDK_HOME=$HOME/.buildozer/android/platform/android-sdk

# Clean build
buildozer clean
buildozer android debug
```

### Memory Optimization
```python
# In astra_mobile.py
import gc
gc.collect()  # Force garbage collection
```

## 🐛 Debugging

### Enable Debug Logging
```ini
# In buildozer.spec
log_level = 2
android.logcat_filters = *:S python:D
```

### View Logs
```bash
# Build logs
cat .buildozer/logs/buildozer-*.log

# Android logs
adb logcat | grep python
```

### Common Debug Commands
```bash
# Check buildozer version
buildozer --version

# List targets
buildozer targets

# Clean build
buildozer clean

# Update dependencies
buildozer android update
```

## 📚 Resources

### Official Documentation
- [Buildozer Documentation](https://buildozer.readthedocs.io/)
- [Kivy Documentation](https://kivy.org/doc/stable/)
- [Android Developer Guide](https://developer.android.com/)

### Community Support
- [Kivy Discord](https://discord.gg/kivy)
- [Buildozer GitHub](https://github.com/kivy/buildozer)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/buildozer)

### Troubleshooting Links
- [Common Buildozer Issues](https://github.com/kivy/buildozer/issues)
- [Android SDK Setup](https://developer.android.com/studio)
- [Gradle Issues](https://gradle.org/docs/)

---

**Astra Mobile APK** - Ready for Android deployment! 🚀

*Built with Buildozer for optimal mobile performance.* 