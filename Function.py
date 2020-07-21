
import os
import operator

from selenium import webdriver
from PIL import Image
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.common.by import *
from selenium.webdriver.chrome.options import Options
from PyPDF2 import PdfFileMerger
import shutil
# driver = webdriver.Chrome()
# driver.get('https://prezi.com/asqylv4mdpjp/civil-engineering-presentation/')
from AbbyyOnlineSdk import *
from process import *

def screenshotelement(id, savename, driver):
    """
    screenshotelement(nameofelement,filename)

    str,str -> none

    Saves a screenshot named filename of the element named nam
    """
    element = driver.find_element_by_id(id)
    driver.get_screenshot_as_file('screenshot.png')
    left = int(element.location['x'])
    top = int(element.location['y'])
    right = int(element.location['x'] + element.size['width'])
    bottom = int(element.location['y'] + element.size['height'])
    im = Image.open('screenshot.png')
    im = im.crop((left, top, right, bottom))
    im.save(savename)


def click_elementxpath(name, driver):
    element = driver.find_element_by_xpath(name)
    element.click()

def getprezi(url):

    options = Options()
    #options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-dev-shm-usage')
    #options.binary_location = r"E:\ProgramFiles\Google\Chrome\Application\chrome.exe"
    cwd = os.getcwd()
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    driver_loca = os.path.join(__location__, 'chromedriver.exe')
    if not os.path.isfile(driver_loca):
        print(driver_loca)
    print(driver_loca)
    #executable_path = driver_loca
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    #driver.set_window_position(-10000, 0) #Hides the window
    driver.get(url)
    playarrowxpath = '/html/body/div[1]/div[2]/div/div/span/div/div[3]/div[2]/div/div/div[1]/div'
    rightarrowxpath = '/html/body/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div[2]/button[2]'
    Fullscreenxpath = '/html/body/div[1]/div[2]/div/div/section[1]/div[1]/div/div/div/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[3]/button/div'

    wait = WebDriverWait(driver, 10)
    element = wait.until(visibility_of_element_located((By.XPATH, playarrowxpath)))
    click_elementxpath(playarrowxpath, driver)
    wait = WebDriverWait(driver, 100)
    element = wait.until(visibility_of_element_located((By.XPATH, rightarrowxpath)))
    #driver.find_element_by_xpath(Fullscreenxpath).click() # Sets to fullscreen
    time.sleep(2)
    Nisdone = True
    x = 0
    while Nisdone:
        x = x + 1
        try:
            print('Getting image '+str(x))
            screenshotelement('canvas', 'prezitest' + str(x) + '.png', driver)
            click_elementxpath(rightarrowxpath, driver)
        except:
            Nisdone = False
        time.sleep(2)
    print('Job Done')
    driver.quit()


def ABBYYY(input, outputname):
    processor = AbbyyOnlineSdk()

    setup_processor()

    source_file = input
    target_file = outputname
    output_format = "pdfSearchable"
    language = "English"

    if os.path.isfile(source_file):
        recognize_file(source_file, target_file, language, output_format, processor)
    else:
        print("No such file: {}".format(source_file))


def appendPDF(dest,pdfs):
    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write(dest)
    merger.close()


def sort_bynumber(lst):
    numbers = []
    for x in lst:
        if x[-6].isdigit():
            n = x[-6] + x[-5]
            numbers.append((int(n), x))
        elif x[-5].isdigit():
            n = x[-5]
            numbers.append((int(n), x))
        else:
            print('file '+x+' does not have a number')
    numbers.sort(key = operator.itemgetter(0))
    return [i[1] for i in numbers]

def DELETE_PNGSANDpdfs():
    directory = os.fsencode(os.getcwd())
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if (filename.endswith('.png') or filename.endswith('.pdf')) and filename[-5].isdigit():
            if os.path.exists(filename):
                os.remove(filename)
            else:
                print('Error Path DOES NOT EXIST')
            continue
        else:
            continue
def DeleteALL():
    directory = os.fsencode(os.getcwd())
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if (filename.endswith('.png') or filename.endswith('.pdf')):
            if os.path.exists(filename):
                os.remove(filename)
            else:
                print('Error Path DOES NOT EXIST')
            continue
        else:
            continue

def main(url):
    DeleteALL()
    getprezi(url)
    abbyr = ''
    mainr = ''
    pngimgs = []
    directory = os.fsencode(os.getcwd())
    print(directory)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith('.png') and filename[-5].isdigit():
            if os.path.exists(filename):
                pngimgs.append(filename)
            else:
                print('Error Path DOES NOT EXIST')
            continue
        else:
            continue
    pngstobeC = sort_bynumber(pngimgs)
    x = 0
    listofpdfs= []
    for png in pngstobeC:
        x = x+1
        currentpdf = 'result'+str(x)+ '.pdf'
        ABBYYY(png, currentpdf)
        listofpdfs.append(currentpdf)
    appendPDF('final.pdf',listofpdfs)
    DELETE_PNGSANDpdfs()



#main('https://prezi.com/view/dD0plxuNKIOEsFbl867J/')