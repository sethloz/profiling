from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os, sys

s = os.path.dirname(os.path.abspath(__file__))
os.chdir(s)

alphabet = 'abcdefghijklmnopqrstuvwxyz'

with open('amounts.txt') as f:
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

root = Tk()
root.title('File Reader')
root.geometry('150x75')
def totalAmounts():

    totalWindow = Tk()
    totalWindow.title('Total Racial Profiling')
    totalWindow.geometry('500x400')

    #scrollbar
    main_frame = Frame(totalWindow)
    main_frame.pack(fill=BOTH, expand=1)

    canvas = Canvas(main_frame)
    canvas.pack(side=LEFT, fill=BOTH, expand=1)

    scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    sframe = Frame(canvas)
    canvas.create_window((0, 0), window=sframe, anchor=NW)
    #end of scrollbar

    totalStopsLabel = Label(sframe, text=f'Total Stops: {total}', font=('Arial 11')).grid(column=0, row=0, sticky=W)

    space = Label(sframe, text='').grid(column=0, row=1)

    i = 2

    stopLocationLabel = Label(sframe, text='Location of Stop', font=('Arial 11 bold')).grid(column=0, row=i, sticky=W)
    c = 0
    for location in address:
        i += 1
        c += 1
        Label(sframe, text=f'{c}. {location}: {address[location]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    
    space1 = Label(sframe, text='').grid(column=0, row=i+1)

    raceKnownLabel = Label(sframe, text='Was race or ethnicity know prior to stop', font=('Arial 11 bold')).grid(column=0, row=i+2, sticky=W)

    i += 2
    c = 0
    for answer in knownRace:
        i += 1
        c += 1
        Label(sframe, text=f'{c}. {answer}: {knownRace[answer]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    
    space2 = Label(sframe, text='').grid(column=0, row=i+1)

    raceLabel = Label(sframe, text='Race or ethnicity', font=('Arial 11 bold')).grid(column=0, row=i+2, sticky=W)

    i += 2
    c = 0
    for racename in race:
        i += 1
        c += 1
        Label(sframe, text=f'{c}. {racename}: {race[racename]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    
    space3 = Label(sframe, text='').grid(column=0, row=i+1)

    genderLabel = Label(sframe, text='Gender', font=('Arial 11 bold')).grid(column=0, row=i+2, sticky=W)

    i += 2
    c = 0
    for femalerace in female_gender:
        i += 1
        c += 1
        if str(femalerace) == 'Female':
            Label(sframe, text=f'{c}. {femalerace}: {female_gender[femalerace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-2]}. {femalerace}: {female_gender[femalerace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    c = 1
    for malerace in male_gender:
        i += 1
        c += 1
        if str(malerace) == 'Male':
            Label(sframe, text=f'{c}. {malerace}: {male_gender[malerace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-3]}. {malerace}: {male_gender[malerace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)    
    
    space4 = Label(sframe, text='').grid(column=0, row=i+1)

    reasonLabel = Label(sframe, text='Reason for Stop', font=('Arial 11 bold')).grid(column=0, row=i+2, sticky=W)

    i += 2
    c = 0
    
    for lawrace in reason_law:
        i += 1
        c += 1
        if str(lawrace) == 'Violation of the law':
            Label(sframe, text=f'{c}. {lawrace}: {reason_law[lawrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-2]}. {lawrace}: {reason_law[lawrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    c = 1
    for knowrace in reason_knowledge:
        i += 1
        c += 1
        if str(knowrace) == 'Pre-Existing Knowledge':
            Label(sframe, text=f'{c}. {knowrace}: {reason_knowledge[knowrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-3]}. {knowrace}: {reason_knowledge[knowrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)  
    c = 2
    for moverace in reason_moving:
        i += 1
        c += 1
        if str(moverace) == 'Moving Traffic Violation':
            Label(sframe, text=f'{c}. {moverace}: {reason_moving[moverace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-4]}. {moverace}: {reason_moving[moverace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    c = 3
    for vehiclerace in reason_vehicle:
        i += 1
        c += 1
        if str(vehiclerace) == 'Vehicle Traffic Violation':
            Label(sframe, text=f'{c}. {vehiclerace}: {reason_vehicle[vehiclerace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-5]}. {vehiclerace}: {reason_vehicle[vehiclerace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)  
    
    space5 = Label(sframe, text='').grid(column=0, row=i+1)

    searchLabel = Label(sframe, text='Search Conducted', font=('Arial 11 bold')).grid(column=0, row=i+2, sticky=W)

    i += 2
    c = 0
    for ysearchrace in yes_search:
        i += 1
        c += 1
        if str(ysearchrace) == 'Yes':
            Label(sframe, text=f'{c}. {ysearchrace}: {yes_search[ysearchrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-2]}. {ysearchrace}: {yes_search[ysearchrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    c = 1
    for nsearchrace in no_search:
        i += 1
        c += 1
        if str(nsearchrace) == 'No':
            Label(sframe, text=f'{c}. {nsearchrace}: {no_search[nsearchrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-3]}. {nsearchrace}: {no_search[nsearchrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)    
    
    space6 = Label(sframe, text='').grid(column=0, row=i+1)

    searchReasonLabel = Label(sframe, text='Reason for Search', font=('Arial 11 bold')).grid(column=0, row=i+2, sticky=W)

    i += 2
    c = 0
    
    for consentrace in consent_search:
        i += 1
        c += 1
        if str(consentrace) == 'Consent':
            Label(sframe, text=f'{c}. {consentrace}: {consent_search[consentrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-2]}. {consentrace}: {consent_search[consentrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    c = 1
    for plainrace in plainview_search:
        i += 1
        c += 1
        if str(plainrace) == 'Plain View':
            Label(sframe, text=f'{c}. {plainrace}: {plainview_search[plainrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-3]}. {plainrace}: {plainview_search[plainrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)  
    c = 2
    for probablerace in cause_search:
        i += 1
        c += 1
        if str(probablerace) == 'Probable Cause':
            Label(sframe, text=f'{c}. {probablerace}: {cause_search[probablerace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-4]}. {probablerace}: {cause_search[probablerace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    c = 3
    for inventoryrace in inventory_search:
        i += 1
        c += 1
        if str(inventoryrace) == 'Inventory':
            Label(sframe, text=f'{c}. {inventoryrace}: {inventory_search[inventoryrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-5]}. {inventoryrace}: {inventory_search[inventoryrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)  
    c = 4
    for incidentrace in incident_search:
        i += 1
        c += 1
        if str(incidentrace) == 'Incident to Arrest':
            Label(sframe, text=f'{c}. {incidentrace}: {incident_search[incidentrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-6]}. {incidentrace}: {incident_search[incidentrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)  

    space7 = Label(sframe, text='').grid(column=0, row=i+1)

    contrabandLabel = Label(sframe, text='Contraband Discovered', font=('Arial 11 bold')).grid(column=0, row=i+2, sticky=W)

    i += 2
    c = 0
    for ycontrarace in yes_contraband:
        i += 1
        c += 1
        if str(ycontrarace) == 'Yes':
            Label(sframe, text=f'{c}. {ycontrarace}: {yes_contraband[ycontrarace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-2]}. {ycontrarace}: {yes_contraband[ycontrarace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
            i += 2
            Label(sframe, text=f'                i. Yes: {yes_contraband_arrest[ycontrarace]}', font=('Arial 9')).grid(column=0, row=i-1, sticky=W)
            Label(sframe, text=f'                ii. No: {no_contraband_arrest[ycontrarace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    c = 1
    for ncontrarace in no_contraband:
        i += 1
        c += 1
        if str(ncontrarace) == 'No':
            Label(sframe, text=f'{c}. {ncontrarace}: {no_contraband[ncontrarace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-3]}. {ncontrarace}: {no_contraband[ncontrarace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    
    arrestcontrabandLabel = Label(sframe, text='Yes/No Arrest for found Contraband', font=('Arial 9')).grid(column=1, row=109)

    space8 = Label(sframe, text='').grid(column=0, row=i+1)

    contrabanddescLabel = Label(sframe, text='Description of Contraband', font=('Arial 11 bold')).grid(column=0, row=i+2, sticky=W)

    i += 2
    c = 0
    
    for drugsrace in drugs_contraband:
        i += 1
        c += 1
        if str(drugsrace) == 'Drugs':
            Label(sframe, text=f'{c}. {drugsrace}: {drugs_contraband[drugsrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-2]}. {drugsrace}: {drugs_contraband[drugsrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    c = 1
    for currenyrace in currency_contraband:
        i += 1
        c += 1
        if str(currenyrace) == 'Currency':
            Label(sframe, text=f'{c}. {currenyrace}: {currency_contraband[currenyrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-3]}. {currenyrace}: {currency_contraband[currenyrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)  
    c = 2
    for weaponsrace in weapons_contraband:
        i += 1
        c += 1
        if str(weaponsrace) == 'Weapons':
            Label(sframe, text=f'{c}. {weaponsrace}: {weapons_contraband[weaponsrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-4]}. {weaponsrace}: {weapons_contraband[weaponsrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    c = 3
    for alcoholrace in alcohol_contraband:
        i += 1
        c += 1
        if str(alcoholrace) == 'Alcohol':
            Label(sframe, text=f'{c}. {alcoholrace}: {alcohol_contraband[alcoholrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-5]}. {alcoholrace}: {alcohol_contraband[alcoholrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)  
    c = 4
    for stolenrace in stolen_contraband:
        i += 1
        c += 1
        if str(stolenrace) == 'Stolen Property':
            Label(sframe, text=f'{c}. {stolenrace}: {stolen_contraband[stolenrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-6]}. {stolenrace}: {stolen_contraband[stolenrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)  
    c = 5
    for otherrace in other_contraband:
        i += 1
        c += 1
        if str(otherrace) == 'Other':
            Label(sframe, text=f'{c}. {otherrace}: {other_contraband[stolenrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-7]}. {otherrace}: {other_contraband[otherrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)  

    space8 = Label(sframe, text='').grid(column=0, row=i+1)

    stopresultLabel = Label(sframe, text='Result of the Stop', font=('Arial 11 bold')).grid(column=0, row=i+2, sticky=W)

    i += 2
    c = 0
    
    for verbalrace in verbal_warning:
        i += 1
        c += 1
        if str(verbalrace) == 'Verbal Warning':
            Label(sframe, text=f'{c}. {verbalrace}: {verbal_warning[verbalrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-2]}. {verbalrace}: {verbal_warning[verbalrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    c = 1
    for writtenrace in written_warning:
        i += 1
        c += 1
        if str(writtenrace) == 'Written Warning':
            Label(sframe, text=f'{c}. {writtenrace}: {written_warning[writtenrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-3]}. {writtenrace}: {written_warning[currenyrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)  
    c = 2
    for citationrace in citation_result:
        i += 1
        c += 1
        if str(citationrace) == 'Citation':
            Label(sframe, text=f'{c}. {citationrace}: {citation_result[citationrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-4]}. {citationrace}: {citation_result[citationrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    c = 3
    for warrestrace in arrest_and_wwarning:
        i += 1
        c += 1
        if str(warrestrace) == 'Written Warning/Arrest':
            Label(sframe, text=f'{c}. {warrestrace}: {arrest_and_wwarning[warrestrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-5]}. {warrestrace}: {arrest_and_wwarning[warrestrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)  
    c = 4
    for carrestrace in citation_and_arrest:
        i += 1
        c += 1
        if str(carrestrace) == 'Citation/Arrest':
            Label(sframe, text=f'{c}. {carrestrace}: {citation_and_arrest[carrestrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-6]}. {carrestrace}: {citation_and_arrest[carrestrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)  
    c = 5
    for arrestrace in arrest_result:
        i += 1
        c += 1
        if str(arrestrace) == 'Arrest':
            Label(sframe, text=f'{c}. {arrestrace}: {arrest_result[arrestrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-7]}. {arrestrace}: {arrest_result[arrestrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)  

    space9 = Label(sframe, text='').grid(column=0, row=i+1)

    arrestbasedLabel = Label(sframe, text='Arrest based on', font=('Arial 11 bold')).grid(column=0, row=i+2, sticky=W)

    i += 2
    c = 0
    
    for crimrace in criminal_violation:
        i += 1
        c += 1
        if str(crimrace) == 'Violation of Penal Code':
            Label(sframe, text=f'{c}. {crimrace}: {criminal_violation[crimrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-2]}. {crimrace}: {criminal_violation[crimrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    c = 1
    for trafficrace in traffic_violation:
        i += 1
        c += 1
        if str(trafficrace) == 'Violation of Traffic Law':
            Label(sframe, text=f'{c}. {trafficrace}: {traffic_violation[trafficrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-3]}. {trafficrace}: {traffic_violation[trafficrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)  
    c = 2
    for ordrace in ordinance_violation:
        i += 1
        c += 1
        if str(ordrace) == 'Violation of City Ordinance':
            Label(sframe, text=f'{c}. {ordrace}: {ordinance_violation[ordrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-4]}. {ordrace}: {ordinance_violation[ordrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    c = 3
    for outrace in oustanding_warrant:
        i += 1
        c += 1
        if str(outrace) == 'Outstanding Warrant':
            Label(sframe, text=f'{c}. {outrace}: {oustanding_warrant[outrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-5]}. {outrace}: {oustanding_warrant[outrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    
    space10 = Label(sframe, text='').grid(column=0, row=i+1)

    physicalLabel = Label(sframe, text='Physical Force', font=('Arial 11 bold')).grid(column=0, row=i+2, sticky=W)

    i += 2
    c = 0
    for yforcerace in yes_physical:
        i += 1
        c += 1
        if str(yforcerace) == 'Yes':
            Label(sframe, text=f'{c}. {yforcerace}: {yes_physical[yforcerace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-2]}. {yforcerace}: {yes_physical[yforcerace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    c = 1
    for nforcerace in no_physical:
        i += 1
        c += 1
        if str(nforcerace) == 'No':
            Label(sframe, text=f'{c}. {nforcerace}: {no_physical[nforcerace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-3]}. {nforcerace}: {no_physical[nforcerace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)    

    totalWindow.mainloop()

def individualAmounts():
    filenamedirectory = str(filedialog.askopenfilename())
    split_filenamedirectory = filenamedirectory.split('/')
    filename = split_filenamedirectory[len(split_filenamedirectory) - 1]
    name = filename.strip('.txt')
    try:
        with open(filenamedirectory, 'r+') as f:
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
    except:
        messagebox.showinfo('Error', 'That file is not readable')
        return
    individualWindow = Tk()
    individualWindow.title(f'{name} Racial Profiling')
    individualWindow.geometry('500x400')

    #scrollbar
    main_frame = Frame(individualWindow)
    main_frame.pack(fill=BOTH, expand=1)

    canvas = Canvas(main_frame)
    canvas.pack(side=LEFT, fill=BOTH, expand=1)

    scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    sframe = Frame(canvas)
    canvas.create_window((0, 0), window=sframe, anchor=NW)
    #end of scrollbar
    i = 0

    stopLocationLabel = Label(sframe, text='Location of Stop', font=('Arial 11 bold')).grid(column=0, row=i, sticky=W)
    c = 0
    for location in address:
        i += 1
        c += 1
        Label(sframe, text=f'{c}. {location}: {address_individual[location]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    
    space1 = Label(sframe, text='').grid(column=0, row=i+1)

    raceKnownLabel = Label(sframe, text='Was race or ethnicity know prior to stop', font=('Arial 11 bold')).grid(column=0, row=i+2, sticky=W)

    i += 2
    c = 0
    for answer in knownRaceIndividual:
        i += 1
        c += 1
        Label(sframe, text=f'{c}. {answer}: {knownRaceIndividual[answer]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    
    space2 = Label(sframe, text='').grid(column=0, row=i+1)

    raceLabel = Label(sframe, text='Race or ethnicity', font=('Arial 11 bold')).grid(column=0, row=i+2, sticky=W)

    i += 2
    c = 0
    for racename in raceIndividual:
        i += 1
        c += 1
        Label(sframe, text=f'{c}. {racename}: {raceIndividual[racename]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    
    space3 = Label(sframe, text='').grid(column=0, row=i+1)

    genderLabel = Label(sframe, text='Gender', font=('Arial 11 bold')).grid(column=0, row=i+2, sticky=W)

    i += 2
    c = 0
    for femalerace in female_individual:
        i += 1
        c += 1
        if str(femalerace) == 'Female':
            Label(sframe, text=f'{c}. {femalerace}: {female_individual[femalerace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-2]}. {femalerace}: {female_individual[femalerace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    c = 1
    for malerace in male_individual:
        i += 1
        c += 1
        if str(malerace) == 'Male':
            Label(sframe, text=f'{c}. {malerace}: {male_individual[malerace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-3]}. {malerace}: {male_individual[malerace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)    
    
    space4 = Label(sframe, text='').grid(column=0, row=i+1)

    reasonLabel = Label(sframe, text='Reason for Stop', font=('Arial 11 bold')).grid(column=0, row=i+2, sticky=W)

    i += 2
    c = 0
    
    for lawrace in individual_law:
        i += 1
        c += 1
        if str(lawrace) == 'Violation of the law':
            Label(sframe, text=f'{c}. {lawrace}: {individual_law[lawrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-2]}. {lawrace}: {individual_law[lawrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    c = 1
    for knowrace in individual_knowledge:
        i += 1
        c += 1
        if str(knowrace) == 'Pre-Existing Knowledge':
            Label(sframe, text=f'{c}. {knowrace}: {individual_knowledge[knowrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-3]}. {knowrace}: {individual_knowledge[knowrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)  
    c = 2
    for moverace in individual_moving:
        i += 1
        c += 1
        if str(moverace) == 'Moving Traffic Violation':
            Label(sframe, text=f'{c}. {moverace}: {individual_moving[moverace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-4]}. {moverace}: {individual_moving[moverace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    c = 3
    for vehiclerace in individual_vehicle:
        i += 1
        c += 1
        if str(vehiclerace) == 'Vehicle Traffic Violation':
            Label(sframe, text=f'{c}. {vehiclerace}: {individual_vehicle[vehiclerace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-5]}. {vehiclerace}: {individual_vehicle[vehiclerace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)  
    
    space5 = Label(sframe, text='').grid(column=0, row=i+1)

    searchLabel = Label(sframe, text='Search Conducted', font=('Arial 11 bold')).grid(column=0, row=i+2, sticky=W)

    i += 2
    c = 0
    for ysearchrace in yes_searchIndividual:
        i += 1
        c += 1
        if str(ysearchrace) == 'Yes':
            Label(sframe, text=f'{c}. {ysearchrace}: {yes_searchIndividual[ysearchrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-2]}. {ysearchrace}: {yes_searchIndividual[ysearchrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    c = 1
    for nsearchrace in no_searchIndividual:
        i += 1
        c += 1
        if str(nsearchrace) == 'No':
            Label(sframe, text=f'{c}. {nsearchrace}: {no_searchIndividual[nsearchrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-3]}. {nsearchrace}: {no_searchIndividual[nsearchrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)    
    
    space6 = Label(sframe, text='').grid(column=0, row=i+1)

    searchReasonLabel = Label(sframe, text='Reason for Search', font=('Arial 11 bold')).grid(column=0, row=i+2, sticky=W)

    i += 2
    c = 0
    
    for consentrace in consent_searchIndividual:
        i += 1
        c += 1
        if str(consentrace) == 'Consent':
            Label(sframe, text=f'{c}. {consentrace}: {consent_searchIndividual[consentrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-2]}. {consentrace}: {consent_searchIndividual[consentrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    c = 1
    for plainrace in plainview_searchIndividual:
        i += 1
        c += 1
        if str(plainrace) == 'Plain View':
            Label(sframe, text=f'{c}. {plainrace}: {plainview_searchIndividual[plainrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-3]}. {plainrace}: {plainview_searchIndividual[plainrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)  
    c = 2
    for probablerace in cause_searchIndividual:
        i += 1
        c += 1
        if str(probablerace) == 'Probable Cause':
            Label(sframe, text=f'{c}. {probablerace}: {cause_searchIndividual[probablerace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-4]}. {probablerace}: {cause_searchIndividual[probablerace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    c = 3
    for inventoryrace in inventory_searchIndividual:
        i += 1
        c += 1
        if str(inventoryrace) == 'Inventory':
            Label(sframe, text=f'{c}. {inventoryrace}: {inventory_searchIndividual[inventoryrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-5]}. {inventoryrace}: {inventory_searchIndividual[inventoryrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)  
    c = 4
    for incidentrace in incident_searchIndividual:
        i += 1
        c += 1
        if str(incidentrace) == 'Incident to Arrest':
            Label(sframe, text=f'{c}. {incidentrace}: {incident_searchIndividual[incidentrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-6]}. {incidentrace}: {incident_searchIndividual[incidentrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)  

    space7 = Label(sframe, text='').grid(column=0, row=i+1)

    contrabandLabel = Label(sframe, text='Contraband Discovered', font=('Arial 11 bold')).grid(column=0, row=i+2, sticky=W)

    i += 2
    c = 0
    for ycontrarace in yes_contrabandIndividual:
        i += 1
        c += 1
        if str(ycontrarace) == 'Yes':
            Label(sframe, text=f'{c}. {ycontrarace}: {yes_contrabandIndividual[ycontrarace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-2]}. {ycontrarace}: {yes_contrabandIndividual[ycontrarace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
            i += 2
            Label(sframe, text=f'                i. Yes: {yes_contraband_arrestIndividual[ycontrarace]}', font=('Arial 9')).grid(column=0, row=i-1, sticky=W)
            Label(sframe, text=f'                ii. No: {no_contraband_arrestIndividual[ycontrarace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    c = 1
    for ncontrarace in no_contrabandIndividual:
        i += 1
        c += 1
        if str(ncontrarace) == 'No':
            Label(sframe, text=f'{c}. {ncontrarace}: {no_contrabandIndividual[ncontrarace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-3]}. {ncontrarace}: {no_contrabandIndividual[ncontrarace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    
    arrestcontrabandLabel = Label(sframe, text='Yes/No Arrest for found Contraband', font=('Arial 9')).grid(column=1, row=109)

    space8 = Label(sframe, text='').grid(column=0, row=i+1)

    contrabanddescLabel = Label(sframe, text='Description of Contraband', font=('Arial 11 bold')).grid(column=0, row=i+2, sticky=W)

    i += 2
    c = 0
    
    for drugsrace in drugs_contrabandIndividual:
        i += 1
        c += 1
        if str(drugsrace) == 'Drugs':
            Label(sframe, text=f'{c}. {drugsrace}: {drugs_contrabandIndividual[drugsrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-2]}. {drugsrace}: {drugs_contrabandIndividual[drugsrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    c = 1
    for currenyrace in currency_contrabandIndividual:
        i += 1
        c += 1
        if str(currenyrace) == 'Currency':
            Label(sframe, text=f'{c}. {currenyrace}: {currency_contrabandIndividual[currenyrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-3]}. {currenyrace}: {currency_contrabandIndividual[currenyrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)  
    c = 2
    for weaponsrace in weapons_contrabandIndividual:
        i += 1
        c += 1
        if str(weaponsrace) == 'Weapons':
            Label(sframe, text=f'{c}. {weaponsrace}: {weapons_contrabandIndividual[weaponsrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-4]}. {weaponsrace}: {weapons_contrabandIndividual[weaponsrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    c = 3
    for alcoholrace in alcohol_contrabandIndividual:
        i += 1
        c += 1
        if str(alcoholrace) == 'Alcohol':
            Label(sframe, text=f'{c}. {alcoholrace}: {alcohol_contrabandIndividual[alcoholrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-5]}. {alcoholrace}: {alcohol_contrabandIndividual[alcoholrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)  
    c = 4
    for stolenrace in stolen_contrabandIndividual:
        i += 1
        c += 1
        if str(stolenrace) == 'Stolen Property':
            Label(sframe, text=f'{c}. {stolenrace}: {stolen_contrabandIndividual[stolenrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-6]}. {stolenrace}: {stolen_contrabandIndividual[stolenrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)  
    c = 5
    for otherrace in other_contrabandIndividual:
        i += 1
        c += 1
        if str(otherrace) == 'Other':
            Label(sframe, text=f'{c}. {otherrace}: {other_contrabandIndividual[stolenrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-7]}. {otherrace}: {other_contrabandIndividual[otherrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)  

    space8 = Label(sframe, text='').grid(column=0, row=i+1)

    stopresultLabel = Label(sframe, text='Result of the Stop', font=('Arial 11 bold')).grid(column=0, row=i+2, sticky=W)

    i += 2
    c = 0
    
    for verbalrace in verbal_warningIndividual:
        i += 1
        c += 1
        if str(verbalrace) == 'Verbal Warning':
            Label(sframe, text=f'{c}. {verbalrace}: {verbal_warningIndividual[verbalrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-2]}. {verbalrace}: {verbal_warningIndividual[verbalrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    c = 1
    for writtenrace in written_warningIndividual:
        i += 1
        c += 1
        if str(writtenrace) == 'Written Warning':
            Label(sframe, text=f'{c}. {writtenrace}: {written_warningIndividual[writtenrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-3]}. {writtenrace}: {written_warningIndividual[currenyrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)  
    c = 2
    for citationrace in citation_resultIndividual:
        i += 1
        c += 1
        if str(citationrace) == 'Citation':
            Label(sframe, text=f'{c}. {citationrace}: {citation_resultIndividual[citationrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-4]}. {citationrace}: {citation_resultIndividual[citationrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    c = 3
    for warrestrace in arrest_and_wwarningIndividual:
        i += 1
        c += 1
        if str(warrestrace) == 'Written Warning/Arrest':
            Label(sframe, text=f'{c}. {warrestrace}: {arrest_and_wwarningIndividual[warrestrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-5]}. {warrestrace}: {arrest_and_wwarningIndividual[warrestrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)  
    c = 4
    for carrestrace in citation_and_arrestIndividual:
        i += 1
        c += 1
        if str(carrestrace) == 'Citation/Arrest':
            Label(sframe, text=f'{c}. {carrestrace}: {citation_and_arrestIndividual[carrestrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-6]}. {carrestrace}: {citation_and_arrestIndividual[carrestrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)  
    c = 5
    for arrestrace in arrest_resultIndividual:
        i += 1
        c += 1
        if str(arrestrace) == 'Arrest':
            Label(sframe, text=f'{c}. {arrestrace}: {arrest_resultIndividual[arrestrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-7]}. {arrestrace}: {arrest_resultIndividual[arrestrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)  

    space9 = Label(sframe, text='').grid(column=0, row=i+1)

    arrestbasedLabel = Label(sframe, text='Arrest based on', font=('Arial 11 bold')).grid(column=0, row=i+2, sticky=W)

    i += 2
    c = 0
    
    for crimrace in criminal_violationIndividual:
        i += 1
        c += 1
        if str(crimrace) == 'Violation of Penal Code':
            Label(sframe, text=f'{c}. {crimrace}: {criminal_violationIndividual[crimrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-2]}. {crimrace}: {criminal_violationIndividual[crimrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    c = 1
    for trafficrace in traffic_violationIndividual:
        i += 1
        c += 1
        if str(trafficrace) == 'Violation of Traffic Law':
            Label(sframe, text=f'{c}. {trafficrace}: {traffic_violationIndividual[trafficrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-3]}. {trafficrace}: {traffic_violationIndividual[trafficrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)  
    c = 2
    for ordrace in ordinance_violationIndividual:
        i += 1
        c += 1
        if str(ordrace) == 'Violation of City Ordinance':
            Label(sframe, text=f'{c}. {ordrace}: {ordinance_violationIndividual[ordrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-4]}. {ordrace}: {ordinance_violationIndividual[ordrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    c = 3
    for outrace in oustanding_warrantIndividual:
        i += 1
        c += 1
        if str(outrace) == 'Outstanding Warrant':
            Label(sframe, text=f'{c}. {outrace}: {oustanding_warrantIndividual[outrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-5]}. {outrace}: {oustanding_warrantIndividual[outrace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    
    space10 = Label(sframe, text='').grid(column=0, row=i+1)

    physicalLabel = Label(sframe, text='Physical Force', font=('Arial 11 bold')).grid(column=0, row=i+2, sticky=W)

    i += 2
    c = 0
    for yforcerace in yes_physicalIndividual:
        i += 1
        c += 1
        if str(yforcerace) == 'Yes':
            Label(sframe, text=f'{c}. {yforcerace}: {yes_physicalIndividual[yforcerace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-2]}. {yforcerace}: {yes_physicalIndividual[yforcerace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
    c = 1
    for nforcerace in no_physicalIndividual:
        i += 1
        c += 1
        if str(nforcerace) == 'No':
            Label(sframe, text=f'{c}. {nforcerace}: {no_physicalIndividual[nforcerace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)
        else:
            Label(sframe, text=f'        {alphabet[c-3]}. {nforcerace}: {no_physicalIndividual[nforcerace]}', font=('Arial 9')).grid(column=0, row=i, sticky=W)    



    individualWindow.mainloop()
    

seeTotal = Button(root, text='See total', command=totalAmounts).pack()
seeIndividual = Button(root, text='Open individual file', command=individualAmounts).pack()


root.mainloop()