def actualMemorySize(memorySize: str):
    memory = "".join(filter(str.isdigit, memorySize))
    if "GB" in memorySize:
        memory = int(memory) * 1000 
    memoryLoss = int(memory) * 0.07
    memory = round(int(memory) - memoryLoss, 2)
    if int(memory) >= 1000:
        memory = int(memory) / 1000
        print(str(memory) + "GB")
    else:
        print(str(memory) + "MB")


actualMemorySize("32GB")
#output = "29.76GB"

actualMemorySize("2GB")
#output = "1.86GB"

actualMemorySize("512MB")
#output = "476MB"