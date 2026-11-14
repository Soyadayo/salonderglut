// The one authored motion: the prompt line types itself in, like the devlog videos.
// Without JS (or with reduced motion) the full line is simply there.
(() => {
  const line = document.querySelector('.prompt__line[data-type]');
  if (!line || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const reply = document.querySelector('.prompt__reply');
  const text = line.textContent;
  const cursor = document.createElement('span');
  cursor.className = 'cursor';
  cursor.setAttribute('aria-hidden', 'true');
  line.setAttribute('aria-label', text);
  line.textContent = '';
  const out = document.createElement('span');
  out.setAttribute('aria-hidden', 'true');
  line.append(out, cursor);
  if (reply) reply.classList.add('is-waiting');
  const chars = [...text];
  const step = Math.max(28, Math.min(70, 1400 / chars.length));
  let i = 0;
  const tick = () => {
    out.textContent = chars.slice(0, ++i).join('');
    if (i < chars.length) setTimeout(tick, step);
    else if (reply) setTimeout(() => reply.classList.remove('is-waiting'), 350);
  };
  setTimeout(tick, 350);
})();
