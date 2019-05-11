import Modules.Wikipedia as wikipedia

if __name__ == '__main__':
    wikipedia.init("sundar pichai")

    if not wikipedia.exists():
        print("Unable to find information regarding sundar pichai")
        exit(0)

    print(wikipedia.defination)