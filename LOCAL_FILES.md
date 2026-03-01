# Using Local Website Files

This guide explains how to bundle local HTML/CSS/JS files inside the app.

## Quick Start

1. **Create the assets folder**: `app/src/main/assets/website/`
2. **Copy your website files** to this folder
3. **Ensure you have `index.html`** as your main file
4. **Build and run the app** - local files load automatically!

## How to Add Files

### Method 1: Using File Explorer
1. Navigate to your project folder
2. Create the folder structure: `app/src/main/assets/website/`
3. Copy your website files here

### Method 2: Using Android Studio
1. In Project view, switch to "Project" mode (not "Android")
2. Navigate to `app > src > main`
3. Create an `assets` folder if it doesn't exist
4. Inside assets, create a `website` folder
5. Copy your files to the website folder

### Method 3: Using Command Line
```bash
mkdir -p app/src/main/assets/website
cp -r your-website-files/* app/src/main/assets/website/
```

## Requirements

- **Required**: `index.html` must exist in `app/src/main/assets/website/`
- **Optional**: Any CSS, JS, images, or other assets in subdirectories
- **Paths**: Use relative paths in your HTML (e.g., `href="css/style.css"`)

## Troubleshooting

**App doesn't load my local files:**
- Verify `index.html` exists in `app/src/main/assets/website/`
- Rebuild the project after adding files
- Clean and rebuild: `Build > Clean Project` then `Build > Rebuild Project`

**Images or CSS not loading:**
- Use relative paths in your HTML (e.g., `src="images/logo.png"`)
- Ensure all files are in the assets folder or subdirectories
- Don't use absolute paths like `/images/logo.png`

**Want to use the remote URL again?**
- Delete or rename the `assets/website` folder
- The app will fall back to the hardcoded URL automatically

## Example Project Structure

```
WebviewPixel/
├── app/
│   └── src/
│       └── main/
│           ├── assets/
│           │   └── website/              ← Your local website files go here
│           │       ├── index.html        ← Required (entry point)
│           │       ├── css/
│           │       │   ├── style.css
│           │       │   └── responsive.css
│           │       ├── js/
│           │       │   ├── app.js
│           │       │   └── utils.js
│           │       ├── images/
│           │       │   ├── logo.png
│           │       │   └── background.jpg
│           │       └── fonts/
│           │           └── custom.woff
│           ├── java/
│           │   └── com/example/webviewpixel/
│           │       └── MainActivity.kt
│           └── res/
└── build.gradle.kts
```

## How It Works

When you build the app:
1. All files in the `assets` folder are compiled into the APK
2. The app checks if `assets/website/index.html` exists
3. If found, it loads the local files using `file:///android_asset/` URLs
4. If not found, it falls back to the hardcoded URL

## Advanced Tips

- **File size**: Large asset files will increase your APK size
- **JavaScript**: Works normally, same as in a browser
- **Local Storage**: Supported for web apps
- **Offline capable**: No internet connection needed
- **Updates**: Rebuild and reinstall the app to update files
- **Version Control**: Your website files are tracked in Git along with the app
