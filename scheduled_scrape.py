print("Script started")

from skraparen import scrape_site

def main():
    print("Inside main function")
    data = scrape_site()
    print("Data scraped:", data)

if __name__ == "__main__":
    main()
    print("Script finished")
