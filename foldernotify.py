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

# Gets difference in intern task folder
# Returns 1) new folder contents 2) list of added files, 3) list of removed files
def get_folder_diff(folder_contents):
	added = []
	removed = []
	new_folder_contents = get_folder_contents()
	if folder_contents:
		if not new_folder_contents:
			removed = folder_contents
		else:
			removed = [f for f in folder_contents if f not in new_folder_contents]
			added = [f for f in new_folder_contents if f not in folder_contents]
	else:
		if folder_contents:
			added = folder_contents;
	return new_folder_contents, added, removed


# Main function
# wait_time = number of minutes to wait before iterating loop
# TODO: Implement wait function
# TODO: Implement notify function
def main():
	current_folder_contents = get_folder_contents()
	while True:
		# wait()
		current_folder_contents, added, removed = get_folder_diff(current_folder_contents)
		if added:
			# notify(current_folder_contents, added, removed)
		else:
			# TODO: print message indicating no new files


if __name__ == "__main__":
	print("Contacts:")
	for contact in get_contacts():
		print("\t- " + contact)
	print("Folder Contents:")
	for file in get_folder_contents():
		print("\t- " + file)
		