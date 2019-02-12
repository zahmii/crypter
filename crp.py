from cryptography.fernet import Fernet
print("\n\n\nHey! \nThis program can help you with crypting text files.\nYou can use your own key!\nCrypted text will be saved in file output.txt in the same directory. \nVersion: 0.3\n\n12.02.2019/zahm\n\n\n")
select = raw_input("Encrypt or decrypt? e/d > ")
if select == "e":
	key_select = raw_input("Enter the key (43 symbols) or press enter if you wanna to generate random key: ")
	if key_select == "":
		key = Fernet.generate_key()
	if key_select != "":
		key = str(key_select) + "="
	f = Fernet(key)
	name = raw_input("Enter name of the file: ")
	file = open(str(name), 'r')
	input = file.read()
	output = f.encrypt(input)
	save = open('output.txt', 'w')
	save.write(output)
	print 'Success! Your crypted file saved as "output.txt" and key is >', str(key)
if select == "d":
	name = raw_input("Enter name of the crypted file: ")
	key = raw_input("Enter the key: ")
	f = Fernet(key)
	file = open(str(name), 'r')
	input = file.read()
	output = f.decrypt(input)
	print 'Success! Text is >\n\n', str(output), '\n\n'

