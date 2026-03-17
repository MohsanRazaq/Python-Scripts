## only letter,digits,spaces are allowed
## remove trailing space --> i will use strip method-->convert to lowercase
## multiple space--> to single space//i do by keep record of first space by flag
## i have to  return dictionary containing digits,letters count

##-----------------------------------------------------------------------------------
def clean_data(text):
    clean = []
    data = text.strip().lower()

    space = False
    digit_count = 0
    letter_count = 0

    for ch in data:
        if ch.isalpha():
            clean.append(ch)
            letter_count += 1
            space = False

        elif ch.isdigit():
            clean.append(ch)
            digit_count += 1
            space = False

        elif ch == " " and not space:
            clean.append(ch)
            space = True

    clean_st = "".join(clean)
    words = clean_st.split()  # this handles every  space

    return {
        "clean": clean_st,
        "letters": letter_count,
        "digits": digit_count,
        "words": len(words)
    }
sample=" mohsan   razaq12   is!!  "
print(clean_data(sample))

