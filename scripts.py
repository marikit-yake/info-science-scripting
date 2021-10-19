# Standardizes pronoun strings for analysis
def pronounClean(pronouns:str) -> str:
    pronounsCleaned = pronouns.lower().strip()
    if "," in pronouns:
        return pronouns.replace(",", "/")
    elif "/" not in pronouns:
        return pronouns.replace(" ", "/")
    else:
        return pronouns.replace(" ", "")


#Standardizes gender identity strings for analysis
def genderClean(gender:str) -> str:
    genderCleaned = gender.lower().strip()
    if " " in genderCleaned:
        genderCleaned = genderCleaned.replace(" ", "")
    if "(?)" in genderCleaned:
        genderCleaned = genderCleaned.replace("(?)", "")
    return genderCleaned
