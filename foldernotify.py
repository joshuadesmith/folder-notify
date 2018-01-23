# foldernotify.py
# Author: Josh Smith

import os, smtplib

contact_filename = 'contact.txt'	# Text file that contains emails
folder_filename = 'fdir.txt'		# Text file that contains directory to be monitored
login_filename = 'login.txt'		# Text file that contains login info for outgoing email


# Gets the emails to which notification messages will be sent
def get_contacts():
	contacts = []
	with open(contact_filename, mode='r', encoding='utf-8') as contact_file:
		for contact in contact_file:
			contacts.append(contact)
	return contacts


# Gets login info from text file
def get_login_info():
	file_lines = open(login_filename, mode='r', encoding='utf-8').read().splitlines()
	return file_lines[0], file_lines[1]


# Sends an email to each contact
def notify(contacts, current_folder_contents, added, removed):
	user, password = get_login_info()
	try:
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.ehlo()
		server.login(user, password)

		server.sendmail(user, contacts[0], 'TEST')
		server.close()

		print 'SUCCESS'
	except:
		print 'Error occurred while setting up SMTP server'


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
			# notify(contacts, current_folder_contents, added, removed)
		else:
			# TODO: print message indicating no new files


if __name__ == "__main__":
	print 'MUST IMPLEMENT'
		
		