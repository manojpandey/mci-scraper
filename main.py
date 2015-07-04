from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

def main():
	"""
		Start a web driver using selenium
	"""
	driver = webdriver.Firefox()

	"""
		Stage 1
	-------------------------------------------------------------------------------
		Get the base url open in a web browser, Firefox FTW !
	"""
	driver.get("http://www.mciindia.org/InformationDesk/IndianMedicalRegister.aspx")

	"""
		Search by state medical council (smc)
	"""
	smc_link = driver.find_element_by_id("dnn_ctr588_IMRIndex_Link_Council")

	"""
		Click the link "Search IMR by =State Medical Council="
	"""
	smc_link.click()

	# Part of the page changes dynamically

	""" 
		Stage 2
	-------------------------------------------------------------------------------
		First, open the dropdown list
	"""
	dropdown = driver.find_element_by_id("dnn_ctr588_IMRIndex_Drp_StateCouncil")
	dropdown.click()

	"""
		Now we get the dropdown list
		Now have to click on preferred State Council, it's Delhi for me.

		Nothing works well, so time for a fix :/
	"""
	for i in range (0,8):
		dropdown.send_keys(Keys.ARROW_DOWN)
	dropdown.send_keys(Keys.ENTER);

	"""
		Click submit button
	"""
	submit_button = driver.find_element_by_id("dnn_ctr588_IMRIndex_Submit_Btn")
	submit_button.click()

	# =========================================================================

	# Getting the page source and Parsing it

	"""
	This fails as things are dynamic
	# resp = requests.get(url)
	# html_doc = resp.content

	"""
	# using selenium
	html = driver.page_source

	soup = BeautifulSoup(html)

	# soup = BeautifulSoup(html_doc, 'html.parser')
	file = open("scraped.html", "w")

	# Use encode('UTF-8'), else it fails on copyright symbol
	file.write(soup.prettify().encode('UTF-8'))

	# print(soup.prettify())

if __name__ == "__main__":
	main()