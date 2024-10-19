import requests

EBAY_API_TOKEN = "v^1.1#i^1#r^0#p^1#I^3#f^0#t^H4sIAAAAAAAAAOVYe2wURRjv9QUFSmNoRAmSy0JQrLu3u7d3vdv0Llxf9IDSwpWGNiLs7c62S/flzizt+cqlQKMQFEyURPgDUdDQSEwb8An+VxAMjygINMQXgjFG0T/ExKDObR9cK4FCL7GJl0s2M/N933zfb77XDJ3ML3i0q6breqFrUvbuJJ3MdrmYqXRBfl7J9JzsWXlZdBqBa3dyXjK3M+eHMihoqsmvANA0dAjcHZqqQ96ZDBG2pfOGABXI64IGII9EPhapXcqzFM2bloEM0VAJd7QyRLClQBQlr0/2cUHOz/rxrD4ks8EIET6ODvp8cdpHe0sZPwjgdQhtENUhEnSE+WmWIxmaZHwNLMP7GJ7lKNrLNBPuRmBBxdAxCUUTYUdd3uG10nS9vaoChMBCWAgRjkaqY3WRaGXVsoYyT5qs8CAOMSQgG44cVRgScDcKqg1uvw10qPmYLYoAQsITHthhpFA+MqTMPajvQC0GSzk5DrxcgAmygp/LCJTVhqUJ6PZ6pGYUiZQdUh7oSEGJOyGK0YivAyIaHC3DIqKV7tRnuS2oiqwAK0RUlUeaIvX1RHix0NICrGaVrDORoglqPRkrX0XSAYB9JhD0kgGR8wMhKA9uNCBtEOZRO1UYuqSkQIPuZQYqB1hrMBobLg0bTFSn11kRGaU0SqfzDmHIYjrP0CnaqFVPnSvQMBBuZ3jnExjmRshS4jYCwxJGLzgQhQjBNBWJGL3o+OKg+3TAENGKkMl7PO3t7VS7lzKsFg9L04xnVe3SmNgKNIHAtKlYH6BX7sxAKo4pIsCcUOFRwsS6dGBfxQroLUSYY4N+r3cQ95FqhUfP/msizWbPyIjIVIQwQiDgpf0CJ4oBHyMFMxEh4UEn9aT0AHEhQWqC1QaQqQoiIEXsZ7YGLEXicQ5kvQEZkJI/KJNcUJbJuE/yk4wMAA1APC4GA/+nQBmrq8eAaAGUEV/PmJ/HVvqrVpiAaapZwrWrbDNcsiJaJcWaFpkxqW59c3VzQEiUdBgyCFSFxhoNtzS+QlUwMg14/0wAkIr1zIFQY0AEpHGZFxMNE9QbqiImJtYBey2pXrBQotxO4HEMqCr+jMvUiGlGM5OxM2bkXSaLe7M7c5XqP6pSt7QKphx3YlmV4odYgGAqFK5DqVhPUKKheQwBNyGp6TWO1u5RhLck8sTtBNViA4iwJhLuA8fMpOBkTuGSJo2dZaBgYiPGzoIvGZItonvayKnMFEZTaWlF8K727BgPKHFbbRs7iwQEdVwuquCrxoRyUGzpgMmKNHBHoBy7KbhepCwADdvC1yOqLtUyNxhtQMcNCLIMVQVWIzPu1KtpNhLiKphoOTgDuUjBse76Y4J1SEwpG6TxP8CNyzbR6X/WTLQKkunKeRc3Ic/Id5lwlvNjOl3H6U5XX7bLRVfirruEXpCfszI3ZxoBce6hoKBLcaODUgSZwmlPF5BtAaoNJExBsbJnZJ14Muux5JQaz7ubH+8saViXyJqc9jy0ezX9wPADUUEOMzXttYiefXMljymaWchyDM34WMbHsFwzPffmai5zf25x75FLR94q7L628GrX/pkX5xib+08bdOEwkcuVl4V9OUv2Xnmpf/lrx789eHrvEx/0X8g/9t3FLRuzyxs3fBU9VbZHK9jyxTt9s45+s+ckm0eVTS/Kf+qZcO37/ecPFL9ZpD/S80v981dfOXbu6wXPTbNf757Enjn3trT1xsOrLx1ILAh/sndO5PjlufP3rX0hX+7ZduHp3+GLP3/+5aK1U5O7ets/3ff95c9q9zz08brWXRU7L+ovb/wtsuPMfu6+mvDWTeSDPfOnHL7eV3nIZIsPVmxaf9a7fcdHR+bdmN2t7bq2oae6r3gh+jD46ubDM7edbf3x0MGTb8ywou6jVnsshzlV2zX5XMn5v3o3eWYt3tc96WRvkYt/ltvpP6O9l7xiX/u1qaKx9u/AT39uj50YONN/ANI2gQi4EwAA"  
EBAY_API_URL = "https://api.sandbox.ebay.com/buy/browse/v1/item_summary/search"  

def search_ebay(query):
    headers = {
        'Authorization': f'Bearer {EBAY_API_TOKEN}',
        'Content-Type': 'application/json',
    }
    params = {
        'q': query,  # Your search query, like 'graphics card'
        'limit': 3  # Limit to 3 results
    }
    response = requests.get(EBAY_API_URL, headers=headers, params=params)

    if response.status_code == 200:
        print("Success: Data retrieved.")
        return response.json()  # Return the JSON response from eBay API
    else:
        print(f"Error: {response.status_code}")
        return None

if __name__ == "__main__":
    query = "laptop"  # Test query
    result = search_ebay(query)
    if result:
        print(result)  # This will print out the raw JSON response from eBay's API
    else:
        print("No results or an error occurred.")
