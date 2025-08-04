#!/usr/bin/env python3
# install_mobile.py - Astra Mobile Installation Script
# Easy setup for the mobile version

import os
import sys
import subprocess
import platform
from pathlib import Path

def print_banner():
    """Print installation banner"""
    print("=" * 60)
    print("📱 ASTRA MOBILE INSTALLATION")
    print("=" * 60)
    print("🤖 Lightweight AI Assistant for Mobile Devices")
    print("🔋 Battery Optimized • 💾 Low Memory • ⚡ Fast")
    print("=" * 60)

def check_python_version():
    """Check if Python version is compatible"""
    print("🔍 Checking Python version...")
    
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 6):
        print(f"❌ Python {version.major}.{version.minor} detected")
        print("💡 Python 3.6+ is required")
        return False
    
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} detected")
    return True

def check_pip():
    """Check if pip is available"""
    print("🔍 Checking pip...")
    
    try:
        subprocess.run([sys.executable, "-m", "pip", "--version"], 
                      capture_output=True, check=True)
        print("✅ pip is available")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ pip not found")
        print("💡 Install pip first")
        return False

def install_kivy():
    """Install Kivy framework"""
    print("📦 Installing Kivy...")
    
    try:
        # Try to install Kivy
        result = subprocess.run([
            sys.executable, "-m", "pip", "install", "kivy>=2.1.0"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Kivy installed successfully")
            return True
        else:
            print("❌ Kivy installation failed")
            print("Error:", result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ Kivy installation error: {e}")
        return False

def install_optional_deps():
    """Install optional dependencies"""
    print("📦 Installing optional dependencies...")
    
    optional_deps = [
        "requests>=2.28.0",
        "psutil>=5.8.0"
    ]
    
    installed = 0
    total = len(optional_deps)
    
    for dep in optional_deps:
        try:
            print(f"Installing {dep}...")
            result = subprocess.run([
                sys.executable, "-m", "pip", "install", dep
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"✅ {dep} installed")
                installed += 1
            else:
                print(f"⚠️ {dep} failed (optional)")
                
        except Exception as e:
            print(f"⚠️ {dep} error (optional): {e}")
    
    print(f"📊 Optional dependencies: {installed}/{total} installed")
    return True

def check_mobile_files():
    """Check if mobile files are present"""
    print("📁 Checking mobile files...")
    
    required_files = [
        'astra_mobile.py',
        'mobile_launcher.py',
        'mobile_requirements.txt',
        'mobile_build.py',
        'README_MOBILE.md'
    ]
    
    missing_files = []
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file} found")
        else:
            print(f"❌ {file} missing")
            missing_files.append(file)
    
    if missing_files:
        print(f"⚠️ Missing files: {', '.join(missing_files)}")
        print("💡 Make sure all mobile files are in the current directory")
        return False
    
    return True

def test_installation():
    """Test the installation"""
    print("🧪 Testing installation...")
    
    try:
        # Test Kivy import
        import kivy
        print("✅ Kivy import successful")
        
        # Test mobile app import
        from astra_mobile import AstraMobileApp
        print("✅ Astra Mobile import successful")
        
        # Test basic functionality
        from astra_mobile import process_mobile_query
        response = process_mobile_query("hello")
        if response:
            print("✅ Query processing works")
        else:
            print("❌ Query processing failed")
            return False
        
        return True
        
    except ImportError as e:
        print(f"❌ Import test failed: {e}")
        return False
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def create_shortcuts():
    """Create shortcut scripts"""
    print("🔗 Creating shortcuts...")
    
    # Create run script
    run_script = """#!/usr/bin/env python3
# Run Astra Mobile
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mobile_launcher import main
if __name__ == "__main__":
    main()
"""
    
    try:
        with open('run_astra_mobile.py', 'w') as f:
            f.write(run_script)
        print("✅ Created run_astra_mobile.py")
    except Exception as e:
        print(f"⚠️ Could not create run script: {e}")
    
    # Create test script
    test_script = """#!/usr/bin/env python3
# Test Astra Mobile
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from test_mobile import main
if __name__ == "__main__":
    main()
"""
    
    try:
        with open('test_astra_mobile.py', 'w') as f:
            f.write(test_script)
        print("✅ Created test_astra_mobile.py")
    except Exception as e:
        print(f"⚠️ Could not create test script: {e}")

def show_usage():
    """Show usage instructions"""
    print("\n" + "=" * 60)
    print("🚀 ASTRA MOBILE INSTALLATION COMPLETE!")
    print("=" * 60)
    
    print("\n📱 How to use Astra Mobile:")
    print("1. Run the app:")
    print("   python mobile_launcher.py")
    print("   python run_astra_mobile.py")
    
    print("\n2. Test the installation:")
    print("   python test_mobile.py")
    print("   python test_astra_mobile.py")
    
    print("\n3. Build for mobile platforms:")
    print("   python mobile_build.py android")
    print("   python mobile_build.py ios")
    print("   python mobile_build.py desktop")
    
    print("\n4. Get help:")
    print("   python mobile_launcher.py --help")
    print("   python test_mobile.py --help")
    
    print("\n📚 Documentation:")
    print("   README_MOBILE.md - Complete documentation")
    print("   mobile_requirements.txt - Dependencies")
    
    print("\n🔧 Troubleshooting:")
    print("   • Check Python version: python --version")
    print("   • Check Kivy: python -c 'import kivy'")
    print("   • Run tests: python test_mobile.py")
    print("   • Reinstall: python install_mobile.py")
    
    print("\n" + "=" * 60)

def show_help():
    """Show installation help"""
    print("""
📱 ASTRA MOBILE INSTALLATION

Usage:
  python install_mobile.py          # Install Astra Mobile
  python install_mobile.py --help   # Show this help

What this script does:
  • Checks Python version (3.6+)
  • Installs Kivy framework
  • Installs optional dependencies
  • Verifies mobile files
  • Tests the installation
  • Creates shortcut scripts

Requirements:
  • Python 3.6+
  • Internet connection (for downloads)
  • Write permissions in current directory

Examples:
  python install_mobile.py
  python install_mobile.py --help

After installation:
  python mobile_launcher.py
  python test_mobile.py
""")

def main():
    """Main installation function"""
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        
        if arg in ['--help', '-h', 'help']:
            show_help()
            return
    
    print_banner()
    
    # Check system requirements
    if not check_python_version():
        print("\n❌ Installation failed: Python version incompatible")
        return False
    
    if not check_pip():
        print("\n❌ Installation failed: pip not available")
        return False
    
    # Install dependencies
    if not install_kivy():
        print("\n❌ Installation failed: Could not install Kivy")
        return False
    
    install_optional_deps()
    
    # Check files
    if not check_mobile_files():
        print("\n❌ Installation failed: Missing mobile files")
        return False
    
    # Test installation
    if not test_installation():
        print("\n❌ Installation failed: Tests failed")
        return False
    
    # Create shortcuts
    create_shortcuts()
    
    # Show usage
    show_usage()
    
    print("\n🎉 Astra Mobile installation completed successfully!")
    return True

if __name__ == "__main__":
    try:
        success = main()
        if not success:
            print("\n❌ Installation failed. Check the errors above.")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n⚠️ Installation interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1) 