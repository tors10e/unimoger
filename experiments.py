# ads = {'atl': [
#             {'title': 'Cool Unimog', 'url': 'http://sweet.com'},
#             {'title': 'Expensive Unimog', 'url': 'http://sweet.com'},
#             {'title': 'Expensive Unimog', 'url': 'http://sweet.com'}
#         ]
#        }
ads = [
        {'city': 'atl', 'url': 'http://sweet.com', 'title': 'cool unimog'},
        {'city': 'atl', 'url': 'http://sweet2.com', 'title': 'cooler unimog'},
        {'city': 'la', 'url': 'http://sweet.com', 'title': 'cool unimog'},
    ]

unique_ads = list({ad['url']: ad for ad in ads}.values())
print(unique_ads)

# ads['atl']['http://sweet.com']['title']
# ads.update({3: "three"})
# for city in ads:
#     print(city)
#     for ads[str(city)] in city:
#         print(url['title'])


thisset = {"apple", "banana", "cherry", "apple"}
thisset.add("apple")
print(thisset)