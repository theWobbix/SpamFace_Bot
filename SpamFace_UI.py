import SpamFace_Request as SF

#program start
print("--------SpamFace Bot 2018--------\n\nTo use the bot, follow the instructions given below: ")


email =     input("Type im a Email or Phonenumber that belongs to a Facebookaccount ->")
anmount =   input("Type in how often the Bot should send a request                  ->")


SF.request(email, int(anmount))

print("\n--------Process started--------")

