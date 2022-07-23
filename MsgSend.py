from twilio.rest import Client
client = Client("ACc551339c4ebfe9e1d0aefc10599abc03", "d63dc43dac85adec50f70d95d1e9d8df")
b='skjd'
a="Hello" + b

client.messages.create(to="+917611073555", 
                       from_="+16105491075", 
                       body=a)
