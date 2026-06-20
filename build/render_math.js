const fs=require('fs');
const path=require('path');
const katex=require('katex');
const root=path.resolve(__dirname,'..');
const d=JSON.parse(fs.readFileSync(path.join(root,'problems.json'),'utf8'));
function esc(s){return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
let fails=0;
function render(s){
  if(!s) return '';
  let out='', last=0, m;
  const re=/\$\$([\s\S]+?)\$\$|\$([^$]+?)\$/g;
  while((m=re.exec(s))){
    out+=esc(s.slice(last,m.index));
    const disp=m[1]!==undefined, tex=disp?m[1]:m[2];
    try{ out+=katex.renderToString(tex,{displayMode:disp,throwOnError:true,strict:false}); }
    catch(e){ fails++; out+=esc(disp?('$$'+tex+'$$'):('$'+tex+'$')); }
    last=re.lastIndex;
  }
  out+=esc(s.slice(last));
  return out;
}
for(const p of d.problems){
  p.short_html=render(p.short_statement);
  p.open_problem_html=render(p.open_problem||'');
  p.full_html=render(p.full_statement);
  p.known_html=render(p.known_results||'');
  if(p.where_posed&&p.where_posed.text) p.where_posed.text_html=render(p.where_posed.text);
}
fs.writeFileSync(path.join(root,'problems_render.json'), JSON.stringify(d));
console.log('rendered problems:',d.problems.length,'| katex failures:',fails);
