import pandas as pd


filePath = "./survey-data/survey-response-data.csv"


# Standardizes pronoun strings for analysis
def pronounClean(pronouns:str) -> str:
    pronounsCleaned = pronouns.lower().strip()
    if "," in pronouns:
        pronounsCleaned = pronounsCleaned.replace(",", "/")
        return pronounsCleaned.replace(" ", "")
    elif "/" not in pronouns:
        pronounsCleaned = pronounsCleaned.replace(" ", "/")
        return pronounsCleaned.replace(" ", "")
    else:
        return pronounsCleaned.replace(" ", "")

#Standardizes gender identity strings for analysis
def genderClean(gender:str) -> str:
    genderCleaned = gender.lower().strip()
    if " " in genderCleaned:
        genderCleaned = genderCleaned.replace(" ", "")
    elif "(?)" in genderCleaned:
        genderCleaned = genderCleaned.replace(" ", "")
        genderCleaned = genderCleaned.replace("(?)", "")
        return genderCleaned.replace(" ", "")
    elif "," in genderCleaned:
        genderCleaned = genderCleaned.replace(",", "/")
        return genderCleaned.replace(" ", "")
    return genderCleaned


# Cleans and exports survey-data
survey_df = pd.read_csv(filePath, infer_datetime_format=True)
survey_df["gender"] = survey_df["gender"].apply(genderClean)
survey_df["pronouns"] = survey_df["pronouns"].apply(pronounClean)
survey_df.to_csv("./survey-data/survey-data-cleaned.csv")
