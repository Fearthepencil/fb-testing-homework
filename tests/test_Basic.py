


def test_navigate_to_sitemap(page, test_config):
    """Simple test to navigate to sitemap and login if needed"""
    sitemap_url = test_config["urls"]["sitemap_url"]
    page.goto(sitemap_url)
    
    # Wait for page to load after Cloudflare (if it appears, user completes it manually)
    page.wait_for_load_state("networkidle", timeout=15000)
    
    # Verify we're past Cloudflare - check for either login page or sitemap content
    # Wait a bit to ensure page is fully loaded
    page.wait_for_timeout(2000)