import os, sys

s = os.path.dirname(os.path.abspath(__file__))
os.chdir(s)

address = {
    'City Street' : 0,
    'US Highway' : 0,
    'State Highway' : 0,
    'Country Road' : 0,
    'Private Property' : 0
}

knownRace = {
    'Yes' : 0,
    'No' : 0
}

race = {
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

female_gender = {
    'Female' : 0,
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

male_gender = {
    'Male' : 0,
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

yes_search = {
    'Yes' : 0,
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

no_search = {
    'No' : 0,
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

reason_law = {
    'Violation of the law' : 0,
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

reason_knowledge = {
    'Pre-Existing Knowledge' : 0,
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

reason_moving = {
    'Moving Traffic Violation' : 0,
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

reason_vehicle = {
    'Vehicle Traffic Violation' : 0,
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

consent_search = {
    'Consent' : 0,
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

plainview_search = {
    'Plain View' : 0,
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

cause_search = {
    'Probable Cause' : 0,
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

inventory_search = {
    'Inventory' : 0,
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

incident_search = {
    'Incident to Arrest' : 0,
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

no_contraband = {
    'No' : 0,
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

yes_contraband = {
    'Yes' : 0,
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

drugs_contraband = {
    'Drugs' : 0,
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

currency_contraband = {
    'Currency' : 0,
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

weapons_contraband = {
    'Weapons' : 0,
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

alcohol_contraband = {
    'Alcohol' : 0,
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

stolen_contraband = {
    'Stolen Property' : 0,
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

other_contraband = {
    'Other' : 0,
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

verbal_warning = {
    'Verbal Warning' : 0,
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

written_warning = {
    'Written Warning' : 0,
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

citation_result = {
    'Citation' : 0,
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

arrest_and_wwarning = {
    'Written Warning/Arrest' : 0,
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

citation_and_arrest = {
    'Citation/Arrest' : 0,
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

arrest_result = {
    'Arrest' : 0,
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

criminal_violation = {
    'Violation of Penal Code' : 0,
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

traffic_violation = {
    'Violation of Traffic Law' : 0,
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

ordinance_violation = {
    'Violation of City Ordinance' : 0,
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

oustanding_warrant = {
    'Outstanding Warrant' : 0,
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

yes_physical = {
    'Yes' : 0,
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

no_physical = {
    'No' : 0,
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

total = 0

yes_contraband_arrest = {
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

no_contraband_arrest = {
    'Black' : 0,
    'Hispanic/Latino' : 0,
    'White' : 0,
    'Asian/Pacific Islander' : 0,
    'Alaska Native/Native American' : 0
}

singlestring = (str(male_gender) + '\n' + str(female_gender) + '\n' + str(race) + '\n' + str(knownRace) + '\n' + str(reason_law) + '\n' + str(reason_knowledge) + '\n' + str(reason_moving) + '\n' + str(reason_vehicle) + '\n' + str(address) + '\n' + str(yes_search) + '\n' + str(no_search) + '\n' + str(consent_search) + '\n' + str(plainview_search) + '\n' + str(cause_search) + '\n' + str(inventory_search) + '\n' + str(incident_search) + '\n' + str(yes_contraband) + '\n' + str(no_contraband) + '\n' + str(drugs_contraband) + '\n' + str(currency_contraband) + '\n' + str(weapons_contraband) + '\n' + str(alcohol_contraband) + '\n' + str(stolen_contraband) + '\n' + str(other_contraband) + '\n' + str(verbal_warning) + '\n' + str(written_warning) + '\n' + str(citation_result) + '\n' + str(arrest_and_wwarning) + '\n' + str(citation_and_arrest) + '\n' + str(arrest_result) + '\n' + str(criminal_violation) + '\n' + str(traffic_violation) + '\n' + str(ordinance_violation) + '\n' + str(oustanding_warrant) + '\n' + str(yes_physical) + '\n' + str(no_physical) + '\n' + str(total) + '\n' + str(yes_contraband_arrest) + '\n' + str(no_contraband_arrest))
print(singlestring)

e = os.listdir('individual/')

for filename in e:
    with open(f'individual/{filename}', 'w+') as f:
        f.writelines(singlestring)

with open('amounts.txt', 'w+') as f:
    f.writelines(singlestring)