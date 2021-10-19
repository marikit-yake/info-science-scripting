import csv


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


# Loads in CSV data from a specified filepath
def openSurveyCSV(filePath: str) -> str:
    
    # I/O for our survey CSV file
    with open(filePath, "r") as csvfile:
        
        # Returns a dictionary for more explicit column names
        reader = csv.DictReader(csvfile)
        
        # Prints each case in our data set 
        for row in reader:
            print(row)    # Modify this line to capture each specific field
