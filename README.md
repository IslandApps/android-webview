# Android WebView Wrapper Template
A simple Android app that wraps a web application in a native WebView, providing a seamless native app experience.

## Features

- Full-screen WebView display
- Automatic URL loading on app start
- JavaScript and DOM storage support
- Progress indicator during page loads
- Error handling with retry functionality
- Back navigation support within WebView
- State preservation on configuration changes
- HTTPS support with network security configuration

## Configuration

### Setting Your Website URL

Open `MainActivity.kt` and modify the `HARDCODED_URL` constant:

```kotlin
// TODO: Change this to your target website URL
private const val HARDCODED_URL = "https://example.com"
```

Replace `https://example.com` with your target website URL.

## Requirements

- Android Studio Hedgehog (2023.1.1) or later
- Minimum SDK: API 24 (Android 7.0)
- Target SDK: API 34 (Android 14)
- Kotlin 1.9.20

## Building the Project

1. Clone or download this project
2. Open the project in Android Studio
3. Wait for Gradle sync to complete
4. Set up your local SDK path in `local.properties`:
   ```
   sdk.dir=PATH_TO_YOUR_ANDROID_SDK
   ```
5. Build the project: `Build > Make Project`
6. Run on emulator or device: `Run > Run 'app'`

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
│   │   └── drawable/
│   │       └── ic_launcher_foreground.xml
│   └── AndroidManifest.xml          # App manifest with permissions
└── build.gradle.kts                  # App-level build configuration
```

## Permissions

The app requires the following permissions:
- `INTERNET` - To load web content
- `ACCESS_NETWORK_STATE` - To check network connectivity

## Customization

### Change App Name

Edit `app/src/main/res/values/strings.xml`:

```xml
<string name="app_name">Your App Name</string>
```

### Change App Icon

Replace the launcher icons in `app/src/main/res/mipmap-*/` directories with your own icons.

### Change App Colors

Edit `app/src/main/res/values/colors.xml` to customize the color scheme.

## Troubleshooting

### Gradle sync fails
- Make sure you have the Android SDK installed
- Check that `local.properties` has the correct SDK path
- Try running `./gradlew clean` and then rebuild

### App crashes on launch
- Check that the `HARDCODED_URL` is valid and accessible
- Verify that INTERNET permission is granted in AndroidManifest.xml
- Check the logcat for error messages

### WebView doesn't load content
- Verify your device/emulator has an internet connection
- Check that the URL is correct and accessible
- Make sure JavaScript is enabled in WebView settings (it is by default)

## License

This project is open source and available under the MIT License.

## Support

For issues and questions, please refer to the Android WebView documentation:
https://developer.android.com/guide/webapps/webview
