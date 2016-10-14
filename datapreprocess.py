import pandas
data=pandas.read_table(r"f:\tianchi\WIFI_AP_Passenger_Records_chusai_1stround.csv",sep=",");
#dw=data['WIFIAPTag']
#data.drop(labels=['WIFIAPTag'],axis=1,inplace=True)
#data.insert(0,'WIFIAPTag',dw)

grouped=data.groupby(['WIFIAPTag','timeStamp']).sum().reset_index()
group2=grouped.groupby(['WIFIAPTag'])
for name,group in group2:
	index1=-1
	index2=len(name)-1
	if(name.find("<")!=-1):
		index1=name.index("<")
		index2=name.index(">")
	group.to_csv('f:/tianchi/result/'+name[index1+1:index2]+'.csv')
