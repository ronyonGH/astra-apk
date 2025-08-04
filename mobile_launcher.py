#!/usr/bin/env python3
# mobile_launcher.py - Astra Mobile Launcher
# Simple launcher for mobile version with error handling

import sys
import os
import traceback
from datetime import datetime

def check_mobile_requirements():
    """Check if mobile requirements are met"""
    try:
        import kivy
        print("✅ Kivy available")
        return True
    except ImportError:
        print("❌ Kivy not available. Install with: pip install kivy")
        return False

def show_mobile_info():
    """Show mobile app information"""
    print("=" * 50)
    print("📱 ASTRA MOBILE")
    print("=" * 50)
    print("🤖 Lightweight AI Assistant")
    print("📱 Optimized for low-end smartphones")
    print("🔋 Battery friendly")
    print("💾 Low memory usage")
    print("📡 Works offline")
    print("⚡ Fast startup")
    print("=" * 50)

def launch_mobile_app():
    """Launch the mobile app"""
    try:
        show_mobile_info()
        
        # Check requirements
        if not check_mobile_requirements():
            print("\n❌ Requirements not met. Please install missing packages.")
            return False
        
        print("\n🚀 Starting Astra Mobile...")
        
        # Import and run mobile app
        from astra_mobile import AstraMobileApp
        
        app = AstraMobileApp()
        app.run()
        
        return True
        
    except ImportError as e:
        print(f"\n❌ Import error: {e}")
        print("💡 Make sure all required files are present:")
        print("   - astra_mobile.py")
        print("   - mobile_requirements.txt")
        return False
        
    except Exception as e:
        print(f"\n❌ Error launching Astra Mobile: {e}")
        print("\n📋 Error details:")
        traceback.print_exc()
        return False

def show_help():
    """Show help information"""
    print("""
📱 ASTRA MOBILE - HELP

Usage:
  python mobile_launcher.py          # Launch mobile app
  python mobile_launcher.py --help   # Show this help
  python mobile_launcher.py --info   # Show app info

Features:
  • Lightweight AI assistant
  • Optimized for mobile devices
  • Works offline
  • Battery friendly
  • Low memory usage
  • Fast startup

Requirements:
  • Python 3.6+
  • Kivy 2.1.0+

Installation:
  pip install -r mobile_requirements.txt

For more information, see README.md
""")

def show_info():
    """Show detailed app information"""
    print("""
📱 ASTRA MOBILE - INFORMATION

Version: 1.0.0
Type: Lightweight AI Assistant
Platform: Mobile (Android/iOS/Desktop)
Architecture: Offline-first

Key Features:
  • 🔋 Battery Optimized
  • 💾 Low Memory Usage
  • 📡 Offline Operation
  • ⚡ Fast Startup
  • 📱 Mobile Friendly UI
  • 🧮 Simple Math
  • ⏰ Time & Date
  • 📝 Chat History

Technical Details:
  • Framework: Kivy
  • Language: Python
  • AI: Lightweight offline responses
  • Storage: Minimal local storage
  • Network: Optional (offline-first)

Performance:
  • Startup: < 2 seconds
  • Memory: < 50MB
  • Battery: Minimal impact
  • CPU: Low usage

Compatibility:
  • Android 5.0+
  • iOS 10.0+
  • Windows 10+
  • Linux (desktop)
  • macOS 10.12+

For support, see the main Astra project.
""")

def main():
    """Main launcher function"""
    # Check command line arguments
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        
        if arg in ['--help', '-h', 'help']:
            show_help()
            return
        
        elif arg in ['--info', '-i', 'info']:
            show_info()
            return
        
        else:
            print(f"❌ Unknown argument: {arg}")
            print("💡 Use --help for available options")
            return
    
    # Launch the app
    success = launch_mobile_app()
    
    if not success:
        print("\n❌ Failed to launch Astra Mobile")
        print("💡 Check the error messages above")
        print("💡 Make sure all requirements are installed")
        print("💡 Try: pip install -r mobile_requirements.txt")
        
        # Wait for user input before exiting
        try:
            input("\nPress Enter to exit...")
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    main() 