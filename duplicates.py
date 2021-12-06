import datetime


def find_duplicates_assets(data):
    data_list=[]
    assets_list=[]
    duplicates=[]


    for assets in data:
        data_list.append(assets)
        if not assets[0] in assets_list:
            assets_list.append(assets[0])
        else:
            item=assets[0]
            duplicates.append(item)

    for duplicate in duplicates:
        count=1
        for index in range(len(data_list)):
            asset=data_list[index][0]
            if duplicate == asset:
                data_list[index][0]=f'{asset} #{count}'
                count+=1
                

    #print(data)
    #print(assets_list)
    #print(duplicates)
    #print(data_list)
    return data_list
    
    

