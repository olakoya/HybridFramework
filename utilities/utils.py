import os
from datetime import datetime

def capture_screenshot(driver, name_prefix):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshots_dir = os.path.join(os.getcwd(), 'screenshots')
    os.makedirs(screenshots_dir, exist_ok=True)  # make sure folder exists
    path = os.path.join(screenshots_dir, f"{name_prefix}_{timestamp}.png")
    driver.save_screenshot(path)
    print("Screenshot saved to:", path)
    driver.save_screenshot(path)
