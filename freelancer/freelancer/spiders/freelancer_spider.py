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
    start_urls = ["https://www.freelancer.com/jobs/python_django_web-scraping/"]

    def parse(self, response):
        for project in response.css("div.JobSearchCard-primary-heading"):
            url = project.css("a.JobSearchCard-primary-heading-link::attr(href)").get()
            url = "https://www.freelancer.com" + url
            yield scrapy.Request(url, callback=self.parse_project)

        pagination_links = response.css(
            "div.ProjectSearch-footer-pagination a.btn.Pagination-item"
        )
        for link in pagination_links:
            if link.attrib.get("rel") == "next":
                next_page_url = link.attrib["href"]
                yield response.follow(next_page_url, self.parse)

    def parse_project(self, response):
        title = response.css("h1::text").get()
        price = response.css("p.PageProjectViewLogout-projectInfo-byLine::text").get()
        detail = response.css("div.PageProjectViewLogout-detail p::text").get()
        tags = response.css("p.PageProjectViewLogout-detail-tags a::text").getall()
        client = response.css(
            "div.PageProjectViewLogout-detail-reputation-employerInfo span::text"
        ).getall()

        item = FreelancerItem()
        item["title"] = title
        item["price"] = price
        item["detail"] = detail
        item["tags"] = [obj.strip() for obj in tags]
        item["client"] = [obj.strip() for obj in client if len(obj.strip()) > 1]

        yield item
