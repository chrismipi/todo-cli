#!/bin/bash
set -e

# Configuration
REPO_URL="https://github.com/chrismipi/todo-cli.git"
APP_NAME="todo"
INSTALL_DIR="/usr/local/bin"
TMP_DIR=$(mktemp -d)

# Helper Functions
info() { echo -e "\033[34m[INFO]\033[0m $1"; }
success() { echo -e "\033[32m[SUCCESS]\033[0m $1"; }
error() { echo -e "\033[31m[ERROR]\033[0m $1" >&2; exit 1; }
cleanup() { info "Cleaning up..."; rm -rf "$TMP_DIR"; }
trap cleanup EXIT

# Main Logic
info "Checking dependencies..."
command -v git >/dev/null || error "Git is not installed."
command -v python3 >/dev/null || error "Python 3 is not installed."
command -v pip3 >/dev/null || error "pip3 is not installed."

info "Cloning repository..."
git clone --depth 1 "$REPO_URL" "$TMP_DIR"
cd "$TMP_DIR"

info "Installing PyInstaller..."
pip3 install pyinstaller

info "Building executable..."
pyinstaller --onefile --name "$APP_NAME" "todo/__main__.py"

EXECUTABLE="dist/$APP_NAME"
[ -f "$EXECUTABLE" ] || error "Build failed."

info "Installing '$APP_NAME' to $INSTALL_DIR..."
if [ -w "$INSTALL_DIR" ]; then
    mv "$EXECUTABLE" "$INSTALL_DIR/"
else
    echo "Write permission to $INSTALL_DIR is required."
    sudo mv "$EXECUTABLE" "$INSTALL_DIR/"
fi

success "'$APP_NAME' installed successfully. You can now use the '$APP_NAME' command."
