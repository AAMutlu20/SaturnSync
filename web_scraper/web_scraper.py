import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from docx import Document

def get_website_data(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the text information and sort it into paragraphs
    paragraphs = []
    for paragraph in soup.find_all('p'):
        text = paragraph.get_text().strip()
        if text:
            paragraphs.append(text)
    
    # Extract the image URLs
    image_urls = []
    for img in soup.find_all('img'):
        img_url = img.get('src')
        if img_url:
            image_urls.append(urljoin(url, img_url))
    
    return sorted(paragraphs), image_urls

def save_to_txt(paragraphs, file_path):
    with open(file_path, 'w') as file:
        for paragraph in paragraphs:
            file.write(paragraph + '\n')

def save_to_word(paragraphs, file_path):
    doc = Document()
    for paragraph in paragraphs:
        doc.add_paragraph(paragraph)
    doc.save(file_path)

def display_website_data(url):
    paragraphs, image_urls = get_website_data(url)
    
    # Display the paragraphs
    print('Text Data:')
    for paragraph in paragraphs:
        print(paragraph)
        print()
    
    # Display the image URLs
    print('Image URLs:')
    for img_url in image_urls:
        print(img_url)

    # Prompt the user for save option
    save_option = input("Save the data to a file? Enter 'txt', 'word', or 'none': ")
    if save_option == 'txt':
        file_path = input("Enter the file path to save the TXT file: ")
        save_to_txt(paragraphs, file_path)
        print("Data saved to TXT file.")
    elif save_option == 'word':
        file_path = input("Enter the file path to save the Word file: ")
        save_to_word(paragraphs, file_path)
        print("Data saved to Word file.")
    elif save_option == 'none':
        print("Data not saved.")
    else:
        print("Invalid option. Data not saved.")

# Prompt the user to enter a website URL
website_url = input("Enter the website URL: ")

# Call the function to display the website data
display_website_data(website_url)
