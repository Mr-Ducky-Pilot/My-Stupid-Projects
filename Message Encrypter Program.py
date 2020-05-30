
##Program to encode and decode two types of messages
import os

alphabhets = "abcdefghijklmnopqrstuvwxyz"
punchunations = " .,'?!$0123456789@()/\>< "

print()
print("====================================")
print()
print("Welcome to Message Encrypter/Cipher Program")
print()

again = "y"
while again.lower() == "y":
    print()
    print("Please Select the type of encrypter you would like to use:")
    print("For The Caesar Cipher select: 1" + "\nFor The Vigenère Cipher select: 2")
    type_chosen = int(input("Type/Select[1/2]: \t"))

##CAESAR CIPHER METHOD:
    if type_chosen == 1:
      print()
      print("You have chosen Caesar Cipher")
      print("Please Select:\nFor Encoding a message : a \nFor Decoding a message : b")
      select = input("Select[a/b] : \t")
      if select == 'a':
         print()
         message = str(input("Please Type the message you would like to Encode below : \n"))
         offset = int(input("Please select a offset: "))
         def encoding_message(message_to_encode, offset):
            encoded_message = ""
            for letter in message_to_encode.lower():
                if not letter in punchunations:
                    letter_value = alphabhets.find(letter)
                    encoded_message += alphabhets[(letter_value - offset) % 26 ]
                else:
                    encoded_message += letter
            return encoded_message
         print("The Encoded Message is : ")
         print(encoding_message(message, offset=10))
         print()
         
         again = input("Do you wish to Encode/Decode again? [y/n]: \n")
       
      if select == 'b':
         print()
         message = str(input("Please Paste/Type the message you would like to Decode below: \n"))
         offset = int(input("Please select a offset: "))
         def decoding_message(message_to_decode, offset):
             decoded_message = ""
             for letter in message_to_decode.lower():
                 if not letter in punchunations:
                     letter_value = alphabhets.find(letter)
                     decoded_message += alphabhets[(letter_value + offset) % 26 ]
                 else:
                      decoded_message += letter
             return decoded_message
         print("The Decoded Message is : ")
         print(decoding_message(message, offset=10))
         print()
         
         again = input("Do you wish to Encode/Decode again? [y/n]: \n")

##Note: Have set offset as defualt 10 in case the user doesn't input any.
##Note: The program seems to be working smoothly uptil now!!
## ==============END OF CAESAR CIPHER METHOD=============
        
##VIGENERE CIPHER MEHTOD:

    if type_chosen == 2:
      print()
      print("You have chosen Vigenère Cipher")
      print("Please Select:\nFor Encoding a message : a \nFor Decoding a message : b")
      select = input("Select[a/b] : \t")
    
      if select == 'a':
         print()
         message = str(input("Please Type the message you would like to Encode below : \n"))
         keyword = str(input("Please Type a Keyword below: \n"))
         def complex_encoding(message_to_encode, give_keyword):
             letter_pointer = 0
             keyword_final = ''
             message_to_encode = message_to_encode.lower()
             give_keyword = give_keyword.lower()
             for i in range(0,len(message_to_encode)):
                 if message_to_encode[i] in punchunations:
                     keyword_final += message_to_encode[i]
                 else:
                     keyword_final += give_keyword[letter_pointer]
                     letter_pointer = (letter_pointer+1)%len(give_keyword)
          
             encoded_message = ''
             for i in range(0,len(message_to_encode)):
                 if message_to_encode[i] not in punchunations:
                     ln = alphabhets.find(message_to_encode[i]) + alphabhets.find(keyword_final[i])
                     encoded_message += alphabhets[ln % 26]
                 else:
                      encoded_message += message_to_encode[i]
          
             return encoded_message
         print("The Encoded Message is : ")
         print(complex_encoding(message, keyword))
         print()
         
         again = input("Do you wish to Encode/Decode again? [y/n]: \n")
    
        
      if select == 'b':
         print()
         message = str(input("Please Paste/Type the message you would like to Decode below: \n"))
         keyword = str(input("Please Paste/Type the Keyword below: \n"))
         def complex_decoding(message_to_decode, keyword_given):
             letter_pointer = 0
             keyword_final = ''
             message_to_decode = message_to_decode.lower()
             keyword_given = keyword_given.lower()
             for i in range(0, len(message_to_decode)):
                 if message_to_decode[i] in punchunations:
                      keyword_final += message_to_decode[i]
                 else:
                      keyword_final += keyword_given[letter_pointer]
                      letter_pointer = (letter_pointer+1)%len(keyword_given)
    
             translated_message = ""
             for i in range(0,len(message_to_decode)):
                 if not message_to_decode[i] in punchunations:
                      ln = alphabhets.find(message_to_decode[i]) - alphabhets.find(keyword_final[i])
                      translated_message += alphabhets[ln % 26]
                 else:
                      translated_message += message_to_decode[i]
            
             return translated_message
         print("The Decoded Message is : ")
         print(complex_decoding(message, keyword))
         print()
         
         again = input("Do you wish to Encode/Decode again? [y/n]: \n")
         
##===================End Of Vigenere Cipher.=======================

print()
print("Thanks For Using This Program. Have Fun!")
print("===================================================")
          
  
