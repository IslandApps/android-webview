# Website to Android App Template

**A simple starter template that turns any website into an Android app!**

## What Does This Do?

This template creates an Android app that displays your website inside a native app wrapper. Think of it like putting a website inside a phone app - it looks and feels like a regular Android app, but it shows your web content.

**Perfect for:**
- Turning your website into a downloadable Android app
- Creating a simple mobile app without learning Android development
- Testing mobile versions of websites
- Building app prototypes quickly

## Features

- Full-screen WebView display
- Automatic URL loading on app start
- JavaScript and DOM storage support
- Progress indicator during page loads
- Error handling with retry functionality
- Back navigation support within WebView
- State preservation on configuration changes
- HTTPS support with network security configuration

## Before You Start

**Checklist - make sure you have these ready:**

- [ ] **Android Studio installed** (download free from https://developer.android.com/studio)
- [ ] **A website URL** (if using Option 1) OR **HTML files** (if using Option 2)
- [ ] **10-30 minutes** for first-time setup (downloads required)
- [ ] **Optional**: An Android phone or emulator for testing

**Don't have Android Studio yet?**
1. Download it from the official website
2. Install it (the installer handles everything)
3. Open it once and let it complete setup
4. Come back to this guide when ready!

## Quick Start Guide

### Option 1: Load a Website (Easiest)

1. **Open the project in Android Studio**
2. **Find the file**: In the left panel, navigate to `app > java > com.example.webviewpixel > MainActivity.kt`
3. **Edit the URL**: Scroll to the bottom of the file (around line 297), you'll see this line:
   ```kotlin
   private const val HARDCODED_URL = "https://example.com"
   ```

   **Pro tip**: Press `Ctrl+F` (Windows/Linux) or `Cmd+F` (Mac) and search for "HARDCODED_URL" to jump straight to it!
4. **Replace the URL**: Change `https://example.com` to your website's address
   ```kotlin
   private const val HARDCODED_URL = "https://yourwebsite.com"
   ```
5. **Run the app**: Click the green play button in Android Studio

That's it! Your app will now load your website when it opens.

### Option 2: Use Local Files (Advanced)

Instead of loading a website from the internet, you can include HTML/CSS/JavaScript files inside the app.

**Step-by-Step Instructions:**

1. **Find the website folder** (it already exists!):
   - In the left panel, navigate to `app > src > main > assets > website`
   - This folder is already created for you

2. **Add your website files**:
   - Copy your HTML, CSS, and JavaScript files into the `website` folder
   - **Important**: Your main file must be named `index.html`
   - You can drag and drop files directly into Android Studio

3. **Your folder structure should look like**:
   ```
   app/
   └── src/
       └── main/
           └── assets/
               └── website/
                   ├── index.html      ← Your main HTML file (required!)
                   ├── css/            ← Optional: your CSS files
                   │   └── style.css
                   ├── js/             ← Optional: your JavaScript files
                   │   └── app.js
                   └── images/         ← Optional: your images
                       └── logo.png
   ```

4. **Run the app**: Click the green play button

**How it works**: The app automatically checks if you have local files. If `index.html` exists in the assets folder, it loads those files. Otherwise, it loads the website URL from Option 1.

## What You Need

**To use this project, you need:**

1. **Android Studio** (version Hedgehog 2023.1.1 or newer)
   - Download from: https://developer.android.com/studio
   - It's free and includes everything you need

2. **A computer** running Windows, Mac, or Linux

3. **Basic knowledge** of using your computer (opening files, copying/pasting)

**What these technical terms mean:**
- **Minimum SDK: API 24**: Your app works on Android 7.0 and newer phones (covers 99%+ of devices)
- **Target SDK: API 34**: Your app is designed for and tested on Android 14
- **Kotlin**: The programming language used (don't worry, you don't need to learn it!)

**Good news - you don't need to install Java!**
Android Studio comes with its own built-in Java Development Kit (JDK), so you don't need to install Java separately. Just install Android Studio and you're ready to go!

## Building Your App

### Using Android Studio (Recommended)

**Follow these simple steps:**

1. **Open the project**
   - Launch Android Studio
   - Click "Open an Existing Project"
   - Navigate to where you saved this project and select it
   - Click "OK"

2. **Wait for setup to complete**
   - Android Studio will automatically download necessary tools
   - Look for the progress bar at the bottom saying "Gradle Build Running..."
   - This may take 5-15 minutes on first run (depending on your internet)
   - ⚠️ Don't interrupt this process!

3. **Check for problems**
   - If you see a red banner at the top about SDK location
   - Click the "Install SDK" button that appears
   - Android Studio will guide you through it

4. **Build your app**
   - In the top menu: `Build > Make Project`
   - Wait for "BUILD SUCCESSFUL" message at the bottom

5. **Run your app**
   - Connect your Android phone with USB (or use the emulator)
   - Click the green ▶️ play button in the toolbar
   - Or press `Shift + F10` on Windows/Linux, `Control + R` on Mac

**Tips:**
- First build takes longer, subsequent builds are much faster
- If something goes wrong, try `File > Invalidate Caches > Invalidate and Restart`

### Using Command Line (Advanced)

If you prefer using the terminal/command prompt:

## Command Line Build

```bash
# Build debug APK
./gradlew assembleDebug

# Build release APK
./gradlew assembleRelease

# Install on connected device
./gradlew installDebug
```

## Project Structure

```
app/
├── src/main/
│   ├── java/com/example/webviewpixel/
│   │   └── MainActivity.kt          # Main activity with WebView configuration
│   ├── res/
│   │   ├── layout/
│   │   │   └── activity_main.xml   # Main UI layout
│   │   ├── values/
│   │   │   ├── colors.xml          # Color definitions
│   │   │   ├── strings.xml         # String resources
│   │   │   ├── themes.xml          # App theme
│   │   │   └── styles.xml          # Custom styles
│   │   ├── xml/
│   │   │   └── network_security_config.xml  # Network security configuration
│   │   ├── drawable/               # Image resources
│   │   └── mipmap-*/               # Launcher icons (auto-generated)
│   └── AndroidManifest.xml          # App manifest with permissions
└── build.gradle.kts                  # App-level build configuration
assets/
├── logo.png                         # Your app logo (add this!)
├── generate_icons.py                # Icon generation script
└── README.md                        # Detailed customization guide
```

## Permissions

The app requires the following permissions:
- `INTERNET` - To load web content
- `ACCESS_NETWORK_STATE` - To check network connectivity

## Customize Your App

### Change the App Icon (Make it Yours!)

**The easy way - automatic icon generation:**

1. **Prepare your logo**
   - Get a square image (PNG works best)
   - Recommended size: 1024x1024 pixels
   - Simple, clean logos work best

2. **Add your logo file**
   - Put your logo file here: `assets/logo.png`
   - Just replace the existing logo.png file

3. **Run the icon generator**
   - **Windows**: Double-click `generate-icons.bat`
   - **Mac/Linux**: Double-click `generate-icons.sh` or run it from terminal
   - **Any OS**: Run `python assets/generate_icons.py` in your terminal

4. **Build your app**
   - The generator automatically creates all the different icon sizes
   - Just click the green play button in Android Studio

**What the generator creates for you:**
- ✅ App icons for all phone screen sizes
- ✅ Special adaptive icons for modern Android phones
- ✅ Splash screen image (shown while app loads)
- ✅ Monochrome icons for Android 13+

**Requirements:**
- Python must be installed on your computer
- Install the imaging library: `pip install Pillow`

**Manual customization** (if you prefer doing it yourself): See [assets/README.md](assets/README.md)

### Change the App Name

Make your app show your chosen name instead of "WebViewPixel":

1. In Android Studio, find: `app > src > main > res > values > strings.xml`
2. Look for this line:
   ```xml
   <string name="app_name">WebViewPixel</string>
   ```
3. Change `WebViewPixel` to your app name:
   ```xml
   <string name="app_name">My Awesome App</string>
   ```
4. Rebuild the app and the new name will appear on your phone!

### Change App Colors

Customize the colors used throughout your app:

1. Find: `app > src > main > res > values > colors.xml`
2. You'll see color definitions like:
   ```xml
   <color name="splash_background">#FFFFFF</color>
   ```
3. Change the color codes (hex values) to your preferred colors
   - Use a color picker tool to find hex codes
   - Example: `#FF5733` = red-orange, `#3498DB` = blue
4. Key colors you can change:
   - `splash_background` - Background color while app loads
   - `splash_icon_background` - Color behind your icon during loading

### Change Package Name (Advanced)

The package name (currently `com.example.webviewpixel`) is your app's unique identifier. It's important to change this before publishing to the Google Play Store.

**⚠️ Important: Changing the package name affects many files. Use Android Studio's built-in refactoring tool!**

**Step-by-Step Instructions:**

1. **Open the refactor tool**
   - In Android Studio, click on the package name in the Project panel: `app > java > com.example.webviewpixel`
   - Or click directly on the folder name in the left panel

2. **Start the refactor**
   - Right-click on the package name (folder)
   - Select `Refactor > Rename...`
   - Or press `Shift + F6` on Windows/Linux, `Fn + Shift + F6` on Mac

3. **Choose rename scope**
   - Select `Rename package`
   - Click `Rename` button

4. **Enter your new package name**
   - Use reverse domain notation: `com.yourcompany.yourappname`
   - Example: `com.mycompany.mywebsite`
   - **Format rules**:
     - Must be all lowercase
     - Use dots to separate parts
     - No spaces or special characters
     - Usually follows: `com.[company].[appname]`

5. **Confirm the changes**
   - Android Studio will show you a preview of all files that will be changed
   - Review the changes to make sure everything looks correct
   - Click `Do Refactor`

6. **Wait for Gradle sync**
   - Android Studio will automatically sync the project
   - Wait for "Gradle sync finished" message at the bottom

**What this changes:**
- ✅ Package name in all your source files
- ✅ `applicationId` in build.gradle.kts
- ✅ `namespace` in build.gradle.kts
- ✅ All imports and references throughout the project

**Common package name examples:**
- `com.google.maps` → Google's Maps app
- `com.instagram.android` → Instagram
- `com.mycompany.myapp` → Your company's app

### Change App Version

Update your app's version number when you release updates:

1. **Find the version file**: `app > build.gradle.kts` (in the Project panel, it's under "Gradle Scripts")

2. **Look for these lines** (around line 14-15):
   ```kotlin
   versionCode = 1
   versionName = "1.0"
   ```

3. **Update the version numbers**:
   - **versionCode**: A whole number that must increase with each release
     - Start at 1, then 2, 3, 4, etc.
     - Google Play uses this to detect updates
     - Example: `versionCode = 2` (for your second release)

   - **versionName**: A string that users see (can be anything you want)
     - Typically uses semantic versioning: `major.minor.patch`
     - Examples: `"1.0"`, `"1.1"`, `"2.0"`, `"1.0.1"`
     - Example: `versionName = "1.1"` (for a minor update)

4. **Version number examples**:
   ```kotlin
   // First release
   versionCode = 1
   versionName = "1.0"

   // Bug fix release
   versionCode = 2
   versionName = "1.0.1"

   // New feature release
   versionCode = 3
   versionName = "1.1"

   // Major update
   versionCode = 4
   versionName = "2.0"
   ```

5. **Rebuild the app** after making changes

**Version Number Tips:**
- **versionCode** must always increase - never reuse old numbers
- **versionName** is for humans - make it meaningful (e.g., "1.0 - First Release", "1.1 - New Features")
- Common versioning strategy:
  - `1.0.0` = First major release
  - `1.0.1` = Bug fix
  - `1.1.0` = New features
  - `2.0.0` = Major update/redesign

## Troubleshooting (Help!)

### Gradle sync fails / Red error banner

**What it looks like**: Red banner at top of Android Studio saying "Gradle sync failed"

**Try these fixes (in order):**

1. **Check your internet connection** - Gradle needs to download files
2. **Wait longer** - First-time setup can take 10-15 minutes
3. **Try again**: `File > Sync Project with Gradle Files`
4. **Clean and rebuild**: `Build > Clean Project`, then `Build > Rebuild Project`
5. **Check SDK location**: `File > Settings > Appearance & Behavior > System Settings > Android SDK`
   - Make sure an SDK path is selected
   - If not, click "Edit" and let Android Studio install it

### App crashes when I open it

**What it looks like**: App opens briefly then closes, or you see "Unfortunately, [App] has stopped"

**Try these fixes:**

1. **Check your URL** (if using Option 1):
   - Make sure the website address is correct
   - Test the URL in your regular browser first
   - Make sure it starts with `https://` or `http://`

2. **Check your index.html** (if using Option 2):
   - Make sure you have an `index.html` file in `app/src/main/assets/website/`
   - Try opening it in a browser to make sure it works

3. **View error messages**:
   - In Android Studio, click the "Logcat" tab at the bottom
   - Look for red text showing what went wrong
   - Copy the error message and search for it online

### Website doesn't load / Blank screen

**What it looks like**: App opens but shows white screen or loading spinner forever

**Try these fixes:**

1. **Test your internet connection**:
   - Open your phone's web browser
   - Try loading any website
   - If it doesn't work, check your Wi-Fi or mobile data

2. **Check the URL in MainActivity.kt**:
   - Make sure it's exactly right (no typos!)
   - Test it in a regular web browser first

3. **Clear app data**:
   - On your phone: `Settings > Apps > [Your App] > Storage > Clear Data`
   - Then try reopening the app

### Still stuck?

**Where to get help:**
- Search for your error message on Google or Stack Overflow
- Check the official Android documentation: https://developer.android.com/guide/webapps/webview
- Make sure you're using the latest version of Android Studio

## Frequently Asked Questions

**Q: Can I put this app on the Google Play Store?**
A: Yes! Once you've customized it with your content, you can publish it. You'll need a Google Play Developer account ($25 one-time fee).

**Q: Do I need to know how to code?**
A: Not for basic usage! If you just want to wrap a website, you only need to change the URL in MainActivity.kt. For more advanced features, some programming knowledge helps.

**Q: Will this work on all Android phones?**
A: It works on Android 7.0 and newer, which covers 99%+ of active Android devices.

**Q: Can I use this for commercial purposes?**
A: Yes! This project is open source under the MIT License, which allows commercial use.

**Q: The app loads slowly. What can I do?**
A: This usually depends on your website's speed. Try optimizing your website for mobile, or consider using local files (Option 2) for instant loading.

**Q: Can I add a custom loading screen?**
A: The app includes a default loading indicator. For a custom splash screen, use the icon generator tool mentioned above.

**Q: Does the app work offline?**
A: Only if you use Option 2 (local files). If loading from a website, internet connection is required.

**Q: How do I update my website in the app?**
A: If using Option 1 (website URL), just update your website normally - the app will automatically show the latest version. If using Option 2 (local files), you'll need to rebuild the app with updated files.

## License

This project is open source and available under the MIT License. You're free to use it for personal or commercial projects.

## Need More Help?

- **Official Android WebView Documentation**: https://developer.android.com/guide/webapps/webview
- **Android Studio User Guide**: https://developer.android.com/studio/intro
- **Search for help**: Try searching your question on Google or Stack Overflow
