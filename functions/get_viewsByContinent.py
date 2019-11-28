data = {'UK': 3, 'MX': 1, 'AZ': 5, 'JP': 2}
continentsDict = {'Africa': 0, 'Americas': 0, 'Asia': 0, 'Europe':0, 'Oceania': 0}

#africa = ['DZ','AO','BJ','BW','BF','BI','CM','CV','CF','KM','CD','DJ','EG','GQ','ER','ET','GA','GM','GH','GN','GW','CI','KE','LS','LR','LY','MG','MW','ML','MR','MU','MA','MZ','NA','NE','NG','CG','RE','RW','SH','ST','SN','SC','SL','SO','ZA','SS','SD','SZ','TZ','TG','TN','UG','EH','ZM','ZW']
#asia = ['AF','AM','AZ','BH','BD','BT','BN','KH','CN','GE','HK','IN','ID','IR','IQ','IL','JP','JO','KZ','KW','KG','LA','LB','MO','MY','MV','MN','MM','NP','KP','OM','PK','PH','QA','SA','SG','KR','LK','SY','TW','TJ','TH','TR','TM','AE','UZ','VN','YE']
#europe = ['AL','AD','AT','BY','BE','BA','BG','HR','CY','CZ','DK','EE','FO','FI','FR','DE','GI','GR','HU','IS','IE','IM','IT','XK','LV','LI','LT','LU','MK','MT','MD','MC','ME','NL','NO','PL','PT','RO','RU','SM','RS','SK','SI','ES','SE','CH','UA','UK', 'GB','VA']
#oceania = ['AS','AU','CK','TL','FJ','PF','GU','KI','MH','FM','NR','NC','NZ','NU','NF','MP','PW','PG','PN','WS','SB','TK','TV','TU']
#americas = ['AI','AR','AW','BS','BB','BZ','BM','BO','BR','VG','CA','KY','CL','CO','CR','CU','CW','DM','DO','EC','SV','FK','GL','GP','GT','GY','HT','HN','JM','MX','MS','NI','PA','PY','PE','PR','BL','KN','LC','MF','PM','VC','SR','TT','US','UY','VE']

countriesDict = {
    'DZ':'Africa','AO':'Africa','BJ':'Africa','BW':'Africa','BF':'Africa','BI':'Africa','CM':'Africa','CV':'Africa','CF':'Africa','KM':'Africa','CD':'Africa','DJ':'Africa','EG':'Africa','GQ':'Africa','ER':'Africa','ET':'Africa','GA':'Africa','GM':'Africa','GH':'Africa','GN':'Africa','GW':'Africa','CI':'Africa','KE':'Africa','LS':'Africa','LR':'Africa','LY':'Africa','MG':'Africa','MW':'Africa','ML':'Africa','MR':'Africa','MU':'Africa','MA':'Africa','MZ':'Africa','NA':'Africa','NE':'Africa','NG':'Africa','CG':'Africa','RE':'Africa','RW':'Africa','SH':'Africa','ST':'Africa','SN':'Africa','SC':'Africa','SL':'Africa','SO':'Africa','ZA':'Africa','SS':'Africa','SD':'Africa','SZ':'Africa','TZ':'Africa','TG':'Africa','TN':'Africa','UG':'Africa','EH':'Africa','ZM':'Africa','ZW':'Africa',
    'AF':'Asia','AM':'Asia','AZ':'Asia','BH':'Asia','BD':'Asia','BT':'Asia','BN':'Asia','KH':'Asia','CN':'Asia','GE':'Asia','HK':'Asia','IN':'Asia','ID':'Asia','IR':'Asia','IQ':'Asia','IL':'Asia','JP':'Asia','JO':'Asia','KZ':'Asia','KW':'Asia','KG':'Asia','LA':'Asia','LB':'Asia','MO':'Asia','MY':'Asia','MV':'Asia','MN':'Asia','MM':'Asia','NP':'Asia','KP':'Asia','OM':'Asia','PK':'Asia','PH':'Asia','QA':'Asia','SA':'Asia','SG':'Asia','KR':'Asia','LK':'Asia','SY':'Asia','TW':'Asia','TJ':'Asia','TH':'Asia','TR':'Asia','TM':'Asia','AE':'Asia','UZ':'Asia','VN':'Asia','YE':'Asia',
    'AL':'Europe','AD':'Europe','AT':'Europe','BY':'Europe','BE':'Europe','BA':'Europe','BG':'Europe','HR':'Europe','CY':'Europe','CZ':'Europe','DK':'Europe','EE':'Europe','FO':'Europe','FI':'Europe','FR':'Europe','DE':'Europe','GI':'Europe','GR':'Europe','HU':'Europe','IS':'Europe','IE':'Europe','IM':'Europe','IT':'Europe','XK':'Europe','LV':'Europe','LI':'Europe','LT':'Europe','LU':'Europe','MK':'Europe','MT':'Europe','MD':'Europe','MC':'Europe','ME':'Europe','NL':'Europe','NO':'Europe','PL':'Europe','PT':'Europe','RO':'Europe','RU':'Europe','SM':'Europe','RS':'Europe','SK':'Europe','SI':'Europe','ES':'Europe','SE':'Europe','CH':'Europe','UA':'Europe','UK':'Europe', 'GB':'Europe','VA':'Europe',
    'AS':'Oceania','AU':'Oceania','CK':'Oceania','TL':'Oceania','FJ':'Oceania','PF':'Oceania','GU':'Oceania','KI':'Oceania','MH':'Oceania','FM':'Oceania','NR':'Oceania','NC':'Oceania','NZ':'Oceania','NU':'Oceania','NF':'Oceania','MP':'Oceania','PW':'Oceania','PG':'Oceania','PN':'Oceania','WS':'Oceania','SB':'Oceania','TK':'Oceania','TV':'Oceania','TU':'Oceania',
    'AI':'Americas','AR':'Americas','AW':'Americas','BS':'Americas','BB':'Americas','BZ':'Americas','BM':'Americas','BO':'Americas','BR':'Americas','VG':'Americas','CA':'Americas','KY':'Americas','CL':'Americas','CO':'Americas','CR':'Americas','CU':'Americas','CW':'Americas','DM':'Americas','DO':'Americas','EC':'Americas','SV':'Americas','FK':'Americas','GL':'Americas','GP':'Americas','GT':'Americas','GY':'Americas','HT':'Americas','HN':'Americas','JM':'Americas','MX':'Americas','MS':'Americas','NI':'Americas','PA':'Americas','PY':'Americas','PE':'Americas','PR':'Americas','BL':'Americas','KN':'Americas','LC':'Americas','MF':'Americas','PM':'Americas','VC':'Americas','SR':'Americas','TT':'Americas','US':'Americas','UY':'Americas','VE':'Americas'
    }

for country in data:
    try:
        continentsDict[countriesDict[country]] = continentsDict[countriesDict[country]] + data[country]
    except KeyError:
        print("Countries continent not found: " + country)
print (continentsDict)
# Outpus: {'Africa': 0, 'Americas': 1, 'Asia': 7, 'Europe': 3, 'Oceania': 0}



