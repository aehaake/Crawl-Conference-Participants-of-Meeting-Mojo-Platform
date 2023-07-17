# Importing necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Cookie and header information for the requests -> Replace them with your session identifiers
cookies = {
    '_gid': 'XXX',
    '_gat_globaltracker': 'XXX',
    'twk_idm_key': 'XXX',
    'frontend': 'XXX',
    'mojoremember': 'XXX',
    '_ga_6KTXZG6V3K': 'XXX',
    '_ga': 'XXX',
    'TawkConnectionTime': 'XXX',
    'twk_uuid_5ef9c6564a7c6258179b884c': 'XXX'}

headers = {
    'authority': 'XXX.meeting-mojo.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'de-DE,de;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://XXX.meeting-mojo.com/search',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

# Maximum number of pages to scrape
maxPages = 41

# Initialize list to store scraped data
newList = []

# Iterating over each page
for p in range(maxPages):
    print(p)
    params = (
        ('page', '{0}'.format(p)),
    )

    # Send a GET request to the URL
    response = requests.get('https://xxxx.meeting-mojo.com/search',
                            headers=headers, params=params, cookies=cookies)

    # Parse the response content with BeautifulSoup
    soup = BeautifulSoup(response.content, "lxml")
    
    # Find all elements with the specified class
    liste = soup.find_all("div", {"class": "search-item-wrapper toggle-short"})
    
    # Iterate over each element in the list
    for el in liste:
        # Extract question and answer pairs
        qa = el.find("div", {"class": "organisation"}).find_all("div", {"class": "profile-answer"})
        qaErg = {t.find("div", {"class": "profile-question"}).text: t.text.replace(t.find("div", {"class": "profile-question"}).text, "").strip() for t in qa}

        # Extract team information
        team = "\n".join([f"{person.find('h5').text.strip()}: {person.text.replace(person.find('h5').text.strip(), '').strip()}" for person in el.find_all("div", {"class": "attendee-profile"})])
        
        # Extract country and URL if available
        country = el.find("div", {"class": "organisation"}).find("img")["alt"].strip() if el.find("div", {"class": "organisation"}).find("img") else ""
        url = el.find("div", {"class": "organisation"}).find("a")["href"].strip() if el.find("div", {"class": "organisation"}).find("a") else ""

        # Append the scraped data to the list
        newList.append({
            "name": el.find("div", {"class": "organisation"}).find("h3").text.strip(),
            "country": country,
            "url": url,
            "team": team,
            **qaErg,
        })

# Convert the list into a pandas DataFrame
df = pd.DataFrame(newList)

# Display the DataFrame
print(df)

# Export the DataFrame to an Excel file
df.to_excel("export_participants.xlsx")
