# author: Mahmud Ahsan
# github: https://github.com/mahmudahsan
# blog: http://thinkdiff.net
# Web: http://pythonbangla.com
# youtube: https://www.youtube.com/c/banglaprogramming
# License: MIT License
# https://github.com/mahmudahsan/thinkdiff/blob/master/LICENSE 

# --------------------------
#      Execute JavaScript
# --------------------------

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from PIL import Image
from io import BytesIO
import os


def main():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1280x1024")

    # download Chrome Webdriver  
    # https://sites.google.com/a/chromium.org/chromedriver/download
    # put driver executable file in the script directory
    chrome_driver = "chromedriver.exe"

    driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)

    driver.get("http://localhost:1947/_int_/features.html")
    assert "gemalto sentinel acc: features".lower() in driver.title.lower()

    # Find element mydata (licenses table)
    element = driver.find_element_by_id('mydata')
    # Get screenshot of full page
    png = driver.get_screenshot_as_png()
    # Get location and size of selected element
    location = element.location
    size = element.size
    # Create PIL image to handle screenshot
    im = Image.open(BytesIO(png))
    # Get screenshot's border points
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']

    # Crop screenshot of element using Pillow
    im = im.crop((left, top, right, bottom))
    # Save image in folder
    im.save('table.png')

    """# fill and submit form
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("python")
    elem.send_keys(Keys.RETURN)"""

    # screenshot capture of full page
    # driver.get_screenshot_as_file("capture.png")
    driver.close()

if __name__ == '__main__' : main()
