# Using Local Website Files

This guide explains how to use local HTML/CSS/JS files with the WebView app.

## Quick Start

1. **Find the website folder** on your device:
   - Using file manager: `Android/data/com.example.webviewpixel/files/website/`
   - Using Files app: App Files > WebviewPixel > website

2. **Copy your website files** to this folder

3. **Ensure you have `index.html`** as your main file

4. **Restart the app** - local files load automatically!

## How to Access the Folder

### On Android Device
1. Open the "Files" app (or any file manager)
2. Navigate to: App Files > WebviewPixel > website
3. Copy your files here

### Via USB Connection
1. Connect device to computer via USB
2. Choose "File Transfer" mode
3. Navigate to: `Android/data/com.example.webviewpixel/files/website/`
4. Copy your website files here

## Requirements

- **Required**: `index.html` must exist in the website folder
- **Optional**: Any CSS, JS, images, or other assets in subdirectories
- **Paths**: Use relative paths in your HTML (e.g., `href="css/style.css"`)

## Troubleshooting

**App doesn't load my local files:**
- Verify `index.html` exists in the correct folder
- Check file permissions (files should be readable)
- Restart the app after adding files
- Check that the file is valid HTML

**Images or CSS not loading:**
- Use relative paths in your HTML (e.g., `src="images/logo.png"`)
- Ensure all files are in the website folder or subdirectories
- Don't use absolute paths like `/images/logo.png`

**Want to use the remote URL again?**
- Delete or rename `index.html` in the website folder
- The app will fall back to the hardcoded URL automatically

## Example Website Structure

```
website/
├── index.html              ← Required (entry point)
├── css/
│   ├── style.css
│   └── responsive.css
├── js/
│   ├── app.js
│   └── utils.js
├── images/
│   ├── logo.png
│   └── background.jpg
└── fonts/
    └── custom.woff
```

## Advanced Tips

- **File size**: Large files may take longer to load
- **JavaScript**: Works normally, same as in a browser
- **Local Storage**: Supported for web apps
- **Offline capable**: No internet connection needed
- **Updates**: Just replace files and restart the app
