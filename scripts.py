# Standardizes pronoun strings for analysis
def pronounClean(pronouns:str) -> str:
    if "," in pronouns:
        return pronouns.lower().strip().replace(",", "/")
    elif "/" not in pronouns:
        return pronouns.lower().strip().replace(" ", "/")
    else:
        return pronouns.lower().strip().replace(" ", "")


#Standardizes gender identity strings for analysis
def genderClean(gender:str) -> str:
    genderCleaned = gender.lower().strip()
    if " " in genderCleaned:
        genderCleaned = genderCleaned.replace(" ", "")
    if "(?)" in genderCleaned:
        genderCleaned = genderCleaned.replace("(?)", "")
    return genderCleaned
