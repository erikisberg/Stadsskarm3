from skraparen import scrape_site

def main():
    data = scrape_site()
    for item in data:
        print(item)

if __name__ == "__main__":
    main()
