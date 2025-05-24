def removeVirus(files: str):
    output = ""
    for file in files.split():
        if "virus" in file or 'malware' in file:
            if "not" in file or "anti" in file:
                output += file + ' '
            else:
                pass
        else:
            output += file + ' '
    print(output)

removeVirus("PC Files: spotifysetup.exe, virus.exe, dog.jpg")
#output = "PC Files: spotifysetup.exe, dog.jpg"

removeVirus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe ")
#output = "PC Files: antivirus.exe, cat.pdf"

removeVirus("PC Files: notvirus.exe, funnycat.gif")
#output = "PC Files: notvirus.exe, funnycat.gif"