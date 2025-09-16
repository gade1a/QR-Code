import qrcode 

data = "Opa, aqui é o gade1a!"

img = qrcode.make('https://www.linkedin.com/in/carlos-henrique-galkowski-402176250/')

img.save("qrcode_linkedin.png")