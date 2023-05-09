payload = {
    "url": "https://www.amazon.com/",
    "filters": {
        "crawl": [".*"],
        "process": [".*"],
        "max_depth": 1
    }, # Add the missing brace
    "scrape_params": {
        "user_agent_type": "desktop",
    },
    "output": {
        "type_": "sitemap"
    }
}