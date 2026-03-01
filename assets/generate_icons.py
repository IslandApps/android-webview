#!/usr/bin/env python3
"""
Android WebView App Icon & Splash Screen Generator

This script automatically generates all required app icons and splash screens
from a single source image.

Usage:
    python assets/generate_icons.py

Requirements:
    - Pillow (PIL): pip install Pillow
"""

import os
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Error: Pillow is required. Install it with:")
    print("  pip install Pillow")
    sys.exit(1)


# Configuration
ASSETS_DIR = Path(__file__).parent.absolute()
PROJECT_ROOT = ASSETS_DIR.parent
RES_DIR = PROJECT_ROOT / "app" / "src" / "main" / "res"

# Icon sizes for different DPIs
ICON_SIZES = {
    "mipmap-mdpi": 48,       # 48x48 dp
    "mipmap-hdpi": 72,       # 72x72 dp
    "mipmap-xhdpi": 96,      # 96x96 dp
    "mipmap-xxhdpi": 144,    # 144x144 dp
    "mipmap-xxxhdpi": 192,   # 192x192 dp
}

# Adaptive icon sizes (Android 8.0+)
ADAPTIVE_ICON_SIZES = {
    "mipmap-mdpi": (108, 108, 48),
    "mipmap-hdpi": (162, 162, 72),
    "mipmap-xhdpi": (216, 216, 96),
    "mipmap-xxhdpi": (324, 324, 144),
    "mipmap-xxxhdpi": (432, 432, 192),
}

# Splash screen sizes
SPLASH_SIZES = {
    "drawable": (1200, 1200),  # Icon for splash screen
}


def create_placeholder_logo(size=(1024, 1024)):
    """Create a placeholder logo if none exists."""
    img = Image.new("RGBA", size, (33, 150, 243, 255))
    draw = ImageDraw.Draw(img)

    # Draw a simple "W" for WebView
    margin = size[0] // 4
    draw.text(
        (margin, margin),
        "WV",
        fill=(255, 255, 255, 255),
        font=None
    )

    return img


def load_logo():
    """Load the logo from assets folder or create a placeholder."""
    logo_path = ASSETS_DIR / "logo.png"

    if logo_path.exists():
        print(f"✓ Loading logo from {logo_path}")
        return Image.open(logo_path)
    else:
        print("⚠ No logo.png found, creating placeholder...")
        print("  Add your logo.png to the assets/ folder!")
        return create_placeholder_logo()


def resize_and_save(image, size, output_path, bg_color=None):
    """Resize image and save to output path."""
    # Create output directory if needed
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if bg_color:
        # Create new image with background
        new_img = Image.new("RGBA", size, bg_color + (255,))
        # Calculate position to center the image
        img_resized = image.thumbnail((size[0] - 40, size[1] - 40))
        img_resized = image.copy()
        img_resized.thumbnail((size[0] - 80, size[1] - 80), Image.Resampling.LANCZOS)

        position = (
            (size[0] - img_resized.width) // 2,
            (size[1] - img_resized.height) // 2
        )
        new_img.paste(img_resized, position, img_resized)
        new_img.save(output_path, "PNG")
    else:
        # Simple resize
        resized = image.resize(size, Image.Resampling.LANCZOS)
        resized.save(output_path, "PNG")


def generate_launcher_icons(logo):
    """Generate standard launcher icons."""
    print("\n📱 Generating launcher icons...")

    for dpi, size in ICON_SIZES.items():
        icon_dir = RES_DIR / dpi
        icon_dir.mkdir(parents=True, exist_ok=True)

        # Regular icon
        output_path = icon_dir / "ic_launcher.png"
        resize_and_save(logo, (size, size), output_path)
        print(f"  ✓ Generated {dpi}/ic_launcher.png")

        # Round icon
        output_path = icon_dir / "ic_launcher_round.png"
        resize_and_save(logo, (size, size), output_path)
        print(f"  ✓ Generated {dpi}/ic_launcher_round.png")


def generate_adaptive_icons(logo):
    """Generate adaptive launcher icons for Android 8.0+."""
    print("\n🎨 Generating adaptive icons...")

    for dpi, (full_size, foreground_size, safe_zone) in ADAPTIVE_ICON_SIZES.items():
        icon_dir = RES_DIR / dpi
        icon_dir.mkdir(parents=True, exist_ok=True)

        # Foreground layer (with safe zone)
        output_path = icon_dir / "ic_launcher_foreground.png"
        resize_and_save(logo, (foreground_size, foreground_size), output_path)
        print(f"  ✓ Generated {dpi}/ic_launcher_foreground.png")

        # Background layer (white)
        output_path = icon_dir / "ic_launcher_background.png"
        bg_img = Image.new("RGBA", (full_size, full_size), (255, 255, 255, 255))
        bg_img.save(output_path, "PNG")
        print(f"  ✓ Generated {dpi}/ic_launcher_background.png")

        # Monochrome version (for Android 13+)
        output_path = icon_dir / "ic_launcher_monochrome.png"
        # Convert to grayscale and use alpha
        monochrome = Image.new("RGBA", (foreground_size, foreground_size), (0, 0, 0, 0))

        # Resize logo and convert to monochrome
        logo_resized = logo.resize((foreground_size, foreground_size), Image.Resampling.LANCZOS)
        for y in range(logo_resized.height):
            for x in range(logo_resized.width):
                r, g, b, a = logo_resized.getpixel((x, y))
                if a > 0:
                    # Use average RGB as the monochrome value
                    gray = int((r + g + b) / 3)
                    monochrome.putpixel((x, y), (0, 0, 0, a))

        monochrome.save(output_path, "PNG")
        print(f"  ✓ Generated {dpi}/ic_launcher_monochrome.png")


def generate_splash_screen(logo):
    """Generate splash screen assets."""
    print("\n💦 Generating splash screen assets...")

    splash_dir = RES_DIR / "drawable"
    splash_dir.mkdir(parents=True, exist_ok=True)

    # Create splash icon (sized for splash screen)
    output_path = splash_dir / "splash_icon.png"
    size = 288  # 288dp for splash screen icon
    resize_and_save(logo, (size, size), output_path)
    print(f"  ✓ Generated drawable/splash_icon.png")


def create_splash_screen_theme():
    """Create splash screen theme configuration."""
    print("\n🎯 Creating splash screen theme...")

    # Create values-v31 folder for Android 12+ splash screen
    values_dir = RES_DIR / "values-v31"
    values_dir.mkdir(parents=True, exist_ok=True)

    splash_theme_path = values_dir / "themes.xml"
    with open(splash_theme_path, 'w') as f:
        f.write('''<?xml version="1.0" encoding="utf-8"?>
<resources>
    <!-- Splash screen theme for Android 12+ -->
    <style name="Theme.WebviewPixel" parent="android:Theme.Material.Light.NoActionBar">
        <item name="android:windowSplashScreenAnimatedIcon">@drawable/splash_icon</item>
        <item name="android:windowSplashScreenBackground">@color/splash_background</item>
        <item name="android:windowSplashScreenAnimationDuration">1000</item>
    </style>
</resources>
''')
    print(f"  ✓ Created values-v31/themes.xml")

    # Add splash background color
    colors_path = RES_DIR / "values" / "colors.xml"
    if colors_path.exists():
        with open(colors_path, 'r') as f:
            content = f.read()
            if 'splash_background' not in content:
                with open(colors_path, 'a') as f2:
                    f2.write('\n    <!-- Splash screen background -->\n')
                    f2.write('    <color name="splash_background">#FFFFFF</color>\n')
        print(f"  ✓ Updated colors.xml with splash_background")


def main():
    print("=" * 60)
    print("  Android WebView App Icon Generator")
    print("=" * 60)

    # Load logo
    logo = load_logo()

    # Ensure logo is square and has alpha
    if logo.mode != "RGBA":
        logo = logo.convert("RGBA")

    # Generate all icons
    generate_launcher_icons(logo)
    generate_adaptive_icons(logo)
    generate_splash_screen(logo)
    create_splash_screen_theme()

    print("\n" + "=" * 60)
    print("✅ All icons generated successfully!")
    print("=" * 60)
    print("\nNext steps:")
    print("  1. Build your app: ./gradlew assembleDebug")
    print("  2. Install on device: ./gradlew installDebug")
    print("\nTo customize further:")
    print("  - Edit app/src/main/res/values/colors.xml for colors")
    print("  - Add logo.png to assets/ folder and re-run this script")
    print("=" * 60)


if __name__ == "__main__":
    main()
