[app]
title = Astra Mobile
package.name = astramobile
package.domain = org.astra.mobile
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,md,txt
source.include_patterns = *.py,*.kv,*.json,*.md,*.txt
source.exclude_dirs = tests,bin,venv,.git,.vscode,__pycache__,astra_env
source.exclude_patterns = *.pyc,*.pyo,*.pyd,__pycache__,*.so,*.dll,*.dylib
version = 1.0.0

# Use Python 3.9 for better compatibility
requirements = python3==3.9.18,kivy>=2.1.0,requests>=2.28.0

orientation = portrait
fullscreen = 0
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 28
android.minapi = 21

# Fix NDK version to 25b (minimum supported)
android.ndk = 25b
android.sdk = 28
android.arch = armeabi-v7a,arm64-v8a
android.allow_backup = True
android.presplash_color = #000000
android.icon.filename = %(source.dir)s/icon.png
android.presplash.filename = %(source.dir)s/presplash.png

# App settings
android.apptheme = "@android:style/Theme.NoTitleBar"
android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-3940256099942544~3347511713

# Build settings - Fixed for NDK compatibility
android.gradle_dependencies = 'androidx.webkit:webkit:1.4.0'
android.add_aars = ~/.gradle/caches/modules-2/files-2.1/androidx.webkit/webkit/1.4.0/*.aar

# Python compatibility fixes
android.enable_androidx = True
android.allow_newer_versions = True

# Cython compatibility
android.cython_compile_options = -O3

# NDK specific settings
android.ndk_api = 21
android.accept_sdk_license = True

# Logging
log_level = 2
warn_on_root = 1

# Buildozer settings
buildozer.log_level = 2
buildozer.warn_on_root = 1 