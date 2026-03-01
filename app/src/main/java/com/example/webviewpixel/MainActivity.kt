package com.example.webviewpixel

import android.annotation.SuppressLint
import android.graphics.Bitmap
import android.os.Bundle
import android.view.View
import android.webkit.WebResourceError
import android.webkit.WebResourceRequest
import android.webkit.WebView
import android.webkit.WebViewClient
import androidx.appcompat.app.AppCompatActivity
import androidx.core.splashscreen.SplashScreen.Companion.installSplashScreen
import com.example.webviewpixel.databinding.ActivityMainBinding

/**
 * Main Activity for WebView Wrapper App
 *
 * This app automatically loads a hardcoded URL when opened,
 * providing a native app experience for web applications.
 */
class MainActivity : AppCompatActivity() {

    // TODO: Change this to your target website URL
    private const val HARDCODED_URL = "https://example.com"

    private lateinit var binding: ActivityMainBinding
    private var currentUrl: String = HARDCODED_URL

    @SuppressLint("SetJavaScriptEnabled")
    override fun onCreate(savedInstanceState: Bundle?) {
        // Handle splash screen
        val splashScreen = installSplashScreen()

        super.onCreate(savedInstanceState)

        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        setupWebView()
        loadUrl(currentUrl)

        // Set up retry button
        binding.retryButton.setOnClickListener {
            binding.errorView.visibility = View.GONE
            binding.webView.visibility = View.VISIBLE
            loadUrl(currentUrl)
        }

        // Restore URL if savedInstanceState exists
        savedInstanceState?.getString(KEY_URL)?.let { url ->
            currentUrl = url
            if (binding.webView.url == null) {
                loadUrl(currentUrl)
            }
        }
    }

    /**
     * Configure WebView with optimal settings
     */
    @SuppressLint("SetJavaScriptEnabled")
    private fun setupWebView() {
        binding.webView.apply {
            settings.apply {
                // Enable JavaScript for modern web apps
                javaScriptEnabled = true

                // Enable DOM storage for web apps that use localStorage
                domStorageEnabled = true

                // Enable database storage
                databaseEnabled = true

                // Enable caching
                cacheMode = android.webkit.WebSettings.LOAD_DEFAULT

                // Allow mixed content (HTTPS pages with HTTP resources)
                mixedContentMode = android.webkit.WebSettings.MIXED_CONTENT_COMPATIBILITY_MODE

                // Zoom settings
                setSupportZoom(true)
                builtInZoomControls = false
                displayZoomControls = false

                // Viewport settings
                useWideViewPort = true
                loadWithOverviewMode = true

                // Performance settings
                setRenderPriority(android.webkit.WebSettings.RenderPriority.HIGH)

                // Media settings
                mediaPlaybackRequiresUserGesture = false

                // Text settings
                textZoom = 100
            }

            // Set custom WebViewClient for handling page loading and errors
            webViewClient = object : WebViewClient() {

                override fun onPageStarted(view: WebView?, url: String?, favicon: Bitmap?) {
                    super.onPageStarted(view, url, favicon)
                    showProgress()
                    hideError()
                }

                override fun onPageFinished(view: WebView?, url: String?) {
                    super.onPageFinished(view, url)
                    hideProgress()
                    currentUrl = url ?: HARDCODED_URL
                }

                override fun shouldOverrideUrlLoading(
                    view: WebView?,
                    request: WebResourceRequest?
                ): Boolean {
                    // Keep navigation within the WebView
                    request?.url?.let { url ->
                        view?.loadUrl(url.toString())
                        currentUrl = url.toString()
                    }
                    return true
                }

                @Deprecated("Deprecated in API 24")
                override fun shouldOverrideUrlLoading(view: WebView?, url: String?): Boolean {
                    // Keep navigation within the WebView
                    url?.let {
                        view?.loadUrl(it)
                        currentUrl = it
                    }
                    return true
                }

                override fun onReceivedError(
                    view: WebView?,
                    request: WebResourceRequest?,
                    error: WebResourceError?
                ) {
                    super.onReceivedError(view, request, error)
                    handleError(error?.description?.toString() ?: "Unknown error")
                }

                @Deprecated("Deprecated in API 24")
                override fun onReceivedError(
                    view: WebView?,
                    errorCode: Int,
                    description: String?,
                    failingUrl: String?
                ) {
                    super.onReceivedError(view, errorCode, description, failingUrl)
                    handleError(description ?: "Error code: $errorCode")
                }
            }

            // Set custom WebChromeClient for progress updates
            webChromeClient = object : android.webkit.WebChromeClient() {
                override fun onProgressChanged(view: WebView?, newProgress: Int) {
                    super.onProgressChanged(view, newProgress)
                    binding.progressBar.progress = newProgress
                }
            }
        }
    }

    /**
     * Load a URL in the WebView
     */
    private fun loadUrl(url: String) {
        binding.webView.loadUrl(url)
    }

    /**
     * Show the progress bar
     */
    private fun showProgress() {
        binding.progressBar.visibility = View.VISIBLE
        binding.progressBar.progress = 0
    }

    /**
     * Hide the progress bar
     */
    private fun hideProgress() {
        binding.progressBar.visibility = View.GONE
    }

    /**
     * Show the error view
     */
    private fun showError(message: String) {
        binding.webView.visibility = View.GONE
        binding.errorView.visibility = View.VISIBLE
        binding.errorMessage.text = message
    }

    /**
     * Hide the error view
     */
    private fun hideError() {
        binding.errorView.visibility = View.GONE
        binding.webView.visibility = View.VISIBLE
    }

    /**
     * Handle errors
     */
    private fun handleError(errorMessage: String) {
        hideProgress()
        showError(errorMessage)
    }

    /**
     * Handle back button press
     * Navigate back in WebView history if available, otherwise exit app
     */
    @Deprecated("Deprecated in API 33")
    override fun onBackPressed() {
        if (binding.webView.canGoBack()) {
            binding.webView.goBack()
        } else {
            super.onBackPressed()
        }
    }

    /**
     * Save instance state
     */
    override fun onSaveInstanceState(outState: Bundle) {
        super.onSaveInstanceState(outState)
        outState.putString(KEY_URL, currentUrl)
        binding.webView.saveState(outState)
    }

    /**
     * Restore instance state
     */
    override fun onRestoreInstanceState(savedInstanceState: Bundle) {
        super.onRestoreInstanceState(savedInstanceState)
        binding.webView.restoreState(savedInstanceState)
    }

    /**
     * Pause WebView when activity is paused
     */
    override fun onPause() {
        super.onPause()
        binding.webView.onPause()
    }

    /**
     * Resume WebView when activity is resumed
     */
    override fun onResume() {
        super.onResume()
        binding.webView.onResume()
    }

    /**
     * Destroy WebView when activity is destroyed
     */
    override fun onDestroy() {
        super.onDestroy()
        binding.webView.destroy()
    }

    companion object {
        private const val KEY_URL = "key_url"
    }
}
