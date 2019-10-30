import wikipedia

search = input("What would you like to search?")
while search != " ":
    try:
        summary = wikipedia.summary(search)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    webpage = wikipedia.page(search)
    url = webpage.url
    title = webpage.title
    print(title, "\n", url, "\n", summary)
    search = input("What would you like to search?")
