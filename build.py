"""Writes every page of the Salon der Glut site from the copy below (CONTENT.md is the approved source).

    python build.py

The output is plain HTML (index.html, stella/, oribe/, tsukumogami/, privacy/, en/...). You can edit
the HTML by hand, but the next run overwrites it, so put lasting changes here. Web-sized images go to
images/web/ (1280 px wide).
"""
import html
import os

from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
YOUTUBE = "https://www.youtube.com/channel/UCJVWJr2p7W69XMKOHQjBb0g"
MAIL = "haustacorari@gmail.com"
UPDATED = "2026-11-14"
e = html.escape

PAGES = ["home", "stella", "oribe", "tsukumogami", "privacy", "impressum"]
PATH = {"home": "", "stella": "stella/", "oribe": "oribe/", "tsukumogami": "tsukumogami/", "privacy": "privacy/",
        "impressum": "impressum/"}

UI = {
    "ja": {"prompt": "プロンプト", "nav": {"stella": "ステラは狼である。", "oribe": "猫と織部", "tsukumogami": "付喪神の盤"},
           "skip": "本文へ", "go": "このゲームを見る", "verdict": ["改善の余地、", "大いにあり"], "dev": "開発中",
           "channel_text": "制作記録は YouTube で、火・金・日に出しています。", "channel_button": "YouTube で制作記録を見る",
           "privacy": "プライバシーポリシー", "ai": "AI"},
    "en": {"prompt": "Prompt", "nav": {"stella": "Stella Is a Wolf", "oribe": "Neko to Oribe", "tsukumogami": "Tsukumogami Board"},
           "skip": "Skip to content", "go": "See this game", "verdict": ["Plenty of room", "to improve"], "dev": "In development",
           "channel_text": "New devlog episodes go up on YouTube on Tuesdays, Fridays and Sundays.",
           "channel_button": "Watch the devlog on YouTube", "privacy": "Privacy Policy", "ai": "AI"},
}

GAMES = {
    "stella": {
        "pixel": False,
        "header": "stella_00_hero.jpg",
        "grid": ["stella_02_burning-village.jpg", "stella_03_battle.jpg", "stella_04_four-legs.jpg", "stella_01_title.jpg"],
        "ja": {
            "title": "ステラは狼である。", "kind": "タクティクス / PC(開発中)", "line": "村は燃えていた。",
            "caption": "人間を殺さない狼の母の、タクティクス。",
            "where": "タクティクス / PC",
            "home_caption": "狼の母が、狩った獣を食べて子を産む。",
            "grid_captions": ["燃える村。物語の最初の場面", "戦闘。母の一手ごとに群れの命運が動く", "四つ足で駆け出すステラ", "タイトル画面"],
            "body": ["人の村を追われた狼の母、ステラ。狩った獣を食べ、その獣の姿を受け継いだ子を産みながら、群れを率いて生き延びます。人間とは戦っても、殺しはしません。"],
            "points": [("食べた獣が、子の姿になる", "熊を食べれば熊の毛の子が、亀を食べれば甲羅を持った子が生まれる。"),
                       ("母が倒れたら、群れが終わる", "子を前に出すか、自分が盾になるか。一手ごとに選ぶ。"),
                       ("物語と曲は作り手のもの", "物語の文章は作り手が書き、曲も作り手が作曲しています。地面の質感やモデルの一部に生成 AI を使っており、どこまでが AI かは制作記録の第6回で公開しています。")],
        },
        "en": {
            "title": "Stella Is a Wolf", "kind": "Tactics / PC, in development", "line": "The village was burning.",
            "caption": "A tactics game about a wolf mother who never kills a human.",
            "where": "Tactics / PC",
            "home_caption": "A wolf mother eats what she hunts, and her children are born from it.",
            "grid_captions": ["The burning village, where the story opens", "Battle. Every move the mother makes decides the pack", "Stella breaking into a run on four legs", "The title screen"],
            "body": ["Stella is a wolf mother driven out of a human village. She keeps her pack alive by hunting, and every animal she eats leaves its mark on the next child she bears. She fights people. She never kills them."],
            "points": [("What she eats, her children become", "Eat a bear and the pup grows a bear's coat. Eat a turtle and it is born with a shell."),
                       ("If the mother falls, the pack is finished", "Send a child ahead, or stand in front yourself. You decide every turn."),
                       ("The story and the music are ours", "The author writes the story text and composed the soundtrack. Some ground textures and models started as AI output; episode 6 of the devlog lists exactly which.")],
        },
    },
    "oribe": {
        "pixel": True,
        "header": "oribe_01_opening.jpg",
        "grid": ["oribe_03_stack.jpg", "oribe_02_battle.jpg", "oribe_04_map.jpg"],
        "ja": {
            "title": "猫と織部", "kind": "YouTube Playables 向け(開発中)", "line": "器を積んで、崩す。",
            "caption": "ある日、遊戯の神の声が響き、世界は石になった。",
            "where": "YouTube Playables",
            "home_caption": "器を積んで崩すと、猫が生まれる。",
            "grid_captions": ["棚に器を積む。崩れ方から猫が生まれる", "猫を連れて、選ばれた者どうしの勝負", "章を終えると、国に色が戻る"],
            "body": ["織部焼の窯がある里の弟子が、窯場に残った器を積み、崩す。その崩れ方から、ケットシー(猫)が一匹生まれます。猫たちを連れて、石の世界で選ばれた者どうしの勝負を、12の章をかけて勝ち抜いていきます。"],
            "points": [("積んで、崩して、生まれる", "落ちてくる器を棚にどう乗せるか。崩れた形から、どんな猫が生まれるかが決まる。"),
                       ("一局は2〜3分", "どこで閉じても、続きから遊べる。"),
                       ("歪みを美しいとする", "灰色の世界に最初に戻ってくる色は、織部の緑。")],
        },
        "en": {
            "title": "Neko to Oribe", "kind": "For YouTube Playables, in development", "line": "Stack the bowls. Let them fall.",
            "caption": "One day the god of games spoke, and the world turned to stone.",
            "where": "YouTube Playables",
            "home_caption": "Stack pottery until it falls, and a cat is born from the wreck.",
            "grid_captions": ["Bowls on the shelf. How they fall decides the cat", "A band of cats against the god's chosen", "Finish a chapter and colour comes back to the land"],
            "body": ["In a village of Oribe potters, an apprentice stacks the bowls left in the kiln yard until they fall. A cat spirit is born from the way they break. With a band of cats, the apprentice works through twelve chapters of contests against the few people the god left moving."],
            "points": [("Stack it, drop it, meet a cat", "How the pieces land on the shelf, and how they fall, decides which cat you get."),
                       ("Two or three minutes a round", "Close it whenever you like. It picks up where you left off."),
                       ("Crooked on purpose", "Oribe ware treats warped shapes as beautiful. The first colour to return to the grey world is Oribe green.")],
        },
    },
    "tsukumogami": {
        "pixel": False,
        "header": "tsukumogami_01_board.jpg",
        "grid": ["tsukumogami_02_melody.jpg", "tsukumogami_03_rows.jpg"],
        "ja": {
            "title": "付喪神の盤", "kind": "音楽を組む盤(開発中)", "line": "駒を置けば、鳴る。",
            "caption": "古道具の妖怪が、16列×6行の盤で音楽になる。",
            "where": "音楽を組む盤",
            "home_caption": "古道具の妖怪を盤に置くと、音楽が鳴りだす。",
            "grid_captions": ["旋律の行。音の高さが駒の浮く高さになる", "行ごとに音とつまみを持つ6行の盤"],
            "body": ["古い道具に宿る妖怪、付喪神。下駄、茶碗、石臼、提灯、箸の駒を、16列×6行の木の盤に置くと、その場で音が鳴ります。",
                     "旋律の行では、音の高さが駒の浮く高さになります。盤を横から回して見ると、メロディーがそのまま立体の線になって見えます。"],
            "points": [("置けば鳴る", "説明を読まなくても、駒を置いた瞬間から音楽になる。"),
                       ("音を自分で作る", "録った音や短いフレーズを工房で作り、盤の行に割り振る。"),
                       ("遊びながら学ぶ", "同じ盤で、リズムと和音の仕組みを体で覚える。")],
        },
        "en": {
            "title": "Tsukumogami Board", "kind": "A board for building music, in development", "line": "Put a piece down. It plays.",
            "caption": "Old household spirits on a 16 by 6 board, turned into music.",
            "where": "A board for building music",
            "home_caption": "Place old household spirits on a wooden board and they start to play.",
            "grid_captions": ["A melody row. Pitch is how high a piece floats", "Six rows, each with its own sound and knobs"],
            "body": ["Tsukumogami are the spirits that move into old household things. Here they are pieces: a geta sandal, a tea bowl, a millstone, a paper lantern, a pair of chopsticks. Put one on the 16 by 6 wooden board and it plays.",
                     "On the melody rows, pitch is how high a piece floats. Turn the board on its side and the tune is right there, a line drawn in the air."],
            "points": [("Place it and it plays", "No manual needed. Music starts with the first piece."),
                       ("Make your own sounds", "Record a sound or build a short phrase in the workshop, then give it to a row."),
                       ("Learn while you play", "The same board teaches how rhythm and chords work.")],
        },
    },
}

HOME = {
    "ja": {"title": "Salon der Glut", "line": "ゲームを三つ、作っている。",
           "reply": "三つとも開発中です。AI にどう頼み、何を自分の手でやっているかを、YouTube で記録しています。"},
    "en": {"title": "Salon der Glut", "line": "We are making three games.",
           "reply": "All three are in development. We film how they get made: the prompts we give the AI, and the parts we still do by hand."},
}

ADDRESS_HTML = "Soya Arakawa<br>Salon der Glut<br>c/o Block Services<br>Stuttgarter Str. 106<br>70736 Fellbach<br>Deutschland"
MAIL_LINK = '<a href="mailto:haustacorari@gmail.com">haustacorari@gmail.com</a>'
GITHUB_PRIVACY = "https://docs.github.com/site-policy/privacy-policies/github-general-privacy-statement"

PRIVACY = {
    "ja": f"""<p class="updated">最終更新: 2026年11月14日</p>
<p>このページでは、Salon der Glut(以下「私たち」)が、このサイトと、自分たちの YouTube チャンネルの運営に使う道具で、個人に関する情報をどう扱うかを説明します。EU 一般データ保護規則(GDPR)に基づく説明です。</p>
<h2>責任者</h2>
<p>{ADDRESS_HTML}<br>メール: {MAIL_LINK}</p>
<h2>このサイトの配信(GitHub Pages)</h2>
<p>このサイトは、GitHub, Inc.(88 Colton Street, San Francisco, CA 94107, USA)の GitHub Pages で配信しています。ページを開くと、GitHub は配信と安全のために、IP アドレス、日時、開いたページ、ブラウザの種類などのアクセス記録を処理します。この処理は、サイトを安定して安全に届けるという私たちの正当な利益に基づきます(GDPR 第6条第1項 f)。情報は米国で処理されることがあります。詳しくは <a href="{GITHUB_PRIVACY}">GitHub のプライバシーに関する声明</a>をご覧ください。</p>
<p>私たち自身は、アクセス解析、Cookie、外部のフォントや追跡の仕組みを使っていません。ページは外部のサーバーから何も読み込みません。</p>
<h2>メールでのお問い合わせ</h2>
<p>メールをいただいた場合、返信のためだけに、お名前、メールアドレス、本文を使います(GDPR 第6条第1項 b または f)。用件が済み、保存の義務がなくなれば削除します。</p>
<h2>YouTube の投稿道具</h2>
<p>私たちは、YouTube API サービスを使って、制作記録の動画を自分たちのチャンネル(Haus Tacorari)に上げ、公開日時を予約する道具を使っています。</p>
<ul>
<li>使う人は、私たち自身だけです。ほかの人のアカウントにはつながりません。</li>
<li>読み書きするのは、Haus Tacorari のチャンネルの情報(動画のアップロード、タイトル、説明、公開日時、サムネイル)と、チャンネル名の確認だけです。</li>
<li>ログインの情報(アクセストークン)は、私たちの作業用のコンピューターの中だけに保存し、外部に送ったり共有したりしません。</li>
<li>取得した情報を、広告、販売、第三者への提供に使いません。</li>
<li>アクセスの許可は、<a href="https://myaccount.google.com/permissions">Google アカウントのセキュリティ設定</a>からいつでも取り消せます。</li>
</ul>
<p>この道具には、<a href="https://www.youtube.com/t/terms">YouTube の利用規約</a>と <a href="https://policies.google.com/privacy">Google のプライバシーポリシー</a>も適用されます。</p>
<h2>あなたの権利</h2>
<p>あなたには、自分に関する情報について、開示(第15条)、訂正(第16条)、削除(第17条)、処理の制限(第18条)、データポータビリティ(第20条)、異議(第21条)を求める権利があります。ご連絡は上のメールアドレスへどうぞ。監督機関に苦情を申し立てることもできます。私たちの所在地の監督機関は、バーデン=ヴュルテンベルク州のデータ保護・情報自由委員(LfDI Baden-Württemberg)です。</p>""",
    "en": f"""<p class="updated">Last updated: 14 November 2026</p>
<p>This page explains how Salon der Glut ("we") handles personal data on this website and in the tool we use to run our own YouTube channel, as required by the EU General Data Protection Regulation (GDPR).</p>
<h2>Controller</h2>
<p>{ADDRESS_HTML}<br>Email: {MAIL_LINK}</p>
<h2>Hosting (GitHub Pages)</h2>
<p>The site is served by GitHub Pages, run by GitHub, Inc., 88 Colton Street, San Francisco, CA 94107, USA. When you open a page, GitHub processes access data such as your IP address, the time, the page requested and your browser type, to deliver the site and keep it secure. The legal basis is our legitimate interest in a stable, secure website (Art. 6(1)(f) GDPR). This data may be processed in the United States. See the <a href="{GITHUB_PRIVACY}">GitHub General Privacy Statement</a>.</p>
<p>We use no analytics, no cookies, and no external fonts or trackers. The pages load nothing from third-party servers.</p>
<h2>Email</h2>
<p>If you write to us, we use your name, email address and message only to reply (Art. 6(1)(b) or (f) GDPR). We delete them once the matter is settled and no retention duty applies.</p>
<h2>Our YouTube publishing tool</h2>
<p>We use the YouTube API Services in a small tool that uploads our devlog videos to our own channel, Haus Tacorari, and schedules when they go public.</p>
<ul>
<li>We are its only users. It does not connect to anyone else's account.</li>
<li>It reads and writes data for the Haus Tacorari channel only: video uploads, titles, descriptions, publish times and thumbnails, plus a check of the channel name.</li>
<li>The sign-in token stays on our own work computer. We do not send it anywhere or share it.</li>
<li>We do not use any of this data for advertising, sell it, or pass it to third parties.</li>
<li>Access can be revoked at any time in your <a href="https://myaccount.google.com/permissions">Google Account security settings</a>.</li>
</ul>
<p>The <a href="https://www.youtube.com/t/terms">YouTube Terms of Service</a> and the <a href="https://policies.google.com/privacy">Google Privacy Policy</a> also apply to this tool.</p>
<h2>Your rights</h2>
<p>You have the right of access (Art. 15), rectification (Art. 16), erasure (Art. 17), restriction of processing (Art. 18), data portability (Art. 20) and objection (Art. 21). Write to the address above. You may also lodge a complaint with a supervisory authority. Ours is the State Commissioner for Data Protection and Freedom of Information of Baden-Württemberg (LfDI Baden-Württemberg).</p>""",
}

IMPRESSUM_DE = f"""<h2 lang="de">Impressum</h2>
<div lang="de">
<p><strong>Angaben gemäß § 5 DDG</strong><br>{ADDRESS_HTML}</p>
<p><strong>Kontakt</strong><br>E-Mail: {MAIL_LINK}</p>
<p><strong>Umsatzsteuer</strong><br>Gemäß § 19 UStG wird keine Umsatzsteuer berechnet (Kleinunternehmerregelung).</p>
<p><strong>Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV</strong><br>Soya Arakawa, Anschrift wie oben.</p>
<p><strong>Verbraucherstreitbeilegung</strong><br>Wir sind nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>
</div>"""

IMPRESSUM = {
    "ja": IMPRESSUM_DE + f"""
<h2>運営者情報(日本語訳)</h2>
<p>ドイツの法律(デジタルサービス法 § 5)に基づく表示です。正文は上のドイツ語です。</p>
<p><strong>運営者</strong><br>{ADDRESS_HTML}</p>
<p><strong>連絡先</strong><br>メール: {MAIL_LINK}</p>
<p><strong>売上税</strong><br>ドイツ売上税法 § 19(小規模事業者の特例)により、売上税は課していません。</p>
<p><strong>内容の責任者(州間メディア協定 § 18 第2項)</strong><br>Soya Arakawa(所在地は上と同じ)</p>
<p><strong>消費者紛争の調停</strong><br>消費者調停機関での紛争解決の手続きには参加しません。参加の義務もありません。</p>""",
    "en": IMPRESSUM_DE + f"""
<h2>Legal notice (English translation)</h2>
<p>German law requires this notice (§ 5 of the Digital Services Act, DDG). The German text above is authoritative.</p>
<p><strong>Provider</strong><br>{ADDRESS_HTML}</p>
<p><strong>Contact</strong><br>Email: {MAIL_LINK}</p>
<p><strong>VAT</strong><br>No VAT is charged under § 19 UStG (small business scheme).</p>
<p><strong>Responsible for content under § 18(2) MStV</strong><br>Soya Arakawa, address as above.</p>
<p><strong>Consumer dispute resolution</strong><br>We are neither willing nor obliged to take part in dispute resolution proceedings before a consumer arbitration board.</p>""",
}


YT_ICON = ('<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8">'
           '<rect x="2.5" y="5" width="19" height="14" rx="4"/><path d="M10 9.2v5.6l4.8-2.8z" fill="currentColor" stroke="none"/></svg>')

CONTRACT = """<!--
THESIS: every page opens as the devlog's prompt card. One typed line, then the game answers in pictures. Refuses the studio default of a hero image over a grid of game cards.
OWN-WORLD: near-black #080606 ground, warm ink #eee6dc, dim #a1968d, one ember gold #d9ad5e (from the flame logo) for action, steel #b0bec8 for the AI reply. A 3px rounded prompt frame with a block cursor; mincho titles, gothic captions, Palatino for Latin. The video's picture window with one caption line beneath.
STORY: a player who came from a Short recognises the card and sees three games as three prompts. They open one, read what it is, and go to the channel.
FIRST VIEWPORT: the flame mark and "Salon der Glut" top left, JA/EN top right. The prompt card fills the column and types "ゲームを三つ、作っている。"; the AI reply follows. The first game's picture window starts below the fold line on desktop and in view on phones.
FORM: devlog prompt card, my 1st of 7. Seed key 8dda7d13 (user chose the pick over the roll).
FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
-->"""


def web_images():
    src = os.path.join(ROOT, "images")
    out = os.path.join(src, "web")
    os.makedirs(out, exist_ok=True)
    sizes = {}
    for name in os.listdir(src):
        if not name.endswith(".jpg"):
            continue
        im = Image.open(os.path.join(src, name)).convert("RGB")
        pixel = name.startswith("oribe_") and name != "oribe_03_stack.jpg"
        if im.width > 1280:
            im = im.resize((1280, round(im.height * 1280 / im.width)), Image.NEAREST if pixel else Image.LANCZOS)
        im.save(os.path.join(out, name), quality=84, optimize=True, progressive=True)
        sizes[name] = im.size
    return sizes


def rel(depth):
    return "../" * depth


def href(lang, page, depth):
    base = rel(depth) + ("en/" if lang == "en" else "")
    return base + PATH[page] if PATH[page] else (base or "./")


def img(sizes, depth, name, alt, lazy=True, cls=""):
    w, h = sizes[name]
    return (f'<img src="{rel(depth)}images/web/{name}" width="{w}" height="{h}" alt="{e(alt)}"'
            f'{" loading=\"lazy\"" if lazy else ""} decoding="async"{f" class=\"{cls}\"" if cls else ""}>')


def prompt(lang, line, reply=None, date=UPDATED):
    u = UI[lang]
    r = (f'<p class="prompt__reply"><b>{u["ai"]}</b>{e(reply)}</p>' if reply else "")
    return (f'<section class="prompt" aria-label="{e(u["prompt"])}">'
            f'<div class="prompt__meta"><span>{u["prompt"]}</span><span>{date}</span></div>'
            f'<div class="prompt__box"><span class="prompt__caret" aria-hidden="true">&gt;</span>'
            f'<h1 class="prompt__line" data-type>{e(line)}</h1>{r}</div></section>')


def shell(lang, page, depth, title, desc, body):
    u = UI[lang]
    other = "en" if lang == "ja" else "ja"
    nav = "".join(f'<a href="{href(lang, p, depth)}"{" aria-current=\"page\"" if p == page else ""}>{e(u["nav"][p])}</a>'
                  for p in ("stella", "oribe", "tsukumogami"))
    if lang == "ja":
        langs = f'<span lang="ja">JA</span><a href="{href("en", page, depth)}" lang="en" hreflang="en">EN</a>'
    else:
        langs = f'<a href="{href("ja", page, depth)}" lang="ja" hreflang="ja">JA</a><span lang="en">EN</span>'
    full_title = title if page == "home" else f"{title} | Salon der Glut"
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full_title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="theme-color" content="#080606">
<link rel="icon" href="{rel(depth)}assets/favicon.png">
<link rel="alternate" hreflang="{lang}" href="{href(lang, page, depth)}">
<link rel="alternate" hreflang="{other}" href="{href(other, page, depth)}">
<meta property="og:title" content="{e(full_title)}">
<meta property="og:description" content="{e(desc)}">
<link rel="stylesheet" href="{rel(depth)}assets/site.css">
</head>
<body>
{CONTRACT}
<a class="skip" href="#main">{u["skip"]}</a>
<header class="bar">
<a class="bar__home" href="{href(lang, "home", depth)}"><img src="{rel(depth)}assets/mark-192.png" width="40" height="40" alt=""><span class="bar__name">Salon der Glut</span></a>
<nav aria-label="Games">{nav}<span class="lang">{langs}</span></nav>
</header>
<main id="main">
{body}
</main>
<p class="verdict" aria-hidden="true">{u["verdict"][0]}<br>{u["verdict"][1]}</p>
<footer>
<span>&copy; 2026 Salon der Glut</span>
<a href="mailto:{MAIL}">{MAIL}</a>
<a href="{YOUTUBE}">YouTube</a>
<a class="spacer" href="{href(lang, "privacy", depth)}">{u["privacy"]}</a>
<a href="{href(lang, "impressum", depth)}" lang="de">Impressum</a>
</footer>
<script src="{rel(depth)}assets/type.js" defer></script>
</body>
</html>
"""


def home(lang, sizes, depth):
    u = UI[lang]
    h = HOME[lang]
    parts = [prompt(lang, h["line"], h["reply"])]
    for i, g in enumerate(("stella", "oribe", "tsukumogami")):
        G = GAMES[g]
        t = G[lang]
        first = G["grid"][0]
        parts.append(
            f'<article class="episode{" pixel" if G["pixel"] else ""}"><a href="{href(lang, g, depth)}">'
            f'<figure class="shot">{img(sizes, depth, first, t["grid_captions"][0], lazy=i > 0)}'
            f'<figcaption>{e(t["home_caption"])}</figcaption></figure>'
            f'<h2 class="episode__title">{e(t["title"])}</h2>'
            f'<p class="episode__where">{e(t["where"])} · {u["dev"]}</p>'
            f'<span class="episode__go">{u["go"]} &rarr;</span></a></article>')
    parts.append(f'<section class="channel"><p>{e(u["channel_text"])}</p>'
                 f'<a class="button" href="{YOUTUBE}">{YT_ICON}{e(u["channel_button"])}</a></section>')
    parts.append(f'<section class="titlecard" aria-label="Salon der Glut"><img class="titlecard__mark" src="{rel(depth)}assets/mark-512.png" width="512" height="512" alt=""><p class="titlecard__name" lang="de">Salon der Glut</p>'
                 f'<p class="titlecard__studio">{"ゲームを作るスタジオ" if lang == "ja" else "A game studio"}</p></section>')
    return "\n".join(parts)


def game(lang, g, sizes, depth):
    u = UI[lang]
    G = GAMES[g]
    t = G[lang]
    pix = " pixel" if G["pixel"] else ""
    parts = [prompt(lang, t["line"]),
             f'<figure class="shot{pix}">{img(sizes, depth, G["header"], t["caption"], lazy=False)}<figcaption>{e(t["caption"])}</figcaption></figure>',
             '<div class="copy">' + f'<p class="kind">{e(t["kind"])}</p>' + "".join(f"<p>{e(p)}</p>" for p in t["body"])
             + '<ul class="points">' + "".join(f"<li><strong>{e(a)}</strong>{e(b)}</li>" for a, b in t["points"]) + "</ul></div>"]
    for name, cap in zip(G["grid"], t["grid_captions"]):
        if name == G["header"]:
            continue
        parts.append(f'<figure class="shot{pix}">{img(sizes, depth, name, cap)}<figcaption>{e(cap)}</figcaption></figure>')
    parts.append(f'<section class="channel"><p>{e(u["channel_text"])}</p>'
                 f'<a class="button" href="{YOUTUBE}">{YT_ICON}{e(u["channel_button"])}</a></section>')
    parts.append(f'<section class="titlecard" aria-label="{e(t["title"])}"><p class="titlecard__name">{e(t["title"])}</p>'
                 f'<p class="titlecard__studio">Salon der Glut</p><p class="titlecard__note">{u["dev"]}</p></section>')
    return "\n".join(parts)


def privacy(lang):
    title = UI[lang]["privacy"]
    return prompt(lang, title) + f'<div class="legal">{PRIVACY[lang]}</div>'


def impressum(lang):
    return prompt(lang, "Impressum") + f'<div class="legal">{IMPRESSUM[lang]}</div>'


def main():
    sizes = web_images()
    count = 0
    for lang in ("ja", "en"):
        for page in PAGES:
            depth = (1 if lang == "en" else 0) + (1 if PATH[page] else 0)
            if page == "home":
                title, desc, body = HOME[lang]["title"], HOME[lang]["reply"], home(lang, sizes, depth)
            elif page == "impressum":
                title, desc, body = "Impressum", "Impressum | Salon der Glut", impressum(lang)
            elif page == "privacy":
                title, desc, body = UI[lang]["privacy"], UI[lang]["privacy"] + " | Salon der Glut", privacy(lang)
            else:
                t = GAMES[page][lang]
                title, desc, body = t["title"], t["caption"] + " " + t["body"][0], game(lang, page, sizes, depth)
            folder = os.path.join(ROOT, "en" if lang == "en" else "", PATH[page])
            os.makedirs(folder, exist_ok=True)
            with open(os.path.join(folder, "index.html"), "w", encoding="utf-8", newline="\n") as f:
                f.write(shell(lang, page, depth, title, desc, body))
            count += 1
    open(os.path.join(ROOT, ".nojekyll"), "w").close()
    print("wrote", count, "pages")


if __name__ == "__main__":
    main()
