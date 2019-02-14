from cryptography.fernet import Fernet
print("\n\n\nHey! \nThis program can help you with crypting text files.\nYou can use your own key!\nCrypted text will be saved in file 'output.txt' in the same directory. \nVersion: 1.0\n\n14.02.2019 // zahm\n\n\n")
select = raw_input("Encrypt or decrypt? e/d : ")
if select == "e":
	key_select = raw_input("\nEnter the key (43 symbols) or press enter if you wanna to generate random key: ")
	if key_select == "":
		key = Fernet.generate_key()
	if key_select != "":
		key = str(key_select) + "="
	f = Fernet(key)
	ft = raw_input("\nText or file? t/f : ")
	if ft == "t":
		input = raw_input("\nEnter the text for encrypt: ")
		output = f.encrypt(input)
		print("\nSucces! Your crypted text > \n\n\n" + str(output) + "\n\n\nYour key is > " + str(key) + "\n")
	if ft == "f":
		name = raw_input("\nEnter name of the file: ")
		file = open(str(name), 'r')
		input = file.read()
		output = f.encrypt(input)
		save = open('encrypted.txt', 'w')
		save.write(output)
		print("\nSuccess! Your crypted file saved as 'encrypted.txt' and key is > " + str(key) + "\n")
if select == "d":
	key = raw_input("\nEnter the key: ")
	ft = raw_input("\nText or file? t/f : ")
	if ft == "t":
		f = Fernet(key)
		input = raw_input("\nEnter the crypted text: ")
		output = f.decrypt(input)
		print '\nSuccess! Text is >\n\n', str(output), '\n'
	if ft == "f":
		name = raw_input("\nEnter name of the crypted file: ")
		f = Fernet(key)
		file = open(str(name), 'r')
		input = file.read()
		output = f.decrypt(input)
		save = open('decrypted.txt', 'w')
		save.write(output)
		print("\nSuccess! Your decrypted file saved as 'decrypted.txt'!\n")
