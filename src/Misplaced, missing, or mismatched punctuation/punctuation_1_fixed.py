payload = {
    "source": "universal",
    "url": "https://sandbox.oxylabs.io/products/1",
    "parse": True,
    "parsing_instructions": {
        "title": {
            "_fns": [
                {
                    "_fn": "css_one",
                    "_args": ["h2"]
                }
            ]
        }
    }
} # Add the missing brace
