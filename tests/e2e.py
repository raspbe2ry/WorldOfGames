from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import argparse

def test_scores_service(url):
    chromeService = Service("C:\DevExperts\Lesson_11\WorldOfGames4\WorldOfGames\chromedriver.exe")
    chromeDriver = webdriver.Chrome(service=chromeService)
    chromeDriver.get(url)
    element = chromeDriver.find_element(By.ID, "score")
    score = int(element.text)
    if(score >= 1 and score <=1000):
        return True
    else:
        return False

def main_function(application_url: str):
    test_result = test_scores_service(application_url)

    if test_result:
        print("Test Passed: Score is valid.")

        return 0
    else:
        print("Test Failed: Score is invalid or not found.")
        return -1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--url', type=str, help='Url to the app', required=True)
    args = parser.parse_args()
    url = args.url

    exit_code = main_function(url)

    # Exit the program with the corresponding code
    exit(exit_code)
