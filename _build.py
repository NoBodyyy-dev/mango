import os
OUT=__import__('os').path.dirname(__import__('os').path.abspath(__file__))

DEFS='''<svg width="0" height="0" aria-hidden="true" focusable="false" style="position:absolute">
  <defs>
    <linearGradient id="gB" x1="0%" y1="70%" x2="100%" y2="20%"><stop stop-color="#FFE08A"/><stop offset=".5" stop-color="#FFC34D"/><stop offset="1" stop-color="#FFA02E"/></linearGradient>
    <linearGradient id="gO" x1="0%" y1="100%" x2="80%" y2="0%"><stop stop-color="#FF8A24"/><stop offset=".6" stop-color="#FF6D1D"/><stop offset="1" stop-color="#FFAC32"/></linearGradient>
    <linearGradient id="gR" x1="0%" y1="100%" x2="100%" y2="0%"><stop stop-color="#F66021"/><stop offset=".55" stop-color="#C72F24"/><stop offset="1" stop-color="#F44325"/></linearGradient>
    <linearGradient id="gL" x1="0%" y1="100%" x2="100%" y2="0%"><stop stop-color="#226849"/><stop offset="1" stop-color="#79B97B"/></linearGradient>
    <clipPath id="cB"><path d="M24 65 C27 50 45 36 65 27 C77 21 88 27 91 39 C100 63 78 90 56 96 C32 103 16 85 24 65 Z"/></clipPath>
    <symbol id="mk" viewBox="0 0 100 104">
      <path d="M24 65 C27 50 45 36 65 27 C77 21 88 27 91 39 C100 63 78 90 56 96 C32 103 16 85 24 65 Z" fill="url(#gB)"/>
      <g clip-path="url(#cB)">
        <path d="M20 89 C37 72 62 66 67 28 C81 19 94 30 94 44 C88 66 64 69 54 87 C50 94 51 100 56 105 L20 105 Z" fill="url(#gO)"/>
        <path d="M97 43 C90 63 65 66 55 83 C48 95 54 104 69 102 L108 96 Z" fill="url(#gR)"/>
      </g>
      <path class="leaf" d="M34 35 C36 15 50 5 72 4 C67 19 54 29 34 35 Z" fill="url(#gL)"/>
    </symbol>
  </defs>
</svg>'''

NAV=[('index.html','Главная'),('prices.html','Цены'),('projects.html','Проекты'),('legal.html','Юридическая информация')]
TG='href="https://t.me/mango_moderation" data-tg'

def head(title,desc):
    return f'''<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0B2E22">
<link rel="icon" type="image/svg+xml" href="assets/mango.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800&family=Onest:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@phosphor-icons/web@2.1.1/src/regular/style.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@phosphor-icons/web@2.1.1/src/fill/style.css">
<link rel="stylesheet" href="styles.css?v=10">
</head>
<body>
<a class="skip" href="#main">Перейти к содержимому</a>
{DEFS}
'''

def header(cur):
    links='\n'.join(f'      <a href="{h}"'+(' aria-current="page"' if h==cur else '')+f'>{t}</a>' for h,t in NAV)
    return f'''<header class="head">
  <div class="wrap head-in">
    <a class="brand" href="index.html" aria-label="Манго, на главную">
      <svg width="36" height="38" viewBox="0 0 100 104" aria-hidden="true"><use href="#mk"/></svg>Манго
    </a>
    <nav class="nav" id="nav" aria-label="Основная навигация">
{links}
      <a class="btn btn-acc nav-cta" {TG} data-book>Записаться</a>
    </nav>
    <a class="btn btn-acc head-cta mag" {TG} data-book>Записаться</a>
    <button class="burger" id="burger" type="button" aria-label="Меню" aria-expanded="false" aria-controls="nav"><i class="ph ph-list" aria-hidden="true"></i></button>
  </div>
  <div class="prog" aria-hidden="true"></div>
</header>
'''

def final(title='Обсудим ваш проект?', text='Напишите нам в Telegram или WhatsApp. Ответим лично, без ботов и менеджеров. Первая консультация 30 минут, бесплатно.'):
    return f'''<section class="sec final">
  <svg class="final-mango a" viewBox="0 0 100 100" aria-hidden="true"><use href="#mk"/></svg>
  <svg class="final-mango b" viewBox="0 0 100 100" aria-hidden="true"><use href="#mk"/></svg>
  <div class="wrap">
    <h2 class="split">{title}</h2>
    <p data-reveal>{text}</p>
    <a class="btn btn-acc btn-lg mag" {TG} data-book data-reveal><i class="ph ph-telegram-logo" aria-hidden="true"></i>Записаться</a>
  </div>
</section>
'''

FOOT=f'''<footer class="foot">
  <div class="wrap">
    <div class="foot-in">
      <div>
        <a class="brand" href="index.html"><svg width="36" height="38" viewBox="0 0 100 104" aria-hidden="true"><use href="#mk"/></svg>Манго</a>
        <p style="margin-top:16px;max-width:340px">Веб-студия разработки. Сайты, приложения, AI-боты, дизайн и сопровождение. Москва, работаем со всей Россией.</p>
      </div>
      <div>
        <h3>Разделы</h3>
        <ul>
          <li><a href="index.html">Главная</a></li>
          <li><a href="prices.html">Цены</a></li>
          <li><a href="projects.html">Проекты</a></li>
          <li><a href="legal.html">Юридическая информация</a></li>
        </ul>
      </div>
      <div>
        <h3>Связаться</h3>
        <ul>
          <li><a {TG}>Telegram: <span data-tg-name>@mango_moderation</span></a></li>
          <li><a href="tel:+79151633540">+7 915 163 35 40</a></li>
          <li><a href="https://wa.me/79151633540" data-wa>WhatsApp</a></li>
          <li><a href="https://t.me/mango_studio_tech" target="_blank" rel="noopener">Telegram-канал студии</a></li>
          <li><a href="mailto:hello@mango.io">hello@mango.io</a></li>
        </ul>
      </div>
    </div>
    <div class="foot-big" aria-hidden="true" data-speed="-0.15">Манго</div>
    <div class="foot-bottom">
      <span>ИП Богданов Дмитрий Сергеевич. ИНН 230812090203 · ОГРНИП 325237500329507 · <a href="legal.html">Реквизиты</a></span>
      <span>Цены без НДС, ИП на УСН. Не является публичной офертой. © 2026 Манго</span>
    </div>
  </div>
</footer>

<dialog class="modal" id="book" aria-labelledby="bookTitle">
  <div class="modal-in">
    <button class="modal-x" type="button" aria-label="Закрыть"><i class="ph ph-x" aria-hidden="true"></i></button>
    <h2 id="bookTitle">Записаться на консультацию</h2>
    <p>Напишите нам лично, где вам удобнее. Отвечаем сами, в течение рабочего дня.</p>
    <div class="messengers">
      <a class="msg" {TG} target="_blank" rel="noopener">
        <span class="mi"><i class="ph-fill ph-telegram-logo" aria-hidden="true"></i></span>
        <span><b>Telegram</b><small data-tg-name>@mango_moderation</small></span>
        <i class="ph ph-arrow-right arr" aria-hidden="true"></i>
      </a>
      <a class="msg" href="https://wa.me/79151633540" data-wa target="_blank" rel="noopener">
        <span class="mi"><i class="ph-fill ph-whatsapp-logo" aria-hidden="true"></i></span>
        <span><b>WhatsApp</b><small>Откроется чат с готовым сообщением</small></span>
        <i class="ph ph-arrow-right arr" aria-hidden="true"></i>
      </a>
    </div>
    <p class="modal-foot">Позвонить: <a href="tel:+79151633540">+7 915 163 35 40</a></p>
    <p class="modal-foot">Удобнее почтой? <a href="mailto:hello@mango.io">hello@mango.io</a></p>
  </div>
</dialog>

<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.13/dist/lenis.min.js"></script>
<script src="app.js?v=8"></script>
</body>
</html>
'''

def page(fn,title,desc,body):
    open(os.path.join(OUT,fn),'w',encoding='utf-8').write(head(title,desc)+header(fn)+'<main id="main">\n'+body+'</main>\n'+FOOT)

ORBIT = 'сайты  приложения  AI-боты  дизайн  сопровождение  ' * 2
# ═════════ Главная ═════════
index_body=f'''<section class="hero">
  <div class="mesh" aria-hidden="true"><i></i><i></i><i></i></div>
  <div class="wrap hero-grid">
    <div>
      <h1 class="split">Сайты, приложения и AI-боты <em>под ключ</em></h1>
      <p class="lede">Студия из двух разработчиков. Делаем всё сами, от дизайна до сервера. Лендинг от 30 000 ₽.</p>
      <div class="hero-cta">
        <a class="btn btn-acc btn-lg mag" {TG} data-book><i class="ph ph-telegram-logo" aria-hidden="true"></i>Записаться</a>
        <a class="btn btn-ghost btn-lg" href="prices.html">Посмотреть цены</a>
      </div>
    </div>
    <div class="hero-art" aria-hidden="true">
      <svg class="orbit" viewBox="0 0 400 400">
        <defs><path id="orb" d="M200,200 m-178,0 a178,178 0 1,1 356,0 a178,178 0 1,1 -356,0"/></defs>
        <text><textPath href="#orb" textLength="1110">{ORBIT}</textPath></text>
      </svg>
      <div class="fruit">
        <svg viewBox="0 0 100 104">
      <path d="M24 65 C27 50 45 36 65 27 C77 21 88 27 91 39 C100 63 78 90 56 96 C32 103 16 85 24 65 Z" fill="url(#gB)"/>
      <g clip-path="url(#cB)">
        <path d="M20 89 C37 72 62 66 67 28 C81 19 94 30 94 44 C88 66 64 69 54 87 C50 94 51 100 56 105 L20 105 Z" fill="url(#gO)"/>
        <path d="M97 43 C90 63 65 66 55 83 C48 95 54 104 69 102 L108 96 Z" fill="url(#gR)"/>
      </g>
      <path class="leaf" d="M34 35 C36 15 50 5 72 4 C67 19 54 29 34 35 Z" fill="url(#gL)"/>
        </svg>
      </div>
    </div>
  </div>
</section>

<div class="marquee" aria-hidden="true">
  <div class="marquee-track">
''' + ''.join('''    <div class="marquee-set">
      <span>Сайты</span><svg viewBox="0 0 100 100"><use href="#mk"/></svg>
      <span>Telegram-боты</span><svg viewBox="0 0 100 100"><use href="#mk"/></svg>
      <span>AI-ассистенты</span><svg viewBox="0 0 100 100"><use href="#mk"/></svg>
      <span>Мобильные приложения</span><svg viewBox="0 0 100 100"><use href="#mk"/></svg>
      <span>Интернет-магазины</span><svg viewBox="0 0 100 100"><use href="#mk"/></svg>
      <span>Брендинг</span><svg viewBox="0 0 100 100"><use href="#mk"/></svg>
      <span>Интеграции</span><svg viewBox="0 0 100 100"><use href="#mk"/></svg>
      <span>Серверы</span><svg viewBox="0 0 100 100"><use href="#mk"/></svg>
    </div>
''' for _ in range(2)) + f'''  </div>
</div>

<section class="sec">
  <div class="wrap">
    <h2 class="split sec-title">Всё, что нужно бизнесу в интернете</h2>
    <p class="sec-sub" data-reveal>Один подрядчик на весь проект. Не придётся искать отдельно дизайнера, программиста и админа.</p>
    <div class="bento" data-stagger>
      <a class="tile t-big" href="prices.html#sites">
        <i class="ph ph-browser ic" aria-hidden="true"></i>
        <h3>Сайты</h3>
        <p>Лендинги, промо и корпоративные сайты, интернет-магазины. Быстрые, удобные с телефона и готовые к рекламе.</p>
        <div class="big-price"><small>Лендинг</small>от 30 000 ₽</div>
      </a>
      <a class="tile t-2 t-dots" href="prices.html#bots">
        <i class="ph ph-robot ic" aria-hidden="true"></i>
        <h3>AI и боты</h3>
        <p>Боты для Telegram, MAX и WhatsApp. AI-ассистенты по вашей базе знаний.</p>
        <span class="from">от 52 000 ₽<i class="ph ph-arrow-right" aria-hidden="true"></i></span>
      </a>
      <a class="tile t-2" href="prices.html#apps">
        <i class="ph ph-device-mobile ic" aria-hidden="true"></i>
        <h3>Приложения</h3>
        <p>Веб и мобильные приложения, личные кабинеты, интеграции с 1С и CRM.</p>
        <span class="from">от 88 000 ₽<i class="ph ph-arrow-right" aria-hidden="true"></i></span>
      </a>
      <a class="tile t-2 t-ripen" href="prices.html#design">
        <i class="ph ph-pen-nib ic" aria-hidden="true"></i>
        <h3>Дизайн и брендинг</h3>
        <p>Логотип, фирменный стиль, интерфейсы, презентации.</p>
        <span class="from">от 52 000 ₽<i class="ph ph-arrow-right" aria-hidden="true"></i></span>
      </a>
      <a class="tile t-2" href="prices.html#infra">
        <i class="ph ph-hard-drives ic" aria-hidden="true"></i>
        <h3>Инфраструктура и SEO</h3>
        <p>Серверы, деплой, бэкапы, аналитика и продвижение в поиске.</p>
        <span class="from">от 40 000 ₽<i class="ph ph-arrow-right" aria-hidden="true"></i></span>
      </a>
      <a class="tile t-2 t-dots" href="prices.html#support">
        <i class="ph ph-lifebuoy ic" aria-hidden="true"></i>
        <h3>Сопровождение</h3>
        <p>Следим, чтобы сайт работал, и развиваем его по часам.</p>
        <span class="from">от 9 600 ₽/мес<i class="ph ph-arrow-right" aria-hidden="true"></i></span>
      </a>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="facts-row" data-stagger>
      <div class="fact"><b><span data-count="30000">30 000</span><small>₽</small></b><span>стоимость лендинга, от</span></div>
      <div class="fact"><b><span data-count="30">30</span><small>мин</small></b><span>бесплатная консультация перед стартом</span></div>
      <div class="fact"><b><span data-count="14">14</span><small>дней</small></b><span>исправляем любые ошибки после сдачи</span></div>
      <div class="fact"><b><span data-count="6">6</span><small>мес</small></b><span>гарантия на критичные ошибки в коде</span></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap pin-split">
    <div class="split-pin">
      <div class="chips"><span class="chip chip-acc">В разработке</span><span class="chip">Онлайн-образование</span></div>
      <h2 class="split" style="margin-top:24px">ПлатОН</h2>
      <p class="lede">Платформа для репетиторов. Уроки, домашние задания, тесты и чат в одном месте вместо пяти сервисов.</p>
      <a class="btn btn-ghost" href="projects.html">Подробнее о проекте<i class="ph ph-arrow-up-right" aria-hidden="true"></i></a>
    </div>
    <div class="feat-list" data-stagger>
      <div class="feat"><i class="ph ph-video-camera" aria-hidden="true"></i><div><h3>Видеоуроки с общей доской</h3><p>Преподаватель и ученик рисуют на одной доске прямо во время занятия.</p></div></div>
      <div class="feat"><i class="ph ph-exam" aria-hidden="true"></i><div><h3>Задания и тесты</h3><p>Выдача, сдача и автопроверка тестов с подсчётом баллов.</p></div></div>
      <div class="feat"><i class="ph ph-chats-circle" aria-hidden="true"></i><div><h3>Чат в реальном времени</h3><p>История переписки и статусы прочтения.</p></div></div>
      <div class="feat"><i class="ph ph-seal-check" aria-hidden="true"></i><div><h3>Проверка по ИНН</h3><p>Самозанятость преподавателя подтверждается через ФНС автоматически.</p></div></div>
      <div class="feat"><i class="ph ph-device-mobile" aria-hidden="true"></i><div><h3>Веб и мобильное приложение</h3><p>Одна система для браузера, iOS и Android.</p></div></div>
      <div class="feat"><i class="ph ph-bell-ringing" aria-hidden="true"></i><div><h3>Telegram-бот</h3><p>Напоминает о занятиях и домашних заданиях.</p></div></div>
    </div>
  </div>
</section>

<section class="sec" style="padding-top:0">
  <div class="wrap">
    <h2 class="split sec-title">Как начинаем работу</h2>
    <div class="stack">
      <article class="stack-card"><div><i class="ph ph-chat-circle-text" aria-hidden="true"></i><h3>Вы пишете нам</h3></div><p>В Telegram или WhatsApp, своими словами. Отвечаем в течение рабочего дня.</p></article>
      <article class="stack-card"><div><i class="ph ph-video-camera" aria-hidden="true"></i><h3>Созвон 30 минут</h3></div><p>Бесплатно. Разбираемся в задаче и честно говорим, подходим ли друг другу.</p></article>
      <article class="stack-card"><div><i class="ph ph-receipt" aria-hidden="true"></i><h3>Цена и сроки</h3></div><p>Присылаем вилку за два рабочих дня. Для крупных задач делаем точную смету.</p></article>
      <article class="stack-card"><div><i class="ph ph-rocket-launch" aria-hidden="true"></i><h3>Работа</h3></div><p>Договор и предоплата 30 % или по договорённости. Показываем результат каждую неделю, а не в самом конце.</p></article>
    </div>
  </div>
</section>
''' + final()
page('index.html','Манго: сайты, приложения и AI-боты под ключ',
     'Веб-студия Манго: сайты от 30 000 ₽, веб и мобильные приложения, AI-ассистенты и боты, дизайн и сопровождение. Бесплатная консультация в Telegram или WhatsApp.',
     index_body)

# ═════════ Цены ═════════
GROUPS=[
 ('sites','Сайты',[('Лендинг','30 000 ₽'),('Промо-сайт','190 000 ₽'),('Корпоративный сайт','340 000 ₽'),('Интернет-магазин','550 000 ₽'),('Редизайн сайта','140 000 ₽')]),
 ('apps','Приложения',[('MVP веб-приложения','500 000 ₽'),('Личный кабинет к сайту','290 000 ₽'),('Мобильное приложение iOS и Android','840 000 ₽'),('Telegram Mini App','270 000 ₽'),('Интеграция с 1С или CRM','88 000 ₽')]),
 ('bots','AI и боты',[('Сценарный бот','52 000 ₽'),('Бот с интеграциями','140 000 ₽'),('Бот-магазин или бот-запись','190 000 ₽'),('AI-ассистент по вашей базе знаний','290 000 ₽'),('AI-поддержка первой линии','420 000 ₽')]),
 ('design','Дизайн и брендинг',[('Логотип и айдентика','88 000 ₽'),('Брендбук','180 000 ₽'),('UI-дизайн сайта','140 000 ₽'),('Дизайн мобильного приложения','220 000 ₽'),('Презентация или питч-дек','52 000 ₽')]),
 ('infra','Инфраструктура и SEO',[('Настройка деплоя и CI/CD','44 000 ₽'),('Серверная инфраструктура','68 000 ₽'),('Технический SEO-аудит','44 000 ₽'),('Настройка аналитики','40 000 ₽'),('SEO-сопровождение','52 000 ₽/мес')]),
 ('support','Сопровождение',[('Сопровождение сайта','9 600 ₽/мес'),('Пакет часов на развитие','32 000 ₽/мес'),('Перенос сайта на другой хостинг','20 000 ₽'),('Восстановление после сбоя','36 000 ₽'),('Разовые правки','2 800 ₽/час')]),
]
spy='\n'.join(f'        <a href="#{i}">{t}</a>' for i,t,_ in GROUPS)
groups='\n'.join(f'''        <div class="pgroup" id="{i}">
          <div class="pgroup-head"><h2>{t}</h2><span>{len(rows)} услуг</span></div>
'''+'\n'.join(f'          <div class="prow"><span>{n}</span><b>от {p}</b></div>' for n,p in rows)+'\n        </div>' for i,t,rows in GROUPS)
prices_body=f'''<section class="page-hero">
  <div class="mesh" aria-hidden="true"><i></i><i></i><i></i></div>
  <div class="wrap">
    <h1 class="split">Цены</h1>
    <p class="lede" data-reveal>Ориентиры по основным услугам. Точную стоимость назовём после короткого бесплатного созвона.</p>
    <div class="ripen"></div>
  </div>
</section>

<section style="padding-bottom:clamp(40px,6vw,80px)">
  <div class="wrap">
    <div class="price-feature" data-stagger>
      <div class="pf pf-main"><span>Самый частый запрос</span><b><small>Лендинг</small>от 30 000 ₽</b></div>
      <div class="pf"><span class="muted">Для продаж онлайн</span><b><small>Интернет-магазин</small>от 550 000 ₽</b></div>
      <div class="pf"><span class="muted">Для заявок и записи</span><b><small>Бот для бизнеса</small>от 52 000 ₽</b></div>
    </div>
    <div class="price-layout">
      <nav class="spy" aria-label="Разделы цен">
{spy}
      </nav>
      <div class="pgroups">
{groups}
      </div>
    </div>
    <div class="terms" data-stagger>
      <div><i class="ph ph-currency-rub" aria-hidden="true"></i><b>Цены указаны «от»</b><p>Итог зависит от объёма и сроков. Вилку присылаем за два рабочих дня после созвона.</p></div>
      <div><i class="ph ph-handshake" aria-hidden="true"></i><b>Предоплата 30 %</b><p>Или по договорённости. Остаток по этапам. Работаем по договору, закрываем актами.</p></div>
      <div><i class="ph ph-file-text" aria-hidden="true"></i><b>Без НДС</b><p>ИП на УСН. Цены на сайте не являются публичной офертой.</p></div>
    </div>
  </div>
</section>
''' + final('Не нашли свою задачу?','Опишите её в Telegram или WhatsApp. Посчитаем стоимость и сроки бесплатно.')
page('prices.html','Цены | Манго',
     'Цены веб-студии Манго: лендинг от 30 000 ₽, интернет-магазин от 550 000 ₽, бот от 52 000 ₽, мобильное приложение от 840 000 ₽.',
     prices_body)

# ═════════ Проекты ═════════
HC=[('ph-fingerprint','Вход и роли','Вход по одноразовому коду. Ученик и преподаватель видят каждый своё.'),
    ('ph-seal-check','Проверка по ИНН','Самозанятость преподавателя подтверждается через API ФНС без ручной модерации.'),
    ('ph-calendar-check','Курсы и расписание','Уроки, посещаемость и дневник для ученика и родителя.'),
    ('ph-video-camera','Видеоурок с доской','Занятие в прямом эфире и общая доска, на которой рисуют оба.'),
    ('ph-exam','Задания и тесты','Выдача, сдача и автопроверка с подсчётом баллов.'),
    ('ph-chats-circle','Чат','Сообщения в реальном времени, история и статусы прочтения.'),
    ('ph-scan','Распознавание документов','Работает внутри своего контура: персональные данные не уходят в чужие сервисы.'),
    ('ph-bell-ringing','Telegram-бот','Напоминания о занятиях и домашних заданиях.')]
hcards='\n'.join(f'      <article class="hcard"><i class="ph {ic}" aria-hidden="true"></i><h3>{t}</h3><p>{d}</p></article>' for ic,t,d in HC)
def chips(items): return ''.join(f'<span class="chip">{x}</span>' for x in items)
projects_body=f'''<section class="page-hero">
  <div class="mesh" aria-hidden="true"><i></i><i></i><i></i></div>
  <div class="wrap">
    <h1 class="split">Проекты</h1>
    <p class="lede" data-reveal>Показываем то, что сделали сами, с реальным стеком и без приукрашенных цифр.</p>
    <div class="ripen"></div>
  </div>
</section>

<section class="sec" style="padding-top:clamp(32px,4vw,56px);padding-bottom:0">
  <div class="wrap">
    <div class="case-hero">
      <h2 class="split">ПлатОН</h2>
      <div class="chips" data-reveal><span class="chip chip-acc">В активной разработке</span><span class="chip">SaaS</span><span class="chip">Онлайн-образование</span></div>
    </div>
    <div class="case-intro">
      <p class="lede" data-reveal>Российская платформа для репетиторов. Занятия в прямом эфире, домашние задания, тесты, чат и дневник ученика в одном месте вместо пяти разных сервисов.</p>
      <dl class="kv" data-stagger>
        <div><dt>Роль</dt><dd>Продукт целиком</dd></div>
        <div><dt>Платформы</dt><dd>Веб, iOS, Android, Telegram</dd></div>
        <div><dt>Что делали</dt><dd>Дизайн, фронтенд, бэкенд, инфраструктура</dd></div>
        <div><dt>Стадия</dt><dd>В разработке</dd></div>
      </dl>
    </div>
  </div>
  <!-- TODO: сюда стоит добавить реальные скриншоты ПлатОН (1600x1000), когда их можно будет показывать -->
  <div class="hpan">
    <div class="hpan-track">
      <div class="hpan-intro"><h3>Что построили</h3><p>Восемь частей, которые работают как одна система.</p></div>
{hcards}
    </div>
  </div>
  <div class="wrap">
    <div class="stack-groups" data-stagger>
      <div class="sg"><h3>Клиент</h3><div class="chips">{chips(['Next.js 15','React 19','Tailwind 4','React Native','LiveKit','Excalidraw','Yjs'])}</div></div>
      <div class="sg"><h3>Сервер</h3><div class="chips">{chips(['Go 1.25','Fiber v3','WebSocket','PostgreSQL 16','Redis','S3 (MinIO)','Python 3.12','FastAPI'])}</div></div>
      <div class="sg"><h3>Инфраструктура</h3><div class="chips">{chips(['Docker','Kubernetes','nginx','GitHub Actions','API ФНС','ЮKassa','Web Push'])}</div></div>
    </div>
    <p class="note" data-reveal>Цифры по нагрузке и выручке опубликуем после запуска. Писать их сейчас было бы выдумкой.</p>
  </div>
</section>

''' + final('Ваш проект может быть следующим','Расскажите о задаче в Telegram или WhatsApp. Первая консультация 30 минут, бесплатно.')
page('projects.html','Проекты | Манго',
     'Проекты веб-студии Манго: платформа для репетиторов ПлатОН. Веб, мобильное приложение, сервер и Telegram-бот.',
     projects_body)

# ═════════ Юридическая информация ═════════
CK='<i class="ph ph-check-circle" aria-hidden="true"></i>'
legal_body=f'''<section class="page-hero">
  <div class="mesh" aria-hidden="true"><i></i><i></i><i></i></div>
  <div class="wrap">
    <h1 class="split">Юридическая информация</h1>
    <p class="lede" data-reveal>Реквизиты, условия работы и то, как мы обращаемся с вашими данными.</p>
    <div class="ripen"></div>
  </div>
</section>
<section style="padding-bottom:clamp(40px,6vw,80px)">
  <div class="wrap legal-layout">
    <nav class="spy" aria-label="Разделы страницы">
      <a href="#requisites">Реквизиты</a>
      <a href="#terms">Условия работы</a>
      <a href="#offer">Цены и оферта</a>
      <a href="#privacy">Персональные данные</a>
    </nav>
    <div class="doc" data-stagger>
      <section id="requisites">
        <h2>Реквизиты</h2>
        <dl class="req">
          <div><dt>Исполнитель</dt><dd>ИП Богданов Дмитрий Сергеевич</dd></div>
          <div><dt>Система налогообложения</dt><dd>УСН, НДС не облагается</dd></div>
          <div><dt>ИНН</dt><dd>230812090203</dd></div>
          <div><dt>ОГРНИП</dt><dd>325237500329507</dd></div>
          <div><dt>Дата регистрации ИП</dt><dd>30.07.2025</dd></div>
          <div><dt>Расчётный счёт</dt><dd>40802810100009555734</dd></div>
          <div><dt>Банк</dt><dd>АО «ТБанк»</dd></div>
          <div><dt>БИК</dt><dd>044525974</dd></div>
          <div><dt>Корреспондентский счёт</dt><dd>30101810145250000974</dd></div>
          <div><dt>Адрес регистрации</dt><dd>350087, г. Краснодар, СНТ «Хуторок-Южный», ул. Дружная, д. 38</dd></div>
          <div><dt>Адрес для корреспонденции</dt><dd>350042, г. Краснодар, ул. Ипподромная, д. 53/1, кв. 3</dd></div>
          <div><dt>Почта для юридической переписки</dt><dd><a href="mailto:gffvfcbh@gmail.com">gffvfcbh@gmail.com</a></dd></div>
          <div><dt>Телефон ИП</dt><dd><a href="tel:+79182436263">+7 918 243 62 63</a></dd></div>
        </dl>
      </section>
      <section id="terms">
        <h2>Условия работы</h2>
        <ul>
          <li>{CK}<b>Договор.</b> Работаем только по договору. Выполненные этапы закрываем актами.</li>
          <li>{CK}<b>Оплата.</b> Стоимость, порядок и сроки оплаты согласуем в договоре. Оплата на расчётный счёт ИП.</li>
          <li>{CK}<b>Сроки.</b> Сроки определяются договором и техническим заданием. Задержка материалов, доступов или согласований сдвигает срок выполнения работ.</li>
          <li>{CK}<b>Правки.</b> Учитываем замечания в пределах согласованного технического задания. Существенные изменения объёма работ оформляем дополнительным соглашением.</li>
          <li>{CK}<b>Права.</b> Исключительные права на созданные по договору результаты переходят заказчику после полной оплаты и подписания акта приёма-передачи. Состав передаваемых материалов и доступов фиксируем в договоре.</li>
          <li>{CK}<b>Гарантия.</b> Срок и объём гарантийной поддержки определяются договором. Исправляем недостатки, допущенные по нашей вине. Дальнейшее сопровождение и развитие согласуем отдельно.</li>
          <li>{CK}<b>Конфиденциальность.</b> По запросу подписываем соглашение о неразглашении (NDA).</li>
        </ul>
      </section>
      <section id="offer">
        <h2>Цены и оферта</h2>
        <p>Цены на сайте указаны в рублях, без НДС, и носят справочный характер. Итоговая стоимость определяется договором после согласования объёма работ.</p>
        <p>Информация на сайте не является публичной офертой в смысле статьи 437 Гражданского кодекса РФ.</p>
      </section>
      <section id="privacy">
        <h2>Персональные данные</h2>
        <p>На сайте нет форм: мы не собираем и не храним данные посетителей через сайт. Связь идёт напрямую в Telegram, WhatsApp или по почте.</p>
        <p>Если вы пишете нам, мы получаем только то, что вы сами отправили: имя, контакт и описание задачи. Используем эти данные, чтобы ответить и подготовить предложение, и не передаём третьим лицам, кроме случаев, предусмотренных законом. Обработка ведётся в соответствии с Федеральным законом № 152-ФЗ «О персональных данных».</p>
        <p>Сайт не устанавливает собственных cookie. Шрифты, иконки и библиотеки анимации загружаются со сторонних серверов (Google Fonts, jsDelivr, cdnjs), которые получают технические данные запроса, например IP-адрес.</p>
        <p>Чтобы узнать, какие ваши данные у нас есть, или попросить их удалить, напишите на <a href="mailto:gffvfcbh@gmail.com">gffvfcbh@gmail.com</a>.</p>
      </section>
    </div>
  </div>
</section>
'''
page('legal.html','Юридическая информация | Манго',
     'Реквизиты ИП Богданов Дмитрий Сергеевич, условия работы веб-студии Манго и обработка персональных данных.',
     legal_body)
print('ok')
