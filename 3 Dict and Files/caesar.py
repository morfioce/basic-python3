# Caesar Cipher
# A cipher is a secret code for a language.
# We will explore a cipher that is reported by contemporary Greek historians
# to have been used by Julius Caesar to send secret messages to generals during times of war.

# The Caesar cipher shifts each letter of this message to another letter in the alphabet,
# which is a fixed number of letters away from the original.
# If our encryption key were 1, we would shift h to the next letter i, i to the next letter j,
# and so on.
# If we reach the end of the alphabet, which for us is the space character, we simply loop back to a.
# To decode the message, we make a similar shift,
# except we move the same number of steps backwards in the alphabet.

# Part 1
# Create a dictionary 'letters' with keys consisting of the numbers from 0 to 26,
# and values consisting of the lowercase letters of the English alphabet, including the space ' ' at the end.

# Let's look at the lowercase letters.
import string
# We will consider the alphabet to be these letters, along with a space.
alphabet = string.ascii_lowercase + " "


def letters_dict(alphabet):
	"""create letters dictionary"""
	return dict(enumerate(alphabet))

# Part 2
# Create a dictionary 'encoding' with keys being the characters in alphabet and values being numbers from 0-26,
# shifted by an integer encryption_key=3. For example, the key a should have value encryption_key,
# key b should have value encryption_key + 1, and so on.
# If any result of this addition is less than 0 or greater than 26,
# you can ensure the result remains within 0-26 using result % 27

# define `encoding` here!
def encoding_dict(alphabet, encryption_key):
	encoding = {}
	## your code goes here
	return encoding

# Part 3
# Write a function 'caesar(message, encryption_key)' to encode a message with the Caesar cipher.
# Use these values as keys in the dictionary 'letters' to determine the encoded letter for each letter in message.
# Your function should return a string consisting of these encoded letters.

def caesar(message, encryption_key):
    cipher = []
    ## your code goes here
    return ''.join(cipher)

def test(message, cipher, expected):
	if cipher == expected: ok = ' Ok '
	else: ok = ' X  '
	print('{} -- message: "{}" -- cipher: "{}" -- expected: "{}"'.format(ok, message, cipher, expected))

def main():
	test_data = [(3, "hi my name is caesar", 'klcpacqdphclvcfdhvdu'),
		     (3, 'this is a secret message', 'wklvclvcdcvhfuhwcphvvdjh'),
	  	     (7, 'hi my name is caesar', 'opgteguhtlgpzgjhlzhy'),
		     (7, 'this is a secret message', ' opzgpzghgzljyl gtlzzhnl')]
	for enk_key, message, expected in test_data:
		print('Test cases with enk_key = ',enk_key)
		test(message, caesar(message, enk_key), expected)

if __name__ == '__main__':
	main()
