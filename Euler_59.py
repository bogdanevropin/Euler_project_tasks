"""
Each character on a computer is assigned a unique code and the preferred standard is ASCII
(American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value,
taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text,
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes.
The user would keep the encrypted message and the encryption key in different locations, and without both "halves",
it is impossible to decrypt the message.
Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key.
If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message.
The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.
Your task has been made easy, as the encryption key consists of three lower case characters.
Using a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words,
decrypt the message and find the sum of the ASCII values in the original text.
"""

import os

a = "11011111101100110110011001011101000"
b = "11001011101100111000011100001100001"
print(int(a, 2))
print(int(b, 2))
y = int(a, 2) ^ int(b, 2)
print(y)

print('{0:b}'.format(y))
a = 32
b = 35
y = a ^ b
print(y)

ROOT_DIR = os.getcwd()
with open(ROOT_DIR + '/data/Euler_59') as f:
	lines = f.readlines()
	num_list = lines[0].split(sep=',')
	print(num_list)
	bin_nums = []
	for num in num_list:
		bin_nums.append(chr(int(num)))
	print(bin_nums)
