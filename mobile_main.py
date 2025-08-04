#!/usr/bin/env python3
# mobile_main.py - Main entry point for Astra Mobile APK
# Optimized for Android build with Buildozer

import os
import sys
from kivy.app import App
from kivy.core.window import Window
from kivy.utils import platform

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import mobile app
from astra_mobile import AstraMobileApp

def main():
    """Main entry point for mobile app"""
    try:
        # Set mobile-specific window properties
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.INTERNET, Permission.WRITE_EXTERNAL_STORAGE])
            
            # Set Android-specific window properties
            Window.softinput_mode = 'below_target'
            Window.clearcolor = (0, 0, 0, 1)
        
        # Create and run the app
        app = AstraMobileApp()
        app.run()
        
    except Exception as e:
        print(f"Error starting Astra Mobile: {e}")
        import traceback
        traceback.print_exc()
        
        # Show error screen
        from kivy.uix.label import Label
        from kivy.uix.boxlayout import BoxLayout
        from kivy.app import App
        
        class ErrorApp(App):
            def build(self):
                layout = BoxLayout(orientation='vertical', padding=20)
                error_label = Label(
                    text=f"Astra Mobile Error:\n{str(e)}",
                    color=(1, 0, 0, 1),
                    size_hint=(1, 1)
                )
                layout.add_widget(error_label)
                return layout
        
        ErrorApp().run()

if __name__ == "__main__":
    main() 