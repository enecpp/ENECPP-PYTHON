import webbrowser

def search(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

if __name__ == "__main__":
    query = input("Bir sey mi aramak istiyorsunuz? : ")
    search(query)