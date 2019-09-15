'''
file to determine whether a material is recyclable, compostable, or other given a search term
'''
running_list = {'Carton':'No','Glass bottle':'Yes','Wine bottle':'Yes','Beer bottle':'Yes',
               'Plastic bottle':'Yes','Cutlery':'No','Book':'Yes',
               'Cardboard':'Yes','Paper products':'Yes','Newspaper':'Yes','Magazine':'Yes',
               'Tin can':'Yes','Plastic bag':'No','Paper bag':'Yes','Coffee cup':'No',
               'Prepackaged food':'No','Clothes':'No','Chain':'No','Wire':'No',
                'Bottled water':'Yes', 'Bottle':'Yes', 'Paper product':'Yes', 'Origami paper':'Yes', 'Paper':'Yes', 'Origami':'Yes', 'Junk food':'Yes', 'Snack':'Yes'}
common_backgrounds = []
def check_list(input_list):
    results = []
    errors = []
    yes = 0
    no = 0
    for item in input_list:
        if item not in common_backgrounds:
            try:
                results.append(running_list[item])
            except:
                errors.append(item)
    for i in results:
        if i == 'Yes':
            yes += 1
        elif i == 'No':
            no += 1
        else:
            print('Wut')
    if yes > no:
        return "recycle"
    elif yes == 0 and no == 0:
        return "dont_know"
    else:
        return "not_recycle"

def update_csv(errors, igen_recycle, csv_dictionary):
    """
    updates csv so count for each item in errors is corrected
    """
    index = 0 if igen_recycle else 1

    for item in errors:
        if item in csv_dictionary:
            csv_dictionary[item][index] += 1 #update the count of recycle/not recycle for that namedWindow
    return csv_dictionary
