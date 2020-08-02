def alphabet_position(text):
    mt = ""
    for i in range(len(text)):
        if text[i].isalpha() and text[i] in "abcdefghijklmnopqrstuvwxyz":
            position = str((ord(text[i] - 64)))
            mt = mt + position
        elif text[i].isalpha() and text[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            position = str((ord(text[i] - 96)))
            mt = mt + position
        print(mt)
        return mt
        pass
    alphabet_position("abcdefghijklmnopqrstuvwxyz  ABCDEFGHIJKLMNOPQRSTUVWXYZ")