from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import os, sys

s = os.path.dirname(os.path.abspath(__file__))
os.chdir(s) 

print(s)

logWindow = Tk()
logWindow.title('Log in')
logWindow.geometry('210x57')
logWindow.resizable(width=False, height=False)
with open('users.txt') as f:
    users = eval(f.read())

def submitForm():
    allFilled = False

    submitWindow = Tk()
    submitWindow.geometry('400x90')
    submitWindow.title('Warning')
    def submit_yes():
        ready = checkAll(allFilled)
        if ready == True:
            clear_all_widgets()
            submitWindow.destroy()
            last_names.current(0)
            formPage.grid_forget()
            secondformPage.grid_forget()
            thirdformPage.grid_forget()
            logPage.grid()
        else:
            messagebox.showinfo('Error', 'Please make sure all the blanks are filled')
            submitWindow.destroy()
    def submit_no():
        submitWindow.destroy()

    submit_confirmation = Label(submitWindow, text='Are you sure you want to submit?').pack()
    submitYes = Button(submitWindow, text='Yes', command=submit_yes).pack()
    submitNo = Button(submitWindow, text='No', command=submit_no).pack()

    submitWindow.mainloop()

def checkAll(readyToGo):
    global total
    with open(f'individual/{last_names.get()}.txt', 'r+') as f:
        lines = f.readlines()
        male_individual = eval(lines[0])
        female_individual = eval(lines[1])
        raceIndividual = eval(lines[2])
        knownRaceIndividual = eval(lines[3])
        individual_law = eval(lines[4])
        individual_knowledge = eval(lines[5])
        individual_moving = eval(lines[6])
        individual_vehicle = eval(lines[7])
        address_individual = eval(lines[8])
        yes_searchIndividual = eval(lines[9])
        no_searchIndividual = eval(lines[10])
        consent_searchIndividual = eval(lines[11])
        plainview_searchIndividual = eval(lines[12])
        cause_searchIndividual = eval(lines[13])
        inventory_searchIndividual = eval(lines[14])
        incident_searchIndividual = eval(lines[15])
        yes_contrabandIndividual = eval(lines[16])
        no_contrabandIndividual = eval(lines[17])
        drugs_contrabandIndividual = eval(lines[18])
        currency_contrabandIndividual = eval(lines[19])
        weapons_contrabandIndividual = eval(lines[20])
        alcohol_contrabandIndividual = eval(lines[21])
        stolen_contrabandIndividual = eval(lines[22])
        other_contrabandIndividual = eval(lines[23])
        verbal_warningIndividual = eval(lines[24])
        written_warningIndividual = eval(lines[25])
        citation_resultIndividual = eval(lines[26])
        arrest_and_wwarningIndividual = eval(lines[27])
        citation_and_arrestIndividual = eval(lines[28])
        arrest_resultIndividual = eval(lines[29])
        criminal_violationIndividual = eval(lines[30])
        traffic_violationIndividual = eval(lines[31])
        ordinance_violationIndividual = eval(lines[32])
        oustanding_warrantIndividual = eval(lines[33])
        yes_physicalIndividual = eval(lines[34])
        no_physicalIndividual = eval(lines[35])
        totalIndividual = eval(lines[36])
        yes_contraband_arrestIndividual = eval(lines[37])
        no_contraband_arrestIndividual = eval(lines[38])

    if stopValue.get() != '' and genderValue.get() != '' and raceValue.get() != '' and raceKnownValue.get() != '' and stopReasonValue.get() != '' and stopLocationValue.get() != '' and searchValue.get() != '' and contrabandValue.get() != '' and physicalforceValue.get() != '' and stopResultValue.get() != '':
        address[stopLocationValue.get()] += 1
        knownRace[raceKnownValue.get()] += 1
        knownRaceIndividual[raceKnownValue.get()] += 1
        address_individual[stopLocationValue.get()] += 1
        race[raceValue.get()] += 1
        raceIndividual[raceValue.get()] += 1
        if genderValue.get() == 'Female':
            female_gender[genderValue.get()] += 1
            female_gender[raceValue.get()] += 1
            female_individual[genderValue.get()] += 1
            female_individual[raceValue.get()] += 1
        elif genderValue.get() == 'Male':
            male_gender[genderValue.get()] += 1
            male_gender[raceValue.get()] += 1
            male_individual[genderValue.get()] += 1
            male_individual[raceValue.get()] += 1
        
        if stopReasonValue.get() == 'Violation of the law':
            reason_law[stopReasonValue.get()] += 1
            reason_law[raceValue.get()] += 1
            individual_law[stopReasonValue.get()] += 1
            individual_law[raceValue.get()] += 1
        elif stopReasonValue.get() == 'Pre-Existing Knowledge':
            reason_knowledge[stopReasonValue.get()] += 1
            reason_knowledge[raceValue.get()] += 1
            individual_knowledge[stopReasonValue.get()] += 1
            individual_knowledge[raceValue.get()] += 1
        elif stopReasonValue.get() == 'Moving Traffic Violation':
            reason_moving[stopReasonValue.get()] += 1
            reason_moving[raceValue.get()] += 1
            individual_moving[stopReasonValue.get()] += 1
            individual_moving[raceValue.get()] += 1
        elif stopReasonValue.get() == 'Vehicle Traffic Violation':
            reason_vehicle[stopReasonValue.get()] += 1
            reason_vehicle[raceValue.get()] += 1
            individual_vehicle[stopReasonValue.get()] += 1
            individual_vehicle[raceValue.get()] += 1
        
        if searchValue.get() == 'Yes':
            yes_search[searchValue.get()] += 1
            yes_search[raceValue.get()] += 1
            yes_searchIndividual[searchValue.get()] += 1
            yes_searchIndividual[raceValue.get()] += 1
            if reasonSearchValue.get() == 'Consent':
                consent_search[reasonSearchValue.get()] += 1
                consent_search[raceValue.get()] += 1
                consent_searchIndividual[reasonSearchValue.get()] += 1
                consent_searchIndividual[raceValue.get()] += 1
            elif reasonSearchValue.get() == 'Plain View':
                plainview_search[reasonSearchValue.get()] += 1
                plainview_search[raceValue.get()] += 1
                plainview_searchIndividual[reasonSearchValue.get()] += 1
                plainview_searchIndividual[raceValue.get()] += 1
            elif reasonSearchValue.get() == 'Probable Cause':
                cause_search[reasonSearchValue.get()] += 1
                cause_search[raceValue.get()] += 1
                cause_searchIndividual[reasonSearchValue.get()] += 1
                cause_searchIndividual[raceValue.get()] += 1
            elif reasonSearchValue.get() == 'Inventory':
                inventory_search[reasonSearchValue.get()] += 1
                inventory_search[raceValue.get()] += 1
                inventory_searchIndividual[reasonSearchValue.get()] += 1
                inventory_searchIndividual[raceValue.get()] += 1
            elif reasonSearchValue.get() == 'Incident to Arrest':
                incident_search[reasonSearchValue.get()] += 1
                incident_search[raceValue.get()] += 1
                incident_searchIndividual[reasonSearchValue.get()] += 1
                incident_searchIndividual[raceValue.get()] += 1
        elif searchValue.get() == 'No':
            no_search[searchValue.get()] += 1
            no_search[raceValue.get()] += 1
            no_searchIndividual[searchValue.get()] += 1
            no_searchIndividual[raceValue.get()] += 1
        
        if contrabandValue.get() == 'Yes':
            yes_contraband[contrabandValue.get()] += 1
            yes_contraband[raceValue.get()] += 1
            yes_contrabandIndividual[contrabandValue.get()] += 1
            yes_contrabandIndividual[raceValue.get()] += 1
            if contrabanddescValue.get() == 'Drugs':
                drugs_contraband[contrabanddescValue.get()] += 1
                drugs_contraband[raceValue.get()] += 1
                drugs_contrabandIndividual[contrabanddescValue.get()] += 1
                drugs_contrabandIndividual[raceValue.get()] += 1
            elif contrabanddescValue.get() == 'Currency':
                currency_contraband[contrabanddescValue.get()] += 1
                currency_contraband[raceValue.get()] += 1
                currency_contrabandIndividual[contrabanddescValue.get()] += 1
                currency_contrabandIndividual[raceValue.get()] += 1
            elif contrabanddescValue.get() == 'Weapons':
                weapons_contraband[contrabanddescValue.get()] += 1
                weapons_contraband[raceValue.get()] += 1
                weapons_contrabandIndividual[contrabanddescValue.get()] += 1
                weapons_contrabandIndividual[raceValue.get()] += 1
            elif contrabanddescValue.get() == 'Alcohol':
                alcohol_contraband[contrabanddescValue.get()] += 1
                alcohol_contraband[raceValue.get()] += 1
                alcohol_contrabandIndividual[contrabanddescValue.get()] += 1
                alcohol_contrabandIndividual[raceValue.get()] += 1
            elif contrabanddescValue.get() == 'Stolen Property':
                stolen_contraband[contrabanddescValue.get()] += 1
                stolen_contraband[raceValue.get()] += 1
                stolen_contrabandIndividual[contrabanddescValue.get()] += 1
                stolen_contrabandIndividual[raceValue.get()] += 1
            elif contrabanddescValue.get() == 'Other':
                other_contraband[contrabanddescValue.get()] += 1
                other_contraband[raceValue.get()] += 1
                other_contrabandIndividual[contrabanddescValue.get()] += 1
                other_contrabandIndividual[raceValue.get()] += 1

            if stopResultValue.get() == 'Written Warning/Arrest' or stopResultValue.get() == 'Citation/Arrest' or stopResultValue.get() == 'Arrest':
                yes_contraband_arrest[raceValue.get()] += 1
                yes_contraband_arrestIndividual[raceValue.get()] += 1
            elif stopResultValue.get() == 'Written Warning' or stopResultValue.get() == 'Citation' or stopResultValue.get() == 'Verbal Warning':
                no_contraband_arrest[raceValue.get()] += 1
                no_contraband_arrestIndividual[raceValue.get()] += 1
        elif contrabandValue.get() == 'No':
            no_contraband[contrabandValue.get()] += 1
            no_contraband[raceValue.get()] += 1
            no_contrabandIndividual[contrabandValue.get()] += 1
            no_contrabandIndividual[raceValue.get()] += 1

        if stopResultValue.get() == 'Verbal Warning':
            verbal_warning[stopResultValue.get()] += 1
            verbal_warning[raceValue.get()] += 1
            verbal_warningIndividual[stopResultValue.get()] += 1
            verbal_warningIndividual[raceValue.get()] += 1
        elif stopResultValue.get() == 'Written Warning':
            written_warning[stopResultValue.get()] += 1
            written_warning[raceValue.get()] += 1
            written_warningIndividual[stopResultValue.get()] += 1
            written_warningIndividual[raceValue.get()] += 1
        elif stopResultValue.get() == 'Citation':
            citation_result[stopResultValue.get()] += 1
            citation_result[raceValue.get()] += 1
            citation_resultIndividual[stopResultValue.get()] += 1
            citation_resultIndividual[raceValue.get()] += 1
        elif stopResultValue.get() == 'Written Warning/Arrest':
            arrest_and_wwarning[stopResultValue.get()] += 1
            arrest_and_wwarning[raceValue.get()] += 1
            arrest_and_wwarningIndividual[stopResultValue.get()] += 1
            arrest_and_wwarningIndividual[raceValue.get()] += 1
            if arrestBasedOnValue.get() == 'Violation of Penal Code':
                criminal_violation[arrestBasedOnValue.get()] += 1
                criminal_violation[raceValue.get()] += 1
                criminal_violationIndividual[arrestBasedOnValue.get()] += 1
                criminal_violationIndividual[raceValue.get()] += 1
            elif arrestBasedOnValue.get() == 'Violation of Traffic Law':
                traffic_violation[arrestBasedOnValue.get()] += 1
                traffic_violation[raceValue.get()] += 1
                traffic_violationIndividual[arrestBasedOnValue.get()] += 1
                traffic_violationIndividual[raceValue.get()] += 1
            elif arrestBasedOnValue.get() == 'Violation of City Ordinance':
                ordinance_violation[arrestBasedOnValue.get()] += 1
                ordinance_violation[raceValue.get()] += 1
                ordinance_violationIndividual[arrestBasedOnValue.get()] += 1
                ordinance_violationIndividual[raceValue.get()] += 1
            elif arrestBasedOnValue.get() == 'Outstanding Warrant':
                oustanding_warrant[arrestBasedOnValue.get()] += 1
                oustanding_warrant[raceValue.get()] += 1
                oustanding_warrantIndividual[arrestBasedOnValue.get()] += 1
                oustanding_warrantIndividual[raceValue.get()] += 1
        elif stopResultValue.get() == 'Citation/Arrest':
            citation_and_arrest[stopResultValue.get()] += 1
            citation_and_arrest[raceValue.get()] += 1
            citation_and_arrestIndividual[stopResultValue.get()] += 1
            citation_and_arrestIndividual[raceValue.get()] += 1
            if arrestBasedOnValue.get() == 'Violation of Penal Code':
                criminal_violation[arrestBasedOnValue.get()] += 1
                criminal_violation[raceValue.get()] += 1
                criminal_violationIndividual[arrestBasedOnValue.get()] += 1
                criminal_violationIndividual[raceValue.get()] += 1
            elif arrestBasedOnValue.get() == 'Violation of Traffic Law':
                traffic_violation[arrestBasedOnValue.get()] += 1
                traffic_violation[raceValue.get()] += 1
                traffic_violationIndividual[arrestBasedOnValue.get()] += 1
                traffic_violationIndividual[raceValue.get()] += 1
            elif arrestBasedOnValue.get() == 'Violation of City Ordinance':
                ordinance_violation[arrestBasedOnValue.get()] += 1
                ordinance_violation[raceValue.get()] += 1
                ordinance_violationIndividual[arrestBasedOnValue.get()] += 1
                ordinance_violationIndividual[raceValue.get()] += 1
            elif arrestBasedOnValue.get() == 'Outstanding Warrant':
                oustanding_warrant[arrestBasedOnValue.get()] += 1
                oustanding_warrant[raceValue.get()] += 1
                oustanding_warrantIndividual[arrestBasedOnValue.get()] += 1
                oustanding_warrantIndividual[raceValue.get()] += 1
        elif stopResultValue.get() == 'Arrest':
            arrest_result[stopResultValue.get()] += 1
            arrest_result[raceValue.get()] += 1
            arrest_resultIndividual[stopResultValue.get()] += 1
            arrest_resultIndividual[raceValue.get()] += 1
            if arrestBasedOnValue.get() == 'Violation of Penal Code':
                criminal_violation[arrestBasedOnValue.get()] += 1
                criminal_violation[raceValue.get()] += 1
                criminal_violationIndividual[arrestBasedOnValue.get()] += 1
                criminal_violationIndividual[raceValue.get()] += 1
            elif arrestBasedOnValue.get() == 'Violation of Traffic Law':
                traffic_violation[arrestBasedOnValue.get()] += 1
                traffic_violation[raceValue.get()] += 1
                traffic_violationIndividual[arrestBasedOnValue.get()] += 1
                traffic_violationIndividual[raceValue.get()] += 1
            elif arrestBasedOnValue.get() == 'Violation of City Ordinance':
                ordinance_violation[arrestBasedOnValue.get()] += 1
                ordinance_violation[raceValue.get()] += 1
                ordinance_violationIndividual[arrestBasedOnValue.get()] += 1
                ordinance_violationIndividual[raceValue.get()] += 1
            elif arrestBasedOnValue.get() == 'Outstanding Warrant':
                oustanding_warrant[arrestBasedOnValue.get()] += 1
                oustanding_warrant[raceValue.get()] += 1
                oustanding_warrantIndividual[arrestBasedOnValue.get()] += 1
                oustanding_warrantIndividual[raceValue.get()] += 1
        
        if physicalforceValue.get() == 'Yes':
            yes_physical[physicalforceValue.get()] += 1
            yes_physical[raceValue.get()] += 1
            yes_physicalIndividual[physicalforceValue.get()] += 1
            yes_physicalIndividual[raceValue.get()] += 1
        elif physicalforceValue.get() == 'No':
            no_physical[physicalforceValue.get()] += 1
            no_physical[raceValue.get()] += 1
            no_physicalIndividual[physicalforceValue.get()] += 1
            no_physicalIndividual[raceValue.get()] += 1

        
        
        total += 1
        def overwriteFiles():
            with open('amounts.txt', 'w+') as f:
                singlestring = (str(male_gender) + '\n' + str(female_gender) + '\n' + str(race) + '\n' + str(knownRace) + '\n' + str(reason_law) + '\n' + str(reason_knowledge) + '\n' + str(reason_moving) + '\n' + str(reason_vehicle) + '\n' + str(address) + '\n' + str(yes_search) + '\n' + str(no_search) + '\n' + str(consent_search) + '\n' + str(plainview_search) + '\n' + str(cause_search) + '\n' + str(inventory_search) + '\n' + str(incident_search) + '\n' + str(yes_contraband) + '\n' + str(no_contraband) + '\n' + str(drugs_contraband) + '\n' + str(currency_contraband) + '\n' + str(weapons_contraband) + '\n' + str(alcohol_contraband) + '\n' + str(stolen_contraband) + '\n' + str(other_contraband) + '\n' + str(verbal_warning) + '\n' + str(written_warning) + '\n' + str(citation_result) + '\n' + str(arrest_and_wwarning) + '\n' + str(citation_and_arrest) + '\n' + str(arrest_result) + '\n' + str(criminal_violation) + '\n' + str(traffic_violation) + '\n' + str(ordinance_violation) + '\n' + str(oustanding_warrant) + '\n' + str(yes_physical) + '\n' + str(no_physical) + '\n' + str(total) + '\n' + str(yes_contraband_arrest) + '\n' + str(no_contraband_arrest))
                f.writelines(singlestring)
            with open(f'individual/{last_names.get()}.txt', 'w+') as i:
                singlestring = (str(male_individual) + '\n' + str(female_individual) + '\n' + str(raceIndividual) + '\n' + str(knownRaceIndividual) + '\n' + str(individual_law) + '\n' + str(individual_knowledge) + '\n' + str(individual_moving) + '\n' + str(individual_vehicle) + '\n' + str(address_individual) + '\n' + str(yes_searchIndividual) + '\n' + str(no_searchIndividual) + '\n' + str(consent_searchIndividual) + '\n' + str(plainview_searchIndividual) + '\n' + str(cause_searchIndividual) + '\n' + str(inventory_searchIndividual) + '\n' + str(incident_searchIndividual) + '\n' + str(yes_contrabandIndividual) + '\n' + str(no_contrabandIndividual) + '\n' + str(drugs_contrabandIndividual) + '\n' + str(currency_contrabandIndividual) + '\n' + str(weapons_contrabandIndividual) + '\n' + str(alcohol_contrabandIndividual) + '\n' + str(stolen_contrabandIndividual) + '\n' + str(other_contrabandIndividual) + '\n' + str(verbal_warningIndividual) + '\n' + str(written_warningIndividual) + '\n' + str(citation_resultIndividual) + '\n' + str(arrest_and_wwarningIndividual) + '\n' + str(citation_and_arrestIndividual) + '\n' + str(arrest_resultIndividual) + '\n' + str(criminal_violationIndividual) + '\n' + str(traffic_violationIndividual) + '\n' + str(ordinance_violationIndividual) + '\n' + str(oustanding_warrantIndividual) + '\n' + str(yes_physicalIndividual) + '\n' + str(no_physicalIndividual) + '\n' + str(totalIndividual) + '\n' + str(yes_contraband_arrestIndividual) + '\n' + str(no_contraband_arrestIndividual))
                i.writelines(singlestring)

        overwriteFiles()
        readyToGo = True
        
    else:
        readyToGo = False
        messagebox.showinfo('Error', 'Make sure all sections are filled')
    return readyToGo

with open('amounts.txt', 'r+') as f:
    lines = f.readlines()
    male_gender = eval(lines[0])
    female_gender = eval(lines[1])
    race = eval(lines[2])
    knownRace = eval(lines[3])
    reason_law = eval(lines[4])
    reason_knowledge = eval(lines[5])
    reason_moving = eval(lines[6])
    reason_vehicle = eval(lines[7])
    address = eval(lines[8])
    yes_search = eval(lines[9])
    no_search = eval(lines[10])
    consent_search = eval(lines[11])
    plainview_search = eval(lines[12])
    cause_search = eval(lines[13])
    inventory_search = eval(lines[14])
    incident_search = eval(lines[15])
    yes_contraband = eval(lines[16])
    no_contraband = eval(lines[17])
    drugs_contraband = eval(lines[18])
    currency_contraband = eval(lines[19])
    weapons_contraband = eval(lines[20])
    alcohol_contraband = eval(lines[21])
    stolen_contraband = eval(lines[22])
    other_contraband = eval(lines[23])
    verbal_warning = eval(lines[24])
    written_warning = eval(lines[25])
    citation_result = eval(lines[26])
    arrest_and_wwarning = eval(lines[27])
    citation_and_arrest = eval(lines[28])
    arrest_result = eval(lines[29])
    criminal_violation = eval(lines[30])
    traffic_violation = eval(lines[31])
    ordinance_violation = eval(lines[32])
    oustanding_warrant = eval(lines[33])
    yes_physical = eval(lines[34])
    no_physical = eval(lines[35])
    total = eval(lines[36])
    yes_contraband_arrest = eval(lines[37])
    no_contraband_arrest = eval(lines[38])

def checkLogIn():
    if last_names.get() != '':
        logPage.grid_forget()
        formPage.grid()
        logWindow.geometry('426x534')
        logWindow.title(f"{last_names.get()}'s form")
        try:
            f = open(f'individual/{last_names.get()}.txt', 'r+')
            f.close()
        except:
            writeValues(last_names.get())
    else:
        messagebox.showinfo('Error', 'Please select a user')

def writeValues(lastnames):
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

    with open(f'individual/{lastnames}.txt', 'w+') as a:
        a.writelines(singlestring)

def backToLogIn():
    warningWindow = Tk()
    warningWindow.title('Warning')
    warningWindow.geometry('400x90')

    def dont_leave():
        warningWindow.destroy()
    def exitForm():
        warningWindow.destroy()

        formPage.grid_forget()
        logPage.grid()
        clear_all_widgets()

    are_you_sure = Label(warningWindow, text='Do you want to go back (you will lose all progress on the form)').pack()
    yes_button = Button(warningWindow, text='Yes', command=exitForm).pack()
    no_button = Button(warningWindow, text='No', command=dont_leave).pack()
    
    warningWindow.mainloop()

def nextPageForm():
    formPage.grid_forget()
    logWindow.geometry('335x610')
    secondformPage.grid()

def backToFirstPage():
    secondformPage.grid_forget()
    logWindow.geometry('426x534')
    formPage.grid()

def gotoThirdPage():
    secondformPage.grid_forget()
    logWindow.geometry('505x352')
    thirdformPage.grid()

def returntoSecondPage():
    thirdformPage.grid_forget()
    logWindow.geometry('335x610')
    secondformPage.grid()

def clear_all_widgets():
    logWindow.title("Log in")
    logWindow.geometry('210x57')
    stopValue.set(None)
    genderValue.set(None)
    raceValue.set(None)
    raceKnownValue.set(None)
    stopReasonValue.set(None)

    stopLocationValue.set(None)
    searchValue.set(None)
    reasonSearchValue.set(None)
    contrabandValue.set(None)

    stopResultValue.set(None)
    arrestBasedOnValue.set(None)
    physicalforceValue.set(None)

def resetLastNames():
    last_names.current(0)
    last_names['values'] = users
    with open('users.txt', 'w+') as f:
        f.write(str(users))

def edit():
    editWindow = Tk()
    editWindow.title('Edit/Add/Remove')
    editWindow.resizable(width=False, height=False)
    editWindow.focus_force()
    
    def reseteditLastNames():
        lastnamesList.current(0)
        lastnamesList['values'] = users
    def toEditPage():
        if lastnamesList.get() != '':
            editPage.grid(columnspan=10)
        else:
            messagebox.showinfo('Error', 'Make sure to pick a user to edit')
            editWindow.focus_force()
    def fromEditPage():
        changeName.delete(0, 'end')
        changeBadge.delete(0, 'end')
        editPage.grid_forget()
    def editChange():
        if changeName.get() != '' and changeBadge.get() != '':
            if len(changeBadge.get()) == 3:
                if lastnamesList.get() != '':
                    userID = changeName.get() + ' #' + changeBadge.get()
                    users.insert(users.index(lastnamesList.get()) + 1, userID)
                    users.pop(users.index(lastnamesList.get()))
                    reseteditLastNames()
                    resetLastNames()
                    fromEditPage()
                else:
                    messagebox.showinfo('Error', 'Make sure a user is selected')
                    editWindow.focus_force()
            else:
                messagebox.showinfo('Error', 'Badge Number must be 3 digits')
                editWindow.focus_force()
        else:
            messagebox.showinfo('Error', 'Please fill in both fields')
            editWindow.focus_force()
    def badgeRestrict(*args):
        nums = '1234567890'
        if badgenumRestriction.get() + 't' != 'Nonet':
            if len(badgenumRestriction.get()) > 3:
                badgenumRestriction.set(badgenumRestriction.get()[:3])
                messagebox.showinfo('Error', 'Please keep the digits to 3 numbers only')
                editWindow.focus_force()
            try:
                lastchar = badgenumRestriction.get()[len(badgenumRestriction.get()) - 1]
                if lastchar not in nums:
                    badgenumRestriction.set(badgenumRestriction.get().replace(lastchar, ''))
                    messagebox.showinfo('Error', 'Only numbers please')
                    editWindow.focus_force()
            except:
                pass
    def addBadgeRestrict(*args):
        nums = '1234567890'
        if addBadgeRestriction.get() + 't' != 'Nonet':
            if len(addBadgeRestriction.get()) > 3:
                addBadgeRestriction.set(addBadgeRestriction.get()[:3])
                messagebox.showinfo('Error', 'Please keep the digits to 3 numbers only')
                editWindow.focus_force()
            try:
                lastchar = addBadgeRestriction.get()[len(addBadgeRestriction.get()) - 1]
                if lastchar not in nums:
                    addBadgeRestriction.set(addBadgeRestriction.get().replace(lastchar, ''))
                    messagebox.showinfo('Error', 'Only numbers please')
                    editWindow.focus_force()
            except:
                pass
    def fromAddPage():
        addPage.grid_forget()
        addBadge.delete(0, 'end')
        addName.delete(0, 'end')
    def add():
        if addBadge.get() != '' and addName != '':
            userID = addName.get() + ' #' + addBadge.get()
            users.append(userID)
            reseteditLastNames()
            resetLastNames()
            fromAddPage()
    def remove():
        if lastnamesList.get() != '':
            try:
                users.pop(users.index(lastnamesList.get()))
                resetLastNames()
                reseteditLastNames()
            except:
                messagebox.showinfo('Error', 'There was an error with removing that user')
                editWindow.focus_force()
        else:
            messagebox.showinfo('Error', 'Please select a user')
            editWindow.focus_force()
    editPage = Frame(editWindow)
    addPage = Frame(editWindow)
    removePage = Frame(editWindow)
    lastnamesLabel = Label(editWindow, text='Select User').grid(column=0, row=0)
    lastnamesList = Combobox(editWindow, values=users, state='readonly', width=15)
    lastnamesList.grid(column=1, row=0, padx=10, pady=5)
    editButton = Button(editWindow, text='Edit', command=toEditPage).grid(column=2, row=0)
    addButton = Button(editWindow, text='Add', command=lambda:addPage.grid(columnspan=10)).grid(column=3, row=0)
    removeButton = Button(editWindow, text='Remove', command=remove).grid(column=4, row=0)

    #edit page
    badgenumRestriction = StringVar(editPage)
    changeNameLabel = Label(editPage, text='Change Name').grid(column=0, row=0)
    changeName = Entry(editPage, width=10)
    changeName.grid(column=1, row=0)
    changeBadgeLabel = Label(editPage, text='Change Badge #').grid(column=0, row=1)
    changeBadge = Entry(editPage, width=5, textvariable=badgenumRestriction)
    changeBadge.grid(column=1, row=1)
    badgenumRestriction.trace_add('write', badgeRestrict)
    editBack = Button(editPage, text='Cancel', command=fromEditPage).grid(column=2, row=2)
    editDone = Button(editPage, text='Done', command=editChange).grid(column=3, row=2)

    #add page
    addBadgeRestriction = StringVar(addPage)
    addNameLabel = Label(addPage, text='Name').grid(column=0, row=0)
    addName = Entry(addPage, width=10)
    addName.grid(column=1, row=0)
    addBadgeLabel = Label(addPage, text='Badge #').grid(column=0, row=1)
    addBadge = Entry(addPage, width=5, textvariable=addBadgeRestriction)
    addBadge.grid(column=1, row=1)
    addBadgeRestriction.trace_add('write', addBadgeRestrict)
    addBack = Button(addPage, text='Cancel', command=fromAddPage).grid(column=2, row=2)
    addDone = Button(addPage, text='Done', command=add).grid(column=3, row=2)
    editWindow.mainloop()


logPage = Frame(logWindow)
logPage.grid()

formPage = Frame(logWindow)
secondformPage = Frame(logWindow)
thirdformPage = Frame(logWindow)

#Log in page
last_name_txt = Label(logPage, text='Select User').grid(column=0, row=1)
last_names = Combobox(logPage, values=users, state='readonly', width=15)
last_names.grid(column=0, row=0, padx=10, pady=5)

s = Button(logPage, text='Next', command=checkLogIn).grid(column=1, row=0)
e = Button(logPage, text='Edit', command=edit).grid(column=2, row=0)

#First Form Page

first_back_button = Button(formPage, text='Back to Log in', command=backToLogIn).grid(column=0, row=0, sticky=W)

stopValue = StringVar(formPage, '')
genderValue = StringVar(formPage, '')
raceValue = StringVar(formPage, '')
raceKnownValue = StringVar(formPage, '')
stopReasonValue = StringVar(formPage, '')

stopLabel = Label(formPage, text='Type of Stop', font='Arial 10 bold').grid(column=0, row=1, sticky=W)
vehicleStop = Radiobutton(formPage, text='Vehicle Stop', variable=stopValue, value='Vehicle Stop').grid(column=0, row=2, pady=5, padx=5, sticky=W)
self_pedestrianStop = Radiobutton(formPage, text='Self-Initiated/Pedestrian Stop', variable=stopValue, value='Self-Initiated/Pedestrian Stop').grid(column=1, row=2, padx=5, sticky=W)

space1 = Label(formPage, text='').grid(column=0, row=3)
genderLabel = Label(formPage, text='Gender', font='Arial 10 bold').grid(column=0, row=4, sticky=W)
genderMale = Radiobutton(formPage, text='Male', variable=genderValue, value='Male').grid(column=0, row=5, pady=5, padx=5, sticky=W)
genderFemale = Radiobutton(formPage, text='Female', variable=genderValue, value='Female').grid(column=1, row=5, padx=5, sticky=W)

space2 = Label(formPage, text='').grid(column=0, row=6)
raceLabel = Label(formPage, text='Race', font='Arial 10 bold').grid(column=0, row=7, sticky=W)
raceBlack = Radiobutton(formPage, text='Black', variable=raceValue, value='Black').grid(column=0, row=8, pady=5, padx=5, sticky=W)
raceWhite = Radiobutton(formPage, text='White', variable=raceValue, value='White').grid(column=1, row=8, padx=5, sticky=W)
raceAsianPacific = Radiobutton(formPage, text='Asian/Pacific Islander', variable=raceValue, value='Asian/Pacific Islander').grid(column=0, row=9, pady=5, padx=5, sticky=W)
raceHispanic = Radiobutton(formPage, text='Hispanic/Latino', variable=raceValue, value='Hispanic/Latino').grid(column=1, row=9, padx=5, sticky=W)
raceAlaskaNative = Radiobutton(formPage, text='Alaska Native/Native American', variable=raceValue, value='Alaska Native/Native American').grid(column=0, row=10, pady=5, padx=5, sticky=W)

space3 = Label(formPage, text='').grid(column=0, row=11)
raceKnownLabel = Label(formPage, text='Race Known Prior to Stop', font='Arial 10 bold').grid(column=0, row=12, sticky=W)
raceKnown = Radiobutton(formPage, text='Yes', variable=raceKnownValue, value='Yes').grid(column=0, row=13, pady=5, padx=5, sticky=W)
raceUnknown = Radiobutton(formPage, text='No', variable=raceKnownValue, value='No').grid(column=1, row=13, padx=5, sticky=W)

space4 = Label(formPage, text='').grid(column=0, row=14)
stopReasonLabel = Label(formPage, text='Reason for Stop', font='Arial 10 bold').grid(column=0, row=15, sticky=W)
lawVio = Radiobutton(formPage, text='Violation of the law', variable=stopReasonValue, value='Violation of the law').grid(column=0, row=16, pady=5, padx=5, sticky=W)
existingVio = Radiobutton(formPage, text='Pre-Existing Knowledge', variable=stopReasonValue, value='Pre-Existing Knowledge').grid(column=1, row=16, padx=5, sticky=W)
movingTrafficVio = Radiobutton(formPage, text='Moving Traffic Violation', variable=stopReasonValue, value='Moving Traffic Violation').grid(column=0, row=17, pady=5, padx=5, sticky=W)
trafficVio = Radiobutton(formPage, text='Vehicle Traffic Violation', variable=stopReasonValue, value='Vehicle Traffic Violation').grid(column=1, row=17, pady=5, padx=5, sticky=W)

firstPage_nextButton = Button(formPage, text='->', command=nextPageForm).grid(column=3, row=23, sticky=SE)


#Second Form Page

def disable_search():
    consentSearch.configure(state=['disabled'])
    plainviewSearch.configure(state=['disabled'])
    probablecauseSearch.configure(state=['disabled'])
    inventorySearch.configure(state=['disabled'])
    incidentSearch.configure(state=['disabled'])

def disable_contraband():
    drugsContraband.configure(state=['disabled'])
    currencyContraband.configure(state=['disabled'])
    weaponsContraband.configure(state=['disabled'])
    alcoholContraband.configure(state=['disabled'])
    stolenContraband.configure(state=['disabled'])
    otherContraband.configure(state=['disabled'])

def enable_search():
    consentSearch.configure(state=['normal'])
    plainviewSearch.configure(state=['normal'])
    probablecauseSearch.configure(state=['normal'])
    inventorySearch.configure(state=['normal'])
    incidentSearch.configure(state=['normal'])

def enable_contraband():
    drugsContraband.configure(state=['normal'])
    currencyContraband.configure(state=['normal'])
    weaponsContraband.configure(state=['normal'])
    alcoholContraband.configure(state=['normal'])
    stolenContraband.configure(state=['normal'])
    otherContraband.configure(state=['normal'])

stopLocationValue = StringVar(secondformPage, '')
searchValue = StringVar(secondformPage, '')
reasonSearchValue = StringVar(secondformPage, '')
contrabandValue = StringVar(secondformPage, '')
contrabanddescValue = StringVar(secondformPage, '')


stopLocationLabel = Label(secondformPage, text='Location of Stop', font='Arial 10 bold').grid(column=0, row=0, sticky=W)
locationStreet = Radiobutton(secondformPage, text='City Street', variable=stopLocationValue, value='City Street').grid(column=0, row=1, pady=5, padx=5, sticky=W)
locationUSHigh = Radiobutton(secondformPage, text='US Highway', variable=stopLocationValue, value='US Highway').grid(column=1, row=1, padx=5, sticky=W)
locationTXHigh = Radiobutton(secondformPage, text='State Highway', variable=stopLocationValue, value='State Highway').grid(column=0, row=2, pady=5, padx=5, sticky=W)
locationCountry = Radiobutton(secondformPage, text='Country Road', variable=stopLocationValue, value='Country Road').grid(column=1, row=2, padx=5, sticky=W)
locationPrivate = Radiobutton(secondformPage, text='Private Property', variable=stopLocationValue, value='Private Property').grid(column=0, row=3, pady=5, padx=5, sticky=W)

space5 = Label(secondformPage, text='').grid(column=0, row=4)
searchLabel = Label(secondformPage, text='Search Conducted', font='Arial 10 bold').grid(column=0, row=5, sticky=W)
yes_search_button = Radiobutton(secondformPage, text='Yes', variable=searchValue, value='Yes', command=enable_search).grid(column=0, row=6, pady=5, padx=5, sticky=W)
no_search_button = Radiobutton(secondformPage, text='No', variable=searchValue, value='No', command=disable_search).grid(column=1, row=6, padx=5, sticky=W)

space6 = Label(secondformPage, text='').grid(column=0, row=7)
reasonSearchLabel = Label(secondformPage, text='Reason for search', font='Arial 10 bold').grid(column=0, row=8, sticky=W)
consentSearch = Radiobutton(secondformPage, text='Consent', variable=reasonSearchValue, value='Consent')
consentSearch.grid(column=0, row=9, pady=5, padx=5, sticky=W)
plainviewSearch = Radiobutton(secondformPage, text='Plain View', variable=reasonSearchValue, value='Plain View')
plainviewSearch.grid(column=1, row=9, padx=5, sticky=W)
probablecauseSearch = Radiobutton(secondformPage, text='Probable Cause', variable=reasonSearchValue, value='Probable Cause')
probablecauseSearch.grid(column=0, row=10, pady=5, padx=5, sticky=W)
inventorySearch = Radiobutton(secondformPage, text='Inventory', variable=reasonSearchValue, value='Inventory')
inventorySearch.grid(column=1, row=10, padx=5, sticky=W)
incidentSearch = Radiobutton(secondformPage, text='Incedent to Arrest', variable=reasonSearchValue, value='Incident to Arrest')
incidentSearch.grid(column=0, row=11, pady=5, padx=5, sticky=W)

space7 = Label(secondformPage, text='').grid(column=0, row=12)
contrabandLabel = Label(secondformPage, text='Contraband Discovered', font='Arial 10 bold').grid(column=0, row=13, sticky=W)
yes_contraband_button = Radiobutton(secondformPage, text='Yes', variable=contrabandValue, value='Yes', command=enable_contraband).grid(column=0, row=14, pady=5, padx=5, sticky=W)
no_contraband_button = Radiobutton(secondformPage, text='No', variable=contrabandValue, value='No', command=disable_contraband).grid(column=1, row=14, padx=5, sticky=W)

space8 = Label(secondformPage, text='').grid(column=0, row=15)
contrabanddescLabel = Label(secondformPage, text='Description of Contraband', font='Arial 10 bold').grid(column=0, row=16, sticky=W)
drugsContraband = Radiobutton(secondformPage, text='Drugs', variable=contrabanddescValue, value='Drugs')
drugsContraband.grid(column=0, row=17, pady=5, padx=5, sticky=W)
currencyContraband = Radiobutton(secondformPage, text='Currency', variable=contrabanddescValue, value='Currency')
currencyContraband.grid(column=1, row=17, padx=5, sticky=W)
weaponsContraband = Radiobutton(secondformPage, text='Weapons', variable=contrabanddescValue, value='Weapons')
weaponsContraband.grid(column=0, row=18, pady=5, padx=5, sticky=W)
alcoholContraband = Radiobutton(secondformPage, text='Alcohol', variable=contrabanddescValue, value='Alcohol')
alcoholContraband.grid(column=1, row=18, padx=5, sticky=W)
stolenContraband = Radiobutton(secondformPage, text='Stolen Property', variable=contrabanddescValue, value='Stolen Property')
stolenContraband.grid(column=0, row=19, pady=5, padx=5, sticky=W)
otherContraband = Radiobutton(secondformPage, text='Other', variable=contrabanddescValue, value='Other')
otherContraband.grid(column=1, row=19, padx=5, sticky=W)

previousPage_button = Button(secondformPage, text='<-', command=backToFirstPage).grid(column=2, row=20, sticky=SE)
nextPage_button = Button(secondformPage, text='->', command=gotoThirdPage).grid(column=3, row=20, sticky=SE)

#Third Form Page

def disable_arrest():
    criminalViolation['state'] = DISABLED
    trafficLawViolation['state'] = DISABLED
    cityOrdinanceViolation['state'] = DISABLED
    outstandingWarrant['state'] = DISABLED

def enable_arrest():
    criminalViolation['state'] = NORMAL
    trafficLawViolation['state'] = NORMAL
    cityOrdinanceViolation['state'] = NORMAL
    outstandingWarrant['state'] = NORMAL

stopResultValue = StringVar(thirdformPage, '')
physicalforceValue = StringVar(thirdformPage, '')
arrestBasedOnValue = StringVar(thirdformPage, '')

stopResultLabel = Label(thirdformPage, text='Result of Stop', font='Arial 10 bold').grid(column=0, row=0, sticky=W)
verbalWarning = Radiobutton(thirdformPage, text='Verbal Warning', variable=stopResultValue, value='Verbal Warning', command=disable_arrest).grid(column=0, row=1, pady=5, padx=5, sticky=W)
writtenWarning = Radiobutton(thirdformPage, text='Written Warning', variable=stopResultValue, value='Written Warning', command=disable_arrest).grid(column=1, row=1, padx=5, sticky=W)
citationWarning = Radiobutton(thirdformPage, text='Citation', variable=stopResultValue, value='Citation', command=disable_arrest).grid(column=0, row=2, pady=5, padx=5, sticky=W)
warningArrest = Radiobutton(thirdformPage, text='Written Warning/Arrest', variable=stopResultValue, value='Written Warning/Arrest', command=enable_arrest).grid(column=1, row=2, padx=5, sticky=W)
citationArrest = Radiobutton(thirdformPage, text='Citation/Arrest', variable=stopResultValue, value='Citation/Arrest', command=enable_arrest).grid(column=0, row=3, pady=5, padx=5, sticky=W)
arrest = Radiobutton(thirdformPage, text='Arrest', variable=stopResultValue, value='Arrest', command=enable_arrest).grid(column=1, row=3, padx=5, sticky=W)

space9 = Label(thirdformPage, text='').grid(column=0, row=4)
arrestBasedOnLabel = Label(thirdformPage, text='Arrest based on', font='Arial 10 bold').grid(column=0, row=5, sticky=W)
criminalViolation = Radiobutton(thirdformPage, text='Violation of Penal Code', variable=arrestBasedOnValue, value='Violation of Penal Code')
criminalViolation.grid(column=0, row=6, pady=5, padx=5, sticky=W)
trafficLawViolation = Radiobutton(thirdformPage, text='Violation of Traffic Law', variable=arrestBasedOnValue, value='Violation of Traffic Law')
trafficLawViolation.grid(column=1, row=6, padx=5, sticky=W)
cityOrdinanceViolation = Radiobutton(thirdformPage, text='Violation of City Ordinance', variable=arrestBasedOnValue, value='Violation of City Ordinance')
cityOrdinanceViolation.grid(column=0, row=7, pady=5, padx=5, sticky=W)
outstandingWarrant = Radiobutton(thirdformPage, text='Outstanding Warrant', variable=arrestBasedOnValue, value='Outstanding Warrant')
outstandingWarrant.grid(column=1, row=7, padx=5, sticky=W)


space10 = Label(thirdformPage, text='').grid(column=0, row=8)
physicalForceLabel = Label(thirdformPage, text='Physical Force Resulting in Bodily Injury', font='Arial 10 bold').grid(column=0, row=9, stick=W)
physicalForce_yes = Radiobutton(thirdformPage, text='Yes', variable=physicalforceValue, value='Yes').grid(column=0, row=10, pady=5, padx=5, sticky=W)
physicalForce_no = Radiobutton(thirdformPage, text='No', variable=physicalforceValue, value='No').grid(column=1, row=10, padx=5, sticky=W)

third_backButton = Button(thirdformPage, text='<-', command=returntoSecondPage).grid(column=2, row=11, sticky=SE)
submit_button = Button(thirdformPage, text='Submit', command=submitForm).grid(column=3, row=11, sticky=SE)

logWindow.mainloop()
