from cryptography.fernet import Fernet
select = raw_input("Encrypt or decrypt? e/d > ")
if select == "e":
	key = Fernet.generate_key()
	f = Fernet(key)
	name = raw_input("Enter name of the file: ")
	file = open(str(name), 'r')
	input = file.read()
	output = f.encrypt(input)
	save = open('output.txt', 'w')
	save.write(output)
	print 'Success! Your crypted file saved as "output.txt" and key is >', str(key)
if select == "d":
	name = raw_input("Eneter name of the crypted file: ")
	key = raw_input("Enter the key: ")
	f = Fernet(key)
	file = open(str(name), 'r')
	input = file.read()
	output = f.decrypt(input)
	print 'Success! Text is >\n\n', str(output), '\n\n'

