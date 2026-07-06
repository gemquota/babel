with open('index.html', 'r') as f:
    html = f.read()

# 1. Remove dead cc from getStab
import re
html = re.sub(
    r'  const c=hp\*hp\*1\.2;let cc=false;\n  if\(Math\.random\(\)<c/300\)cc=true;\n  return\{s:p,p:p,m:ms\*\(1\+ri\)\}',
    '  return{s:p,p:p,m:ms*(1+ri)}',
    html
)

# 2. Remove dead cp from state and load  
html = html.replace(
    'const S = {res:{},mat:{},upg:{},tech:{},tower:{rows:[],colCount:3,collapses:0,_coll:false},stat:{gold:0,bricks:0,totalClicks:0,taps:0,tallest:0},\n  cp:{},sk:{gathering:{xp:0,lv:1},',
    'const S = {res:{},mat:{},upg:{},tech:{},tower:{rows:[],colCount:3,collapses:0,_coll:false},stat:{gold:0,bricks:0,totalClicks:0,taps:0,tallest:0},\n  sk:{gathering:{xp:0,lv:1},'
)
html = html.replace(
    'if(!S.cp)S.cp={};if(!S.tech)S.tech={};if(!S.tal)S.tal={};',
    'if(!S.tech)S.tech={};if(!S.tal)S.tal={};'
)

# 3. Fix auto interval to scale per level continuously
html = html.replace(
    'function getAutoInterval(id){const l=Math.min(aL(id),5);return Math.max(250,3000/(1+l*0.8))*1000;}',
    'function getAutoInterval(id){const l=Math.min(aL(id),15);return Math.max(100,3000/(1+l*0.5))*1000;}'
)

# 4. Remove dead bT/mT functions
html = html.replace(
    'function bT(){return 4-Math.min(3,skLv(\'building\')*0.1)}\nfunction mT(){return 5-Math.min(4,skLv(\'building\')*0.1)}\n\n\nfunction initTower',
    '\n\nfunction initTower'
)

# 5. Fix build HUD - remove multi-tap logic  
html = html.replace(
    "  let ct=0,cm=4;const lr=rows.length?rows[rows.length-1]:null;\n  if(lr){const cb=lr.bricks.find(b=>b.st==='p'||b.st==='m');if(cb){ct=cb.st==='p'?(cb.pr||0):(cb.mp||0);cm=cb.st==='p'?bT():mT()}}\n  document.getElementById('bhud-action').innerHTML=S.tower._coll?'💥 Rebuild!':rows.length?'👉 Tap to add row':'👉 Tap to start!';",
    "  document.getElementById('bhud-action').innerHTML=S.tower._coll?'💥 Rebuild!':rows.length?'👉 Tap to add row':'👉 Tap to start!';"
)

# 6. Better collapse gold reward
html = html.replace(
    "S.stat.gold=(S.stat.gold||0)+Math.floor(Math.max(50,rows.length*10+S.stat.totalClicks*0.5));",
    "S.stat.gold=(S.stat.gold||0)+Math.floor(Math.max(100,100+rows.length*15+S.stat.totalClicks*0.2));"
)

# 7. Show auto interval in automation section
# Find the auto upgrade rendering and add interval display
html = html.replace(
    "'<div class=\"u\"><div class=\"d\"><div class=\"nm\">\U0001f916 '+u.n+(mx?' \u2705':l>0?' Lv.'+l:'')+'</div><div class=\"dc\">'+u.d+'</div></div><span class=\"co\">\U0001fa99'+fmt(c)+'</span><button onclick=\"G.buyUpg(\\''+u.id+'\\')\"',
    "'<div class=\"u\"><div class=\"d\"><div class=\"nm\">\U0001f916 '+u.n+(mx?' \u2705':l>0?' Lv.'+l:'')+'</div><div class=\"dc\">'+u.d+(l>0?' \u23f1'+Math.round(getAutoInterval(u.sk)/1000*10)/10+'s':'')+'</div></div><span class=\"co\">\U0001fa99'+fmt(c)+'</span><button onclick=\"G.buyUpg(\\''+u.id+'\\')\"'
)

with open('index.html', 'w') as f:
    f.write(html)
print('All fixes applied')
