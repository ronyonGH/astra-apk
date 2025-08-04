#!/usr/bin/env python3
# build_apk.py - Build Astra Mobile APK with Buildozer
# Complete APK building process

import os
import sys
import subprocess
import shutil
import platform
from pathlib import Path

def print_banner():
    """Print build banner"""
    print("=" * 60)
    print("📱 ASTRA MOBILE APK BUILDER")
    print("=" * 60)
    print("🔨 Building Android APK with Buildozer")
    print("📦 Creating installable APK file")
    print("=" * 60)

def check_system():
    """Check system requirements"""
    print("🔍 Checking system requirements...")
    
    # Check OS
    system = platform.system().lower()
    if system not in ['linux', 'darwin']:
        print(f"⚠️ Warning: {system} detected. Buildozer works best on Linux/macOS")
    
    # Check Python
    if sys.version_info < (3, 6):
        print("❌ Python 3.6+ required")
        return False
    
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    
    # Check if we're in the right directory
    required_files = ['astra_mobile.py', 'buildozer.spec']
    missing_files = [f for f in required_files if not os.path.exists(f)]
    
    if missing_files:
        print(f"❌ Missing required files: {missing_files}")
        return False
    
    print("✅ Required files found")
    return True

def install_buildozer():
    """Install Buildozer if not available"""
    print("📦 Checking Buildozer installation...")
    
    try:
        result = subprocess.run(['buildozer', '--version'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Buildozer already installed")
            return True
    except FileNotFoundError:
        pass
    
    print("📦 Installing Buildozer...")
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'buildozer'], 
                      check=True)
        print("✅ Buildozer installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install Buildozer: {e}")
        return False

def setup_android_sdk():
    """Setup Android SDK and dependencies"""
    print("🔧 Setting up Android SDK...")
    
    # Check if ANDROID_HOME is set
    android_home = os.environ.get('ANDROID_HOME')
    if android_home:
        print(f"✅ ANDROID_HOME set to: {android_home}")
    else:
        print("⚠️ ANDROID_HOME not set (Buildozer will handle this)")
    
    # Check for Java
    try:
        result = subprocess.run(['java', '-version'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Java detected")
        else:
            print("⚠️ Java not found (Buildozer will install OpenJDK)")
    except FileNotFoundError:
        print("⚠️ Java not found (Buildozer will install OpenJDK)")

def create_app_icon():
    """Create a simple app icon if it doesn't exist"""
    print("🎨 Creating app icon...")
    
    if os.path.exists('icon.png'):
        print("✅ App icon already exists")
        return True
    
    try:
        # Create a simple icon using PIL if available
        try:
            from PIL import Image, ImageDraw, ImageFont
            
            # Create a 512x512 icon
            size = (512, 512)
            img = Image.new('RGBA', size, (0, 0, 0, 0))
            draw = ImageDraw.Draw(img)
            
            # Draw a simple icon (A for Astra)
            draw.ellipse([50, 50, 462, 462], fill=(0, 255, 0, 255))
            draw.text((256, 256), "A", fill=(0, 0, 0, 255), anchor="mm")
            
            img.save('icon.png')
            print("✅ Created app icon")
            return True
            
        except ImportError:
            print("⚠️ PIL not available, creating placeholder icon")
            # Create a simple text file as placeholder
            with open('icon.png', 'w') as f:
                f.write("Placeholder icon - replace with actual icon.png")
            return True
            
    except Exception as e:
        print(f"⚠️ Could not create icon: {e}")
        return False

def create_presplash():
    """Create a splash screen"""
    print("🎨 Creating splash screen...")
    
    if os.path.exists('presplash.png'):
        print("✅ Splash screen already exists")
        return True
    
    try:
        # Create a simple splash screen
        try:
            from PIL import Image, ImageDraw, ImageFont
            
            # Create a 512x512 splash screen
            size = (512, 512)
            img = Image.new('RGBA', size, (0, 0, 0, 255))
            draw = ImageDraw.Draw(img)
            
            # Draw Astra Mobile text
            draw.text((256, 256), "Astra\nMobile", fill=(0, 255, 0, 255), anchor="mm")
            
            img.save('presplash.png')
            print("✅ Created splash screen")
            return True
            
        except ImportError:
            print("⚠️ PIL not available, creating placeholder splash")
            with open('presplash.png', 'w') as f:
                f.write("Placeholder splash - replace with actual presplash.png")
            return True
            
    except Exception as e:
        print(f"⚠️ Could not create splash: {e}")
        return False

def clean_build():
    """Clean previous build artifacts"""
    print("🧹 Cleaning previous build...")
    
    dirs_to_clean = ['.buildozer', 'bin', 'dist']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            try:
                shutil.rmtree(dir_name)
                print(f"✅ Cleaned {dir_name}")
            except Exception as e:
                print(f"⚠️ Could not clean {dir_name}: {e}")

def build_apk():
    """Build the APK using Buildozer"""
    print("🔨 Building APK...")
    
    try:
        # Run buildozer android debug
        print("📱 Running: buildozer android debug")
        result = subprocess.run(['buildozer', 'android', 'debug'], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ APK build successful!")
            
            # Find the APK file
            apk_files = []
            for root, dirs, files in os.walk('.'):
                for file in files:
                    if file.endswith('.apk'):
                        apk_files.append(os.path.join(root, file))
            
            if apk_files:
                print(f"📦 APK files found:")
                for apk in apk_files:
                    size = os.path.getsize(apk) / (1024 * 1024)  # MB
                    print(f"   • {apk} ({size:.1f} MB)")
                
                # Copy to bin directory
                os.makedirs('bin', exist_ok=True)
                for apk in apk_files:
                    shutil.copy2(apk, 'bin/')
                    print(f"✅ Copied to bin/{os.path.basename(apk)}")
                
                return True
            else:
                print("⚠️ No APK files found")
                return False
        else:
            print("❌ APK build failed!")
            print("Error output:")
            print(result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ Build error: {e}")
        return False

def show_build_info():
    """Show build information"""
    print("\n" + "=" * 60)
    print("📱 ASTRA MOBILE APK BUILD COMPLETE!")
    print("=" * 60)
    
    # Check for APK files
    apk_files = []
    if os.path.exists('bin'):
        for file in os.listdir('bin'):
            if file.endswith('.apk'):
                apk_files.append(file)
    
    if apk_files:
        print(f"\n✅ APK files created:")
        for apk in apk_files:
            apk_path = os.path.join('bin', apk)
            size = os.path.getsize(apk_path) / (1024 * 1024)  # MB
            print(f"   📦 {apk} ({size:.1f} MB)")
        
        print(f"\n📱 Installation instructions:")
        print(f"1. Transfer APK to Android device")
        print(f"2. Enable 'Install from unknown sources'")
        print(f"3. Tap APK file to install")
        print(f"4. Launch Astra Mobile from app drawer")
        
        print(f"\n🔧 Build details:")
        print(f"   • Target: Android API 28+")
        print(f"   • Architecture: armeabi-v7a, arm64-v8a")
        print(f"   • Permissions: Internet, Storage")
        print(f"   • Features: Offline AI, Touch UI")
        
    else:
        print("❌ No APK files found")
        print("💡 Check the build output above for errors")
    
    print("\n" + "=" * 60)

def show_help():
    """Show build help"""
    print("""
🔨 ASTRA MOBILE APK BUILDER

Usage:
  python build_apk.py          # Build APK
  python build_apk.py --help   # Show this help

What this script does:
  • Checks system requirements
  • Installs Buildozer if needed
  • Sets up Android SDK
  • Creates app icon and splash
  • Cleans previous builds
  • Builds APK with Buildozer
  • Copies APK to bin/ directory

Requirements:
  • Linux/macOS (recommended)
  • Python 3.6+
  • Internet connection
  • 2GB+ free disk space

Examples:
  python build_apk.py
  python build_apk.py --help

After build:
  • APK files in bin/ directory
  • Transfer to Android device
  • Install and run
""")

def main():
    """Main build function"""
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        
        if arg in ['--help', '-h', 'help']:
            show_help()
            return
    
    print_banner()
    
    # Check system
    if not check_system():
        print("\n❌ System requirements not met")
        return False
    
    # Install Buildozer
    if not install_buildozer():
        print("\n❌ Could not install Buildozer")
        return False
    
    # Setup Android SDK
    setup_android_sdk()
    
    # Create assets
    create_app_icon()
    create_presplash()
    
    # Clean previous build
    clean_build()
    
    # Build APK
    if build_apk():
        show_build_info()
        print("\n🎉 APK build completed successfully!")
        return True
    else:
        print("\n❌ APK build failed!")
        print("💡 Check the error messages above")
        print("💡 Make sure all requirements are installed")
        return False

if __name__ == "__main__":
    try:
        success = main()
        if not success:
            print("\n❌ Build failed. Check the errors above.")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n⚠️ Build interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1) 