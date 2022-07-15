#Creates the Markdown (.md) file
fileName = input("What is the name of the file? ")
fileNameWithExtension = fileName + ".md"
mdFile = open(fileNameWithExtension, "w")
pOpen = "<p>"
pClose = "</p>"
h1Open = "<h1>"
h1Close = "</h1>"
h2Open = "<h2>"
h2Close = "</h2>"
h3Open = "<h3>"
h3Close = "</h3>"
h4Open = "<h4>"
h4Close = "</h4>"
h5Open = "<h5>"
h5Close = "</h5>"
h6Open = "<h6>"
h6Close = "</h6>"
br = "<br>"


running = True

while (running == True):
    inputtedElement = input("What element would you like to add (p, h1-6, br)? ")
    if (inputtedElement == "p" or inputtedElement == "P"):
        paragraphText = input("Enter your text here: \n")
        mdFile.write(pOpen + paragraphText + pClose + "\n")
    elif (inputtedElement == "h1" or inputtedElement == "H1"):
        h1Text = input("Enter your text here: \n")
        mdFile.write(h1Open + h1Text + h1Close + "\n")
    elif (inputtedElement == "h2" or inputtedElement == "H2"):
        h2Text = input("Enter your text here: \n")
        mdFile.write(h2Open + h2Text + h2Close + "\n")
    elif (inputtedElement == "h3" or inputtedElement == "H3"):
        h3Text = input("Enter your text here: \n")
        mdFile.write(h3Open + h3Text + h3Close + "\n")
    elif (inputtedElement == "h4" or inputtedElement == "H4"):
        h4Text = input("Enter your text here: \n")
        mdFile.write(h4Open + h4Text + h4Close + "\n")
    elif (inputtedElement == "h5" or inputtedElement == "H5"):
        h5Text = input("Enter your text here: \n")
        mdFile.write(h5Open + h5Text + h5Close + "\n")
    elif (inputtedElement == "h6" or inputtedElement == "H6"):
        h6Text = input("Enter your text here: \n")
        mdFile.write(h6Open + h6Text + h6Close + "\n")
    elif (inputtedElement == "br" or inputtedElement == "Br"):
        mdFile.write(br)
    elif (inputtedElement == "end" or inputtedElement == "End"):
        print("Goodbye!")
        mdFile.close()
        break
    else:
        print("I didn't understand that! Try again!")
