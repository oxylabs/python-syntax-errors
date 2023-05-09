def extract_product_data():
    for url in product_urls:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find("h1").text
        price = soup.find("span", {"itemprop": "price"}).text
        product_data.append({
            "title": title,
            "price": price,
        })