# mci-scraper
utility scraper using selenium and bs4 in python

## How to start:

- Clone the repo `cd && git clone https://github.com/manojpandey/mci-scraper.git && cd mci-scraper`

- setup virtualenv `virtualenv venv`

- `source venv/bin/activate`

- `pip install -r requirements.txt`

- Now, run the script `python main.py`

- Collected data will dump into `data.json` file, with attributes:

	- Example:

	{
		"name": "tarun suri",
		"university": "U.Punjabi",
		"registration_date": "02/08/2001",
		"registration_no": "11913",
		"year_of_info": "2001",
		"qualification": "MBBS",
		"father_husband": "kulbhushan suri",
		"permanent_address": "B/614, Panchvati Apartments, Vikaspuri, New Delhi-110018.",
		"qualification_year": "1988",
		"s_no": 30
	}
