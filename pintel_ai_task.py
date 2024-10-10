import requests
from bs4 import BeautifulSoup
import re

# Step 1: Crawl the page and extract HTML
url = "https://www.sec.gov/Archives/edgar/data/200406/000020040624000013/jnj-20231231.htm"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Step 2: Clean the text by removing HTML tags and unnecessary content
def clean_text(text):
    # Remove extra spaces and newlines
    clean = re.sub(r'\s+', ' ', text)
    return clean.strip()

# Step 3: Extract sections and subsections
def extract_sections(soup):
    sections = []
    section_headers = soup.find_all(['h2', 'h3'])  # Assuming h2/h3 tags mark sections/subsections
    for header in section_headers:
        section = {}
        section_name = header.get_text(strip=True).lower()
        next_sibling = header.find_next_sibling()

        # Check if there is a subsection or direct content
        if next_sibling and next_sibling.name == 'h3':
            sub_section_name = next_sibling.get_text(strip=True).lower()
            content = clean_text(next_sibling.find_next_sibling().get_text())
        else:
            sub_section_name = ''
            content = clean_text(header.find_next_sibling().get_text())

        section["section_name"] = section_name
        section["sub_section_name"] = sub_section_name
        section["content"] = content
        sections.append(section)

    return sections

# Step 4: Get the structured data
data = extract_sections(soup)

# Print the output (list of dictionaries)
for entry in data:
    print(entry)

# Step 5: Select a section (for example 'risk') and analyze using LLM
risk_section = [entry for entry in data if 'risk' in entry['section_name']]

# Optional: Using OpenAI API for extracting risks
import openai

def analyze_risk(content):
    openai.api_key = 'Openai_api_key'
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"List 3-5 risks the company might be facing from the following text: {content}",
        max_tokens=200
    )
    return response.choices[0].text.strip()

# Analyze the risks
for entry in risk_section:
    risks = analyze_risk(entry['content'])
    print(f"Risks for section {entry['section_name']}: {risks}")

# Extract important phrases
def extract_phrases(text):
    return re.findall(r'\b\w{4,}\b', text)  # Example of extracting words with length >= 4

for entry in risk_section:
    phrases = extract_phrases(entry['content'])
    print(f"Important phrases for section {entry['section_name']}: {phrases}")
