# 📱 Astra Mobile APK Build Guide - Windows

Complete guide to build Astra Mobile into a fully functional Android APK on Windows using Buildozer.

## ⚠️ Important Note

**Buildozer works best on Linux/macOS.** Windows support is limited and may require additional setup. For the best experience, consider:

1. **WSL (Windows Subsystem for Linux)** - Recommended
2. **Virtual Machine with Linux**
3. **Dual Boot with Linux**
4. **Cloud Build Service**

## 🚀 Quick Start (Windows)

### Option 1: WSL (Recommended)

#### 1. Install WSL
```powershell
# Open PowerShell as Administrator
wsl --install

# Restart computer, then open Ubuntu terminal
```

#### 2. Setup Ubuntu in WSL
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and dependencies
sudo apt install -y python3 python3-pip python3-venv
sudo apt install -y git zip unzip openjdk-8-jdk
sudo apt install -y autoconf libtool pkg-config zlib1g-dev
sudo apt install -y libncurses5-dev libncursesw5-dev libtinfo5 cmake
sudo apt install -y libffi-dev libssl-dev

# Install Buildozer
pip3 install buildozer
```

#### 3. Copy Files to WSL
```bash
# In WSL, navigate to your project
cd /mnt/c/Users/rishi/Downloads/astra

# Build APK
python3 build_apk.py
```

### Option 2: Windows Native (Limited Support)

#### 1. Install Python
```powershell
# Download Python from https://python.org
# Install with "Add to PATH" checked
```

#### 2. Install Buildozer
```powershell
pip install buildozer
```

#### 3. Install WSL for Android SDK
```powershell
# Buildozer will use WSL for Android tools
wsl --install Ubuntu
```

#### 4. Build APK
```powershell
python build_apk.py
```

## 🔧 Detailed Windows Setup

### Prerequisites

#### 1. Windows Requirements
- **Windows 10/11** (64-bit)
- **WSL2** (Windows Subsystem for Linux)
- **Python 3.6+**
- **Git for Windows**
- **8GB+ RAM** (recommended)
- **10GB+ free space**

#### 2. Install WSL2
```powershell
# Open PowerShell as Administrator
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

# Restart computer

# Install WSL
wsl --install

# Set WSL2 as default
wsl --set-default-version 2
```

#### 3. Install Ubuntu in WSL
```powershell
# Install Ubuntu from Microsoft Store
# Or use command:
wsl --install -d Ubuntu
```

### WSL Environment Setup

#### 1. Update Ubuntu
```bash
# In WSL Ubuntu terminal
sudo apt update && sudo apt upgrade -y
```

#### 2. Install Dependencies
```bash
# Install system packages
sudo apt install -y python3 python3-pip python3-venv
sudo apt install -y git zip unzip curl wget
sudo apt install -y openjdk-8-jdk openjdk-8-jre
sudo apt install -y autoconf automake libtool pkg-config
sudo apt install -y zlib1g-dev libncurses5-dev libncursesw5-dev
sudo apt install -y libtinfo5 cmake libffi-dev libssl-dev
sudo apt install -y build-essential

# Install additional Android dependencies
sudo apt install -y libltdl-dev libffi-dev libssl-dev
```

#### 3. Install Buildozer
```bash
# Install Buildozer
pip3 install buildozer

# Verify installation
buildozer --version
```

### Project Setup in WSL

#### 1. Access Windows Files
```bash
# Navigate to your Windows project directory
cd /mnt/c/Users/rishi/Downloads/astra

# List files to verify
ls -la
```

#### 2. Verify Required Files
```bash
# Check if all required files are present
ls -la *.py *.spec *.md
```

#### 3. Set Permissions
```bash
# Make scripts executable
chmod +x *.py
chmod +x buildozer.spec
```

## 🔨 Building the APK

### Step 1: Prepare Build Environment
```bash
# In WSL Ubuntu terminal
cd /mnt/c/Users/rishi/Downloads/astra

# Clean previous builds
buildozer clean

# Initialize Buildozer (if needed)
buildozer init
```

### Step 2: Build APK
```bash
# Build debug APK
buildozer android debug

# Or use the build script
python3 build_apk.py
```

### Step 3: Check Results
```bash
# Check for APK files
ls -la bin/

# Check build logs
cat .buildozer/logs/buildozer-*.log
```

## 📱 APK Features

### Android Configuration
- **Target API**: 28 (Android 9.0+)
- **Min API**: 21 (Android 5.0+)
- **Architecture**: armeabi-v7a, arm64-v8a
- **Orientation**: Portrait
- **Permissions**: Internet, Storage

### App Features
- **Offline AI**: Works without internet
- **Touch UI**: Mobile-optimized interface
- **Dark Theme**: Battery-friendly design
- **Chat History**: Persistent conversations
- **Math Calculator**: Simple calculations
- **Command System**: Built-in commands

## 🔍 Troubleshooting

### Common Windows Issues

#### 1. WSL Not Found
```powershell
# Install WSL
wsl --install

# Check WSL status
wsl --list --verbose
```

#### 2. Python Not Found in WSL
```bash
# Install Python in WSL
sudo apt update
sudo apt install python3 python3-pip
```

#### 3. Buildozer Not Found
```bash
# Install Buildozer in WSL
pip3 install buildozer

# Check installation
buildozer --version
```

#### 4. Java Not Found
```bash
# Install OpenJDK in WSL
sudo apt install openjdk-8-jdk

# Set JAVA_HOME
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
```

#### 5. Permission Denied
```bash
# Fix file permissions
chmod +x *.py
chmod +x buildozer.spec

# Clean and rebuild
buildozer clean
buildozer android debug
```

### Build Errors

#### "SDK not found"
```bash
# Buildozer will download SDK automatically
# If manual setup needed:
export ANDROID_HOME=$HOME/.buildozer/android/platform/android-sdk
export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools
```

#### "Gradle build failed"
```bash
# Check Java version
java -version

# Update Gradle wrapper
buildozer android clean
buildozer android debug
```

#### "Memory issues"
```bash
# Increase WSL memory limit
# Create .wslconfig in Windows user directory:
[wsl2]
memory=4GB
processors=4
```

### Performance Optimization

#### 1. WSL Performance
```powershell
# Create .wslconfig in C:\Users\[username]\
[wsl2]
memory=4GB
processors=4
swap=2GB
```

#### 2. Build Speed
```bash
# Use multiple cores
export ANDROID_NDK_HOME=$HOME/.buildozer/android/platform/android-ndk
export ANDROID_SDK_HOME=$HOME/.buildozer/android/platform/android-sdk

# Clean build
buildozer clean
buildozer android debug
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

### Transfer APK to Android

#### 1. Copy APK from WSL to Windows
```bash
# In WSL
cp bin/*.apk /mnt/c/Users/rishi/Downloads/
```

#### 2. Transfer to Android Device
- **USB**: Connect device and copy APK
- **Email**: Send APK to yourself
- **Cloud**: Upload to Google Drive/Dropbox
- **ADB**: Use Android Debug Bridge

#### 3. Install on Android
1. Enable "Unknown sources" in Settings
2. Tap APK file to install
3. Grant permissions when prompted
4. Launch Astra Mobile from app drawer

## 🔧 Advanced Configuration

### Customizing buildozer.spec

#### App Information
```ini
title = Astra Mobile
package.name = astramobile
package.domain = org.astra.mobile
version = 1.0.0
```

#### Requirements
```ini
requirements = python3,kivy>=2.1.0,requests>=2.28.0
```

#### Android Settings
```ini
android.api = 28
android.minapi = 21
android.arch = armeabi-v7a,arm64-v8a
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
```

### Debug Configuration
```ini
# Enable debug logging
log_level = 2
android.logcat_filters = *:S python:D

# Enable debug build
android.debug = True
```

## 🐛 Debugging

### View Build Logs
```bash
# Build logs
cat .buildozer/logs/buildozer-*.log

# Android logs (if device connected)
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

### Windows-Specific
- [WSL Documentation](https://docs.microsoft.com/en-us/windows/wsl/)
- [Windows Buildozer Guide](https://buildozer.readthedocs.io/en/latest/installation.html#windows)

### General Resources
- [Buildozer Documentation](https://buildozer.readthedocs.io/)
- [Kivy Documentation](https://kivy.org/doc/stable/)
- [Android Developer Guide](https://developer.android.com/)

### Community Support
- [Kivy Discord](https://discord.gg/kivy)
- [Buildozer GitHub](https://github.com/kivy/buildozer)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/buildozer)

## 🎯 Tips for Windows Users

### 1. Use WSL for Best Results
- Buildozer is designed for Linux
- WSL provides native Linux environment
- Better compatibility and performance

### 2. Keep WSL Updated
```bash
# Regular updates
sudo apt update && sudo apt upgrade -y
```

### 3. Monitor Resources
- WSL can use significant RAM/CPU
- Monitor with Task Manager
- Adjust .wslconfig as needed

### 4. Backup Important Files
- APK files are in bin/ directory
- Copy to Windows before closing WSL
- Keep build logs for troubleshooting

---

**Astra Mobile APK** - Ready for Android deployment on Windows! 🚀

*Built with Buildozer in WSL for optimal compatibility.* 