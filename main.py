from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import json

def main():

	print "\n\t\tLET THE SCRAP BEGIN !!\n\n"
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

	"""
		Stage 3
		----------------------------------------------------------------------------
		Clicking the view button for particular ID and open the pop up window
	"""

	data = []

	for loop in range (0,330):
		for i in range (3,33):
			# Create empty dictionary
			doctors = {}

			# Get view button's xpath
			view_button = driver.find_element_by_xpath('/html/body/form/div[3]/div/div/div[5]/div/div/div[1]/div/table/tbody/tr/td[2]/div/div/table[2]/tbody/tr[2]/td/div/table/tbody/tr['+str(i)+']/td[7]/a/span')
			
			# Parent handle
			parent_h = driver.current_window_handle
			
			# Switch to pop up window
			view_button.click()
			handles = driver.window_handles
			handles.remove(parent_h)
			driver.switch_to_window(handles.pop())
			
			# Get the data
			s_no = (loop*30) + i - 2
			name = driver.find_element_by_xpath('/html/body/form/div[3]/table/tbody/tr[3]/td[2]/span')
			father_husband = driver.find_element_by_xpath('/html/body/form/div[3]/table/tbody/tr[4]/td[2]/span')
			year_of_info = driver.find_element_by_xpath('/html/body/form/div[3]/table/tbody/tr[5]/td[4]/span')
			registration_no = driver.find_element_by_xpath('/html/body/form/div[3]/table/tbody/tr[6]/td[2]/span')
			registration_date = driver.find_element_by_xpath('/html/body/form/div[3]/table/tbody/tr[6]/td[4]/span')
			qualification = driver.find_element_by_xpath('/html/body/form/div[3]/table/tbody/tr[8]/td[2]/span')
			qualification_year = driver.find_element_by_xpath('/html/body/form/div[3]/table/tbody/tr[8]/td[4]/span')
			university = driver.find_element_by_xpath('/html/body/form/div[3]/table/tbody/tr[9]/td[2]/span')
			permanent_address = driver.find_element_by_xpath('/html/body/form/div[3]/table/tbody/tr[13]/td[2]/span')

			# Save the data
			doctors["s_no"] = s_no
			doctors["name"]=str(name.text)
			doctors["father_husband"] = str(father_husband.text)
			doctors["year_of_info"] = year_of_info.text
			doctors["registration_no"] = str(registration_no.text)
			doctors["registration_date"] = str(registration_date.text)
			doctors["qualification"] = str(qualification.text)
			doctors["qualification_year"] = qualification_year.text
			doctors["university"] = str(university.text)
			doctors["permanent_address"] = str(permanent_address.text)

			# Append the data
			data.append(doctors)

			# Close window
			# cancel = driver.find_element_by_id("Btn_Cancel")
			# cancel.click()
			# cancel = driver.find_element_by_xpath('/html/body/form/div[3]/table/tbody/tr[14]/td/input')

			# Move back to parent window
			driver.switch_to_window(parent_h)
			print doctors

		# Move to next page
		if loop == 0:
			next_button = driver.find_element_by_xpath('/html/body/form/div[3]/div/div/div[5]/div/div/div[1]/div/table/tbody/tr/td[2]/div/div/table[2]/tbody/tr[2]/td/div/table/tbody/tr[33]/td/table/tbody/tr/td[1]/a')
		else:
			next_button = driver.find_element_by_xpath('/html/body/form/div[3]/div/div/div[5]/div/div/div[1]/div/table/tbody/tr/td[2]/div/div/table[2]/tbody/tr[2]/td/div/table/tbody/tr[33]/td/table/tbody/tr/td[3]/a')			
		next_button.click()
	# =========================================================================

	myfile = open("data.json", "w")
	myfile.write(json.dumps(data))

	# Getting the page source and Parsing it

	"""
	This fails as things are dynamic
	# resp = requests.get(url)
	# html_doc = resp.content

	"""
	# using selenium
	html = driver.page_source

	soup = BeautifulSoup(html, 'html.parser')
	# soup = BeautifulSoup(html_doc, 'html.parser')
	file = open("scraped.html", "w")

	# Use encode('UTF-8'), else it fails on copyright symbol
	file.write(soup.prettify().encode('UTF-8'))

	# print(soup.prettify())

	print "\n\t\tSCRAPING IS DONE !! WHAT A RELIEF!!\n\n"

if __name__ == "__main__":
	main()