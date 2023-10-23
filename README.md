# Freelancer-Scrapy

A web scraping Scrapy spider for extracting project details from Freelancer.com, including project titles, prices, descriptions, tags, and client information.

## Prerequisites

Before running this spider, make sure you have the following prerequisites installed on your operating system:

- Python
- MongoDB

## Installation

1. Clone this repository to your local machine:

    git clone https://github.com/Amirhamidi2001/Freelancer-Scrapy.git

Change into the project directory:

    cd Freelancer-Scrapy

Install the required Python dependencies using pip:

    pip install -r requirements.txt

## Usage

The directory where the scrapy.cfg file resides is known as the project root directory.
Change into the configuration directory:

    cd freelancer

To run the spider, use the following command:

    scrapy crawl freelancer

The spider will start by visiting the initial page with Python and Django web scraping jobs on Freelancer.com and follow pagination links to scrape multiple pages of project listings. The extracted data will be stored in a MongoDB database.

The scraped data is stored in MongoDB in the following structure:

    MONGODB_DATABASE = "freelancer"
    MONGODB_COLLECTION = "items"

License

This project is licensed under the MIT License. See the LICENSE file for details.
