from bs4 import BeautifulSoup
import json,re
from pathlib import Path
out=Path(__file__).resolve().parent
for name,lp in [('gs',908),('fsp',146)]:
 soup=BeautifulSoup((out/'sources'/('GS_Deutsch_2026.html' if name=='gs' else 'FSP_DE_HKS_2019.html')).read_text(),'html.parser')
 areas=[]; rows=[]
 for area in soup.select('.lernbereich'):
  ancestor=area.find_parent('div',class_='lplanpage')
  while ancestor and not re.match(r'Klassenstuf',ancestor.get('data-ci','')): ancestor=ancestor.find_parent('div',class_='lplanpage')
  if not ancestor: continue
  grade=re.search(r'\d(?:/\d)?',ancestor['data-ci']).group()
  aid=area['id']; title=area.find(['h3','h4']).get_text(' ',strip=True)
  blocks=[];block=None
  for tr in area.select('tr'):
   td=tr.find('td',class_='lz');note=tr.find('td',class_='lzb')
   if not td:continue
   level=next((int(c[3:]) for c in tr.get('class',[]) if re.match(r'lze\d',c)),0)
   row={'id':tr.get('id'),'grade':grade,'area_id':aid,'area':title,'level':level,'target':td.get_text(' ',strip=True),'remarks':note.get_text(' ',strip=True) if note else '', 'url':f'https://www.schulportal.sachsen.de/lplandb/lehrplan/{lp}#'+tr.get('id','')}
   if level==1 or block is None:
    block={'id':row['id'],'target':row['target'],'rows':[]};blocks.append(block)
   row['parent_target_id']=block['id'];rows.append(row);block['rows'].append(row)
  areas.append({'id':aid,'grade':grade,'title':title,'blocks':blocks})
 (out/(name+'_inventory.json')).write_text(json.dumps({'source_version':'2026' if name=='gs' else '2019','areas':areas,'rows':rows},ensure_ascii=False,indent=2))
 with (out/(name+'_review.txt')).open('w') as f:
  for a in areas:
   f.write('\n### '+a['grade']+' '+a['id']+' '+a['title']+'\n')
   for b in a['blocks']:
    for r in b['rows']:f.write(f"{r['id']} {'*' if r['level']==1 else '-'} {r['target']} | {r['remarks']}\n")
 print(name,len(areas),'areas',sum(len(a['blocks']) for a in areas),'blocks',len(rows),'rows')
