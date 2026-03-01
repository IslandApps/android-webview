# App Assets

This folder contains your app's branding assets.

## How to Customize Your App Icon and Splash Screen

### Easy Way (Recommended)

1. **Add your logo**: Place a square PNG logo (1024x1024px recommended) named `logo.png` in this folder
2. **Run the generator**: Execute the script from the project root:
   ```bash
   python assets/generate_icons.py
   ```
   Or on Windows:
   ```cmd
   python assets\generate_icons.py
   ```

That's it! The script will automatically:
- Generate all required launcher icon sizes
- Create adaptive icons for Android 8.0+
- Generate a splash screen image
- Update the app configuration

### Manual Way

If you prefer manual control, place your icons in:
- `app/src/main/res/mipmap-mdpi/ic_launcher.png` (48x48dp)
- `app/src/main/res/mipmap-hdpi/ic_launcher.png` (72x72dp)
- `app/src/main/res/mipmap-xhdpi/ic_launcher.png` (96x96dp)
- `app/src/main/res/mipmap-xxhdpi/ic_launcher.png` (144x144dp)
- `app/src/main/res/mipmap-xxxhdpi/ic_launcher.png` (192x192dp)

## File Structure

```
assets/
├── logo.png              # Your main logo (1024x1024 recommended)
├── logo_monochrome.png   # Optional: Monochrome version for adaptive icons
├── splash_logo.png       # Optional: Custom splash screen logo
└── generate_icons.py     # Icon generation script
```

## Tips

- Use a **transparent PNG** for best results
- Minimum size: 512x512px
- Recommended size: 1024x1024px or larger
- For splash screens, a horizontal or stacked version works best
