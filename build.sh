#!/bin/bash
# build.sh — Django build automation script

set -e  # Exit immediately if a command exits with a non-zero status
set -o pipefail  # Fail if any command in a pipeline fails

echo "🚀 Starting Django build process..."

# 1. Install dependencies
if [ -f requirements.txt ]; then
    echo "📦 Installing Python dependencies..."
    pip install --upgrade pip
    pip install -r requirements.txt
else
    echo "⚠️ requirements.txt not found. Skipping dependency installation."
fi

# 2. Apply database migrations
echo "🗄 Applying database migrations..."
python manage.py migrate --noinput

# 3. Collect static files
echo "🎨 Collecting static files..."
python manage.py collectstatic --noinput

# 4. (Optional) Run tests
echo "🧪 Running tests..."
python manage.py test || { echo "❌ Tests failed!"; exit 1; }

echo "✅ Build completed successfully!"
