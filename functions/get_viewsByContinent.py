data = {'UK': 3, 'MX': 1, 'AZ': 5, 'JP': 2}
continentsDict = {'Africa': 0, 'Americas': 0, 'Asia': 0, 'Europe':0, 'Oceania': 0}
africa = ['DZ','AO','BJ','BW','BF','BI','CM','CV','CF','KM','CD','DJ','EG','GQ','ER','ET','GA','GM','GH','GN','GW','CI','KE','LS','LR','LY','MG','MW','ML','MR','MU','MA','MZ','NA','NE','NG','CG','RE','RW','SH','ST','SN','SC','SL','SO','ZA','SS','SD','SZ','TZ','TG','TN','UG','EH','ZM','ZW']
asia = ['AF','AM','AZ','BH','BD','BT','BN','KH','CN','GE','HK','IN','ID','IR','IQ','IL','JP','JO','KZ','KW','KG','LA','LB','MO','MY','MV','MN','MM','NP','KP','OM','PK','PH','QA','SA','SG','KR','LK','SY','TW','TJ','TH','TR','TM','AE','UZ','VN','YE']
europe = ['AL','AD','AT','BY','BE','BA','BG','HR','CY','CZ','DK','EE','FO','FI','FR','DE','GI','GR','HU','IS','IE','IM','IT','XK','LV','LI','LT','LU','MK','MT','MD','MC','ME','NL','NO','PL','PT','RO','RU','SM','RS','SK','SI','ES','SE','CH','UA','UK', 'GB','VA']
oceania = ['AS','AU','CK','TL','FJ','PF','GU','KI','MH','FM','NR','NC','NZ','NU','NF','MP','PW','PG','PN','WS','SB','TK','TV','TU']
americas = ['AI','AR','AW','BS','BB','BZ','BM','BO','BR','VG','CA','KY','CL','CO','CR','CU','CW','DM','DO','EC','SV','FK','GL','GP','GT','GY','HT','HN','JM','MX','MS','NI','PA','PY','PE','PR','BL','KN','LC','MF','PM','VC','SR','TT','US','UY','VE']

for country in data:
    if country in africa:
        continentsDict['Africa'] = continentsDict['Africa'] + data[country]
    elif country in asia:
        continentsDict['Asia'] = continentsDict['Asia'] + data[country]
    elif country in europe:
        continentsDict['Europe'] = continentsDict['Europe'] + data[country]
    elif country in oceania:
        continentsDict['Oceania'] = continentsDict['Oceania'] + data[country]
    elif country in americas:
        continentsDict['Americas'] = continentsDict['Americas'] + data[country]
    else:
        print("Fuck " + country)
        ## MAKE NICE EXCEPTION ISNTEAD OF FUCK

print (continentsDict)
# Outpus: {'Africa': 0, 'Americas': 1, 'Asia': 7, 'Europe': 3, 'Oceania': 0}



