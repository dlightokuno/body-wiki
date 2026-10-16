HEAD='''<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t} | Body Wiki</title><link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;600;700&display=swap" rel="stylesheet"><link rel="stylesheet" href="{r}style.css"></head><body>
<header><div class="bar"><a class="logo" href="{r}index.html">Body Wiki</a><nav><a href="{r}index.html#anatomy">解剖学</a><a href="{r}index.html#kinesiology">運動学</a><a href="{r}index.html#pathology">病理学</a><a href="{r}index.html#assessment">評価</a></nav></div></header><main>'''
FOOT='''</main><footer>Body Wiki — トレーナー・理学療法士の学習用。診断・治療の代わりにはなりません。<br>解剖図：Wikimedia Commons のパブリックドメイン画像（出典は各ページに記載）</footer></body></html>'''
def page(path,title,body,r="../"):
    open(path,"w").write(HEAD.format(t=title,r=r)+body+FOOT)

GENRES=[("anatomy","解剖学","体の構造：骨・筋・関節",[("anatomy/pectoralis-major.html","大胸筋","胸の大きな筋。腕を前・内へ"),("anatomy/gluteus-maximus.html","大殿筋","お尻の筋。股関節を伸ばす主力")]),
("kinesiology","運動学","体の動きと力学",[("kinesiology/squat.html","スクワット","しゃがむ動作の力学と指導")]),
("pathology","病理学","病気・けがの仕組み",[("pathology/inflammation.html","炎症と組織修復","けがが治る3段階と負荷の考え方")]),
("assessment","評価","観察・検査・測定",[("assessment/observation.html","体表観察の基本","事実・仮説・追加確認を分ける")])]
idx='<h1>Body Wiki<small>身体の百科事典</small></h1><p class="lead">ジャンルを選び、学びたい項目を開いてください。1ページ1テーマで、図と一緒に解説します。</p>'
for gid,g,desc,items in GENRES:
    idx+=f'<section class="genre" id="{gid}"><h2>{g}<span style="font-size:13px;color:#5d6472;font-weight:400;margin-left:10px">{desc}</span></h2><div class="grid">'
    idx+="".join(f'<a class="card" href="{h}"><b>{n}</b><span>{d}</span></a>' for h,n,d in items)+'</div></section>'
page("index.html","ホーム",idx,r="")

def pins(w,h,pts):
    k=max(1,w/560)
    s=f'<svg class="ov" viewBox="0 0 {w} {h}">'
    for x,y,c,lab,dx,dy in pts:
        col={"o":"#c8372d","i":"#2a62b8","m":"#1d7a4a"}[c]
        s+=f'<circle cx="{x}" cy="{y}" r="{10*k}" fill="{col}" stroke="#fff" stroke-width="{3*k}"/>'
        s+=f'<line x1="{x}" y1="{y}" x2="{x+dx}" y2="{y+dy}" stroke="{col}" stroke-width="{2*k}"/>'
        tw=(len(lab)*15+14)*k; tx=x+dx-(tw if dx<0 else 0)
        s+=f'<rect x="{tx}" y="{y+dy-14*k}" width="{tw}" height="{28*k}" rx="5" fill="{col}"/><text x="{tx+7*k}" y="{y+dy+6*k}" font-size="{15*k}" fill="#fff" font-family="Noto Sans JP,sans-serif" font-weight="600">{lab}</text>'
    return s+'</svg>'
LEG='<div class="legend"><span><i class="dot" style="background:#c8372d"></i>起始</span><span><i class="dot" style="background:#2a62b8"></i>停止</span></div>'

# 大胸筋
ov=pins(1000,800,[(600,150,"o","鎖骨の内側半分",-40,-80),(512,300,"o","胸骨",-120,0),(520,420,"o","第1〜6肋軟骨",-150,30),(610,505,"o","腹直筋鞘（腹部）",-200,110),(790,268,"i","上腕骨の大結節稜へ",-20,300)])
ov2=pins(531,650,[(305,268,"i","停止：上腕骨の大結節稜",40,-75)])
page("anatomy/pectoralis-major.html","大胸筋",f'''<div class="crumb"><a href="../index.html">ホーム</a> › <a href="../index.html#anatomy">解剖学</a> › 大胸筋</div>
<h1>大胸筋<small>Pectoralis major</small></h1>
<p class="lead">胸の前面をおおう扇形の大きな筋。腕を<b>前に出す・内側に閉じる・内側にひねる</b>働きをもち、腕立て伏せやベンチプレスの主役です。</p>
<figure class="fig"><div class="wrap" style="max-width:820px"><img src="../img/sobotta-chest.jpg" alt="胸と腹の筋を前から見たカラー解剖図">{ov}</div>{LEG}
<figcaption>体幹を前から見た図。<b>図の右側（体の左側）</b>に大胸筋全体が見えます。上から鎖骨部（Clavicular portion）・胸肋部（Sternocostal portion）・腹部（Abdominal portion）の3つの部分が、腕の付け根へ集まります。図の左側（体の右側）は大胸筋を切って外側へめくり、その下の小胸筋を見せています。印の位置はおおよその目安です。<br>図：Sobotta, Atlas and Text-book of Human Anatomy (1909) Fig.245（パブリックドメイン, Wikimedia Commons "Sobo 1909 245.png"）</figcaption></figure>
<figure class="fig"><div class="wrap" style="max-width:460px"><img src="../img/gray410.png" alt="大胸筋と三角筋・上腕二頭筋の解剖図">{ov2}</div>
<figcaption>腕との関係：大胸筋の腱は三角筋の内側をくぐって上腕骨に付きます。<br>図：Gray's Anatomy (1918) Fig.410（パブリックドメイン, Wikimedia Commons "Gray410.png"）</figcaption></figure>
<h2>起始・停止・神経支配</h2>
<table><tr><th>起始</th><td><b>鎖骨部</b>：鎖骨の内側半分<br><b>胸肋部</b>：胸骨の前面、第1〜6肋軟骨<br><b>腹部</b>：腹直筋鞘の前葉（外腹斜筋腱膜）</td></tr>
<tr><th>停止</th><td>上腕骨の大結節稜（結節間溝の外側唇）</td></tr>
<tr><th>神経支配</th><td>内側胸筋神経・外側胸筋神経（C5〜T1）<br><span style="font-size:13px;color:#5d6472">外側胸筋神経は主に鎖骨部を支配。髄節の記載は資料によって幅があります。</span></td></tr></table>
<h2>働き</h2>
<div class="two"><div><table><tr><th>筋全体</th><td>肩関節の<b>水平内転</b>（腕を体の前で閉じる）・<b>内転</b>・<b>内旋</b></td></tr>
<tr><th>鎖骨部</th><td>肩関節の<b>屈曲</b>（腕を前に上げる）を助ける</td></tr>
<tr><th>胸肋部・腹部</th><td>上げた腕を<b>下ろす（伸展）</b>動きを助ける</td></tr></table></div>
<div><p>停止腱は<b>ねじれて付着</b>しており、下のほうの線維ほど上腕骨の高い位置に付きます。腕を大きく上げたときに、筋全体がほどよく引き伸ばされる仕組みと説明されます。</p>
<p>上から斜め下へ押す「インクラインプレス」は鎖骨部、下へ押す「ディップス」は胸肋部の下部が働きやすい、というように、腕を押し出す角度で働く部分が変わります。</p></div></div>
<h2>運動との関係</h2>
<table><tr><th>主な種目</th><td>腕立て伏せ、ベンチプレス、ダンベルフライ、ケーブルクロスオーバー</td></tr>
<tr><th>体表での確認</th><td>腋の前の壁（前腋窩ヒダ）をつくる筋。手のひらを合わせて押し合うと収縮が触れやすい。</td></tr></table>
<div class="warn" style="margin-top:14px"><b>けがについて</b>：大胸筋の断裂は、ベンチプレスなどで高重量を下ろす局面に起こりやすいと報告されています。急な痛み、内出血、腋の前のヒダの形の変化があれば整形外科へ。</div>
<h2>トレーナー／理学療法士で必要な深さ</h2>
<div class="depth"><div><b>トレーナー</b><br>起始・停止と働き、種目による違い、断裂のサインに気づく</div><div><b>理学療法士</b><br>上記＋神経支配、肩の可動域制限や巻き肩との関係の評価、術後のリハビリ</div></div>
<h2>関連ページ</h2><div class="grid"><a class="card" href="gluteus-maximus.html"><b>大殿筋</b><span>同じく「大きな表層の筋」</span></a></div>
<h2>参考文献</h2><ol class="refs"><li>Standring S (ed). Gray's Anatomy. 42nd ed. Elsevier; 2020.</li><li>Neumann DA. Kinesiology of the Musculoskeletal System. 3rd ed. Elsevier; 2017.</li><li>StatPearls: Anatomy, Thorax, Pectoralis Major（起始・停止・神経の確認, 2026-10-16）</li></ol>''')

# 大殿筋
ov=pins(630,900,[(320,112,"o","腸骨の後部",-20,-55),(205,330,"o","仙骨・尾骨の後面",-10,-70),(165,560,"o","仙結節靱帯",20,40),(470,640,"i","腸脛靱帯",10,-80),(380,760,"i","殿筋粗面（深部）",30,70)])
page("anatomy/gluteus-maximus.html","大殿筋",f'''<div class="crumb"><a href="../index.html">ホーム</a> › <a href="../index.html#anatomy">解剖学</a> › 大殿筋</div>
<h1>大殿筋<small>Gluteus maximus</small></h1>
<p class="lead">お尻の丸みをつくる、体の中でも特に大きな筋。股関節を<b>後ろに伸ばす・外にひねる</b>主力で、立ち上がる・階段を上る・跳ぶ動作で大きく働きます。</p>
<figure class="fig"><div class="wrap"><img src="../img/sobotta-gluteus.png" alt="右のお尻を後ろから見た大殿筋の解剖図">{ov}</div>{LEG}
<figcaption>右のお尻を後ろから見た図。線維は<b>内側の上から外側の下へ</b>斜めに走ります。殿筋粗面への停止は深いところにあるため、図では位置の目安を示しています。<br>図：Sobotta, Atlas and Text-book of Human Anatomy (1909) Fig.294（パブリックドメイン, Wikimedia Commons "Sobo 1909 294.png"）</figcaption></figure>
<h2>起始・停止・神経支配</h2>
<table><tr><th>起始</th><td>腸骨の後部（後殿筋線より後ろ）、仙骨・尾骨の後面、仙結節靱帯、胸腰筋膜</td></tr>
<tr><th>停止</th><td>大部分は<b>腸脛靱帯</b>へ。下部の深い線維は大腿骨の<b>殿筋粗面</b>へ</td></tr>
<tr><th>神経支配</th><td>下殿神経（L5〜S2）</td></tr></table>
<h2>働き</h2>
<table><tr><th>股関節の伸展</th><td>主な働き。深くしゃがむ・坂や階段を上るなど、股関節が大きく曲がった状態から伸ばす動きで特に強く働きます。</td></tr>
<tr><th>股関節の外旋</th><td>強力な外旋筋</td></tr><tr><th>上部線維／下部線維</th><td>上部は外転、下部は内転を助ける（線維で働きが違う）</td></tr></table>
<div class="note" style="margin-top:14px">静かに立っているときや、平地をゆっくり歩くときの活動は比較的小さい筋です。「立っているだけで常に強く働く筋」ではありません。</div>
<h2>運動との関係</h2>
<table><tr><th>主な種目</th><td>スクワット、ヒップスラスト、ブリッジ、ステップアップ、ランジ</td></tr>
<tr><th>筋力の確認</th><td>うつ伏せで膝を曲げ、太ももを床から持ち上げる（徒手筋力検査）。腰を反らせる代償に注意。</td></tr></table>
<div class="note" style="margin-top:14px"><b>よくある誤解</b>：「お尻が使えていない」は一般向けの言い方で、確立した評価法や病名ではありません。また、殿筋の弱さと腰痛の関連を示す研究はありますが、原因とは確定していません。</div>
<h2>トレーナー／理学療法士で必要な深さ</h2>
<div class="depth"><div><b>トレーナー</b><br>起始・停止・働き、種目による違い、体表での位置</div><div><b>理学療法士</b><br>上記＋神経支配、線維ごとの働き、殿部痛の鑑別（腰椎・仙腸関節・股関節）</div></div>
<h2>関連ページ</h2><div class="grid"><a class="card" href="../kinesiology/squat.html"><b>スクワット</b><span>大殿筋が主に働く種目</span></a><a class="card" href="pectoralis-major.html"><b>大胸筋</b><span>上半身の大きな筋</span></a></div>
<h2>参考文献</h2><ol class="refs"><li>Standring S (ed). Gray's Anatomy. 42nd ed. Elsevier; 2020.</li><li>Neumann DA. Kinesiology of the Musculoskeletal System. 3rd ed. Elsevier; 2017.</li><li>Selkowitz DM, et al. J Orthop Sports Phys Ther. 2013;43(2):54–64.</li></ol>''')
print("ok")

# スクワット図：2つのフォーム、床反力線と関節のモーメントアーム
def fig(hip, knee, ank, sh, label):
    # 棒人間（側面・右向き）
    s=f'<g><text x="{ank[0]}" y="40" text-anchor="middle" font-size="16" font-weight="700" fill="#1f2430">{label}</text>'
    s+=f'<line x1="{ank[0]}" y1="330" x2="{ank[0]}" y2="70" stroke="#c8372d" stroke-width="2.5" stroke-dasharray="7 5"/>'
    s+=f'<polyline points="{sh[0]},{sh[1]} {hip[0]},{hip[1]} {knee[0]},{knee[1]} {ank[0]},{ank[1]} {ank[0]+40},{ank[1]}" fill="none" stroke="#1f2430" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>'
    s+=f'<circle cx="{sh[0]+8}" cy="{sh[1]-28}" r="18" fill="#1f2430"/><line x1="{sh[0]-25}" y1="{sh[1]}" x2="{sh[0]+40}" y2="{sh[1]}" stroke="#5d6472" stroke-width="7"/>'
    for (x,y),c,t in [(hip,"#2a62b8","股"),(knee,"#1d7a4a","膝")]:
        s+=f'<line x1="{x}" y1="{y}" x2="{ank[0]}" y2="{y}" stroke="{c}" stroke-width="5"/><circle cx="{x}" cy="{y}" r="8" fill="#fff" stroke="{c}" stroke-width="4"/>'
        s+=f'<text x="{(x+ank[0])/2}" y="{y-10}" text-anchor="middle" font-size="14" fill="{c}" font-weight="700">{t} {abs(x-ank[0])}</text>'
    s+=f'<line x1="{ank[0]-80}" y1="332" x2="{ank[0]+90}" y2="332" stroke="#5d6472" stroke-width="3"/></g>'
    return s
sq='<svg viewBox="0 0 640 360" style="width:100%;font-family:Noto Sans JP,sans-serif">'+fig((110,230),(270,235),(170,325),(165,90),"体幹を立てる")+fig((341,210),(500,194),(470,325),(470,133),"体幹を前に倒す")+'</svg>'
phase='<svg viewBox="0 0 640 345" style="width:100%;font-family:Noto Sans JP,sans-serif"><defs><marker id="ar" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10z" fill="#5d6472"/></marker></defs>'
def pose(x,hip,knee,sh,lab,sub):
    g=f'<polyline points="{x+sh[0]},{sh[1]} {x+hip[0]},{hip[1]} {x+knee[0]},{knee[1]} {x},310 {x+34},310" fill="none" stroke="#1f2430" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>'
    g+=f'<circle cx="{x+sh[0]+6}" cy="{sh[1]-24}" r="15" fill="#1f2430"/><line x1="{x+sh[0]-20}" y1="{sh[1]}" x2="{x+sh[0]+34}" y2="{sh[1]}" stroke="#5d6472" stroke-width="6"/>'
    g+=f'<text x="{x+10}" y="337" text-anchor="middle" font-size="14" font-weight="700" fill="#1f2430">{lab}</text><text x="{x+10}" y="18" text-anchor="middle" font-size="12.5" fill="#5d6472">{sub}</text>'
    return g
phase+='<line x1="20" y1="312" x2="620" y2="312" stroke="#cfc8bb" stroke-width="2"/>'
phase+=pose(80,(0,155),(2,235),(0,65),"① 開始姿勢","立位")
phase+=pose(250,(-25,190),(35,243),(10,107),"② 下降","エキセントリック")
phase+=pose(420,(-33,236),(45,252),(20,161),"③ ボトム","切り返し")
phase+=pose(570,(-25,190),(35,243),(10,107),"④ 上昇","コンセントリック")
phase+='<line x1="140" y1="200" x2="190" y2="200" stroke="#5d6472" stroke-width="2.5" marker-end="url(#ar)"/><line x1="310" y1="200" x2="350" y2="200" stroke="#5d6472" stroke-width="2.5" marker-end="url(#ar)"/><line x1="480" y1="200" x2="520" y2="200" stroke="#5d6472" stroke-width="2.5" marker-end="url(#ar)"/></svg>'
ovt=pins(400,1025,[(150,440,"m","大腿直筋",40,-70),(100,520,"m","外側広筋",20,90),(230,690,"m","内側広筋",40,60),(285,380,"m","長内転筋",-10,-80)])
page("kinesiology/squat.html","スクワット",f'''<div class="crumb"><a href="../index.html">ホーム</a> › <a href="../index.html#kinesiology">運動学</a> › スクワット</div>
<h1>スクワット<small>Squat</small></h1>
<p class="lead">股関節・膝関節・足関節を同時に屈曲・伸展させて、体を下ろして上げる<b>多関節の閉鎖運動連鎖（CKC）動作</b>。椅子からの立ち上がりと同じ運動パターンであり、下肢の筋力・筋量を高める代表的なレジスタンストレーニング種目でもあります。</p>
<nav class="note" style="font-size:14px"><b>目次</b>　1 分類 ／ 2 動作の局面 ／ 3 関節運動 ／ 4 主働筋 ／ 5 力学 ／ 6 深さ ／ 7 バーの位置 ／ 8 足幅・つま先 ／ 9 体幹と呼吸 ／ 10 指導とエラー ／ 11 プログラム ／ 12 進行と退行 ／ 13 対象者別 ／ 14 よくある誤解 ／ 15 評価指標</nav>

<h2>1. 分類</h2>
<table><tr><th>負荷のかけ方</th><td><b>自重</b>／<b>ゴブレット</b>（胸の前でダンベル）／<b>ハイバー・バックスクワット</b>（僧帽筋上部にバー）／<b>ローバー・バックスクワット</b>（肩甲棘の高さ、三角筋後部にバー）／<b>フロントスクワット</b>（鎖骨・三角筋前部にバー）／<b>オーバーヘッド</b></td></tr>
<tr><th>足の置き方</th><td>両脚（バイラテラル）／スプリットスクワット／ブルガリアンスクワット（後ろ足を台に）／片脚スクワット（ピストル）</td></tr>
<tr><th>深さ</th><td>クォーター（膝屈曲約45°）／ハーフ（約90°）／パラレル（大腿上面が床と平行）／フル（ディープ、パラレルより深い）<br><span style="font-size:13px;color:#5d6472">角度の定義は研究・団体で異なります。論文を読むときは「膝の角度」か「股関節の高さ」か、どちらで定義しているかを確認してください。</span></td></tr></table>

<h2>2. 動作の局面</h2>
<figure class="fig">{phase}<figcaption>横から見た模式図（右向き）。下降で筋は伸ばされながら力を出し（エキセントリック収縮）、ボトムで切り返し、上昇で縮みながら力を出します（コンセントリック収縮）。</figcaption></figure>
<table><tr><th>① 開始姿勢</th><td>足裏全体で立ち、重心を足の中央の上に置く。体幹を固め、呼吸を整える。</td></tr>
<tr><th>② 下降</th><td>股関節・膝・足首を同時に曲げる。下肢の伸筋群がエキセントリックに働いてブレーキをかける。</td></tr>
<tr><th>③ ボトム（切り返し）</th><td>最も深い位置。伸ばされた筋と腱の弾性、伸張反射が切り返しを助ける（伸張–短縮サイクル）。ここで止めて一時停止する方法（ポーズスクワット）は、この助けを減らし難しくなる。</td></tr>
<tr><th>④ 上昇</th><td>伸筋群がコンセントリックに働く。上昇の途中に<b>スティッキングポイント</b>（速度が最も落ち、挙上に失敗しやすい位置）があり、高重量で顕著。</td></tr></table>

<h2>3. 関節運動</h2>
<table><tr><th>関節</th><td><b>下降時の運動</b> → 上昇時はその逆</td></tr>
<tr><th>股関節</th><td>屈曲（深さに応じて大きくなる）。わずかに外転・外旋を伴うことが多い</td></tr>
<tr><th>膝関節</th><td>屈曲。フルスクワットでは大腿と下腿が接するほど深くなる</td></tr>
<tr><th>足関節</th><td><b>背屈</b>（すねが前に倒れる）。背屈が制限されると、かかとが浮く・体幹がより前に倒れる</td></tr>
<tr><th>脊柱</th><td>理想的には大きな動きを抑えて保持。深い位置で骨盤が後傾し腰椎が丸まることがある（いわゆるbutt wink）</td></tr></table>
<p style="font-size:13px;color:#5d6472">各関節の到達角度は、深さ・バーの位置・体格（大腿と下腿の長さの比）・足関節の柔軟性で大きく変わります。</p>

<h2>4. 主働筋と協働筋</h2>
<div class="two"><figure class="fig" style="margin:0"><div class="wrap" style="max-width:340px"><img src="../img/sobotta-thigh.jpg" alt="右の太ももを前から見た解剖図">{ovt}</div><figcaption>右の太ももを前から見た図。大腿四頭筋（大腿直筋・外側広筋・内側広筋、中間広筋は深層）と内転筋群。<br>図：Sobotta (1909) Fig.573（パブリックドメイン, Wikimedia Commons "Sobo 1909 573-574.png"）</figcaption></figure>
<div><table><tr><th>膝の伸展</th><td><b>大腿四頭筋</b>。広筋群（単関節筋）が主に働く。大腿直筋は股関節もまたぐ二関節筋のため、スクワットでの長さの変化は小さい</td></tr>
<tr><th>股関節の伸展</th><td><b><a href="../anatomy/gluteus-maximus.html">大殿筋</a></b>、<b>大内転筋</b>、ハムストリングス</td></tr>
<tr><th>足関節の制御</th><td>ヒラメ筋・腓腹筋（下降時に背屈を制御）</td></tr>
<tr><th>体幹の保持</th><td>脊柱起立筋、腹筋群（腹直筋・腹斜筋・腹横筋）、横隔膜・骨盤底筋</td></tr>
<tr><th>膝の向きの制御</th><td>中殿筋・深層外旋筋など（膝が内側へ入るのを抑える）</td></tr></table>
<div class="note" style="margin-top:12px"><b>ハムストリングス</b>は股関節伸展と膝屈曲を同時に担う二関節筋で、スクワットでは筋の長さがあまり変わりません。10週間のトレーニング研究でも、ハムストリングスの筋量は増えませんでした（Kubo 2019）。</div></div></div>

<h2>5. 力学</h2>
<figure class="fig">{sq}<figcaption>横から見た模式図。赤い点線は<b>床反力</b>の作用線。青と緑の線は関節中心から作用線までの距離＝<b>モーメントアーム</b>（数字は図上の長さの比較）。体幹を立てると膝のモーメントが、前に倒すと股関節（と腰部）のモーメントが大きくなります。</figcaption></figure>
<p>関節を回す力（関節モーメント）は<b>力 × モーメントアーム</b>で決まります。体と重りを合わせた重心は、バランスを保つために足の中央付近の上に来ます。このため、重りの位置や体幹の角度を変えると、股関節と膝の負担の配分が変わります。</p>
<table><tr><th>膝が前に出ないように制限</th><td>膝の負担は減るが、股関節と腰の負担が増える（Fry 2003）。<b>負担は消えず、配分が変わるだけ</b></td></tr>
<tr><th>膝にかかる力（Escamilla 2001のレビュー）</th><td>脛骨大腿関節の圧縮力・せん断力、膝蓋大腿関節の圧縮力は、<b>膝が深く曲がるほど大きくなり</b>、最も深い位置付近で最大。前十字靱帯にかかる前方せん断力は膝屈曲0〜60°で小さく、全体を通して後方せん断力（後十字靱帯が制御）が主。健康な膝ではパラレルスクワットが傷害を起こすことは示されていない</td></tr>
<tr><th>リハビリへの示唆</th><td>膝の力が小さい屈曲0〜50°の範囲は、多くの膝のリハビリ患者に適しうる（Escamilla 2001）</td></tr></table>

<h2>6. 深さ</h2>
<table><tr><th>筋肥大への影響</th><td>フルスクワット（膝屈曲約140°）とハーフスクワット（約90°）を10週間比べた研究：大殿筋（6.7% vs 2.2%）と内転筋（6.2% vs 2.7%）の筋量の増加はフルが大きく、大腿四頭筋（4.9% vs 4.6%）は同程度（Kubo 2019：未経験の男性17名）</td></tr>
<tr><th>膝・腰への負担</th><td>深くしゃがむと膝に悪いという考えに対し、深い屈曲では太ももとふくらはぎの接触や膝蓋骨の接触面積の増加で負担が分散されるため、深いスクワットが軟骨の変性などのリスクを高めるという懸念は根拠に乏しい、とするレビューがある（Hartmann 2013）。同じ刺激を得るためにハーフやクォーターではより重い重量が必要になり、脊柱への負担が増えうるとも指摘されている</td></tr>
<tr><th>実務の判断</th><td>深さは目的・可動域・痛み・既往で決める。腰が丸まらず、痛みなく制御できる深さを基本とする</td></tr></table>

<h2>7. バーの位置による違い</h2>
<table><tr><th>ハイバー</th><td>体幹がより起き、膝の屈曲が大きく、大腿四頭筋の活動が大きい</td></tr>
<tr><th>ローバー</th><td>股関節の屈曲が大きく体幹が前傾し、脊柱起立筋・内転筋・殿筋の活動が大きい。床反力の違いは小さい（Glassbrook 2017のレビュー）</td></tr>
<tr><th>フロント</th><td>体幹がさらに起きる。バックスクワットより膝の圧縮力・膝伸展モーメントが小さく、脊柱起立筋の活動は大きかった（Gullett 2009、15名）</td></tr></table>

<h2>8. 足幅とつま先の向き</h2>
<p>足幅を広げると股関節の外転・外旋が大きくなり、内転筋の関与が増えると説明されます。つま先の向きは<b>股関節の形（臼蓋や大腿骨頸部の向き）に個人差がある</b>ため、一律の「正しい角度」はありません。膝とつま先の向きをおおむね揃え、深くしゃがめて痛みのない位置を探します。</p>

<h2>9. 体幹と呼吸</h2>
<table><tr><th>腹腔内圧</th><td>息を吸ってお腹を張り（ブレーシング）腹腔内圧を高めると、体幹が硬くなりバーを支えやすくなる</td></tr>
<tr><th>息こらえ（バルサルバ法）</th><td>高重量では一時的に息を止める方法が使われるが、血圧が大きく上がる。<b>高血圧・心疾患・妊娠中・眼疾患などでは避け</b>、呼吸を止めずに行う</td></tr>
<tr><th>リフティングベルト</th><td>腹腔内圧を高めやすくする道具。初心者や軽い重量では必須ではない</td></tr></table>

<h2>10. 指導：セットアップとよくあるエラー</h2>
<p><b>基本の手順</b>：①足幅は肩幅程度、つま先はやや外向き ②足裏の3点（母趾球・小趾球・かかと）に体重を乗せる ③息を吸って体幹を固める ④股関節と膝を同時に曲げ、膝はつま先の方向へ ⑤腰を丸めずに制御できる深さまで ⑥床を押して立ち上がる</p>
<p>エラーは「観察した事実」です。原因は複数考えられるので、追加の確認で絞り込んでから修正します（→ <a href="../assessment/observation.html">体表観察の基本</a>）。</p>
<table><tr><th>観察したこと</th><td><b>考えられる原因（仮説）</b> ／ <b>確認</b> ／ <b>修正の例</b></td></tr>
<tr><th>膝が内側に入る（knee-in）</th><td>股関節の外転・外旋の筋力不足、足関節の背屈制限、動き方の癖、骨の形 ／ 片脚動作の観察、股関節の筋力、背屈の可動域 ／ 声かけ（「膝を足の外側へ」）、ゴムバンドを膝に巻く、負荷を下げる<br><span style="font-size:13px;color:#5d6472">膝の内側への入り（動的外反）は前十字靱帯損傷の受傷のしかたに関わりますが、着地テストで将来のけがを予測できるかについては、小規模研究で予測できたという報告（Hewett 2005）と、710名の研究で予測の役に立たなかったという報告（Krosshaug 2016）があり、結論は出ていません。</span></td></tr>
<tr><th>かかとが浮く</th><td>足関節の背屈制限、重心が前すぎる ／ 膝を壁に近づける背屈テスト ／ かかとに薄い板を敷く、ゴブレットで練習、ふくらはぎの柔軟性</td></tr>
<tr><th>深い位置で腰が丸まる</th><td>股関節の屈曲可動域、深さが可動域を超えている、体幹の保持 ／ 仰向けでの股関節屈曲、四つ這いで後ろへ下がる動作 ／ 丸まらない深さで止める、ボックスで深さを管理</td></tr>
<tr><th>体幹が過度に前に倒れる</th><td>足関節の背屈制限、大腿四頭筋の筋力不足、体格（大腿が長い） ／ 背屈の可動域、フロントスクワットとの比較 ／ ゴブレット・フロントスクワット、かかとを上げる</td></tr>
<tr><th>左右にずれる</th><td>痛みを避ける動き、左右の筋力・可動域の差、過去のけが ／ 問診、片脚ずつの評価 ／ 片脚種目で補う、痛みがあれば医療者へ</td></tr></table>

<h2>11. プログラムの組み方</h2>
<table><tr><th>筋持久力</th><td>1RMの67%以下 ／ 12回以上 ／ 2〜3セット ／ 休息30秒以内</td></tr><tr><th>筋肥大</th><td>67〜85% ／ 6〜12回 ／ 3〜6セット ／ 30〜90秒</td></tr><tr><th>筋力</th><td>85%以上 ／ 6回以下 ／ 2〜6セット ／ 2〜5分</td></tr>
<tr><th>パワー</th><td>軽〜中重量を速く、またはジャンプスクワット。回数は少なめで質を重視</td></tr>
<tr><th>頻度</th><td>同じ筋群を週2〜3回が一般的。2026年のACSM指針は「主要な筋群を週2日以上」から始めることを推奨</td></tr>
<tr><th>漸進</th><td>目標回数を1〜2回上回ってできたら重量を2〜10%上げる（ACSM 2009）</td></tr></table>
<p style="font-size:13px;color:#5d6472">負荷の目安はNSCAの教科書（健康な成人向け）。初心者・高齢者・疾患のある人はより軽い負荷から。</p>

<h2>12. 進行と退行</h2>
<table><tr><th>退行（易しく）</th><td>手すりを使った椅子からの立ち上がり → 椅子から立つ → ボックスに座るまで → 浅い自重スクワット</td></tr>
<tr><th>基本</th><td>自重スクワット → ゴブレットスクワット</td></tr>
<tr><th>進行（難しく）</th><td>バーベル（ハイバー／ローバー／フロント）→ ポーズ（ボトムで静止）・テンポ（ゆっくり下ろす）→ 片脚系（スプリット、ブルガリアン）→ ジャンプスクワット</td></tr></table>

<h2>13. 対象者別の配慮</h2>
<table><tr><th>高齢者</th><td>椅子からの立ち上がりとして生活機能に直結。手すり・椅子で安全を確保。評価に30秒椅子立ち上がりテストや5回椅子立ち上がり（12秒以上でサルコペニア基準の該当：AWGS 2019）</td></tr>
<tr><th>変形性膝関節症</th><td>運動療法は治療の中核（OARSI 2019）。痛みの出ない深さ・負荷から。運動後の痛みや腫れが翌日まで強く残れば量を調整</td></tr>
<tr><th>腰痛</th><td>重い病気のサインがないことが前提。腰を丸めない深さから、痛みの反応を見て調整</td></tr>
<tr><th>骨粗鬆症</th><td>重りを持って背中を丸める動きは避ける（ESSA 2017）。医師の骨折リスク評価を前提に</td></tr>
<tr><th>高血圧</th><td>息こらえを避ける。安静時血圧が非常に高い日は行わない</td></tr>
<tr><th>妊娠中</th><td>医師の許可が前提。仰向けで気分が悪くなる人は姿勢に注意。腹圧を強くかける高重量は避ける</td></tr></table>
<div class="warn">急な痛みや腫れがある、手術後で制限がある、しびれや筋力低下が進む場合は、運動を中止して医療者の判断を受けてください。</div>

<h2>14. よくある誤解</h2>
<table><tr><th>「膝はつま先より前に出してはいけない」</th><td>膝の負担は減るが股関節・腰の負担が増える。目的と体に合わせて選ぶ</td></tr>
<tr><th>「深くしゃがむと膝に悪い」</th><td>健康な膝で深いスクワットが有害だという根拠は乏しい（Escamilla 2001, Hartmann 2013）。既往・痛み・負荷で判断</td></tr>
<tr><th>「スクワットでハムストリングスも十分に鍛えられる」</th><td>筋量はほとんど増えないという報告がある（Kubo 2019）。別の種目（ルーマニアンデッドリフト、レッグカールなど）で補う</td></tr>
<tr><th>「正しいフォームは1つ」</th><td>体格・股関節の形・目的で適切なフォームは変わる</td></tr></table>

<h2>15. 評価指標</h2>
<p>1RM・推定1RM（何回できたかから推定）、反復回数、挙上速度、30秒椅子立ち上がりテスト、動作の質（動画）、痛み（NRS 0〜10）。</p>

<h2>関連ページ</h2><div class="grid"><a class="card" href="../anatomy/gluteus-maximus.html"><b>大殿筋</b><span>股関節伸展の主力</span></a><a class="card" href="../assessment/observation.html"><b>体表観察の基本</b><span>エラーの見方</span></a><a class="card" href="../pathology/inflammation.html"><b>炎症と組織修復</b><span>痛みがあるときの負荷調整</span></a></div>
<h2>参考文献</h2><ol class="refs">
<li>Schoenfeld BJ. Squatting kinematics and kinetics and their application to exercise performance. J Strength Cond Res. 2010;24(12):3497–3506.</li>
<li>Escamilla RF. Knee biomechanics of the dynamic squat exercise. Med Sci Sports Exerc. 2001;33(1):127–141.</li>
<li>Fry AC, et al. Effect of knee position on hip and knee torques during the barbell squat. J Strength Cond Res. 2003;17(4):629–633.</li>
<li>Hartmann H, Wirth K, Klusemann M. Analysis of the load on the knee joint and vertebral column with changes in squatting depth and weight load. Sports Med. 2013;43(10):993–1008.</li>
<li>Kubo K, Ikebukuro T, Yata H. Effects of squat training with different depths on lower limb muscle volumes. Eur J Appl Physiol. 2019. doi:10.1007/s00421-019-04181-y</li>
<li>Glassbrook DJ, et al. A review of the biomechanical differences between the high-bar and low-bar back-squat. J Strength Cond Res. 2017;31(9):2618–2634.</li>
<li>Gullett JC, et al. A biomechanical comparison of back and front squats in healthy trained individuals. J Strength Cond Res. 2009;23(1):284–292.</li>
<li>Hewett TE, et al. Biomechanical measures of neuromuscular control and valgus loading of the knee predict ACL injury risk in female athletes. Am J Sports Med. 2005;33(4):492–501.</li>
<li>Krosshaug T, et al. The vertical drop jump is a poor screening test for ACL injuries in female elite soccer and handball players. Am J Sports Med. 2016;44(4):874–883.</li>
<li>Haff GG, Triplett NT (eds). Essentials of Strength Training and Conditioning. 4th ed. NSCA; 2016.</li>
<li>ACSM Position Stand. Resistance Training Prescription for Muscle Function, Hypertrophy and Physical Performance in Healthy Adults. Med Sci Sports Exerc. 2026;58(4):851–872.</li>
<li>American College of Sports Medicine. Progression models in resistance training for healthy adults. Med Sci Sports Exerc. 2009;41(3):687–708.</li>
<li>Chen LK, et al. AWGS 2019. J Am Med Dir Assoc. 2020;21(3):300–307.</li>
<li>Bannuru RR, et al. OARSI guidelines. Osteoarthritis Cartilage. 2019;27(11):1578–1589.</li>
<li>Beck BR, et al. ESSA position statement on osteoporosis. J Sci Med Sport. 2017;20(5):438–445.</li></ol>''')


# 炎症
tl='''<svg viewBox="0 0 680 230" style="width:100%;font-family:Noto Sans JP,sans-serif">
<text x="20" y="25" font-size="13" fill="#5d6472">けがをした日 →　時間の流れ（各段階は重なりながら進む）</text>
<rect x="20" y="45" width="170" height="44" rx="6" fill="#c8372d"/><text x="32" y="73" font-size="16" fill="#fff" font-weight="700">① 炎症期</text>
<rect x="130" y="100" width="290" height="44" rx="6" fill="#d9902a"/><text x="142" y="128" font-size="16" fill="#fff" font-weight="700">② 増殖期</text>
<rect x="320" y="155" width="340" height="44" rx="6" fill="#2a62b8"/><text x="332" y="183" font-size="16" fill="#fff" font-weight="700">③ 成熟・再構築期</text>
<text x="196" y="72" font-size="13" fill="#1f2430">直後〜数日</text><text x="426" y="127" font-size="13" fill="#1f2430">数日〜数週</text><text x="332" y="222" font-size="13" fill="#1f2430">数週〜1年以上</text></svg>'''
page("pathology/inflammation.html","炎症と組織修復",f'''<div class="crumb"><a href="../index.html">ホーム</a> › <a href="../index.html#pathology">病理学</a> › 炎症と組織修復</div>
<h1>炎症と組織修復<small>Inflammation and tissue repair</small></h1>
<p class="lead">けがや感染に対して体が起こす<b>防御と修理の反応</b>。修理の段階に合った負荷をかけると組織は強くなり、合わない負荷は回復を遅らせます。</p>
<figure class="fig">{tl}<figcaption>治癒の3段階の模式図。期間は組織（筋・腱・靱帯・骨）・けがの程度・年齢・血流で大きく変わる目安です。血流の少ない腱・靱帯・軟骨は治りが遅くなります。</figcaption></figure>
<h2>炎症の5つのサイン</h2><div class="grid"><div class="card"><b>発赤</b><span>赤くなる</span></div><div class="card"><b>熱感</b><span>熱をもつ</span></div><div class="card"><b>腫脹</b><span>腫れる</span></div><div class="card"><b>疼痛</b><span>痛む</span></div><div class="card"><b>機能障害</b><span>動かしにくい</span></div></div>
<p>血管が広がって血液の成分がしみ出し、白血球が集まることで起こります。</p>
<h2>各段階で起きていることと、負荷の考え方</h2>
<table><tr><th>① 炎症期</th><td>出血が止まり、白血球が壊れた組織を掃除し、修復の合図を出す。<br><b>負荷</b>：守る。ただし完全な安静ではなく、痛みの出ない範囲で周りを動かす。</td></tr>
<tr><th>② 増殖期</th><td>線維芽細胞が新しいコラーゲン（未熟なⅢ型が多い）をつくり、新しい血管ができる。<br><b>負荷</b>：軽い負荷で、修復中の線維の向きをそろえる。</td></tr>
<tr><th>③ 成熟・再構築期</th><td>コラーゲンが丈夫なⅠ型に置き換わり、組織が強くなる。<br><b>負荷</b>：少しずつ負荷を増やす。</td></tr></table>
<h2>負荷の調整のしかた</h2><p>運動中・直後・<b>翌日</b>の症状の変化を見て、量・強さ・回数を調整します。急に負荷を増やすことはけがと関連し、段階的に積み上げた負荷は体を守る方向に働くと考えられています（Gabbett 2016）。ただし「急性:慢性負荷比」のような数値の基準は、方法論の問題が指摘されています。</p>
<div class="note"><b>よくある誤解</b><br>・「炎症＝悪いもの」→ 治るために必要な過程です。<br>・「痛み止めを飲めば早く治る」→ 痛みは楽になりますが、組織の修復への影響は時期・組織によって議論があります。薬は医師・薬剤師に相談を。<br>・「長引く痛み＝まだ傷んでいる」→ 慢性の痛みでは、組織の状態と痛みの強さが一致しないことがあります。</div>
<div class="warn" style="margin-top:14px"><b>医療機関へ</b>：強い腫れや変形、体重をかけられない、発熱を伴う赤み・熱感、傷から膿が出る、しびれや麻痺、数週たっても良くならない。</div>
<h2>参考文献</h2><ol class="refs"><li>Kumar V, Abbas AK, Aster JC. Robbins Basic Pathology. 10th ed. Elsevier; 2018.</li><li>Khan KM, Scott A. Mechanotherapy. Br J Sports Med. 2009;43(4):247–252.</li><li>Gabbett TJ. The training–injury prevention paradox. Br J Sports Med. 2016;50(5):273–280.</li><li>Impellizzeri FM, et al. J Athl Train. 2020;55(9):893–901.</li></ol>''')

# 体表観察
fl='''<svg viewBox="0 0 680 170" style="width:100%;font-family:Noto Sans JP,sans-serif">
<defs><marker id="a" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10z" fill="#5d6472"/></marker></defs>
<rect x="10" y="20" width="190" height="130" rx="8" fill="#fff" stroke="#1d3a5f" stroke-width="2"/><text x="105" y="52" text-anchor="middle" font-size="17" font-weight="700" fill="#1d3a5f">① 観察した事実</text><text x="105" y="84" text-anchor="middle" font-size="13" fill="#1f2430">見た・触れた・測った</text><text x="105" y="106" text-anchor="middle" font-size="13" fill="#1f2430">ことだけを</text><text x="105" y="128" text-anchor="middle" font-size="13" fill="#1f2430">条件と一緒に書く</text>
<line x1="205" y1="85" x2="240" y2="85" stroke="#5d6472" stroke-width="2.5" marker-end="url(#a)"/>
<rect x="245" y="20" width="190" height="130" rx="8" fill="#fff" stroke="#d9902a" stroke-width="2"/><text x="340" y="52" text-anchor="middle" font-size="17" font-weight="700" fill="#b07015">② 仮説</text><text x="340" y="84" text-anchor="middle" font-size="13" fill="#1f2430">考えられる理由を</text><text x="340" y="106" text-anchor="middle" font-size="13" fill="#1f2430">1つに決めず</text><text x="340" y="128" text-anchor="middle" font-size="13" fill="#1f2430">複数あげる</text>
<line x1="440" y1="85" x2="475" y2="85" stroke="#5d6472" stroke-width="2.5" marker-end="url(#a)"/>
<rect x="480" y="20" width="190" height="130" rx="8" fill="#fff" stroke="#1d7a4a" stroke-width="2"/><text x="575" y="52" text-anchor="middle" font-size="17" font-weight="700" fill="#1d7a4a">③ 追加の確認</text><text x="575" y="84" text-anchor="middle" font-size="13" fill="#1f2430">仮説を区別する</text><text x="575" y="106" text-anchor="middle" font-size="13" fill="#1f2430">検査・測定・問診で</text><text x="575" y="128" text-anchor="middle" font-size="13" fill="#1f2430">確かめる</text></svg>'''
page("assessment/observation.html","体表観察の基本",f'''<div class="crumb"><a href="../index.html">ホーム</a> › <a href="../index.html#assessment">評価</a> › 体表観察の基本</div>
<h1>体表観察の基本<small>Surface observation</small></h1>
<p class="lead">体の表面から見える・触れられる情報（骨の目印、筋の形、皮膚、姿勢、動き）を<b>事実として正確に記録し</b>、仮説を立て、追加の確認につなげる技術です。</p>
<figure class="fig">{fl}<figcaption>観察は必ずこの3段階に分けて考えます。</figcaption></figure>
<h2>例：骨盤の高さに左右差があったとき</h2>
<table><tr><th>① 事実</th><td>立った姿勢で、右の上前腸骨棘（骨盤の前の出っ張り）が左より約1cm低い（触診と目視）</td></tr>
<tr><th>② 仮説</th><td>脚の長さの差、骨盤の傾き、足のアーチの差、立ち方の癖、骨の形の個人差、触診の誤差</td></tr>
<tr><th>③ 追加の確認</th><td>仰向けでの比較、脚の長さの計測、足部の観察、動いているときの変化、痛みとの関係を問診</td></tr></table>
<h2>観察する項目</h2><table><tr><th>骨の目印</th><td>上前腸骨棘・上後腸骨棘・大転子・肩峰・肩甲骨下角・脛骨粗面・くるぶし</td></tr><tr><th>筋・腱</th><td>形、左右差、力を入れたときの変化</td></tr><tr><th>皮膚</th><td>色（赤み・青白さ・内出血）、腫れ、むくみ（押して跡が残るか）、傷あと、熱感</td></tr><tr><th>姿勢</th><td>前・横・後ろから。基準の線との関係</td></tr><tr><th>動き・呼吸</th><td>動作の流れ、歩き方、胸とお腹の動き</td></tr></table>
<h2>限界：ここが一番大切</h2>
<div class="note">・<b>姿勢や左右差だけで痛みの原因は決められません</b>。姿勢と腰痛の因果関係は、研究のまとめでも一致した結論が出ていません（Swain 2020）。<br>・左右差は健康な人にも普通にあります（利き手・競技・骨の形）。<br>・背骨の触診の評価は、検査する人どうしで結果が一致しにくいと報告されています（Seffinger 2004）。深い筋を皮膚の上から区別するのは難しく、皮下脂肪の厚さでも精度が変わります。<br>・押して痛い場所が、痛みの原因の組織とは限りません。</div>
<h2>手順のコツ</h2><ul><li>服装・照明・足の位置・時間帯・撮影の距離と高さをそろえる</li><li>全体 → 部分 → もう一度全体、の順に見る</li><li>写真を撮るときは本人の同意を取り、個人情報として管理する</li></ul>
<div class="warn"><b>すぐ医療機関へ</b>：急な腫れと強い熱・赤み、発熱、ふくらはぎの片側の腫れと痛み（血栓の可能性）、急に大きくなるしこり、けがのあとの変形。</div>
<h2>関連ページ</h2><div class="grid"><a class="card" href="../kinesiology/squat.html"><b>スクワット</b><span>動作観察の例</span></a><a class="card" href="../anatomy/gluteus-maximus.html"><b>大殿筋</b><span>骨の目印と筋の位置</span></a></div>
<h2>参考文献</h2><ol class="refs"><li>Kendall FP, et al. Muscles: Testing and Function with Posture and Pain. 5th ed. 2005.</li><li>Swain CTV, et al. No consensus on causality of spine postures or physical exposure and low back pain. J Biomech. 2020;102:109312.</li><li>Seffinger MA, et al. Reliability of spinal palpation for diagnosis of back and neck pain. Spine. 2004;29(19):E413–E425.</li></ol>''')
print("all")
