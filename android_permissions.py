#!/usr/bin/env python3
# android_permissions.py - Android permissions handler for Astra Mobile

import os
from kivy.utils import platform

def request_android_permissions():
    """Request Android permissions if on Android platform"""
    if platform == 'android':
        try:
            from android.permissions import request_permissions, Permission
            
            # Request necessary permissions
            permissions = [
                Permission.INTERNET,
                Permission.WRITE_EXTERNAL_STORAGE,
                Permission.READ_EXTERNAL_STORAGE
            ]
            
            request_permissions(permissions)
            return True
            
        except ImportError:
            print("⚠️ Android permissions module not available")
            return False
        except Exception as e:
            print(f"⚠️ Error requesting permissions: {e}")
            return False
    
    return True

def check_android_permissions():
    """Check if Android permissions are granted"""
    if platform == 'android':
        try:
            from android.permissions import check_permission, Permission
            
            permissions = [
                Permission.INTERNET,
                Permission.WRITE_EXTERNAL_STORAGE,
                Permission.READ_EXTERNAL_STORAGE
            ]
            
            granted = True
            for permission in permissions:
                if not check_permission(permission):
                    granted = False
                    print(f"⚠️ Permission not granted: {permission}")
            
            return granted
            
        except ImportError:
            print("⚠️ Android permissions module not available")
            return True
        except Exception as e:
            print(f"⚠️ Error checking permissions: {e}")
            return True
    
    return True

def get_android_storage_path():
    """Get Android storage path for saving files"""
    if platform == 'android':
        try:
            from android.storage import primary_external_storage_path
            return primary_external_storage_path()
        except ImportError:
            print("⚠️ Android storage module not available")
            return None
        except Exception as e:
            print(f"⚠️ Error getting storage path: {e}")
            return None
    
    return None

def save_to_android_storage(filename, content):
    """Save file to Android external storage"""
    if platform == 'android':
        try:
            storage_path = get_android_storage_path()
            if storage_path:
                file_path = os.path.join(storage_path, 'AstraMobile', filename)
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"✅ Saved to Android storage: {file_path}")
                return True
                
        except Exception as e:
            print(f"❌ Error saving to Android storage: {e}")
            return False
    
    return False 