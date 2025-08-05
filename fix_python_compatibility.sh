#!/bin/bash
# Fix Python compatibility issues with Buildozer
# This script downgrades Python to 3.9 which is more compatible with Buildozer

echo "🔧 Fixing Python compatibility issues..."

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

# Check current Python version
print_status "Checking current Python version..."
python3 --version

# Install Python 3.9 (more compatible with Buildozer)
print_status "Installing Python 3.9..."
sudo apt update
sudo apt install -y python3.9 python3.9-venv python3.9-dev

# Create virtual environment with Python 3.9
print_status "Creating virtual environment with Python 3.9..."
python3.9 -m venv astra_env
source astra_env/bin/activate

# Verify Python version in virtual environment
print_status "Verifying Python version in virtual environment..."
python --version

# Install Buildozer in the virtual environment
print_status "Installing Buildozer in virtual environment..."
pip install buildozer

# Install additional dependencies
print_status "Installing additional dependencies..."
pip install cython requests

# Set environment variables
export PYTHONPATH=$VIRTUAL_ENV/lib/python3.9/site-packages:$PYTHONPATH

print_success "Python compatibility fix completed!"
print_status "Now run the build with:"
echo "source astra_env/bin/activate"
echo "buildozer clean"
echo "buildozer android debug" 