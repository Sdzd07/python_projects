#Using Enumerate make all the sentences in the list upper case and replace spaces with dashes
sentences = ['Hello from Codezilla', 'Python Course is awesome', 'I enjoy learning Python with you']
for index,sentence in enumerate(sentences):
    sentences[index] = sentences[index].replace(" ","_").upper()    
print("The modified list of sentences is:")
print(sentences)
    #print(sentence)
    