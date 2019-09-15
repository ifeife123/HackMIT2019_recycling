'''
file to determine whether a material is recyclable, compostable, or other given a search term
'''
running_list = {'Carton':'No','Glass Bottle':'Yes','Wine Bottle':'Yes','Beer Bottle':'Yes',
               'Plastic Bottle':'Yes','Cutlery':'No','Book':'Yes',
               'Cardboard':'Yes','Paper Products':'Yes','Newspaper':'Yes','Magazine':'Yes',
               'Tin Can':'Yes','Plastic Bag':'No','Paper Bag':'Yes','Coffee Cup':'No',
               'Prepackaged Food':'No','Clothes':'No','Chain':'No','Wire':'No',
                'Bottled Water':'Yes', 'Bottle':'Yes'}

def check_list(input_list):
    results = []
    errors = []
    for item in input_list:
        try:
            results.append(running_list[item])
        except:
            errors.append(item)
    return results