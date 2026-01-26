from config import tools as configTools

def main():
    pass

def testLine():
    print(configTools.compileDefault(configTools.default))
    print(configTools.extractLanguage(configTools.defaultCompiled))

if __name__ == "__main__":
    main()
