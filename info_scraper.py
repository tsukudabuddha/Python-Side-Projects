"""Web Scraper built to pull from repos of chosen user."""
# Next step - build slack bot to alert user
import requests
import datetime
from bs4 import BeautifulSoup


def create_url(name):
    """Take in github username and return their repo list url."""
    return "https://www.github.com/" + str(name) + "?tab=repositories"


def build_soup(url):
    """Build and return soup."""
    # query the website and return the html to the variable ‘page’
    page = requests.get(url)
    # parse the html using beautiful soup and store in variable `soup`
    return BeautifulSoup(page.content, "html.parser")


def find_date(soup):
    """Find and return the most recent commit."""
    holding_class = soup.find("div", {"class": "f6 text-gray mt-2"})
    date = str(holding_class.find("relative-time")["datetime"]).split('T')[0]
    return date


def compare_date(date):
    """Compare current date against latest commit date."""
    current_date = str(datetime.datetime.now().date())
    if current_date == date:
        return True
    else:
        return False


def main():
    """Begin the script."""
    name = input("Enter your github username: ")  # possibly pass from call
    # specify the url
    page_url = create_url(name)
    # Create 'soup'
    soup = build_soup(page_url)
    date = find_date(soup)
    if compare_date(date):
        print("Good Job! You've committed today!")
    else:
        print("Hurry and commit soon! Don't want to lose your streak")


main()
