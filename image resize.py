from  PIL import  Image

im=Image.open("img.png")
print(im.size)
new_size=im.resize((500,400))
print(new_size.size)
new_size.show()


