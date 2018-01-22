# foldernotify.py
# Author: Josh Smith

import os

contact_filename = 'contact.txt'
folder_filename = 'fdir.txt'

def get_contacts():
	contacts = []
	with open(contact_filename, mode='r', encoding='utf-8') as contact_file:
		for contact in contact_file:
			contacts.append(contact)
	return contacts


# Gets contents of folder that contains intern tasks
def get_folder_contents():
	fdir = open(folder_filename, mode='r', encoding='utf-8').read().splitlines()[0]
	files = [f for f in os.listdir(fdir) if os.path.isfile(f)]
	return files


if __name__ == "__main__":
	print("Contacts:")
	for contact in get_contacts():
		print("\t- " + contact)
	print("Folder Contents:")
	for file in get_folder_contents():
		print("\t- " + file)
		