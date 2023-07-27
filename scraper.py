import os
import requests
from bs4 import BeautifulSoup

url = 'https://engineering.buffalo.edu/computer-science-engineering/people/faculty-directory.html'
html = requests.get(url)

s = BeautifulSoup(html.content, 'html.parser')
quotes = []

results = s.find(id='center')
faculty_members = results.find_all('div', class_='profileinfo-teaser-name')

# Save the list of URLs to 'urls.txt' in the current working directory
filename_urls = 'urls.txt'
with open(filename_urls, 'w', encoding='utf-8') as file:
    for link in results.find_all('a', href=True):
        url = link['href']
        if url.endswith('.html'):
            file.write(url + '\n')

print(f"URLs have been saved to {filename_urls}.")

# Save the faculty member data to 'Bios.txt' in the current working directory
filename_faculty = 'Bios.txt'
with open(filename_faculty, 'w', encoding='utf-8') as file:
    for faculty in faculty_members:
        faculty_member = {}  # Create a dictionary to store faculty member data
        faculty_member['name'] = faculty.text.strip()

        # Find the other details for the same faculty member
        faculty_member['bio'] = faculty.find_next('div', class_='profileinfo-teaser-dept').text.strip()
        
        # Add the faculty member data to the 'quotes' list
        quotes.append(faculty_member)

        file.write(f"Name: {faculty_member['name']}\n")
        file.write(f"Bio: {faculty_member['bio']}\n")
        file.write("\n")

print(f"Faculty member data has been saved to {filename_faculty}.")


with open('courses_taught.txt', 'w', encoding='utf-8') as file:
    for faculty in faculty_members:
        faculty_member = {}  # Create a dictionary to store faculty member data
        faculty_member['name'] = faculty.text.strip()
        faculty_member['subject'] =faculty.find_next('div', class_='profileinfo-teaser-interests').text.strip()

        file.write(f"Name: {faculty_member['name']}\n")
        file.write(f"Subject: {faculty_member['subject']}\n")
        file.write("\n")

print("Faculty member data has been saved to courses_taught.txt.")

