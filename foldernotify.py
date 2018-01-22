# foldernotify.py
# Author: Josh Smith

filename = "contact.txt"

def get_contacts(filename):
	contacts = []
	with open(filename, mode='r', encoding='utf-8') as contact_file:
		for contact in contact_file:
			contacts.append(contact)
	return contacts


if __name__ == "__main__":
	for contact in get_contacts(filename):
		print(contact)
		