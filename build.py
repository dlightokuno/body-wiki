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
    s=f'<svg class="ov" viewBox="0 0 {w} {h}">'
    for x,y,c,lab,dx,dy in pts:
        col="#c8372d" if c=="o" else "#2a62b8"
        s+=f'<circle cx="{x}" cy="{y}" r="10" fill="{col}" stroke="#fff" stroke-width="3"/>'
        s+=f'<line x1="{x}" y1="{y}" x2="{x+dx}" y2="{y+dy}" stroke="{col}" stroke-width="2"/>'
        tw=len(lab)*15+14; tx=x+dx-(tw if dx<0 else 0)
        s+=f'<rect x="{tx}" y="{y+dy-14}" width="{tw}" height="28" rx="5" fill="{col}"/><text x="{tx+7}" y="{y+dy+6}" font-size="15" fill="#fff" font-family="Noto Sans JP,sans-serif" font-weight="600">{lab}</text>'
    return s+'</svg>'
LEG='<div class="legend"><span><i class="dot" style="background:#c8372d"></i>起始</span><span><i class="dot" style="background:#2a62b8"></i>停止</span></div>'

# 大胸筋
ov=pins(531,650,[(115,100,"o","鎖骨の内側半分",10,-60),(40,200,"o","胸骨",30,-30),(55,330,"o","第1〜6肋軟骨",25,75),(120,450,"o","腹直筋鞘（腹部）",40,40),(305,268,"i","上腕骨の大結節稜",40,-75)])
page("anatomy/pectoralis-major.html","大胸筋",f'''<div class="crumb"><a href="../index.html">ホーム</a> › <a href="../index.html#anatomy">解剖学</a> › 大胸筋</div>
<h1>大胸筋<small>Pectoralis major</small></h1>
<p class="lead">胸の前面をおおう扇形の大きな筋。腕を<b>前に出す・内側に閉じる・内側にひねる</b>働きをもち、腕立て伏せやベンチプレスの主役です。</p>
<figure class="fig"><div class="wrap"><img src="../img/gray410.png" alt="大胸筋と三角筋・上腕二頭筋の解剖図（体の左側を前から見た図）">{ov}</div>{LEG}
<figcaption>体の左側を前から見た図。扇の形に広がった筋が、腕の付け根へ向かって細く集まっていきます。印の位置はおおよその目安です。<br>図：Gray's Anatomy (1918) Fig.410, Henry Vandyke Carter（パブリックドメイン, Wikimedia Commons "Gray410.png"）</figcaption></figure>
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
page("kinesiology/squat.html","スクワット",f'''<div class="crumb"><a href="../index.html">ホーム</a> › <a href="../index.html#kinesiology">運動学</a> › スクワット</div>
<h1>スクワット<small>Squat</small></h1>
<p class="lead">股関節・膝・足首を同時に曲げ伸ばしして、体を下ろして上げる動作。椅子からの立ち上がりと同じ仕組みで、日常生活の動作であり、代表的な筋トレ種目でもあります。</p>
<figure class="fig">{sq}<figcaption>横から見た模式図（右向き）。赤い点線は<b>床反力</b>（床が体を押し返す力）の線。青と緑の線の長さは、関節からその線までの距離＝<b>モーメントアーム</b>で、数字は図上の長さの比較です。長いほど、その関節まわりの筋の負担が大きくなります。体幹を立てると膝の負担が増え、前に倒すと股関節（と腰）の負担が増えます。</figcaption></figure>
<h2>力学：負担は「消える」のではなく「配分が変わる」</h2>
<p>関節を回す力（モーメント）は<b>力 × 関節からの距離</b>で決まります。重心を足の上に保つ範囲で、体幹の角度や膝の出し方を変えると、股関節と膝の負担の配分が変わります。</p>
<div class="note">膝がつま先より前に出ないように制限すると膝の負担は減りますが、股関節と腰の負担は増えることが報告されています（Fry 2003）。どちらが正しいかではなく、<b>目的と体に合わせて選ぶ</b>ものです。</div>
<h2>主に働く筋</h2>
<table><tr><th>股関節を伸ばす</th><td><a href="../anatomy/gluteus-maximus.html">大殿筋</a>、ハムストリングス、大内転筋</td></tr><tr><th>膝を伸ばす</th><td>大腿四頭筋</td></tr><tr><th>足首の制御</th><td>下腿三頭筋、前脛骨筋</td></tr><tr><th>体幹の保持</th><td>脊柱起立筋、腹筋群</td></tr></table>
<h2>やり方（基本）</h2><ol><li>足幅は肩幅くらい、つま先はやや外向き（骨格に合わせて調整）</li><li>股関節と膝を同時に曲げ、膝はつま先と同じ向きへ</li><li>足の裏全体で床を押したまま、体幹を保てる深さまで下ろす</li><li>床を押して立ち上がる。息は止めない</li></ol>
<h2>目的別の負荷の目安</h2>
<table><tr><th>筋持久力</th><td>1RMの67%以下 ／ 12回以上 ／ 2〜3セット ／ 休息30秒以内</td></tr><tr><th>筋肥大</th><td>67〜85% ／ 6〜12回 ／ 3〜6セット ／ 30〜90秒</td></tr><tr><th>筋力</th><td>85%以上 ／ 6回以下 ／ 2〜6セット ／ 2〜5分</td></tr></table>
<p style="font-size:13px;color:#5d6472">NSCAの教科書の、健康な成人向けの目安。初心者・高齢者・病気のある人は軽い負荷から。2026年のACSM指針は「主要な筋群を週2日以上」から始め、個人に合わせて調整することを重視しています。</p>
<h2>易しく・難しくする</h2><table><tr><th>易しく</th><td>手すりを使って椅子から立ち上がる → 浅くしゃがむ → 台に座るまで</td></tr><tr><th>基本</th><td>自重スクワット</td></tr><tr><th>難しく</th><td>ゴブレット → バーベル → 片脚系（スプリットスクワット）→ ジャンプ</td></tr></table>
<h2>観察するときの注意</h2><p>膝が内に入る、かかとが浮く、腰が丸まる、などは<b>観察できた事実</b>です。原因は可動域・筋力・動き方の癖・骨の形・痛みを避ける動きなど複数考えられるため、追加の評価で確かめます。→ <a href="../assessment/observation.html">体表観察の基本</a></p>
<div class="warn">急な痛みや腫れがあるとき、手術後で制限があるとき、骨粗鬆症で重りを持って背中を丸める動きは、医療者の判断に従ってください。高血圧の人は息をこらえないこと。</div>
<h2>参考文献</h2><ol class="refs"><li>Schoenfeld BJ. Squatting kinematics and kinetics and their application to exercise performance. J Strength Cond Res. 2010;24(12):3497–3506.</li><li>Fry AC, et al. Effect of knee position on hip and knee torques during the barbell squat. J Strength Cond Res. 2003;17(4):629–633.</li><li>Haff GG, Triplett NT (eds). Essentials of Strength Training and Conditioning. 4th ed. NSCA; 2016.</li><li>ACSM Position Stand. Resistance Training Prescription… Med Sci Sports Exerc. 2026;58(4):851–872.</li></ol>''')

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
