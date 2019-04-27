import Modules.Wiki as wiki

if __name__ == "__main__":
    Wi = wiki.Wikipedia()
    if Wi.Start("Sundar pichai") == 2:
        print("Unable to find information")
    
    print("== Sundar Pichai ==")
    Wi.GetInfoCard()
    for i in Wi.InfoCard:
        print(i + " : " + Wi.InfoCard[i])
