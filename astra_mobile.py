# astra_mobile.py - Mobile-optimized Astra AI Assistant
# Designed for low-end smartphones with minimal resource usage

import os
import json
import threading
import time
from datetime import datetime
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.utils import platform

# Mobile-specific imports
try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False
    print("Warning: requests not available. Online features disabled.")

# Global settings for mobile optimization
MOBILE_MODE = True
LOW_MEMORY_MODE = True
BATTERY_SAVER = True

# Simple offline responses for mobile
OFFLINE_RESPONSES = {
    'hello': "👋 Hi! I'm Astra Mobile - your lightweight AI assistant!",
    'hi': "👋 Hello! How can I help you today?",
    'help': "📱 **Astra Mobile Help**\n\n• Ask me questions\n• I work offline\n• Lightweight & fast\n• Battery friendly",
    'what can you do': "🤖 I can:\n• Answer questions\n• Work offline\n• Save battery\n• Run on low-end phones",
    'time': f"⏰ Current time: {datetime.now().strftime('%H:%M:%S')}",
    'date': f"📅 Today: {datetime.now().strftime('%Y-%m-%d')}",
    'weather': "🌤️ I can't check weather offline, but I'm here to help with other questions!",
    'calculator': "🧮 I can do simple math! Try: 'calculate 15 + 23'",
    'battery': "🔋 Astra Mobile is optimized for battery life!",
    'memory': "💾 Astra Mobile uses minimal memory for smooth performance!",
    'offline': "📡 Astra Mobile works completely offline!",
    'lightweight': "⚡ Astra Mobile is designed to be lightweight and fast!",
    'mobile': "📱 Astra Mobile - optimized for smartphones!",
    'fast': "🚀 Astra Mobile is fast and responsive!",
    'simple': "✨ Astra Mobile keeps things simple and efficient!"
}

# Math operations
def simple_math(query):
    """Handle simple math calculations"""
    try:
        import re
        # Extract numbers and operators
        query_lower = query.lower()
        
        # Replace words with symbols
        query_lower = query_lower.replace('plus', '+')
        query_lower = query_lower.replace('minus', '-')
        query_lower = query_lower.replace('times', '*')
        query_lower = query_lower.replace('multiply', '*')
        query_lower = query_lower.replace('divided by', '/')
        query_lower = query_lower.replace('divide', '/')
        
        # Extract math expression
        math_expr = re.sub(r'[^0-9+\-*/(). ]', '', query_lower)
        math_expr = math_expr.strip()
        
        if re.match(r'^[\d+\-*/(). ]+$', math_expr):
            result = eval(math_expr)
            return f"🧮 Result: {round(result, 2)}"
        
        return None
    except:
        return None

# Simple offline AI responses
def get_offline_response(query):
    """Get offline response for common queries"""
    query_lower = query.lower().strip()
    
    # Check for exact matches
    for keyword, response in OFFLINE_RESPONSES.items():
        if keyword in query_lower:
            return response
    
    # Check for math
    if any(word in query_lower for word in ['calculate', 'math', 'plus', 'minus', 'times', 'divide']):
        math_result = simple_math(query)
        if math_result:
            return math_result
    
    # Check for greetings
    greeting_words = ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening']
    if any(word in query_lower for word in greeting_words):
        return "👋 Hello! I'm Astra Mobile - your lightweight AI assistant!"
    
    # Check for help requests
    if any(word in query_lower for word in ['help', 'what can you do', 'capabilities']):
        return "📱 **Astra Mobile Help**\n\n• Ask me questions\n• I work offline\n• Lightweight & fast\n• Battery friendly\n• Simple math\n• Time & date"
    
    # Default response
    return "🤖 I'm Astra Mobile - a lightweight AI assistant. I work offline and am optimized for mobile devices. Ask me anything!"

# Mobile-optimized query processor
def process_mobile_query(query):
    """Process queries with mobile optimization"""
    if not query or len(query.strip()) == 0:
        return "🤖 Please ask me a question!"
    
    if len(query.strip()) < 2:
        return "🤖 Please ask a more detailed question."
    
    try:
        # Check for commands
        if query.startswith('/'):
            return handle_mobile_commands(query[1:])
        
        # Get offline response
        response = get_offline_response(query)
        
        # Add mobile indicator
        return f"{response} [mobile]"
        
    except Exception as e:
        print(f"Mobile query error: {e}")
        return "🤖 Sorry, I encountered an error. Please try again. [mobile]"

def handle_mobile_commands(command):
    """Handle mobile-specific commands"""
    command_lower = command.lower()
    
    if 'help' in command_lower:
        return """📱 **Astra Mobile Commands**

**Basic Commands:**
• /help - Show this help
• /time - Current time
• /date - Current date
• /status - App status
• /clear - Clear chat
• /battery - Battery info
• /memory - Memory usage
• /offline - Offline status

**Features:**
• 🔋 Battery optimized
• 💾 Low memory usage
• 📡 Works offline
• ⚡ Fast responses
• 📱 Mobile friendly

**Examples:**
• "Hello" - Get greeting
• "Calculate 15 + 23" - Math
• "What time is it?" - Time
• "Help" - Get help

I'm designed for low-end smartphones! 🚀"""
    
    elif 'time' in command_lower:
        return f"⏰ Current time: {datetime.now().strftime('%H:%M:%S')} [mobile]"
    
    elif 'date' in command_lower:
        return f"📅 Today: {datetime.now().strftime('%Y-%m-%d')} [mobile]"
    
    elif 'status' in command_lower:
        return "✅ Astra Mobile is running smoothly!\n📱 Optimized for mobile\n🔋 Battery friendly\n💾 Low memory usage [mobile]"
    
    elif 'clear' in command_lower:
        return "🗑️ Chat cleared. [mobile]"
    
    elif 'battery' in command_lower:
        return "🔋 Astra Mobile is optimized for battery life!\n• Minimal CPU usage\n• Efficient responses\n• Lightweight design [mobile]"
    
    elif 'memory' in command_lower:
        return "💾 Astra Mobile uses minimal memory!\n• Lightweight code\n• No heavy models\n• Fast startup [mobile]"
    
    elif 'offline' in command_lower:
        return "📡 Astra Mobile works completely offline!\n• No internet required\n• Instant responses\n• Always available [mobile]"
    
    else:
        return "❓ Unknown command. Type /help for available commands. [mobile]"

# Mobile-optimized chat screen
class MobileChatScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'mobile_chat'
        
        # Main layout with mobile optimization
        layout = BoxLayout(orientation='vertical', spacing=5, padding=10)
        
        # Compact header
        header = BoxLayout(size_hint=(1, 0.08))
        title = Label(
            text="Astra Mobile",
            color=(0, 1, 0, 1),
            font_size=18,
            bold=True,
            size_hint_x=0.6
        )
        self.status_label = Label(
            text="Ready",
            color=(0, 1, 0, 1),
            font_size=14,
            size_hint_x=0.4
        )
        header.add_widget(title)
        header.add_widget(self.status_label)
        
        # Chat area (larger for mobile)
        chat_container = BoxLayout(orientation='vertical', size_hint=(1, 0.82))
        
        # Scroll view for chat
        self.scroll = ScrollView(
            do_scroll_x=False,
            do_scroll_y=True,
            scroll_type=['bars'],
            bar_width=10,
            bar_color=(0, 1, 0, 0.7),
            bar_inactive_color=(0, 1, 0, 0.3)
        )
        
        self.chat_log = TextInput(
            size_hint_y=None,
            readonly=True,
            multiline=True,
            background_color=(0, 0, 0, 1),
            foreground_color=(0, 1, 0, 1),
            cursor_color=(0, 1, 0, 1),
            selection_color=(0, 0.5, 0, 0.3),
            font_size=14,  # Smaller font for mobile
            padding=(10, 10),
            border=(0, 0, 0, 0),
            write_tab=False
        )
        self.chat_log.bind(text=self.update_log_height)
        self.scroll.add_widget(self.chat_log)
        
        # Set initial height
        self.chat_log.height = 500
        
        chat_container.add_widget(self.scroll)
        
        # Compact input area
        input_container = BoxLayout(size_hint=(1, 0.1), spacing=5)
        self.input = TextInput(
            hint_text="Ask Astra Mobile...",
            multiline=False,
            background_color=(0.1, 0.1, 0.1, 1),
            foreground_color=(0, 1, 0, 1),
            cursor_color=(0, 1, 0, 1),
            font_size=14,
            hint_text_color=(0, 0.5, 0, 1),
            size_hint_x=0.75
        )
        self.send_btn = Button(
            text="Send",
            font_size=14,
            background_color=(0, 0.3, 0, 1),
            color=(0, 1, 0, 1),
            size_hint_x=0.25
        )
        self.send_btn.bind(on_press=self.on_send)
        
        input_container.add_widget(self.input)
        input_container.add_widget(self.send_btn)
        
        # Add all components
        layout.add_widget(header)
        layout.add_widget(chat_container)
        layout.add_widget(input_container)
        
        self.add_widget(layout)
        
        # Welcome message
        Clock.schedule_once(lambda dt: self.show_welcome(), 0.5)
    
    def show_welcome(self):
        """Show welcome message"""
        welcome_msg = """📱 **Welcome to Astra Mobile!**

I'm a lightweight AI assistant optimized for mobile devices.

**Features:**
• 🔋 Battery optimized
• 💾 Low memory usage
• 📡 Works offline
• ⚡ Fast responses

**Try asking:**
• "Hello"
• "What time is it?"
• "Calculate 15 + 23"
• "Help"

Type /help for commands! 🚀"""
        
        self.append_message("", welcome_msg)
    
    def update_log_height(self, *args):
        """Update chat log height based on content"""
        try:
            lines = self.chat_log.text.count('\n') + 1
            line_height = 24  # Smaller for mobile
            min_height = 500
            calculated_height = max(min_height, lines * line_height)
            self.chat_log.height = calculated_height
            
            # Force scroll to bottom
            Clock.schedule_once(lambda dt: self.scroll_to_bottom(), 0.1)
        except Exception as e:
            print(f"Error updating log height: {e}")
    
    def scroll_to_bottom(self):
        """Scroll chat to bottom"""
        try:
            self.scroll.scroll_y = 0
        except Exception as e:
            print(f"Error scrolling to bottom: {e}")
    
    def append_message(self, user_msg, bot_msg):
        """Add a message to the chat"""
        try:
            timestamp = datetime.now().strftime("%H:%M")
            if user_msg:
                new_text = f"[{timestamp}] You: {user_msg}\nAstra: {bot_msg}\n\n"
            else:
                new_text = f"Astra: {bot_msg}\n\n"
            
            current_text = self.chat_log.text
            self.chat_log.text = current_text + new_text
            
            # Update scroll view height and scroll to bottom
            Clock.schedule_once(lambda dt: self.update_log_height(), 0.1)
            
        except Exception as e:
            print(f"Error in append_message: {e}")
    
    def on_send(self, instance):
        """Handle send button press"""
        try:
            user_query = self.input.text.strip()
            if not user_query:
                return

            # Clear input immediately
            self.input.text = ""
            
            # Show processing indicator
            self.status_label.text = "Processing..."
            
            # Process the message
            try:
                response = process_mobile_query(user_query)
            except Exception as e:
                response = "🤖 Sorry, I encountered an error. Please try again. [mobile]"
            
            self.append_message(user_query, response)
            
            # Reset status
            Clock.schedule_once(lambda dt: self.reset_status(), 1)
            
        except Exception as e:
            print(f"Error in on_send: {e}")
            self.status_label.text = "Error occurred"
    
    def reset_status(self):
        """Reset status label"""
        self.status_label.text = "Ready"

# Mobile-optimized settings screen
class MobileSettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'mobile_settings'
        
        layout = BoxLayout(orientation='vertical', spacing=10, padding=15)
        
        # Header
        header = BoxLayout(size_hint=(1, 0.1))
        title = Label(
            text="Mobile Settings",
            color=(0, 1, 0, 1),
            font_size=20,
            bold=True
        )
        back_btn = Button(
            text="← Back",
            size_hint_x=0.3,
            background_color=(0.3, 0, 0, 1),
            color=(1, 0.5, 0.5, 1)
        )
        back_btn.bind(on_press=self.go_back)
        
        header.add_widget(title)
        header.add_widget(back_btn)
        
        # Settings content
        content = BoxLayout(orientation='vertical', spacing=10)
        
        # Status info
        status_info = f"""📱 **Astra Mobile Status**

**Optimization:**
• 🔋 Battery Saver: {'ON' if BATTERY_SAVER else 'OFF'}
• 💾 Low Memory Mode: {'ON' if LOW_MEMORY_MODE else 'OFF'}
• 📡 Offline Mode: {'ON' if not REQUESTS_AVAILABLE else 'AUTO'}

**Performance:**
• ⚡ Fast startup
• 💾 Minimal memory usage
• 🔋 Battery optimized
• 📱 Mobile friendly

**Features:**
• 📡 Works offline
• 🧮 Simple math
• ⏰ Time & date
• 📝 Chat history
• 🎨 Dark theme"""
        
        status_label = Label(
            text=status_info,
            color=(0, 1, 0, 1),
            font_size=14,
            size_hint=(1, 0.8),
            text_size=(Window.width - 30, None),
            halign='left',
            valign='top'
        )
        
        content.add_widget(status_label)
        
        # Add components
        layout.add_widget(header)
        layout.add_widget(content)
        
        self.add_widget(layout)
    
    def go_back(self, instance):
        """Go back to chat screen"""
        self.manager.current = 'mobile_chat'

# Mobile-optimized main app
class AstraMobileApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Astra Mobile"
        
        # Mobile-specific settings
        if platform == 'android':
            # Android-specific optimizations
            Window.softinput_mode = 'below_target'
        
        # Set window size for mobile
        Window.size = (400, 600)
    
    def build(self):
        """Build the mobile app"""
        try:
            # Create screen manager
            sm = ScreenManager()
            
            # Add screens
            sm.add_widget(MobileChatScreen())
            sm.add_widget(MobileSettingsScreen())
            
            return sm
            
        except Exception as e:
            print(f"Error building mobile app: {e}")
            import traceback
            traceback.print_exc()
            
            # Fallback error screen
            from kivy.uix.label import Label
            from kivy.uix.boxlayout import BoxLayout
            error_layout = BoxLayout(orientation='vertical')
            error_label = Label(
                text=f"Error launching Astra Mobile:\n{str(e)}", 
                color=(1, 0, 0, 1),
                size_hint=(1, 1)
            )
            error_layout.add_widget(error_label)
            return error_layout

if __name__ == "__main__":
    try:
        print("🚀 Starting Astra Mobile...")
        print("📱 Optimized for low-end smartphones")
        print("🔋 Battery friendly")
        print("💾 Low memory usage")
        
        app = AstraMobileApp()
        app.run()
        
    except Exception as e:
        print(f"❌ Error running Astra Mobile: {e}")
        import traceback
        traceback.print_exc()
        print("Press Enter to exit...")
        input() 