// DarknessBot site: channel menu on phones, current-channel highlight, and the composer demo.
// No network requests, no storage, no third-party code. Everything here is progressive:
// without JavaScript the page is complete, only the composer stays hidden.
(() => {
  'use strict';

  // ---------- Channel drawer on narrow screens ----------
  const menuBtn = document.querySelector('.menu-btn');
  const side = document.getElementById('channels');
  if (menuBtn && side) {
    menuBtn.hidden = false;
    const main = document.querySelector('.channel-main');
    const backdrop = document.createElement('button');
    backdrop.type = 'button';
    backdrop.className = 'backdrop';
    backdrop.tabIndex = -1;
    backdrop.setAttribute('aria-hidden', 'true');
    side.after(backdrop);
    const setOpen = (open) => {
      side.classList.toggle('is-open', open);
      backdrop.classList.toggle('is-open', open);
      menuBtn.setAttribute('aria-expanded', String(open));
      if (main) main.inert = open;
      if (open) side.querySelector('a')?.focus();
    };
    backdrop.addEventListener('click', () => {
      setOpen(false);
      menuBtn.focus();
    });
    menuBtn.addEventListener('click', () => setOpen(!side.classList.contains('is-open')));
    side.addEventListener('click', (e) => {
      if (e.target.closest('a')) setOpen(false);
    });
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && side.classList.contains('is-open')) {
        setOpen(false);
        menuBtn.focus();
      }
    });
  }

  // ---------- Current channel follows the section in view (home only) ----------
  const sections = ['welcome', 'commands', 'riot-data', 'about']
    .map((id) => document.getElementById(id))
    .filter(Boolean);
  const channelName = document.getElementById('channel-name');
  if (sections.length && 'IntersectionObserver' in window) {
    const links = new Map();
    for (const a of document.querySelectorAll('.side .channel')) {
      const hash = a.getAttribute('href');
      if (hash && hash.startsWith('#')) links.set(hash.slice(1), a);
    }
    const observer = new IntersectionObserver((entries) => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        const link = links.get(entry.target.id);
        if (!link) continue;
        for (const a of links.values()) a.removeAttribute('aria-current');
        link.setAttribute('aria-current', 'location');
        if (channelName) channelName.textContent = link.textContent.trim();
      }
    }, { rootMargin: '-45% 0px -50% 0px' });
    sections.forEach((s) => observer.observe(s));
  }

  // ---------- Composer: type / to pick a command, see an example reply ----------
  const composer = document.querySelector('.composer');
  const input = document.getElementById('composer-input');
  const list = document.getElementById('suggest');
  const out = document.getElementById('demo-replies');
  if (!composer || !input || !list || !out) return;

  const pt = input.dataset.lang === 'pt';
  const L = pt
    ? {
        profile: 'Nível 312', solo: 'Solo/Duo', flex: 'Flex', aram: 'ARAM', linked: 'Conta vinculada',
        linkedSub: 'Pronto: o seu elo já aparece no /lol perfil.', unlinked: 'Conta desvinculada',
        unlinkedSub: 'O vínculo com a sua conta Riot foi apagado.', playing: 'Tocando agora',
        queue: 'Fila', next: 'A seguir', skip: 'Pulou para a próxima música.', pause: 'Música pausada.',
        seek: 'Foi para 1:30.', remove: 'Música 2 tirada da fila.', stop: 'Música parada. Até a próxima!',
        clear: 'Uma janela pede confirmação antes de apagar qualquer mensagem.', example: 'Exemplo',
        song: 'Música de exemplo', artist: 'Artista de exemplo', empty: 'Nenhum comando com esse nome.',
      }
    : {
        profile: 'Level 312', solo: 'Solo/Duo', flex: 'Flex', aram: 'ARAM', linked: 'Account linked',
        linkedSub: 'Done: your rank now shows on /lol perfil.', unlinked: 'Account unlinked',
        unlinkedSub: 'The link to your Riot account was deleted.', playing: 'Now playing',
        queue: 'Queue', next: 'Up next', skip: 'Skipped to the next song.', pause: 'Music paused.',
        seek: 'Jumped to 1:30.', remove: 'Song 2 removed from the queue.', stop: 'Music stopped. See you next time!',
        clear: 'A window asks for confirmation before any message is deleted.', example: 'Example',
        song: 'Example song', artist: 'Example artist', empty: 'No command with that name.',
      };

  // Command list comes from the page itself (the commands section), so it never drifts.
  const commands = [...document.querySelectorAll('.picker .cmd')].map((row) => ({
    name: row.querySelector('dt').textContent.trim(),
    desc: row.querySelector('dd').firstChild.textContent.trim(),
  }));

  const el = (tag, attrs = {}, children = []) => {
    const node = document.createElement(tag);
    for (const [k, v] of Object.entries(attrs)) {
      if (k === 'text') node.textContent = v;
      else node.setAttribute(k, v);
    }
    for (const child of children) node.append(child);
    return node;
  };

  const card = (title, sub, rows = [], bar = false) => {
    const box = el('div', { class: 'card' }, [
      el('h4', { text: title }),
      el('div', { class: 'sub', text: sub }),
    ]);
    if (rows.length) {
      const dl = el('dl');
      for (const [k, v] of rows) dl.append(el('dt', { text: k }), el('dd', { text: v }));
      box.append(dl);
    }
    if (bar) box.append(el('div', { class: 'bar', 'aria-hidden': 'true' }, [el('i')]));
    return box;
  };

  const replies = {
    '/lol partida': () => el('figure', { class: 'shot' }, [
      el('img', { src: input.dataset.board, alt: input.dataset.alt, width: '1000', height: '1276', decoding: 'async' }),
      el('figcaption', { text: input.dataset.note }),
    ]),
    '/lol perfil': () => card('Noite Clara#DKN', `${L.profile} · ${L.example}`, [
      [L.solo, pt ? 'Diamante II · 45 PDL · 56%' : 'Diamond II · 45 LP · 56%'],
      [L.flex, pt ? 'Esmeralda I · 12 PDL · 51%' : 'Emerald I · 12 LP · 51%'],
    ]),
    '/lol vincular': () => card(L.linked, L.linkedSub, [['Riot ID', 'Noite Clara#DKN']]),
    '/lol desvincular': () => card(L.unlinked, L.unlinkedSub),
    '/play': () => card(L.playing, `${L.song} · ${L.artist}`, [[L.next, `${L.song} 2`]], true),
    '/queue': () => card(L.queue, L.example, [['1', `${L.song} 2`], ['2', `${L.song} 3`]]),
    '/skip': () => card(L.skip, L.example),
    '/pause': () => card(L.pause, L.example),
    '/seek': () => card(L.seek, L.example),
    '/remove': () => card(L.remove, L.example),
    '/stop': () => card(L.stop, L.example),
    '/clear': () => card(L.clear, L.example),
  };

  const message = (who, body, isBot) => {
    const avatar = isBot
      ? el('img', { class: 'msg-avatar', src: input.dataset.avatar, alt: '', width: '40', height: '40' })
      : el('div', { class: 'msg-avatar user', 'aria-hidden': 'true', text: who.slice(0, 1) });
    const head = el('div', { class: 'msg-head' }, [el('span', { class: isBot ? 'msg-name bot' : 'msg-name', text: who })]);
    if (isBot) head.append(el('span', { class: 'badge', text: 'APP' }));
    return el('article', { class: 'msg reply-enter' }, [avatar, head, el('div', { class: 'msg-body' }, [body])]);
  };

  let items = [];
  let active = -1;

  const close = () => {
    list.hidden = true;
    input.setAttribute('aria-expanded', 'false');
    input.removeAttribute('aria-activedescendant');
    active = -1;
  };

  const highlight = (index) => {
    active = index;
    items.forEach((li, i) => li.setAttribute('aria-selected', String(i === index)));
    if (items[index]) {
      input.setAttribute('aria-activedescendant', items[index].id);
      items[index].scrollIntoView({ block: 'nearest' });
    }
  };

  const run = (name) => {
    close();
    input.value = '';
    const make = replies[name];
    const user = message(input.dataset.you, el('span', { class: 'slash', text: name }), false);
    const bot = message('DarknessBot', make ? make() : card(L.empty, name), true);
    out.replaceChildren(user, bot);
    bot.scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'end' });
  };

  const open = () => {
    const q = input.value.trim().toLowerCase();
    if (!q.startsWith('/')) return close();
    const found = commands.filter((c) => c.name.toLowerCase().startsWith(q) || c.name.toLowerCase().includes(q.slice(1)));
    list.replaceChildren();
    items = found.map((c, i) => {
      const li = el('li', { id: `cmd-${i}`, role: 'option', 'aria-selected': 'false' }, [
        el('b', { text: c.name }),
        el('span', { text: c.desc }),
      ]);
      li.addEventListener('mousedown', (e) => {
        e.preventDefault();
        run(c.name);
      });
      list.append(li);
      return li;
    });
    if (!items.length) return close();
    list.hidden = false;
    input.setAttribute('aria-expanded', 'true');
    highlight(0);
  };

  input.addEventListener('input', open);
  input.addEventListener('keydown', (e) => {
    if (list.hidden) {
      if (e.key === 'Enter' && input.value.trim()) {
        e.preventDefault();
        const exact = commands.find((c) => c.name === input.value.trim().toLowerCase());
        run(exact ? exact.name : input.value.trim());
      }
      return;
    }
    if (e.key === 'ArrowDown') {
      e.preventDefault();
      highlight((active + 1) % items.length);
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      highlight((active - 1 + items.length) % items.length);
    } else if (e.key === 'Enter' || e.key === 'Tab') {
      if (active >= 0) {
        e.preventDefault();
        run(items[active].querySelector('b').textContent);
      }
    } else if (e.key === 'Escape') {
      close();
    }
  });
  input.addEventListener('blur', () => setTimeout(close, 120));
  composer.hidden = false;
})();
