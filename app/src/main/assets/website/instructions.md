# WebView Wrapper - Local Assets Instructions

This folder is designed to host your local website files.

### 🚀 Using Local Files
To display a local website in the app:
1. Place your HTML, CSS, and JavaScript files in this folder (`app/src/main/assets/website/`).
2. Ensure your main entry point is named **`index.html`**.
3. When the app launches, it will automatically detect `index.html` and load it.

### 🌐 Using a Remote URL
If you want the app to load a website from the internet instead:
1. Delete or rename the `index.html` file in this folder.
2. Open `MainActivity.kt` (`app/src/main/java/com/example/webviewpixel/MainActivity.kt`).
3. Locate the `HARDCODED_URL` constant in the `companion object` at the bottom of the file and update it with your URL.

The app is programmed to look for `index.html` in this directory first. If no such file exists, it will fall back to the URL specified in the `MainActivity` file.
