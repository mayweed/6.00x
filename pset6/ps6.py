#!/usr/bin/python

import string
import random

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print ('Loading word list from file...')
    # inFile: file
    with open(file_name, 'r') as in_file : 
        # line: string
        line = in_file.readline()
        # word_list: list of strings
        word_list = line.split()
        print ('{0} words loaded.'.format(len(word_list)))
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function
            load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        # no: use len + shift mod 26?? cf wikipedia
        minuscules=string.ascii_lowercase
        maj=string.ascii_uppercase
        dico={}

        for i in range(len(minuscules)):
        #c'est l'indice qui change ne pas oublier les () pour la précédence
        #cf 6.16 language ref
            dico[minuscules[i]]= minuscules[(i+shift)%26] 
        
        for i in range(len(maj)):
            dico[maj[i]]= maj[(i+shift)%26] 

        return dico

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''

        mess_to_encrypt=self.message_text
        dico=self.build_shift_dict(shift)
        encrypted_mess=''
        for letter in mess_to_encrypt:
            if letter in string.ascii_lowercase or letter in string.ascii_uppercase:
                encrypted_mess+=dico[letter]
            #we do not crypt those
            else:encrypted_mess+=letter
        return encrypted_mess

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''

        Message.__init__(self,text)
        self.shift=shift
        self.encrypting_dict=self.build_shift_dict(self.shift)
        self.message_text_encrypted=self.apply_shift(self.shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift=shift
        self.encrypting_dict=self.build_shift_dict(self.shift)
        self.message_text_encrypted=self.apply_shift(self.shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self,text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        alphabet=26
        original_shift=0
        best_shift=0

        for original_shift in range(0,26):
            decrypt_string=self.apply_shift(alphabet-original_shift)
            for word in decrypt_string.split(' '):
                if is_word(self.get_valid_words(),word):
                    best_shift=alphabet-original_shift

        if best_shift==26:
            #passes that way...
            return (0,self.apply_shift(0))
        else:
            return (best_shift,self.apply_shift(best_shift))

def decrypt_story():
    ciphertext=CiphertextMessage(get_story_string())
    return (ciphertext.decrypt_message())

#Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello', 2)
print ('Expected Output: jgnnq')
print ('Actual Output:', plaintext.get_message_text_encrypted())
    
#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('jgnnq')
ciphertext_bis = CiphertextMessage('Xyxcoxco gybnc')
ciphertext_ter = CiphertextMessage('cymsodi lkmugkbn wkbmr kvbokni \
dylkmmy gsvn ckn kmmeco cred loddob kmmozd kxqvo wokd combod aekbbov \
byzo cdbodmr xoon cywo mrsop zyfobdi crkuo wsxn vkeqr gbyxq pbyxd wynobx \
go coon drsop zbyfsno uxyg pbkwo csxqvo povvyg')
#print ('Expected Output:', (24, 'hello'))
#print ('Actual Output:', ciphertext.decrypt_message())
#print(ciphertext_bis.decrypt_message())
print(ciphertext_ter.decrypt_message())
