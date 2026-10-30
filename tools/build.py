"""Gera as páginas do site em inglês e português a partir dos mesmos blocos.

Uso: python tools/build.py  (escreve os .html na raiz e em pt/)
Os textos dos dois idiomas ficam lado a lado aqui, para nunca divergirem.
"""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent.parent

APP_ID = "1539409410491818075"
# Ver Canais, Enviar Mensagens, Gerenciar Mensagens, Inserir Links, Anexar Arquivos,
# Ler Histórico, Emojis Externos, Conectar, Falar.
PERMISSIONS = "3533824"
INVITE = (f"https://discord.com/oauth2/authorize?client_id={APP_ID}"
          f"&permissions={PERMISSIONS}&integration_type=0&scope=bot+applications.commands")
SITE = "https://juniorstofel.github.io/Darknessbot-website"
UPDATED = {"en": "October 30, 2026", "pt": "30 de outubro de 2026"}

RIOT_LEGAL = {
    "en": "DarknessBot isn’t endorsed by Riot Games and doesn’t reflect the views or opinions of Riot Games "
          "or anyone officially involved in producing or managing Riot Games properties. Riot Games, and all "
          "associated properties are trademarks or registered trademarks of Riot Games, Inc.",
    "pt": "O DarknessBot não é endossado pela Riot Games e não reflete as opiniões da Riot Games nem de "
          "ninguém oficialmente envolvido na produção ou gestão das propriedades da Riot Games. Riot Games e "
          "todas as propriedades associadas são marcas comerciais ou registradas da Riot Games, Inc.",
}

# Caminhos de cada página nos dois idiomas (relativos à raiz do site).
PAGES = {
    "home": {"en": "index.html", "pt": "pt/index.html"},
    "privacy": {"en": "privacy.html", "pt": "pt/privacidade.html"},
    "terms": {"en": "terms.html", "pt": "pt/termos.html"},
}

T = {
    "en": {
        "skip": "Skip to content",
        "server": "DarknessBot",
        "info": "Information",
        "legal": "Legal",
        "ch_welcome": "welcome",
        "ch_commands": "commands",
        "ch_riot": "riot-data",
        "ch_about": "about",
        "ch_privacy": "privacy",
        "ch_terms": "terms",
        "topic": "League of Legends and music for Discord servers",
        "add": "Add to Discord",
        "add_short": "Add",
        "menu": "Open channels",
        "foot_name": "DarknessBot",
        "foot_by": "by Adriano Junior",
        "today": "Today",
        "h1": "League of Legends and music, right inside Discord.",
        "lede": "Link your Riot account, check anyone’s rank, and post a live game as one image with every "
                "player’s numbers. Made for ARAM and ARAM: Mayhem first. Music in the voice channel, same bot.",
        "see_cmds": "See the commands",
        "fine": "Free. No ads, no paid tiers. Built and run by one player for his community.",
        "user": "Lia",
        "reply_note": "Example with fictitious names and numbers. The bot answers in Portuguese.",
        "alt_board": "Example DarknessBot scoreboard for an ARAM: Mayhem game: two teams of five, each player with "
                     "champion, Riot ID, ARAM rank, ARAM wins, pentakills and champion mastery.",
        "cmds_title": "Commands",
        "cmds_intro": "Everything the bot does today. Type / in any channel the bot can see.",
        "g_lol": "League of Legends",
        "g_music": "Music",
        "g_mod": "Moderation",
        "riot_title": "How we use Riot data",
        "riot_intro": "DarknessBot reads public League of Legends data from the Riot Games API, on BR1, only when "
                      "someone runs a command. This is the full list.",
        "th_api": "Riot API",
        "th_for": "Used for",
        "riot_cap": "APIs and what each one is for",
        "riot_points": [
            "Stored: your Discord user ID linked to your Riot PUUID and Riot ID, only after you run "
            "<code>/lol vincular</code>. Removed the moment you run <code>/lol desvincular</code>.",
            "Live game data is reused for 60 seconds, then discarded, so the same game asked twice costs one request.",
            "Champion images and icons come from Data Dragon and Community Dragon, not from the API.",
            "Nothing is sold or shared. No ads, no tracking, no analytics on the bot or on this site.",
        ],
        "planned_title": "Coming next",
        "planned": "Champion win rate in ARAM for every player in a live game, read from each player’s recent "
                   "matches (match-v5). Finished matches never change, so each one is read once and reused for "
                   "everyone who played in it.",
        "about_name": "Adriano Junior",
        "about_badge": "Developer",
        "about": "I made DarknessBot for Darkness, the League community I play with. It started as our music bot "
                 "and turned into the place where we check ranks and argue about the live game. Now it’s open to "
                 "any server.",
        "join": "Join the Darkness server",
        "composer_label": "Try a command",
        "composer_ph": "Type / to try a command",
        "you": "You",
        "privacy": "Privacy Policy",
        "terms": "Terms of Service",
        "rights": "© 2026 Adriano Junior. DarknessBot is a free, independent project.",
        "back": "Back to DarknessBot",
        "updated": "Last updated",
    },
    "pt": {
        "skip": "Pular para o conteúdo",
        "server": "DarknessBot",
        "info": "Informações",
        "legal": "Legal",
        "ch_welcome": "boas-vindas",
        "ch_commands": "comandos",
        "ch_riot": "dados-da-riot",
        "ch_about": "sobre",
        "ch_privacy": "privacidade",
        "ch_terms": "termos",
        "topic": "League of Legends e música para servidores do Discord",
        "add": "Adicionar ao Discord",
        "add_short": "Adicionar",
        "menu": "Abrir canais",
        "foot_name": "DarknessBot",
        "foot_by": "por Adriano Junior",
        "today": "Hoje",
        "h1": "League of Legends e música, direto no seu Discord.",
        "lede": "Vincule sua conta Riot, veja o elo de qualquer pessoa e mostre a partida ao vivo numa imagem só, "
                "com os números de todos os jogadores. Feito pensando primeiro em ARAM e ARAM: Caos. E música "
                "no canal de voz, no mesmo bot.",
        "see_cmds": "Ver os comandos",
        "fine": "Grátis. Sem anúncios, sem plano pago. Feito e mantido por um jogador para a comunidade dele.",
        "user": "Lia",
        "reply_note": "Exemplo com nomes e números fictícios.",
        "alt_board": "Exemplo de placar do DarknessBot numa partida de ARAM: Caos: dois times de cinco, cada "
                     "jogador com campeão, Riot ID, classificação de ARAM, vitórias em ARAM, pentakills e maestria.",
        "cmds_title": "Comandos",
        "cmds_intro": "Tudo o que o bot faz hoje. Digite / em qualquer canal que o bot consiga ver.",
        "g_lol": "League of Legends",
        "g_music": "Música",
        "g_mod": "Moderação",
        "riot_title": "Como usamos os dados da Riot",
        "riot_intro": "O DarknessBot lê dados públicos do League of Legends pela API da Riot Games, no BR1, só "
                      "quando alguém usa um comando. Esta é a lista completa.",
        "th_api": "API da Riot",
        "th_for": "Para quê",
        "riot_cap": "APIs e para que cada uma serve",
        "riot_points": [
            "Guardado: o seu ID de usuário do Discord ligado ao seu PUUID e Riot ID, só depois que você usa "
            "<code>/lol vincular</code>. Apagado na hora em que você usa <code>/lol desvincular</code>.",
            "Os dados da partida ao vivo são reaproveitados por 60 segundos e depois descartados, para a mesma "
            "partida pedida duas vezes custar um pedido só.",
            "Imagens de campeões e ícones vêm do Data Dragon e do Community Dragon, não da API.",
            "Nada é vendido nem repassado. Sem anúncios, sem rastreamento, sem análise de uso no bot ou neste site.",
        ],
        "planned_title": "Em breve",
        "planned": "Taxa de vitória por campeão no ARAM para todos os jogadores da partida ao vivo, lida das "
                   "partidas recentes de cada um (match-v5). Partidas encerradas não mudam, então cada uma é lida "
                   "uma vez e reaproveitada para todos que jogaram nela.",
        "about_name": "Adriano Junior",
        "about_badge": "Desenvolvedor",
        "about": "Fiz o DarknessBot para o Darkness, a comunidade de LoL com quem eu jogo. Começou como o nosso bot "
                 "de música e virou o lugar onde a gente vê o elo e discute a partida ao vivo. Agora ele está "
                 "aberto para qualquer servidor.",
        "join": "Entrar no servidor Darkness",
        "composer_label": "Teste um comando",
        "composer_ph": "Digite / para testar um comando",
        "you": "Você",
        "privacy": "Política de Privacidade",
        "terms": "Termos de Uso",
        "rights": "© 2026 Adriano Junior. O DarknessBot é um projeto independente e gratuito.",
        "back": "Voltar ao DarknessBot",
        "updated": "Atualizado em",
    },
}

# Comandos: (grupo, nome, opções, descrição en, descrição pt)
COMMANDS = [
    ("lol", "/lol vincular", "", "Link your Riot account by typing your Riot ID.",
     "Vincula a sua conta Riot digitando o seu Riot ID."),
    ("lol", "/lol perfil", "membro · riotid", "Level and ranked info for you, a member, or any Riot ID.",
     "Nível e ranqueadas suas, de um membro ou de qualquer Riot ID."),
    ("lol", "/lol partida", "membro · riotid",
     "The live game as one image: every player with rank, win rate or ARAM numbers, and mastery.",
     "A partida ao vivo numa imagem: cada jogador com elo, taxa de vitória ou números de ARAM, e maestria."),
    ("lol", "/lol desvincular", "", "Remove the link between your Discord and your Riot account.",
     "Remove o vínculo entre o seu Discord e a sua conta Riot."),
    ("music", "/play", "busca", "Play a song or playlist from YouTube in your voice channel.",
     "Toca uma música ou playlist do YouTube no seu canal de voz."),
    ("music", "/queue", "", "Show what is playing and what comes next.", "Mostra o que está tocando e o que vem depois."),
    ("music", "/skip", "para", "Skip the current song, or jump to a position in the queue.",
     "Pula a música atual, ou vai direto para uma posição da fila."),
    ("music", "/pause", "", "Pause or resume.", "Pausa ou continua."),
    ("music", "/seek", "tempo", "Jump to a point in the song, like 1:30.", "Vai para um ponto da música, como 1:30."),
    ("music", "/remove", "posicao", "Remove a song from the queue.", "Tira uma música da fila."),
    ("music", "/stop", "", "Stop the music, clear the queue and leave the channel.",
     "Para a música, limpa a fila e sai do canal."),
    ("mod", "/clear", "quantidade · usuario · canal",
     "Delete recent messages, after a confirmation. Moderators only.",
     "Apaga mensagens recentes, depois de uma confirmação. Só para moderadores."),
]

RIOT_APIS = [
    ("account-v1", "Find an account by Riot ID and keep the Riot ID up to date.",
     "Achar a conta pelo Riot ID e manter o Riot ID atualizado."),
    ("summoner-v4", "Summoner level and profile icon.", "Nível e ícone de invocador."),
    ("league-v4", "Rank, LP, wins and losses in Solo/Duo and Flex.",
     "Elo, PDL, vitórias e derrotas na Solo/Duo e na Flex."),
    ("spectator-v5", "Find the game a player is in right now.", "Achar a partida em que o jogador está agora."),
    ("champion-mastery-v4", "Mastery on the champion each player picked.",
     "Maestria no campeão que cada jogador escolheu."),
    ("challenges-v1", "ARAM and Arena rank, ARAM wins and pentakills.",
     "Classificação de ARAM e Arena, vitórias e pentakills em ARAM."),
]

ICON = {
    "hash": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M10.9 3.2a1 1 0 0 1 .8 1.2L11 8h4l.8-4a1 1 0 1 1 2 .4L17 8h3a1 1 0 1 1 0 2h-3.4l-.8 4H19a1 1 0 1 1 0 2h-3.6l-.8 4a1 1 0 1 1-2-.4l.7-3.6h-4l-.7 4a1 1 0 1 1-2-.4L7.4 16H4a1 1 0 1 1 0-2h3.8l.8-4H5a1 1 0 0 1 0-2h4l.8-4a1 1 0 0 1 1.1-.8ZM10.6 10l-.8 4h4l.8-4h-4Z"/></svg>',
    "doc": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M7 3h7l5 5v12a1 1 0 0 1-1 1H7a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2Zm6 1.5V8a1 1 0 0 0 1 1h3.5L13 4.5ZM8 12a1 1 0 0 0 0 2h8a1 1 0 1 0 0-2H8Zm0 4a1 1 0 0 0 0 2h5a1 1 0 1 0 0-2H8Z"/></svg>',
    "plus": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 4a1 1 0 0 1 1 1v6h6a1 1 0 1 1 0 2h-6v6a1 1 0 1 1-2 0v-6H5a1 1 0 1 1 0-2h6V5a1 1 0 0 1 1-1Z"/></svg>',
    "menu": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M4 6a1 1 0 0 1 1-1h14a1 1 0 1 1 0 2H5a1 1 0 0 1-1-1Zm0 6a1 1 0 0 1 1-1h14a1 1 0 1 1 0 2H5a1 1 0 0 1-1-1Zm1 5a1 1 0 1 0 0 2h14a1 1 0 1 0 0-2H5Z"/></svg>',
    "check": '<svg viewBox="0 0 12 12" aria-hidden="true"><path fill="currentColor" d="M4.6 8.6 2.3 6.3a.7.7 0 0 1 1-1l1.3 1.3 4.1-4.1a.7.7 0 1 1 1 1L4.6 8.6Z"/></svg>',
    "slash": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M15.7 3.3a1 1 0 0 1 .6 1.3l-6 15a1 1 0 0 1-1.9-.7l6-15a1 1 0 0 1 1.3-.6Z"/></svg>',
}


def rel(frm, to):
    """Caminho relativo de uma página para outro arquivo do site."""
    depth = frm.count("/")
    return "../" * depth + to


def head(lang, page, title, description):
    path = PAGES[page][lang]
    other = "pt" if lang == "en" else "en"
    return f"""<!doctype html>
<html lang="{'en' if lang == 'en' else 'pt-BR'}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; img-src 'self'; style-src 'self'; font-src 'self'; script-src 'self'; base-uri 'none'; form-action 'none'">
<meta name="referrer" content="no-referrer">
<title>{escape(title)}</title>
<meta name="description" content="{escape(description)}">
<meta name="theme-color" content="#313338">
<link rel="canonical" href="{SITE}/{path}">
<link rel="alternate" hreflang="{lang}" href="{SITE}/{path}">
<link rel="alternate" hreflang="{other}" href="{SITE}/{PAGES[page][other]}">
<link rel="icon" href="{rel(path, 'assets/img/avatar.svg')}" type="image/svg+xml">
<link rel="stylesheet" href="{rel(path, 'assets/site.css')}">
</head>
"""


def channel_link(lang, path, target, label, icon, current):
    cur = ' aria-current="page"' if current else ""
    return f'<li><a class="channel" href="{target}"{cur}>{ICON[icon]}<span>{escape(label)}</span></a></li>'


def frame_start(lang, page, current_channel, title_channel):
    t = T[lang]
    path = PAGES[page][lang]
    home = rel(path, PAGES["home"][lang])
    on_home = page == "home"
    anchor = (lambda a: f"#{a}") if on_home else (lambda a: f"{home}#{a}")
    channels = [
        ("welcome", t["ch_welcome"], anchor("welcome")),
        ("commands", t["ch_commands"], anchor("commands")),
        ("riot", t["ch_riot"], anchor("riot-data")),
        ("about", t["ch_about"], anchor("about")),
    ]
    info = "".join(channel_link(lang, path, href, label, "hash", key == current_channel) for key, label, href in channels)
    legal = "".join([
        channel_link(lang, path, rel(path, PAGES["privacy"][lang]), t["ch_privacy"], "doc", current_channel == "privacy"),
        channel_link(lang, path, rel(path, PAGES["terms"][lang]), t["ch_terms"], "doc", current_channel == "terms"),
    ])
    other = "pt" if lang == "en" else "en"
    other_href = rel(path, PAGES[page][other])
    if lang == "en":
        langs = f'<span aria-current="true">EN</span><a href="{other_href}" hreflang="pt-BR" lang="pt-BR">PT</a>'
    else:
        langs = f'<a href="{other_href}" hreflang="en" lang="en">EN</a><span aria-current="true">PT</span>'
    avatar = rel(path, "assets/img/avatar.svg")
    return f"""<body>
<a class="skip" href="#content">{t['skip']}</a>
<div class="app">
  <div class="rail" aria-hidden="true">
    <a class="rail-item rail-current" href="{home}" tabindex="-1"><img src="{avatar}" alt="" width="48" height="48"></a>
    <span class="rail-sep"></span>
    <a class="rail-item rail-add" href="{INVITE}" tabindex="-1" rel="noopener noreferrer">{ICON['plus']}</a>
  </div>
  <aside class="side" id="channels" aria-label="{t['server']}">
    <div class="side-head"><a class="side-brand" href="{home}">DarknessBot</a></div>
    <nav aria-label="{t['server']}">
      <h2>{t['info']}</h2>
      <ul>{info}</ul>
      <h2>{t['legal']}</h2>
      <ul>{legal}</ul>
    </nav>
    <div class="side-foot"><img src="{avatar}" alt="" width="32" height="32"><div><strong>{t['foot_name']}</strong>{t['foot_by']}</div></div>
  </aside>
  <div class="channel-main">
    <header class="topbar">
      <button class="menu-btn" type="button" aria-controls="channels" aria-expanded="false" aria-label="{t['menu']}" hidden>{ICON['menu']}</button>
      <div class="topbar-title">{ICON['hash' if on_home else 'doc']}<span id="channel-name">{escape(title_channel)}</span></div>
      <div class="topbar-topic">{escape(t['topic'])}</div>
      <div class="topbar-actions">
        <div class="lang" role="group" aria-label="Language / Idioma">{langs}</div>
        <a class="btn btn-primary" href="{INVITE}" rel="noopener noreferrer">{ICON['plus']}<span>{t['add']}</span></a>
      </div>
    </header>
"""


def footer(lang, page):
    t = T[lang]
    path = PAGES[page][lang]
    return f"""    <footer class="footer">
      <nav aria-label="{t['legal']}">
        <a href="{rel(path, PAGES['privacy'][lang])}">{t['privacy']}</a>
        <a href="{rel(path, PAGES['terms'][lang])}">{t['terms']}</a>
        <a href="{rel(path, 'join.html')}" rel="noopener noreferrer">{t['join']}</a>
      </nav>
      <p>{t['rights']}</p>
      <p>{RIOT_LEGAL[lang]}</p>
    </footer>
"""


def frame_end(lang, page, with_script=True):
    path = PAGES[page][lang]
    script = f'<script src="{rel(path, "assets/site.js")}" defer></script>' if with_script else ""
    return f"""  </div>
</div>
{script}
</body>
</html>
"""


def bot_head(lang, path, time_label):
    return (f'<img class="msg-avatar" src="{rel(path, "assets/img/avatar.svg")}" alt="" width="40" height="40">'
            f'<div class="msg-head"><span class="msg-name bot">DarknessBot</span>'
            f'<span class="badge">{ICON["check"]}APP</span><span class="msg-time">{time_label}</span></div>')


def home(lang):
    t = T[lang]
    path = PAGES["home"][lang]
    img = rel(path, "assets/img/scoreboard-example.png")
    groups = [("lol", t["g_lol"]), ("music", t["g_music"]), ("mod", t["g_mod"])]
    picker = ""
    for key, label in groups:
        rows = ""
        for g, name, opts, en, pt in COMMANDS:
            if g != key:
                continue
            desc = en if lang == "en" else pt
            opt_html = ""
            if opts:
                opt_html = '<span class="opts">' + " · ".join(f"<code>{escape(o)}</code>" for o in opts.split(" · ")) + "</span>"
            rows += f'<div class="cmd"><dt>{escape(name)}</dt><dd>{escape(desc)}{opt_html}</dd></div>'
        picker += f'<div class="picker-group"><h3>{label}</h3><dl>{rows}</dl></div>'
    api_rows = "".join(
        f"<tr><td>{api}</td><td>{escape(en if lang == 'en' else pt)}</td></tr>" for api, en, pt in RIOT_APIS)
    points = "".join(f"<li>{p}</li>" for p in t["riot_points"])
    time_today = f'{t["today"]} 21:14'
    time_reply = f'{t["today"]} 21:15'
    html = head(lang, "home", "DarknessBot",
                t["lede"]) + frame_start(lang, "home", "welcome", t["ch_welcome"])
    html += f"""    <main class="stream" id="content">
      <section id="welcome" aria-labelledby="hero-title">
        <article class="msg hero">
          {bot_head(lang, path, time_today)}
          <div class="msg-body">
            <h1 id="hero-title">{escape(t['h1'])}</h1>
            <p class="lede">{escape(t['lede'])}</p>
            <div class="actions">
              <a class="btn btn-primary btn-lg" href="{INVITE}" rel="noopener noreferrer">{ICON['plus']}{t['add']}</a>
              <a class="btn btn-secondary btn-lg" href="#commands">{t['see_cmds']}</a>
            </div>
            <p class="fine">{escape(t['fine'])}</p>
          </div>
        </article>
        <article class="msg">
          <div class="msg-avatar user" aria-hidden="true">L</div>
          <div class="msg-head"><span class="msg-name">{t['user']}</span><span class="msg-time">{time_reply}</span></div>
          <div class="msg-body"><span class="slash">/lol partida <span class="opt">riotid:</span><span class="val">Noite Clara#DKN</span></span></div>
        </article>
        <article class="msg">
          {bot_head(lang, path, time_reply)}
          <div class="msg-body">
            <figure class="shot">
              <a href="{img}"><img src="{img}" width="1000" height="1276" alt="{escape(t['alt_board'])}" loading="eager" decoding="async"></a>
              <figcaption>{escape(t['reply_note'])}</figcaption>
            </figure>
          </div>
        </article>
      </section>

      <section id="commands" aria-labelledby="commands-title">
        <h2 class="divider" id="commands-title">{t['cmds_title']}</h2>
        <article class="msg">
          {bot_head(lang, path, time_reply)}
          <div class="msg-body">
            <p>{escape(t['cmds_intro'])}</p>
            <div class="picker">{picker}</div>
          </div>
        </article>
      </section>

      <section id="riot-data" aria-labelledby="riot-title">
        <h2 class="divider" id="riot-title">{t['riot_title']}</h2>
        <article class="msg">
          {bot_head(lang, path, time_reply)}
          <div class="msg-body">
            <p>{escape(t['riot_intro'])}</p>
            <div class="data">
              <table>
                <caption class="visually-hidden">{t['riot_cap']}</caption>
                <thead><tr><th scope="col">{t['th_api']}</th><th scope="col">{t['th_for']}</th></tr></thead>
                <tbody>{api_rows}</tbody>
              </table>
            </div>
            <ul class="points">{points}</ul>
            <p><strong>{t['planned_title']}:</strong> {escape(t['planned'])}</p>
          </div>
        </article>
      </section>

      <section id="about" aria-labelledby="about-title">
        <h2 class="divider" id="about-title">{t['ch_about']}</h2>
        <article class="msg">
          <div class="msg-avatar user dev" aria-hidden="true">A</div>
          <div class="msg-head"><span class="msg-name">{t['about_name']}</span><span class="badge">{t['about_badge']}</span></div>
          <div class="msg-body">
            <p>{escape(t['about'])}</p>
            <img class="banner-img" src="{rel(path, 'assets/img/darkness-banner.png')}" width="1200" height="300" alt="Darkness" loading="lazy" decoding="async">
            <div class="actions"><a class="btn btn-secondary" href="{rel(path, 'join.html')}" rel="noopener noreferrer">{t['join']}</a></div>
          </div>
        </article>
      </section>
      <div id="demo-replies" aria-live="polite"></div>
    </main>
FOOTER_SLOT
    <div class="composer" hidden>
      <div class="composer-box">
        {ICON['slash']}
        <label class="visually-hidden" for="composer-input">{t['composer_label']}</label>
        <input id="composer-input" type="text" autocomplete="off" spellcheck="false" role="combobox"
          aria-expanded="false" aria-controls="suggest" aria-autocomplete="list" placeholder="{escape(t['composer_ph'])}"
          data-lang="{lang}" data-you="{escape(t['you'])}" data-avatar="{rel(path, 'assets/img/avatar.svg')}"
          data-board="{img}" data-note="{escape(t['reply_note'])}" data-alt="{escape(t['alt_board'])}">
        <ul class="suggest" id="suggest" role="listbox" hidden></ul>
      </div>
    </div>
"""
    html = html.replace("FOOTER_SLOT\n", footer(lang, "home"))
    html += frame_end(lang, "home")
    return html


PRIVACY = {
    "en": ("Privacy Policy", [
        ("Who runs DarknessBot",
         "<p>DarknessBot is a free Discord bot made and operated by Adriano Junior (Discord: juniorstofel), an "
         "individual developer in Brazil. The fastest way to reach me is the Darkness Discord server linked at the "
         "bottom of this page.</p>"),
        ("What the bot stores",
         "<ul><li><strong>Riot account link.</strong> When you run <code>/lol vincular</code>, the bot stores your "
         "Discord user ID, your Riot PUUID, your Riot ID (name and tag) and the date you linked. Nothing is stored "
         "until you run that command.</li>"
         "<li><strong>Music player message.</strong> For each server, the ID of the channel and of the last music "
         "player message, so the next session can delete the old one.</li>"
         "<li><strong>Server logs.</strong> The bot writes technical logs (errors, and lines such as a Discord user "
         "ID linking a Riot ID). They stay on the server that runs the bot and are not shared with anyone.</li></ul>"),
        ("What the bot reads but does not keep",
         "<ul><li>League of Legends data from the Riot Games API (rank, mastery, live game, challenges) is fetched "
         "when someone runs a command. Live game data is reused for 60 seconds, then discarded, and is never "
         "written to disk.</li><li>Music searches are sent to YouTube through the bot’s audio server to find the song. They are "
         "not stored.</li><li>Commands and their options, to answer them. Message content in your server is not read, "
         "except the messages <code>/clear</code> deletes when a moderator asks for it.</li></ul>"),
        ("What we never do",
         "<p>No selling, renting or sharing of data. No ads, trackers or analytics, in the bot or on this website. "
         "This website sets no cookies and loads nothing from other websites.</p>"),
        ("Deleting your data",
         "<p>Run <code>/lol desvincular</code> and your Riot link is deleted immediately. To ask for anything else "
         "to be deleted, or for a copy of what is stored about you, message me on the Darkness server. The music "
         "player record of a server is a single line (channel and message ID); ask and I delete it.</p>"),
        ("Services the bot relies on",
         "<p>Discord (where the bot runs), the Riot Games API (League of Legends data) and YouTube (music). Each has "
         "its own privacy policy. The bot runs on a private server (VPS) rented by the developer. This "
         "website is hosted by GitHub Pages, which keeps standard access logs (such as IP addresses) under "
         "GitHub’s own privacy statement.</p>"),
        ("Children",
         "<p>DarknessBot is for people old enough to use Discord under Discord’s own rules.</p>"),
        ("Changes",
         "<p>If this policy changes, the date at the top changes too, and big changes are announced on the Darkness "
         "server.</p>"),
    ]),
    "pt": ("Política de Privacidade", [
        ("Quem mantém o DarknessBot",
         "<p>O DarknessBot é um bot de Discord gratuito, feito e mantido por Adriano Junior (Discord: juniorstofel), "
         "desenvolvedor independente no Brasil. O jeito mais rápido de falar comigo é o servidor Darkness, no link no "
         "fim desta página.</p>"),
        ("O que o bot guarda",
         "<ul><li><strong>Vínculo com a conta Riot.</strong> Quando você usa <code>/lol vincular</code>, o bot guarda "
         "o seu ID de usuário do Discord, o seu PUUID da Riot, o seu Riot ID (nome e tag) e a data do vínculo. Nada é "
         "guardado antes de você usar esse comando.</li>"
         "<li><strong>Mensagem do player de música.</strong> Para cada servidor, o ID do canal e da última mensagem "
         "do player, para a sessão seguinte apagar a antiga.</li>"
         "<li><strong>Registros do servidor.</strong> O bot escreve registros técnicos (erros e linhas como um ID do "
         "Discord vinculando um Riot ID). Eles ficam no servidor onde o bot roda e não são repassados a ninguém.</li></ul>"),
        ("O que o bot lê, mas não guarda",
         "<ul><li>Dados do League of Legends pela API da Riot Games (elo, maestria, partida ao vivo, desafios), "
         "buscados quando alguém usa um comando. Os dados da partida ao vivo são reaproveitados por 60 segundos, depois "
         "descartados, e nunca são gravados em disco.</li><li>Buscas de música, enviadas ao YouTube pelo servidor de áudio do bot "
         "para achar a música. Não são guardadas.</li><li>Comandos e as opções deles, para responder. O conteúdo das "
         "mensagens do seu servidor não é lido, exceto as mensagens que o <code>/clear</code> apaga quando um "
         "moderador pede.</li></ul>"),
        ("O que nunca fazemos",
         "<p>Não vendemos, alugamos nem repassamos dados. Sem anúncios, rastreadores ou análise de uso, no bot ou "
         "neste site. Este site não usa cookies e não carrega nada de outros sites.</p>"),
        ("Apagar os seus dados",
         "<p>Use <code>/lol desvincular</code> e o seu vínculo com a Riot é apagado na hora. Para pedir que qualquer "
         "outra coisa seja apagada, ou uma cópia do que está guardado sobre você, fale comigo no servidor Darkness. "
         "O registro do player de um servidor é uma linha só (ID do canal e da mensagem); é só pedir que eu apago.</p>"),
        ("Serviços que o bot usa",
         "<p>Discord (onde o bot roda), a API da Riot Games (dados do League of Legends) e o YouTube (música). Cada um "
         "tem a sua própria política de privacidade. O bot roda num servidor privado (VPS) alugado pelo "
         "desenvolvedor. Este site é hospedado pelo GitHub Pages, que mantém registros de acesso comuns (como o "
         "endereço IP) conforme a declaração de privacidade do próprio GitHub.</p>"),
        ("Crianças",
         "<p>O DarknessBot é para pessoas com idade para usar o Discord, pelas regras do próprio Discord.</p>"),
        ("Mudanças",
         "<p>Se esta política mudar, a data no topo muda junto, e mudanças grandes são avisadas no servidor "
         "Darkness.</p>"),
    ]),
}

TERMS = {
    "en": ("Terms of Service", [
        ("Using DarknessBot",
         "<p>By adding DarknessBot to a server or using its commands, you agree to these terms, to "
         "<a href=\"https://discord.com/terms\" rel=\"noopener noreferrer\">Discord’s Terms of Service</a> and to "
         "<a href=\"https://www.riotgames.com/en/terms-of-service\" rel=\"noopener noreferrer\">Riot Games’ Terms of "
         "Service</a>.</p>"),
        ("Free, as it is",
         "<p>DarknessBot is free and provided as it is, without any warranty. It can be offline, slow, or change "
         "how a command works at any time. League of Legends data comes from the Riot Games API and can be late, "
         "missing or wrong.</p>"),
        ("Fair use",
         "<ul><li>Don’t use the bot to harass people, spam commands, or try to break it or its server.</li>"
         "<li>Only link a Riot account that is yours.</li>"
         "<li>Music is streamed from YouTube for listening together in a voice channel. Don’t use the bot to copy or "
         "redistribute music.</li></ul>"),
        ("Stopping access",
         "<p>The developer can remove the bot from a server or block a user who breaks these terms. You can stop "
         "anytime: run <code>/lol desvincular</code> and remove the bot from your server.</p>"),
        ("Riot Games",
         f"<p>{RIOT_LEGAL['en']}</p>"),
        ("Contact and changes",
         "<p>Questions go to the developer on the Darkness Discord server. If these terms change, the date at the "
         "top changes too.</p>"),
    ]),
    "pt": ("Termos de Uso", [
        ("Usando o DarknessBot",
         "<p>Ao adicionar o DarknessBot a um servidor ou usar os comandos dele, você concorda com estes termos, com "
         "os <a href=\"https://discord.com/terms\" rel=\"noopener noreferrer\">Termos de Serviço do Discord</a> e com "
         "os <a href=\"https://www.riotgames.com/pt-br/terms-of-service-BR\" rel=\"noopener noreferrer\">Termos de "
         "Serviço da Riot Games</a>.</p>"),
        ("Grátis, como está",
         "<p>O DarknessBot é gratuito e oferecido como está, sem garantia. Ele pode ficar fora do ar, lento, ou mudar "
         "o funcionamento de um comando a qualquer momento. Os dados do League of Legends vêm da API da Riot Games e "
         "podem chegar atrasados, faltar ou estar errados.</p>"),
        ("Uso justo",
         "<ul><li>Não use o bot para assediar pessoas, mandar comandos em excesso ou tentar derrubar o bot ou o "
         "servidor dele.</li><li>Vincule só uma conta Riot que seja sua.</li>"
         "<li>A música vem do YouTube para ouvir junto no canal de voz. Não use o bot para copiar ou redistribuir "
         "músicas.</li></ul>"),
        ("Fim do acesso",
         "<p>O desenvolvedor pode tirar o bot de um servidor ou bloquear quem descumprir estes termos. Você pode parar "
         "quando quiser: use <code>/lol desvincular</code> e remova o bot do seu servidor.</p>"),
        ("Riot Games",
         f"<p>{RIOT_LEGAL['pt']}</p>"),
        ("Contato e mudanças",
         "<p>Dúvidas vão para o desenvolvedor no servidor Darkness, no Discord. Se estes termos mudarem, a data no "
         "topo muda junto.</p>"),
    ]),
}


def document(lang, page, data):
    t = T[lang]
    path = PAGES[page][lang]
    title, sections = data[lang]
    channel = t["ch_privacy"] if page == "privacy" else t["ch_terms"]
    html = head(lang, page, f"{title} · DarknessBot", f"{title} · DarknessBot") + frame_start(lang, page, page, channel)
    body = "".join(f"<h2>{escape(h)}</h2>{content}" for h, content in sections)
    html += f"""    <main class="doc" id="content">
      <h1>{escape(title)}</h1>
      <p class="updated">{t['updated']}: {UPDATED[lang]}</p>
      {body}
      <p><a href="{rel(path, PAGES['home'][lang])}">{t['back']}</a></p>
    </main>
"""
    html += footer(lang, page) + frame_end(lang, page)
    return html


def main():
    out = {}
    for lang in ("en", "pt"):
        out[PAGES["home"][lang]] = home(lang)
        out[PAGES["privacy"][lang]] = document(lang, "privacy", PRIVACY)
        out[PAGES["terms"][lang]] = document(lang, "terms", TERMS)
    for path, html in out.items():
        target = ROOT / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(html, encoding="utf-8", newline="\n")
        print("escrito", path)


if __name__ == "__main__":
    main()
