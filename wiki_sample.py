import Modules.Wikipedia as wikipedia

if __name__ == '__main__':
    wiki = wikipedia.wikipedia("bill gates")
    if not wiki.exist() :
        print("Page not exist")
    print(wiki.defination())
