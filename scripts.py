import csv


def openSurveyCSV(filePath: str, fieldname:str = None) -> str:
    # I/O for our survey CSV file
    with open(filePath, "r") as csvfile:
        
        # Returns a dictionary for more explicit column names
        reader = csv.DictReader(csvfile)
        
        # If a fieldname is specified, this will return that csv column
        if fieldname:
            results = [row[fieldname] for row in reader]
            return results
        else:
            # Prints each case in our data set 
            results = [row for row in reader]
            return results


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


# Counts number of transfer and non-transfer students
def transferCount(transferStatus):
    transferCounter = 0
    nonTransferCounter = 0
    
    for status in transferStatus:
        if status == "Yes":
            transferCounter += 1
        else:
            nonTransferCounter += 1
        
    print(f"Number of Transfer Students: {transferCounter}")
    print(f"Number of non-Transfer Students: {nonTransferCounter}")
