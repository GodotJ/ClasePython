email = input("ingresa tu correo elecatronico:  ").strip()
username= email[:email.index('@')]
domain = email[email.index('@')+1:]

if domain == "gmail.com":
    annex = "I see your email is registered with Google. That's cool!."
elif domain == "outlook.com":
    annex = "I see your email is registered with Microsoft. That's cool!."
elif domain == "hotmail.com":
    annex = "I see your email is registered with Microsoft. That's cool!."
else:
    annex = "looks like you've got your own custom setup at MyFantasy. Impressive!"

result = "Tu nombre de usuario es: "+username+"\nEl dominio es: "+domain+" "+annex
print(result)