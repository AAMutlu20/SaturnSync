<p align="center">
  <img src="logo/SaturnLogo.png" alt="SaturnSync Logo">
</p>

# SaturnSync Web Scraper

This Python script allows you to extract text information and image URLs from a website and provides options to save the data in various formats.

## Sample script input:

```plaintext
Enter the website URL: https://www.example.com

Text Data:
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Vestibulum eget ipsum vitae massa placerat feugiat.
Nunc eget ligula vel neque consequat dignissim.

Image URLs:
https://www.example.com/images/image1.jpg
https://www.example.com/images/image2.jpg

Save the data to a file? Enter 'txt', 'word', or 'none': txt
Enter the file path to save the TXT file: C:/path/to/save/data.txt
Data saved to TXT file: C:/path/to/save/data.txt

```

## Functionality

- Retrieves text information from the specified website and sorts it into paragraphs.
- Retrieves URLs of images from the website.
- Displays the extracted text data and image URLs.
- Offers options to save the data to a TXT file or Word file.

## Usage

1. Clone the repository or download the `web_scraper.py` file to your computer.

2. Install the required libraries:
- `pip install requests`
- `pip install beautifulsoup4`
- `pip install python-docx`
   
3. Run the script:
   python web_scraper.py

4. Enter the desired website URL when prompted.

5. The script will extract the data from the website and display it - the text data and image URLs.

6. Choose whether to save the data by entering one of the following options: 'txt', 'word' or 'none'.
- If you choose 'txt', specify the file path where to save the data as a TXT file.
- If you select 'word', specify the file path where to save the data as a Word file.
- If you select 'none', the data will not be saved.

7. The script will save the data to the specified path if you have selected it.

## Requirements

- Python 3.x
- Library Requests
- Library BeautifulSoup
- Library python-docx

## License

This project is licensed under the [MIT license](LICENSE).