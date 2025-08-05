#!/bin/bash
# Fix NDK version error and rebuild APK
# This script fixes the Android NDK version issue

echo "🔧 Fixing NDK version error..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Step 1: Replace buildozer.spec with fixed version
print_status "Updating buildozer.spec with correct NDK version..."
cp buildozer_ndk_fixed.spec buildozer.spec

# Step 2: Clean previous builds
print_status "Cleaning previous builds..."
buildozer clean -q 2>/dev/null || true
rm -rf .buildozer bin dist 2>/dev/null || true

# Step 3: Create placeholder assets
print_status "Creating app assets..."
if [ ! -f "icon.png" ]; then
    echo "Creating placeholder icon..."
    echo "Placeholder icon - replace with actual icon.png" > icon.png
fi

if [ ! -f "presplash.png" ]; then
    echo "Creating placeholder splash..."
    echo "Placeholder splash - replace with actual presplash.png" > presplash.png
fi

# Step 4: Set file permissions
print_status "Setting file permissions..."
chmod +x *.py *.spec 2>/dev/null || true

# Step 5: Build with fixed NDK version
print_status "Building APK with NDK 25b (this may take 10-20 minutes)..."
echo "⏳ Please wait while Buildozer downloads NDK 25b and builds the APK..."

# Build with verbose output
if buildozer android debug; then
    print_success "APK build completed successfully!"
else
    print_error "APK build failed"
    echo "📋 Check logs: cat .buildozer/logs/buildozer-*.log"
    exit 1
fi

# Step 6: Check results
print_status "Checking build results..."

# Find APK files
APK_FILES=$(find . -name "*.apk" -type f 2>/dev/null || true)

if [ -n "$APK_FILES" ]; then
    print_success "APK files found:"
    for apk in $APK_FILES; do
        SIZE=$(ls -lh "$apk" | awk '{print $5}')
        echo "   📦 $apk ($SIZE)"
    done
    
    # Copy APK to workspace root for easy download
    cp bin/*.apk ./ 2>/dev/null || cp .buildozer/android/platform/build-*/build/outputs/apk/*.apk ./ 2>/dev/null || true
    
    print_success "APK copied to workspace root for easy download"
    
    # Show final file info
    echo ""
    echo "🎉 Build completed successfully!"
    echo "📱 APK files available:"
    ls -lh *.apk 2>/dev/null || echo "   (Check bin/ directory for APK files)"
    echo ""
    echo "📥 To download the APK:"
    echo "   1. Look for the APK file in the file explorer"
    echo "   2. Right-click and select 'Download'"
    echo "   3. Transfer to your Android device"
    echo ""
    echo "📱 To install on Android:"
    echo "   1. Enable 'Unknown sources' in Settings"
    echo "   2. Tap the APK file to install"
    echo "   3. Launch Astra Mobile from app drawer"
    
else
    print_error "No APK files found"
    echo "📋 Check build logs:"
    echo "   cat .buildozer/logs/buildozer-*.log"
    exit 1
fi

echo ""
print_success "Astra Mobile APK build completed with NDK 25b! 🚀" 