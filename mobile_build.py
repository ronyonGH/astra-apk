#!/usr/bin/env python3
# mobile_build.py - Astra Mobile Build Script
# Builds the mobile app for different platforms

import os
import sys
import shutil
import subprocess
from pathlib import Path

def check_build_requirements():
    """Check if build requirements are met"""
    print("🔍 Checking build requirements...")
    
    # Check Python version
    if sys.version_info < (3, 6):
        print("❌ Python 3.6+ required")
        return False
    
    # Check Kivy
    try:
        import kivy
        print("✅ Kivy available")
    except ImportError:
        print("❌ Kivy not available")
        return False
    
    # Check build tools
    build_tools = {
        'buildozer': 'buildozer',
        'kivy-ios': 'kivy-ios',
        'kivy-sdk': 'kivy-sdk'
    }
    
    for tool, command in build_tools.items():
        try:
            subprocess.run([command, '--version'], capture_output=True, check=True)
            print(f"✅ {tool} available")
        except (subprocess.CalledProcessError, FileNotFoundError):
            print(f"⚠️ {tool} not found (optional)")
    
    return True

def create_buildozer_spec():
    """Create buildozer.spec for Android build"""
    spec_content = """[app]
title = Astra Mobile
package.name = astramobile
package.domain = org.astra.mobile
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 28
android.minapi = 21
android.ndk = 23b
android.sdk = 28
android.arch = armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
"""
    
    with open('buildozer.spec', 'w') as f:
        f.write(spec_content)
    
    print("✅ Created buildozer.spec")

def create_ios_config():
    """Create iOS build configuration"""
    config_content = """# iOS build configuration for Astra Mobile
# Run: kivy-ios build astra_mobile.py

# Requirements
requirements = kivy

# App settings
app_name = Astra Mobile
app_version = 1.0.0
app_identifier = org.astra.mobile

# Build settings
ios_deployment_target = 10.0
ios_arch = arm64
"""
    
    with open('ios_config.txt', 'w') as f:
        f.write(config_content)
    
    print("✅ Created iOS configuration")

def build_android():
    """Build Android APK"""
    print("📱 Building Android APK...")
    
    try:
        # Create buildozer.spec if it doesn't exist
        if not os.path.exists('buildozer.spec'):
            create_buildozer_spec()
        
        # Run buildozer
        result = subprocess.run(['buildozer', 'android', 'debug'], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Android build successful!")
            print("📦 APK should be in bin/ directory")
        else:
            print("❌ Android build failed:")
            print(result.stderr)
            
    except FileNotFoundError:
        print("❌ buildozer not found")
        print("💡 Install with: pip install buildozer")
    except Exception as e:
        print(f"❌ Build error: {e}")

def build_ios():
    """Build iOS app"""
    print("🍎 Building iOS app...")
    
    try:
        # Check if kivy-ios is available
        result = subprocess.run(['kivy-ios', '--version'], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ kivy-ios available")
            
            # Create iOS project
            subprocess.run(['kivy-ios', 'create', 'AstraMobile', 'astra_mobile.py'])
            print("✅ iOS project created")
            
            # Build iOS app
            subprocess.run(['kivy-ios', 'build', 'astra_mobile.py'])
            print("✅ iOS build completed")
            
        else:
            print("❌ kivy-ios not available")
            print("💡 Install with: pip install kivy-ios")
            
    except FileNotFoundError:
        print("❌ kivy-ios not found")
        print("💡 Install with: pip install kivy-ios")
    except Exception as e:
        print(f"❌ iOS build error: {e}")

def build_desktop():
    """Build desktop executable"""
    print("🖥️ Building desktop executable...")
    
    try:
        # Use PyInstaller if available
        result = subprocess.run(['pyinstaller', '--version'], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ PyInstaller available")
            
            # Create spec file
            spec_content = """# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['mobile_launcher.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=['kivy'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='AstraMobile',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          argv_emulation=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
"""
            
            with open('AstraMobile.spec', 'w') as f:
                f.write(spec_content)
            
            # Build executable
            subprocess.run(['pyinstaller', 'AstraMobile.spec'])
            print("✅ Desktop build successful!")
            print("📦 Executable should be in dist/ directory")
            
        else:
            print("❌ PyInstaller not available")
            print("💡 Install with: pip install pyinstaller")
            
    except FileNotFoundError:
        print("❌ PyInstaller not found")
        print("💡 Install with: pip install pyinstaller")
    except Exception as e:
        print(f"❌ Desktop build error: {e}")

def create_mobile_package():
    """Create a mobile package with all necessary files"""
    print("📦 Creating mobile package...")
    
    # Create mobile directory
    mobile_dir = Path("astra_mobile_package")
    mobile_dir.mkdir(exist_ok=True)
    
    # Copy necessary files
    files_to_copy = [
        'astra_mobile.py',
        'mobile_launcher.py',
        'mobile_requirements.txt',
        'mobile_build.py'
    ]
    
    for file in files_to_copy:
        if os.path.exists(file):
            shutil.copy2(file, mobile_dir)
            print(f"✅ Copied {file}")
    
    # Create README for mobile package
    readme_content = """# Astra Mobile Package

📱 Lightweight AI Assistant for Mobile Devices

## Quick Start

1. Install requirements:
   ```
   pip install -r mobile_requirements.txt
   ```

2. Run the app:
   ```
   python mobile_launcher.py
   ```

## Features

- 🔋 Battery optimized
- 💾 Low memory usage
- 📡 Works offline
- ⚡ Fast startup
- 📱 Mobile friendly UI

## Building

### Android
```
python mobile_build.py android
```

### iOS
```
python mobile_build.py ios
```

### Desktop
```
python mobile_build.py desktop
```

## Requirements

- Python 3.6+
- Kivy 2.1.0+

## Support

See the main Astra project for more information.
"""
    
    with open(mobile_dir / "README.md", 'w') as f:
        f.write(readme_content)
    
    print("✅ Mobile package created in astra_mobile_package/")

def show_help():
    """Show build help"""
    print("""
🔨 ASTRA MOBILE BUILD SCRIPT

Usage:
  python mobile_build.py [platform]

Platforms:
  android    - Build Android APK
  ios        - Build iOS app
  desktop    - Build desktop executable
  package    - Create mobile package
  all        - Build for all platforms

Examples:
  python mobile_build.py android
  python mobile_build.py ios
  python mobile_build.py desktop
  python mobile_build.py package
  python mobile_build.py all

Requirements:
  • Python 3.6+
  • Kivy 2.1.0+
  • buildozer (for Android)
  • kivy-ios (for iOS)
  • pyinstaller (for desktop)

Installation:
  pip install buildozer kivy-ios pyinstaller
""")

def main():
    """Main build function"""
    if len(sys.argv) < 2:
        show_help()
        return
    
    platform = sys.argv[1].lower()
    
    # Check requirements first
    if not check_build_requirements():
        print("❌ Build requirements not met")
        return
    
    if platform == 'android':
        build_android()
    elif platform == 'ios':
        build_ios()
    elif platform == 'desktop':
        build_desktop()
    elif platform == 'package':
        create_mobile_package()
    elif platform == 'all':
        print("🔨 Building for all platforms...")
        create_mobile_package()
        build_android()
        build_ios()
        build_desktop()
    elif platform in ['help', '--help', '-h']:
        show_help()
    else:
        print(f"❌ Unknown platform: {platform}")
        show_help()

if __name__ == "__main__":
    main() 