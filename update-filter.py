#!/usr/bin/env python

__author__ = "Pourliver - https://github.com/Pourliver"
__version__ = "1.0"

import os
import re
import requests
import shutil
import zipfile
from bs4 import BeautifulSoup

############# Custom filter location
#You may update the following variables to specify a custom PoE filter path.

current_user_path = os.environ["USERPROFILE"]
folder_location = current_user_path + "\Documents\My Games\Path of Exile"
zip_location = folder_location + "\\temp.zip"
created_content = []

def main():
	url = "https://github.com/NeverSinkDev/NeverSink-Filter/releases/latest"

	print("Neversink's itemfilter updater, made by Pourliver.")

	os.chdir(folder_location)
	result = requests.get(url)
	download_file(find_latest_filter(result))
	move_files(extract_files())
	cleanup()

	print("Done!")
	os.system('pause')

def find_latest_filter(result):
	soup = BeautifulSoup(result.content, "html.parser")
	print("Found version :", soup.find("div", class_="release-header").a.text)
	
	for a in soup.find_all('a', href=True):
		if ".zip" in a["href"]:
			return "https://github.com/" + a["href"]

def download_file(url):
	print("Downloading from :", url)

	r = requests.get(url, stream=True)

	with open(zip_location, 'wb') as f:
		for chunk in r.iter_content(chunk_size=1024):
			if chunk: # filter out keep-alive new chunks
				f.write(chunk)
	created_content.append(zip_location)

def extract_files():
	print("Extracting to :", folder_location)

	zip_ref = zipfile.ZipFile(zip_location)
	extracted_archive_path = folder_location + "\\" + zip_ref.infolist()[0].filename[:-1]
	for info in zip_ref.infolist():
		if re.match(r'.*\.filter', info.filename) and info.filename.count("/") == 1:
			zip_ref.extract(info.filename)
	zip_ref.close()

	created_content.append(extracted_archive_path)
	return extracted_archive_path

def move_files(path):
	for filename in os.listdir(path):
		src = path + "\\" + filename
		dst = folder_location + "\\" + filename
		shutil.move(src, dst)

def cleanup():
	print("Cleaning up...")

	for folder in created_content:
		if folder[-4:] == ".zip":
			os.remove(folder)	
		else:
			shutil.rmtree(folder)

if __name__ == "__main__":
    main()