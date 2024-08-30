from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time


def readInput(sample_games='./sample_games.txt', sample_statements='./sample_statements.txt'):
    '''Reads a list of games and statements from files and return two lists.'''
    # Read a list of games from sample_games
    with open(sample_games, 'r') as f:
        game_name = [game[:-1] for game in f] # Note: strips newline char from file
        f.close()
    # Read a list of statements from sample_statements
    with open(sample_statements, 'r') as f:
        statements = [st[:-1] for st in f]
        f.close()
    return game_name, statements

def openBrowser():
    '''Open a chrome browser'''
    browser = webdriver.Chrome()
    return browser

def openPage(browser, url):
    '''Open a webpage'''
    browser.get(url)

def wait_and_find(browser, path):
    '''Wait for the webpage to respond and find element by xpath'''
    return WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, path)))

def itemExistsOnWikidata(browser, game_nameList, dict_existsWiki):
    '''
    Go to Wikidata and check of an item page has been created for a game.
    Store the result in a dict for further actions.
    '''
    # Go to Wikidata
    openPage(browser, 'https://wikidata.org')

    for game_name in game_nameList:
        try:
            # Find search bar and start searching
            search = browser.find_element(By.ID, 'searchInput')
            search.clear()
            search.send_keys(game_name)

            # Wait for the dropdown menu
            page = wait_and_find(browser, "//li/a/span/span[contains(text(), 'game')]")
            page.click()

            dict_existsWiki[game_name] = True
    
        except NoSuchElementException:
            dict_existsWiki[game_name] = False
    
    browser.close()

def find_statement(browser, dict_existsWiki, statementList, dict_missingStatements):
    '''
    For games that exists on Wikidata, loop through all statements to see if any of them 
    are missing.
    Use another dict to record all statements missing for a game.
    '''
    # Find statement for those that has a page
    for game_name in dict_existsWiki:
        if dict_existsWiki[game_name] == False:
            pass

        for statement in statementList:
            try:
                browser.find_element(By.XPATH, f"//a[contains(text(), '{statement}')]")
            except NoSuchElementException:
                if dict_missingStatements[game_name]:
                    dict_missingStatements[game_name].append(statement)
                else:
                    dict_missingStatements[game_name] = []

def reorganizeDict(dict_missingStatements, statementList):
    '''
    Create a dict with games as keys, and a list of missing statements as values.
    '''
    result = {}
    for statement in statementList:
        for game_name in dict_missingStatements:
            if statement in dict_missingStatements[game_name]:
                if result[statement]:
                    result[statement].append(game_name)
                else: 
                    result[statement] = []
    return result

######################################################################
# Below is an attempt to collect information from other websites and #
# fill it into corresponding places in Wikidata.The code does not    #
# give stable results and needs further modification. Use with care. #
######################################################################
""" def getGameUIDatabaseID(browser, pre_dict, post_dict):
    for game in pre_dict['Game UI Database ID']:
        try:
            search = browser.find_element(By.ID, 'searchbox')
            search.clear()
            search.send_keys(game)
            page = wait_and_find(browser, "//div[contains(text(), 'GAME')]")
            page.click()
            url = browser.current_url
            post_dict[game] = url
        except NoSuchElementException:
            post_dict[game] = None

def fill_gameUIDatabaseID(browser, post_dict, statement):
    openPage(browser, 'https://wikidata.org')
    for game_name in post_dict:
        try:
            search = browser.find_element(By.ID, 'searchInput')
            search.clear()
            search.send_keys(game_name)

            # Wait for the dropdown menu
            page = wait_and_find(browser, "//li/a/span/span[contains(text(), 'game')]")
            page.click()

            add = wait_and_find(browser, "//h2[contains(text(),'Identifiers')]/following-sibling::div/div/span/a")
            add.click()

            state_property = wait_and_find(browser, "//input[@Placeholder='Property']")
            state_property.send_keys('Game UI Database ID')

            property_button = wait_and_find(browser, "//span[contains(text(), 'Game UI Database ID')]")
            property_button.click()

            input_value = wait_and_find(browser, "//textarea[@class='valueview-expert-StringValue-input valueview-input']")
            input_value.send_keys(post_dict[game_name])

        except NoSuchElementException:
            pass
 """
