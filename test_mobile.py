#!/usr/bin/env python3
# test_mobile.py - Test script for Astra Mobile
# Tests basic functionality without launching the full UI

import sys
import os
from datetime import datetime

def test_imports():
    """Test if all required modules can be imported"""
    print("🔍 Testing imports...")
    
    try:
        import kivy
        print("✅ Kivy imported successfully")
    except ImportError as e:
        print(f"❌ Kivy import failed: {e}")
        return False
    
    try:
        from astra_mobile import process_mobile_query, OFFLINE_RESPONSES
        print("✅ Astra Mobile modules imported successfully")
    except ImportError as e:
        print(f"❌ Astra Mobile import failed: {e}")
        return False
    
    return True

def test_query_processing():
    """Test query processing functionality"""
    print("\n🧪 Testing query processing...")
    
    try:
        from astra_mobile import process_mobile_query
        
        test_queries = [
            "hello",
            "what time is it?",
            "calculate 15 + 23",
            "help",
            "/status",
            "/time",
            "/date",
            "this is a test query"
        ]
        
        for query in test_queries:
            try:
                response = process_mobile_query(query)
                print(f"✅ '{query}' → {response[:50]}...")
            except Exception as e:
                print(f"❌ '{query}' failed: {e}")
                return False
        
        return True
        
    except Exception as e:
        print(f"❌ Query processing test failed: {e}")
        return False

def test_offline_responses():
    """Test offline response database"""
    print("\n📚 Testing offline responses...")
    
    try:
        from astra_mobile import OFFLINE_RESPONSES
        
        # Test a few responses
        test_cases = [
            ('hello', 'hello'),
            ('help', 'help'),
            ('time', 'time'),
            ('battery', 'battery')
        ]
        
        for query, expected_key in test_cases:
            if expected_key in OFFLINE_RESPONSES:
                print(f"✅ '{query}' response available")
            else:
                print(f"❌ '{query}' response missing")
                return False
        
        print(f"✅ Found {len(OFFLINE_RESPONSES)} offline responses")
        return True
        
    except Exception as e:
        print(f"❌ Offline responses test failed: {e}")
        return False

def test_math_operations():
    """Test math calculation functionality"""
    print("\n🧮 Testing math operations...")
    
    try:
        from astra_mobile import simple_math
        
        test_calculations = [
            ("calculate 15 + 23", "38"),
            ("what is 10 times 5", "50"),
            ("20 minus 8", "12"),
            ("100 divided by 4", "25")
        ]
        
        for query, expected in test_calculations:
            try:
                result = simple_math(query)
                if result and expected in result:
                    print(f"✅ '{query}' → {result}")
                else:
                    print(f"❌ '{query}' failed or incorrect")
                    return False
            except Exception as e:
                print(f"❌ '{query}' error: {e}")
                return False
        
        return True
        
    except Exception as e:
        print(f"❌ Math operations test failed: {e}")
        return False

def test_commands():
    """Test command handling"""
    print("\n⚙️ Testing commands...")
    
    try:
        from astra_mobile import handle_mobile_commands
        
        test_commands = [
            "/help",
            "/time",
            "/date",
            "/status",
            "/clear",
            "/battery",
            "/memory",
            "/offline"
        ]
        
        for command in test_commands:
            try:
                response = handle_mobile_commands(command)
                if response and len(response) > 10:
                    print(f"✅ '{command}' → {response[:50]}...")
                else:
                    print(f"❌ '{command}' returned empty response")
                    return False
            except Exception as e:
                print(f"❌ '{command}' error: {e}")
                return False
        
        return True
        
    except Exception as e:
        print(f"❌ Commands test failed: {e}")
        return False

def test_mobile_settings():
    """Test mobile-specific settings"""
    print("\n📱 Testing mobile settings...")
    
    try:
        from astra_mobile import MOBILE_MODE, LOW_MEMORY_MODE, BATTERY_SAVER
        
        settings = {
            'MOBILE_MODE': MOBILE_MODE,
            'LOW_MEMORY_MODE': LOW_MEMORY_MODE,
            'BATTERY_SAVER': BATTERY_SAVER
        }
        
        for setting, value in settings.items():
            print(f"✅ {setting}: {value}")
        
        return True
        
    except Exception as e:
        print(f"❌ Mobile settings test failed: {e}")
        return False

def test_file_structure():
    """Test if all required files exist"""
    print("\n📁 Testing file structure...")
    
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
            print(f"✅ {file} exists")
        else:
            print(f"❌ {file} missing")
            missing_files.append(file)
    
    if missing_files:
        print(f"⚠️ Missing files: {', '.join(missing_files)}")
        return False
    
    return True

def run_all_tests():
    """Run all tests"""
    print("🚀 Starting Astra Mobile Tests")
    print("=" * 50)
    
    tests = [
        ("File Structure", test_file_structure),
        ("Imports", test_imports),
        ("Mobile Settings", test_mobile_settings),
        ("Offline Responses", test_offline_responses),
        ("Math Operations", test_math_operations),
        ("Commands", test_commands),
        ("Query Processing", test_query_processing)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🧪 Running {test_name} test...")
        try:
            if test_func():
                print(f"✅ {test_name} test passed")
                passed += 1
            else:
                print(f"❌ {test_name} test failed")
        except Exception as e:
            print(f"❌ {test_name} test error: {e}")
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Astra Mobile is ready to use.")
        return True
    else:
        print("⚠️ Some tests failed. Check the errors above.")
        return False

def show_help():
    """Show test help"""
    print("""
🧪 ASTRA MOBILE TEST SCRIPT

Usage:
  python test_mobile.py          # Run all tests
  python test_mobile.py --help   # Show this help

Tests:
  • File structure validation
  • Module imports
  • Mobile settings
  • Offline responses
  • Math operations
  • Command handling
  • Query processing

Examples:
  python test_mobile.py
  python test_mobile.py --help

Requirements:
  • Python 3.6+
  • Kivy 2.1.0+
  • All mobile files present
""")

def main():
    """Main test function"""
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        
        if arg in ['--help', '-h', 'help']:
            show_help()
            return
    
    # Run all tests
    success = run_all_tests()
    
    if success:
        print("\n🚀 Astra Mobile is ready!")
        print("💡 Run with: python mobile_launcher.py")
    else:
        print("\n❌ Some issues found")
        print("💡 Check the errors above and fix them")
        print("💡 Make sure all requirements are installed")
    
    # Wait for user input
    try:
        input("\nPress Enter to exit...")
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main() 