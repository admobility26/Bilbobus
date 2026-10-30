"""Rebuild the bundled official route patterns from a downloaded Bilbao GTFS ZIP."""
import csv,io,json,sys,zipfile
from pathlib import Path
z=zipfile.ZipFile(sys.argv[1])
def read(n):return list(csv.DictReader(io.StringIO(z.read(n+'.txt').decode('utf-8-sig'))))
stops={s['stop_id']:{'code':s['stop_code'],'name':s['stop_name'].strip(),'coordinates':[float(s['stop_lon']),float(s['stop_lat'])]} for s in read('stops')}
aliases={}
for d in json.loads(Path('src/bilbobus-data.json').read_text())['directions']:
 for s in d['stops']:aliases.setdefault(s['code'],[]).extend([s['name'],s['officialName']])
for s in stops.values():s['aliases']=list(set(aliases.get(s['code'],[])))
seq={}
for s in read('stop_times'):seq.setdefault(s['trip_id'],[]).append((int(s['stop_sequence']),s['stop_id']))
shapes={}
for s in read('shapes'):shapes.setdefault(s['shape_id'],[]).append((int(s['shape_pt_sequence']),[round(float(s['shape_pt_lon']),6),round(float(s['shape_pt_lat']),6)]))
trips=read('trips');out=[]
for r in read('routes'):
 seen=set();patterns=[]
 for t in trips:
  if t['route_id']!=r['route_id']:continue
  ids=[s for _,s in sorted(seq.get(t['trip_id'],[]))];key=(t['direction_id'],tuple(ids),t['shape_id'])
  if key in seen or len(ids)<2:continue
  seen.add(key);patterns.append({'id':t['trip_id'],'direction':t['direction_id'],'name':f"{stops[ids[0]]['name']} → {stops[ids[-1]]['name']}",'stops':[stops[i] for i in ids],'shape':[c for _,c in sorted(shapes.get(t['shape_id'],[]))]})
 out.append({'number':r['route_short_name'],'name':r['route_long_name'],'patterns':patterns})
Path('src/official-routes.json').write_text(json.dumps({'date':'2026-10-29','source':'https://www.bilbao.eus/opendata/datos/bilbobus-gtfs','lines':out},ensure_ascii=False,separators=(',',':')))
print(len(out),'lines',sum(len(l['patterns']) for l in out),'patterns')
