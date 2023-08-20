import pandas as pd
df=pd.read_csv('timestamp.csv')
print(df)
content = []
md_path='questions.md'
with open(md_path, "r") as file:
    filedata = file.read().splitlines()

temp='<!--timestamp_content--><table style="width:100%" id="j_table">'+ "<thead><tr>"+ "<th>Question</th>"+ "<th>Responses</th>"+ "</tr></thead>"
count=0
df=df.dropna()
for i,ii in df.iterrows():
   
    count+=1
    part1 = str(ii['Questions']) #.split('-')[1]
    part2 = ii['Timestamp']
    part2 = "<a href="+str(ii['Timestamp'])+' >Link</a>' #.split('-')[1]
    #part2 = '[link]('+str(ii['Timestamp'])+')' #.split('-')[1]
    temp+='<tr>'+'<td>'+str(count)+'.'+str(part1)+'</td>'+'<td>'+str(part2)+'</td>'+'</tr>'

for j in filedata:
    if "<!--timestamp_content-->" in j:
        content.append(temp+"</table>")
        #content.append("<!--timestamp_content-->"+temp+"</table>")
    else:
        content.append(j)

with open(md_path, "w") as file:
        file.write("\n".join(content))


   
