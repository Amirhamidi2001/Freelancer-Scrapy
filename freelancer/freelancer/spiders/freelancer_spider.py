from pathlib import Path

import scrapy
import os


class FreelancerSpider(scrapy.Spider):
    name = "freelancer"
    start_urls = ["https://www.freelancer.com/"]

    def parse(self, response):
        directory = f"templates/"
        filename = os.path.join(directory, f"freelancer.html")
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
