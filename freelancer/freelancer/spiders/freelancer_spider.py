from pathlib import Path
from freelancer.items import FreelancerItem

import scrapy
import os


# class FreelancerSpider(scrapy.Spider):
#     name = "freelancer"
#     start_urls = ["https://www.freelancer.com/"]

#     def parse(self, response):
#         directory = f"templates/"
#         filename = os.path.join(directory, f"freelancer.html")
#         Path(filename).write_bytes(response.body)
#         self.log(f"Saved file {filename}")


class FreelancerSpider(scrapy.Spider):
    name = "freelancer"
    start_urls = [
        "https://www.freelancer.com/jobs/python_django_scrapy_web-scraping/"
    ]

    # Define a callback function "parse" for processing the initial page
    def parse(self, response):
        # Iterate through each project on the page
        for project in response.css("div.JobSearchCard-primary-heading"):
            # Extract the URL for each project
            url = project.css("a.JobSearchCard-primary-heading-link::attr(href)").get()
            url = "https://www.freelancer.com" + url
            # Create a Scrapy Request to visit the project's URL and parse it
            yield scrapy.Request(url, callback=self.parse_project)

        # Extract pagination links and follow the "next" link if available
        pagination_links = response.css(
            "div.ProjectSearch-footer-pagination a.btn.Pagination-item"
        )
        for link in pagination_links:
            if link.attrib.get("rel") == "next":
                next_page_url = link.attrib["href"]
                # Follow the "next" link and continue parsing the next page
                yield response.follow(next_page_url, self.parse)

    # Define a callback function "parse_project" for processing individual project pages
    def parse_project(self, response):
        # Extract project details from the project page
        url = response.url
        title = response.css("h1::text").get()
        price = response.css("p.PageProjectViewLogout-projectInfo-byLine::text").get()
        detail = response.css("div.PageProjectViewLogout-detail p::text").get()
        tags = response.css("p.PageProjectViewLogout-detail-tags a::text").getall()
        about = response.css(
            "div.PageProjectViewLogout-detail-summary span::text"
        ).getall()
        client = response.css(
            "div.PageProjectViewLogout-detail-reputation-employerInfo span::text"
        ).getall()

        # Create an instance of the "FreelancerItem" to store the extracted data
        item = FreelancerItem()
        item["url"] = url
        item["title"] = title
        item["price"] = price
        item["detail"] = detail
        item["tags"] = [obj.strip() for obj in tags]
        item["about"] = [obj.strip() for obj in about if len(obj.strip()) > 1]
        item["client"] = [obj.strip() for obj in client if len(obj.strip()) > 1]

        # Yield the item to be processed and stored by Scrapy
        yield item
