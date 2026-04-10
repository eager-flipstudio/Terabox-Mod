from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TeraBox MOD — Unlimited Cloud Storage</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap" rel="stylesheet">
<style>
  :root {
    --bg:#050813;--surface:#0d1225;--card:#111828;
    --accent:#3b8cf8;--accent2:#7c3aed;--gold:#f59e0b;
    --neon:#00f5d4;--text:#f0f4ff;--muted:#8896b3;
    --border:rgba(59,140,248,0.18);--radius:18px;
  }
  *{margin:0;padding:0;box-sizing:border-box;}
  html{scroll-behavior:smooth;}
  body{font-family:'DM Sans',sans-serif;background:var(--bg);color:var(--text);min-height:100vh;overflow-x:hidden;}
  body::before{content:'';position:fixed;inset:0;background:radial-gradient(ellipse 80% 60% at 20% 10%,rgba(59,140,248,.13) 0%,transparent 60%),radial-gradient(ellipse 60% 50% at 80% 80%,rgba(124,58,237,.13) 0%,transparent 60%),radial-gradient(ellipse 40% 40% at 50% 50%,rgba(0,245,212,.07) 0%,transparent 60%);pointer-events:none;z-index:0;}

  .particles{position:fixed;inset:0;pointer-events:none;z-index:0;overflow:hidden;}
  .particle{position:absolute;border-radius:50%;animation:floatUp linear infinite;}
  @keyframes floatUp{0%{transform:translateY(100vh) rotate(0deg);opacity:0;}10%{opacity:.2;}90%{opacity:.2;}100%{transform:translateY(-100px) rotate(720deg);opacity:0;}}

  nav{position:fixed;top:0;left:0;right:0;z-index:100;display:flex;align-items:center;justify-content:space-between;padding:16px 36px;background:rgba(5,8,19,.8);backdrop-filter:blur(24px);border-bottom:1px solid var(--border);}
  .logo{font-family:'Syne',sans-serif;font-weight:800;font-size:1.35rem;background:linear-gradient(135deg,var(--accent),var(--neon));-webkit-background-clip:text;-webkit-text-fill-color:transparent;display:flex;align-items:center;gap:10px;}
  .logo-icon{width:32px;height:32px;border-radius:9px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;font-size:15px;-webkit-text-fill-color:white;flex-shrink:0;}
  .nav-right{display:flex;align-items:center;gap:14px;}
  .nav-badge{background:linear-gradient(135deg,var(--gold),#ef4444);color:#fff;font-size:.62rem;font-weight:700;padding:4px 12px;border-radius:20px;letter-spacing:.5px;-webkit-text-fill-color:white;animation:pulseBadge 2s infinite;}
  @keyframes pulseBadge{0%,100%{box-shadow:0 0 0 0 rgba(245,158,11,.5);}50%{box-shadow:0 0 0 8px rgba(245,158,11,0);}}
  .nav-dl{display:inline-flex;align-items:center;gap:8px;background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;font-family:'Syne',sans-serif;font-weight:700;font-size:.82rem;padding:10px 22px;border-radius:40px;text-decoration:none;box-shadow:0 4px 20px rgba(59,140,248,.35);transition:all .3s;-webkit-text-fill-color:white;}
  .nav-dl:hover{transform:translateY(-2px);box-shadow:0 8px 30px rgba(59,140,248,.5);}

  /* HERO */
  .hero{position:relative;z-index:1;min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:130px 20px 80px;}
  .hero-ring{position:absolute;border-radius:50%;border:1px solid rgba(59,140,248,.1);pointer-events:none;top:50%;left:50%;animation:spinRing linear infinite;}
  .hero-ring:nth-child(1){width:600px;height:600px;margin-top:-300px;margin-left:-300px;animation-duration:40s;}
  .hero-ring:nth-child(2){width:850px;height:850px;margin-top:-425px;margin-left:-425px;border-color:rgba(124,58,237,.07);animation-duration:60s;animation-direction:reverse;}
  .hero-ring:nth-child(3){width:1100px;height:1100px;margin-top:-550px;margin-left:-550px;border-color:rgba(0,245,212,.05);animation-duration:80s;}
  @keyframes spinRing{from{transform:rotate(0deg);}to{transform:rotate(360deg);}}

  .hero-pill{display:inline-flex;align-items:center;gap:8px;background:rgba(59,140,248,.1);border:1px solid rgba(59,140,248,.3);border-radius:30px;padding:8px 22px;font-size:.72rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--accent);margin-bottom:32px;animation:fadeUp .7s ease both;}
  .pill-dot{width:7px;height:7px;background:var(--neon);border-radius:50%;animation:blink 1.4s infinite;}
  @keyframes blink{0%,100%{opacity:1;}50%{opacity:0;}}
  @keyframes fadeUp{from{opacity:0;transform:translateY(28px);}to{opacity:1;transform:translateY(0);}}

  h1{font-family:'Syne',sans-serif;font-weight:800;font-size:clamp(2.8rem,7.5vw,6rem);line-height:1.06;letter-spacing:-2.5px;margin-bottom:8px;animation:fadeUp .8s .1s ease both;}
  .h1-white{display:block;color:var(--text);}
  .h1-grad{display:block;background:linear-gradient(135deg,var(--accent) 0%,var(--neon) 45%,var(--accent2) 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-size:200%;animation:shimmer 4s linear infinite,fadeUp .8s .15s ease both;}
  @keyframes shimmer{0%{background-position:0%}100%{background-position:200%}}

  .hero-tagline{font-size:1rem;color:var(--muted);margin:18px 0 44px;max-width:520px;line-height:1.7;animation:fadeUp .8s .25s ease both;}
  .hero-tagline strong{color:var(--text);}

  .stats{display:flex;gap:40px;margin-bottom:52px;flex-wrap:wrap;justify-content:center;animation:fadeUp .8s .35s ease both;}
  .stat-item{text-align:center;}
  .stat-num{font-family:'Syne',sans-serif;font-weight:800;font-size:1.9rem;background:linear-gradient(135deg,var(--accent),var(--neon));-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
  .stat-lbl{font-size:.7rem;color:var(--muted);text-transform:uppercase;letter-spacing:1.2px;margin-top:2px;}
  .stat-div{width:1px;background:var(--border);align-self:stretch;}

  .mockup-wrap{position:relative;margin-bottom:60px;animation:fadeUp .8s .3s ease both;}
  .mockup-halo{position:absolute;inset:-40px;background:radial-gradient(ellipse at center,rgba(59,140,248,.22),transparent 65%);pointer-events:none;}
  .mockup-img{width:min(360px,78vw);border-radius:28px;display:block;border:2px solid rgba(59,140,248,.35);box-shadow:0 40px 100px rgba(0,0,0,.55),0 0 80px rgba(59,140,248,.12);}
  .mockup-chip{position:absolute;top:-16px;right:-10px;background:linear-gradient(135deg,var(--gold),#f97316);color:#fff;font-family:'Syne',sans-serif;font-weight:700;font-size:.68rem;padding:8px 16px;border-radius:12px;box-shadow:0 6px 24px rgba(245,158,11,.45);transform:rotate(4deg);-webkit-text-fill-color:white;animation:chipFloat 3s ease-in-out infinite;}
  @keyframes chipFloat{0%,100%{transform:rotate(4deg) translateY(0);}50%{transform:rotate(4deg) translateY(-5px);}}

  /* ★★★ MEGA DOWNLOAD BUTTON ★★★ */
  .dl-section{animation:fadeUp .8s .45s ease both;width:100%;max-width:540px;}

  .dl-card{position:relative;background:linear-gradient(135deg,rgba(59,140,248,.09),rgba(124,58,237,.09));border:1px solid rgba(59,140,248,.28);border-radius:26px;padding:36px 36px 28px;overflow:hidden;margin-bottom:16px;}
  .dl-card::before{content:'';position:absolute;top:-80px;left:50%;transform:translateX(-50%);width:400px;height:200px;background:radial-gradient(ellipse,rgba(59,140,248,.18),transparent 70%);pointer-events:none;}
  .dl-top-label{font-size:.65rem;font-weight:700;letter-spacing:2.5px;text-transform:uppercase;color:var(--neon);margin-bottom:8px;display:flex;align-items:center;justify-content:center;gap:10px;}
  .dl-top-label span{display:inline-block;width:28px;height:1px;background:var(--neon);opacity:.35;}
  .dl-card-title{font-family:'Syne',sans-serif;font-weight:800;font-size:1.5rem;letter-spacing:-.5px;margin-bottom:4px;}
  .dl-card-desc{color:var(--muted);font-size:.82rem;margin-bottom:26px;}

  .btn-mega{
    position:relative;display:flex;align-items:center;gap:14px;width:100%;
    background:linear-gradient(135deg,#1565e0,var(--accent),var(--accent2),#1565e0);
    background-size:300%;
    color:#fff;font-family:'Syne',sans-serif;font-weight:800;font-size:1.1rem;
    padding:20px 24px;border-radius:16px;
    text-decoration:none;cursor:pointer;
    box-shadow:0 10px 40px rgba(59,140,248,.45),0 0 0 0 rgba(59,140,248,.3);
    transition:transform .25s ease,box-shadow .25s ease;
    animation:btnGlow 3s 2s infinite,btnColorShift 5s linear infinite;
    overflow:hidden;-webkit-text-fill-color:white;
  }
  @keyframes btnGlow{0%,100%{box-shadow:0 10px 40px rgba(59,140,248,.45),0 0 0 0 rgba(59,140,248,.25);}50%{box-shadow:0 10px 40px rgba(59,140,248,.45),0 0 0 16px rgba(59,140,248,0);}}
  @keyframes btnColorShift{0%{background-position:0%}100%{background-position:300%}}
  .btn-mega::after{content:'';position:absolute;top:0;left:-120%;width:65%;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,.25),transparent);animation:sweep 2.8s 1s infinite;}
  @keyframes sweep{0%{left:-120%;}55%,100%{left:130%;}}
  .btn-mega:hover{transform:translateY(-4px) scale(1.015);box-shadow:0 20px 60px rgba(59,140,248,.6),0 0 0 10px rgba(59,140,248,.1);}
  .btn-mega:active{transform:translateY(-1px) scale(.99);}

  .btn-icon-wrap{width:52px;height:52px;border-radius:14px;background:rgba(255,255,255,.18);display:flex;align-items:center;justify-content:center;font-size:1.6rem;flex-shrink:0;animation:iconBounce 2s ease-in-out infinite;}
  @keyframes iconBounce{0%,100%{transform:translateY(0);}50%{transform:translateY(-5px);}}
  .btn-text-wrap{flex:1;text-align:left;}
  .btn-main-txt{display:block;font-size:1.05rem;font-weight:800;letter-spacing:.1px;}
  .btn-sub-txt{display:block;font-size:.68rem;font-weight:400;opacity:.8;margin-top:3px;}
  .btn-arrow-ico{font-size:1.4rem;flex-shrink:0;animation:arrowBounce 1.6s ease-in-out infinite;}
  @keyframes arrowBounce{0%,100%{transform:translateX(0);}50%{transform:translateX(6px);}}

  /* Progress */
  .dl-progress{margin-top:18px;background:rgba(59,140,248,.1);border-radius:6px;overflow:hidden;height:5px;}
  .dl-bar{height:100%;width:0%;background:linear-gradient(90deg,var(--accent),var(--neon));border-radius:6px;transition:width .35s ease;}
  .dl-status-row{display:flex;justify-content:space-between;margin-top:8px;font-size:.7rem;color:var(--muted);}
  .dl-status-left{display:flex;align-items:center;gap:6px;}
  .status-dot{width:6px;height:6px;border-radius:50%;background:var(--neon);display:inline-block;animation:blink 1.4s infinite;}
  .dl-count{color:var(--accent);font-weight:600;}

  /* Badges */
  .dl-badges{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-top:4px;}
  .dl-badge{display:flex;align-items:center;gap:5px;background:var(--card);border:1px solid var(--border);border-radius:30px;padding:6px 14px;font-size:.72rem;color:var(--muted);transition:all .3s;}
  .dl-badge:hover{border-color:rgba(59,140,248,.35);color:var(--text);}

  .trust-row{display:flex;gap:18px;margin-top:24px;flex-wrap:wrap;justify-content:center;animation:fadeUp .8s .55s ease both;}
  .trust-item{display:flex;align-items:center;gap:7px;font-size:.74rem;color:var(--muted);}
  .trust-icon{color:var(--neon);}

  /* SECTIONS */
  section{position:relative;z-index:1;padding:90px 20px;}
  .container{max-width:1100px;margin:0 auto;}
  .sec-label{font-size:.7rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--accent);margin-bottom:14px;display:block;}
  .sec-title{font-family:'Syne',sans-serif;font-weight:800;font-size:clamp(1.8rem,4vw,2.8rem);letter-spacing:-1px;margin-bottom:14px;}
  .sec-desc{color:var(--muted);font-size:.95rem;line-height:1.7;max-width:520px;}

  .feat-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px;margin-top:52px;}
  .feat-card{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:28px;transition:all .3s;position:relative;overflow:hidden;}
  .feat-card::before{content:'';position:absolute;inset:0;background:linear-gradient(135deg,rgba(59,140,248,.05),transparent);opacity:0;transition:.3s;}
  .feat-card:hover{transform:translateY(-5px);border-color:rgba(59,140,248,.4);box-shadow:0 20px 50px rgba(0,0,0,.3);}
  .feat-card:hover::before{opacity:1;}
  .feat-ico{width:48px;height:48px;border-radius:13px;display:flex;align-items:center;justify-content:center;font-size:1.35rem;margin-bottom:16px;}
  .ico-b{background:rgba(59,140,248,.12);border:1px solid rgba(59,140,248,.2);}
  .ico-p{background:rgba(124,58,237,.12);border:1px solid rgba(124,58,237,.2);}
  .ico-g{background:rgba(245,158,11,.12);border:1px solid rgba(245,158,11,.2);}
  .ico-n{background:rgba(0,245,212,.1);border:1px solid rgba(0,245,212,.2);}
  .ico-r{background:rgba(239,68,68,.1);border:1px solid rgba(239,68,68,.2);}
  .ico-gr{background:rgba(34,197,94,.1);border:1px solid rgba(34,197,94,.2);}
  .feat-card h3{font-family:'Syne',sans-serif;font-weight:700;font-size:.98rem;margin-bottom:8px;}
  .feat-card p{color:var(--muted);font-size:.83rem;line-height:1.6;}
  .feat-tag{display:inline-block;font-size:.6rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;padding:3px 10px;border-radius:20px;margin-top:12px;}
  .tag-mod{background:rgba(0,245,212,.12);color:var(--neon);border:1px solid rgba(0,245,212,.2);}
  .tag-free{background:rgba(34,197,94,.12);color:#22c55e;border:1px solid rgba(34,197,94,.2);}
  .tag-pro{background:rgba(59,140,248,.12);color:var(--accent);border:1px solid rgba(59,140,248,.2);}

  .gal-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:52px;}
  .gal-card{border-radius:var(--radius);overflow:hidden;border:1px solid var(--border);position:relative;transition:all .3s;}
  .gal-card:hover{transform:scale(1.03);border-color:rgba(59,140,248,.4);box-shadow:0 20px 50px rgba(0,0,0,.4);}
  .gal-card img{width:100%;height:220px;object-fit:cover;display:block;}
  .gal-lbl{position:absolute;bottom:0;left:0;right:0;background:linear-gradient(0deg,rgba(5,8,19,.95),transparent);padding:20px 14px 12px;font-family:'Syne',sans-serif;font-weight:700;font-size:.8rem;}

  .steps-row{display:flex;margin-top:52px;position:relative;}
  .steps-row::before{content:'';position:absolute;top:27px;left:10%;right:10%;height:2px;background:linear-gradient(90deg,var(--accent),var(--accent2));opacity:.22;}
  .step-item{flex:1;text-align:center;padding:0 14px;position:relative;}
  .step-num{width:54px;height:54px;background:linear-gradient(135deg,var(--accent),var(--accent2));border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:'Syne',sans-serif;font-weight:800;font-size:1.1rem;margin:0 auto 16px;box-shadow:0 0 0 6px rgba(59,140,248,.12);position:relative;z-index:1;}
  .step-item h4{font-family:'Syne',sans-serif;font-weight:700;font-size:.93rem;margin-bottom:8px;}
  .step-item p{color:var(--muted);font-size:.8rem;line-height:1.6;}

  .cmp-wrap{margin-top:52px;border-radius:var(--radius);border:1px solid var(--border);overflow:hidden;}
  .cmp-table{width:100%;border-collapse:collapse;}
  .cmp-table th{background:var(--surface);padding:15px 18px;font-family:'Syne',sans-serif;font-weight:700;font-size:.8rem;text-align:center;border-bottom:1px solid var(--border);}
  .cmp-table th:first-child{text-align:left;}
  .cmp-table th.hl{background:linear-gradient(135deg,rgba(59,140,248,.18),rgba(124,58,237,.18));color:var(--accent);}
  .cmp-table td{padding:13px 18px;font-size:.83rem;border-bottom:1px solid rgba(255,255,255,.04);text-align:center;color:var(--muted);}
  .cmp-table td:first-child{text-align:left;color:var(--text);font-weight:500;}
  .cmp-table tr:last-child td{border-bottom:none;}
  .cmp-table tr:hover td{background:rgba(59,140,248,.04);}
  .hl-col{background:rgba(59,140,248,.06);font-weight:600;color:var(--text)!important;}
  .chk{color:#22c55e;}.crs{color:#ef4444;}

  /* BOTTOM DOWNLOAD */
  .btm-dl{position:relative;z-index:1;background:linear-gradient(135deg,rgba(59,140,248,.08),rgba(124,58,237,.08));border-top:1px solid var(--border);border-bottom:1px solid var(--border);padding:90px 20px;text-align:center;}
  .btm-card{max-width:560px;margin:0 auto;background:var(--card);border:1px solid rgba(59,140,248,.28);border-radius:26px;padding:50px 34px;position:relative;overflow:hidden;}
  .btm-card::before{content:'';position:absolute;top:-60px;left:50%;transform:translateX(-50%);width:350px;height:250px;background:radial-gradient(ellipse,rgba(59,140,248,.14),transparent 70%);pointer-events:none;}
  .btm-ver{display:inline-flex;align-items:center;gap:8px;background:rgba(59,140,248,.1);border:1px solid rgba(59,140,248,.22);border-radius:30px;padding:7px 18px;font-size:.7rem;font-weight:700;color:var(--accent);letter-spacing:1px;text-transform:uppercase;margin-bottom:20px;}
  .btm-card h2{font-family:'Syne',sans-serif;font-weight:800;font-size:1.9rem;letter-spacing:-1px;margin-bottom:10px;}
  .btm-card>p{color:var(--muted);font-size:.86rem;margin-bottom:30px;}

  .btn-btm{position:relative;display:inline-flex;align-items:center;gap:14px;background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;font-family:'Syne',sans-serif;font-weight:800;font-size:1.05rem;padding:20px 44px;border-radius:50px;text-decoration:none;box-shadow:0 12px 44px rgba(59,140,248,.45);transition:all .3s;overflow:hidden;-webkit-text-fill-color:white;margin-bottom:24px;animation:btnGlow 3s 1s infinite;}
  .btn-btm::after{content:'';position:absolute;top:0;left:-120%;width:65%;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,.22),transparent);animation:sweep 3s 1s infinite;}
  .btn-btm:hover{transform:translateY(-4px);box-shadow:0 22px 60px rgba(59,140,248,.58);}
  .btm-ico{width:44px;height:44px;border-radius:12px;background:rgba(255,255,255,.15);display:flex;align-items:center;justify-content:center;font-size:1.3rem;animation:iconBounce 2s ease-in-out infinite;}
  .btn-btm-txt{text-align:left;}
  .btn-btm-main{display:block;font-size:1rem;}
  .btn-btm-sub{display:block;font-size:.67rem;font-weight:400;opacity:.78;margin-top:2px;}

  .btm-meta{display:flex;gap:16px;justify-content:center;flex-wrap:wrap;}
  .btm-meta-item{font-size:.74rem;color:var(--muted);display:flex;align-items:center;gap:5px;}
  .btm-meta-icon{color:var(--neon);}

  .faq-list{margin-top:46px;display:flex;flex-direction:column;gap:10px;}
  .faq-item{background:var(--card);border:1px solid var(--border);border-radius:14px;overflow:hidden;transition:border-color .3s;}
  .faq-item:hover{border-color:rgba(59,140,248,.3);}
  .faq-q{display:flex;justify-content:space-between;align-items:center;padding:20px 24px;cursor:pointer;font-weight:600;font-size:.9rem;}
  .faq-ico{width:26px;height:26px;border-radius:50%;background:rgba(59,140,248,.1);display:flex;align-items:center;justify-content:center;font-size:1rem;color:var(--accent);flex-shrink:0;transition:transform .3s;}
  .faq-a{max-height:0;overflow:hidden;transition:max-height .4s ease;}
  .faq-a-inner{padding:0 24px 20px;font-size:.84rem;color:var(--muted);line-height:1.7;}
  .faq-item.open .faq-a{max-height:200px;}
  .faq-item.open .faq-ico{transform:rotate(45deg);background:rgba(59,140,248,.2);}

  footer{position:relative;z-index:1;border-top:1px solid var(--border);padding:42px 34px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:14px;}
  .footer-brand{font-family:'Syne',sans-serif;font-weight:800;font-size:1.05rem;background:linear-gradient(135deg,var(--accent),var(--neon));-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
  .footer-copy{color:var(--muted);font-size:.78rem;}

  .reveal{opacity:0;transform:translateY(26px);transition:opacity .7s ease,transform .7s ease;}
  .reveal.visible{opacity:1;transform:translateY(0);}

  @media(max-width:768px){
    nav{padding:13px 16px;}
    .nav-badge{display:none;}
    h1{letter-spacing:-1.5px;}
    .steps-row{flex-direction:column;gap:26px;}
    .steps-row::before{display:none;}
    .gal-grid{grid-template-columns:1fr;}
    footer{flex-direction:column;text-align:center;}
    .dl-card{padding:26px 18px;}
    .btn-mega{padding:17px 16px;}
    .btn-btm{padding:18px 28px;}
  }
</style>
</head>
<body>

<div class="particles" id="particles"></div>

<nav>
  <div class="logo">
    <div class="logo-icon">☁</div>
    TeraBox MOD
  </div>
  <div class="nav-right">
    <span class="nav-badge">✦ PREMIUM FREE</span>
    <a href="#download" class="nav-dl">⬇ Download</a>
  </div>
</nav>

<section class="hero">
  <div class="hero-ring"></div>
  <div class="hero-ring"></div>
  <div class="hero-ring"></div>

  <div class="hero-pill">
    <span class="pill-dot"></span>
    TeraBox MOD v4.14 — Premium Unlocked
  </div>

  <h1>
    <span class="h1-white">Unlimited Cloud</span>
    <span class="h1-grad">No Ads. No Limits.</span>
  </h1>

  <p class="hero-tagline">
    Get <strong>TeraBox MOD APK</strong> — unlimited storage, zero ads,
    blazing fast downloads & multi-device sync. <strong>100% Free Forever.</strong>
  </p>

  <div class="mockup-wrap reveal">
    <div class="mockup-halo"></div>
    <img src="https://apkteraboxx.com/wp-content/uploads/2026/01/Multi-device-support-768x1536.webp" alt="TeraBox MOD" class="mockup-img"/>
    <div class="mockup-chip">★ Premium Unlocked</div>
  </div>

  <div class="stats">
    <div class="stat-item"><div class="stat-num">1TB+</div><div class="stat-lbl">Free Storage</div></div>
    <div class="stat-div"></div>
    <div class="stat-item"><div class="stat-num">0</div><div class="stat-lbl">Ads</div></div>
    <div class="stat-div"></div>
    <div class="stat-item"><div class="stat-num">10M+</div><div class="stat-lbl">Downloads</div></div>
    <div class="stat-div"></div>
    <div class="stat-item"><div class="stat-num">4.9★</div><div class="stat-lbl">Rating</div></div>
  </div>

  <!-- ★ PREMIUM DOWNLOAD CARD ★ -->
  <div class="dl-section">
    <div class="dl-card reveal">
      <div class="dl-top-label"><span></span> Direct Fast Download <span></span></div>
      <div class="dl-card-title">Download TeraBox MOD APK</div>
      <div class="dl-card-desc">v4.14.0 · Premium Unlocked · No Ads · Unlimited Storage</div>

      <a href="https://store-na-phx-3.gofile.io/download/web/131e7cb8-04f1-486e-bdcc-0c8ce312bf48/TeraBox_4.14.0_apks_opt.apk"
         class="btn-mega" onclick="startProgress(event)">
        <div class="btn-icon-wrap">⬇</div>
        <div class="btn-text-wrap">
          <span class="btn-main-txt">Download Free APK</span>
          <span class="btn-sub-txt">TeraBox MOD v4.14.0 · 48 MB · Android 6.0+</span>
        </div>
        <span class="btn-arrow-ico">→</span>
      </a>

      <div class="dl-progress">
        <div class="dl-bar" id="progressBar"></div>
      </div>
      <div class="dl-status-row">
        <div class="dl-status-left">
          <span class="status-dot"></span>
          <span id="dlStatusText">Ready to download</span>
        </div>
        <span class="dl-count" id="dlCount">10,482,359 downloads</span>
      </div>
    </div>

    <div class="dl-badges">
      <div class="dl-badge">🛡 Virus Free</div>
      <div class="dl-badge">⚡ Fast CDN</div>
      <div class="dl-badge">🔓 No Root</div>
      <div class="dl-badge">♾ Unlimited</div>
      <div class="dl-badge">✅ Verified</div>
    </div>
  </div>

  <div class="trust-row">
    <div class="trust-item"><span class="trust-icon">🛡</span> 100% Safe</div>
    <div class="trust-item"><span class="trust-icon">📱</span> Android 6.0+</div>
    <div class="trust-item"><span class="trust-icon">🔗</span> Direct Link</div>
    <div class="trust-item"><span class="trust-icon">🆓</span> Always Free</div>
  </div>
</section>

<!-- FEATURES -->
<section id="features">
  <div class="container">
    <span class="sec-label reveal">✦ Premium Features</span>
    <h2 class="sec-title reveal">Everything Unlocked.<br>Nothing to Pay.</h2>
    <p class="sec-desc reveal">Every premium feature fully unlocked — no subscription, no hidden fees.</p>
    <div class="feat-grid">
      <div class="feat-card reveal"><div class="feat-ico ico-b">☁</div><h3>Unlimited Cloud Storage</h3><p>Store unlimited photos, videos and documents. 1TB+ base with MOD expansion — no cap ever.</p><span class="feat-tag tag-free">Free</span></div>
      <div class="feat-card reveal"><div class="feat-ico ico-g">🚫</div><h3>Zero Ads Forever</h3><p>Complete ad removal — no banners, no popups, no video ads. Pure clean experience.</p><span class="feat-tag tag-mod">MOD</span></div>
      <div class="feat-card reveal"><div class="feat-ico ico-n">⚡</div><h3>Unlimited Download Speed</h3><p>No throttling. Full network speed downloads with no queuing or waiting limits.</p><span class="feat-tag tag-pro">Premium</span></div>
      <div class="feat-card reveal"><div class="feat-ico ico-p">📱</div><h3>Multi-Device Sync</h3><p>Phone, tablet, PC — all perfectly synced simultaneously in real time.</p><span class="feat-tag tag-mod">New</span></div>
      <div class="feat-card reveal"><div class="feat-ico ico-r">🔐</div><h3>Private Encrypted Vault</h3><p>Lock sensitive files behind fingerprint or password. Military-grade AES-256 encryption.</p><span class="feat-tag tag-pro">Premium</span></div>
      <div class="feat-card reveal"><div class="feat-ico ico-gr">🔗</div><h3>Instant Share Links</h3><p>Generate shareable download links instantly. Share large files with anyone, no size limit.</p><span class="feat-tag tag-free">Free</span></div>
    </div>
  </div>
</section>

<!-- GALLERY -->
<section>
  <div class="container">
    <span class="sec-label reveal">✦ Screenshots</span>
    <h2 class="sec-title reveal">See it in Action</h2>
    <div class="gal-grid">
      <div class="gal-card reveal"><img src="https://apkteraboxx.com/wp-content/uploads/2026/01/Multi-device-support-768x1536.webp" alt="Multi Device"/><div class="gal-lbl">Multi-Device Support</div></div>
      <div class="gal-card reveal"><img src="https://apkteraboxx.com/wp-content/uploads/2026/01/Multi-device-support-768x1536.webp" alt="Storage" style="filter:hue-rotate(40deg);"/><div class="gal-lbl">Unlimited Storage</div></div>
      <div class="gal-card reveal"><img src="https://apkteraboxx.com/wp-content/uploads/2026/01/Multi-device-support-768x1536.webp" alt="Speed" style="filter:hue-rotate(200deg);"/><div class="gal-lbl">Ultra-Fast Downloads</div></div>
    </div>
  </div>
</section>

<!-- STEPS -->
<section>
  <div class="container">
    <span class="sec-label reveal">✦ Quick Start</span>
    <h2 class="sec-title reveal">3 Simple Steps</h2>
    <div class="steps-row">
      <div class="step-item reveal"><div class="step-num">1</div><h4>Download APK</h4><p>Tap the download button. APK starts immediately — no signup needed.</p></div>
      <div class="step-item reveal"><div class="step-num">2</div><h4>Enable Unknown Sources</h4><p>Settings → Security → Enable "Install from Unknown Sources".</p></div>
      <div class="step-item reveal"><div class="step-num">3</div><h4>Install & Enjoy</h4><p>Open APK, install, and enjoy unlimited premium cloud storage with zero ads!</p></div>
    </div>
  </div>
</section>

<!-- COMPARE -->
<section>
  <div class="container">
    <span class="sec-label reveal">✦ Comparison</span>
    <h2 class="sec-title reveal">MOD vs Official</h2>
    <div class="cmp-wrap reveal">
      <table class="cmp-table">
        <thead><tr><th>Feature</th><th>Official Free</th><th>Official Premium</th><th class="hl">TeraBox MOD ✦</th></tr></thead>
        <tbody>
          <tr><td>Storage</td><td>1 TB</td><td>2 TB</td><td class="hl-col">Unlimited ♾</td></tr>
          <tr><td>Ads</td><td><span class="crs">✗ Yes</span></td><td><span class="chk">✓ No</span></td><td class="hl-col"><span class="chk">✓ Zero Ads</span></td></tr>
          <tr><td>Download Speed</td><td><span class="crs">✗ Limited</span></td><td><span class="chk">✓ Fast</span></td><td class="hl-col"><span class="chk">✓ Unlimited</span></td></tr>
          <tr><td>Multi-Device</td><td><span class="crs">✗ No</span></td><td><span class="chk">✓ Yes</span></td><td class="hl-col"><span class="chk">✓ Yes</span></td></tr>
          <tr><td>Private Vault</td><td><span class="crs">✗ No</span></td><td><span class="chk">✓ Yes</span></td><td class="hl-col"><span class="chk">✓ Yes</span></td></tr>
          <tr><td>Price</td><td>Free</td><td>$3.99/mo</td><td class="hl-col" style="color:var(--neon)!important;font-weight:700;">100% FREE</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<!-- BOTTOM DOWNLOAD -->
<div class="btm-dl" id="download">
  <div class="btm-card reveal">
    <div class="btm-ver">✦ v4.14.0 MOD — Latest</div>
    <h2>Download TeraBox<br>MOD APK Free</h2>
    <p>Premium unlocked · No ads · Unlimited storage · Fast speed</p>
    <a href="https://store-na-phx-3.gofile.io/download/web/131e7cb8-04f1-486e-bdcc-0c8ce312bf48/TeraBox_4.14.0_apks_opt.apk"
       class="btn-btm" onclick="startProgress(event)">
      <div class="btm-ico">⬇</div>
      <div class="btn-btm-txt">
        <span class="btn-btm-main">Download Free APK</span>
        <span class="btn-btm-sub">48 MB · Android 6.0+ · Safe & Verified</span>
      </div>
    </a>
    <div class="btm-meta">
      <div class="btm-meta-item"><span class="btm-meta-icon">🛡</span> Virus Free</div>
      <div class="btm-meta-item"><span class="btm-meta-icon">⚡</span> Direct Link</div>
      <div class="btm-meta-item"><span class="btm-meta-icon">🔓</span> No Root</div>
      <div class="btm-meta-item"><span class="btm-meta-icon">♾</span> Unlimited</div>
    </div>
  </div>
</div>

<!-- FAQ -->
<section>
  <div class="container" style="max-width:700px;">
    <span class="sec-label reveal">✦ FAQ</span>
    <h2 class="sec-title reveal">Frequently Asked Questions</h2>
    <div class="faq-list">
      <div class="faq-item reveal"><div class="faq-q" onclick="toggleFaq(this)">Is TeraBox MOD APK safe?<div class="faq-ico">+</div></div><div class="faq-a"><div class="faq-a-inner">Yes! Fully scanned and verified. No malware, spyware, or harmful code. Millions of users have safely installed it.</div></div></div>
      <div class="faq-item reveal"><div class="faq-q" onclick="toggleFaq(this)">Do I need to root my device?<div class="faq-ico">+</div></div><div class="faq-a"><div class="faq-a-inner">No root required. Just enable "Install from Unknown Sources" in your Android settings and install like any normal app.</div></div></div>
      <div class="faq-item reveal"><div class="faq-q" onclick="toggleFaq(this)">Is storage really unlimited?<div class="faq-ico">+</div></div><div class="faq-a"><div class="faq-a-inner">Yes! MOD version removes all storage caps. Start with 1TB and the limit is effectively removed — massive cloud capacity for free.</div></div></div>
      <div class="faq-item reveal"><div class="faq-q" onclick="toggleFaq(this)">Can I use on multiple devices?<div class="faq-ico">+</div></div><div class="faq-a"><div class="faq-a-inner">Absolutely. Install on phone, tablet, sync with PC — all simultaneously with real-time sync.</div></div></div>
    </div>
  </div>
</section>

<footer>
  <div>
    <div class="footer-brand">☁ TeraBox MOD</div>
    <div style="font-size:.7rem;color:var(--muted);margin-top:4px;">Free · Premium · Unlimited</div>
  </div>
  <div class="footer-copy">© 2026 TeraBox MOD. For educational purposes.</div>
</footer>

<script>
// PARTICLES
(function(){
  const c=document.getElementById('particles');
  for(let i=0;i<24;i++){
    const p=document.createElement('div');
    p.className='particle';
    const s=Math.random()*4+2;
    p.style.cssText=`width:${s}px;height:${s}px;left:${Math.random()*100}%;animation-duration:${Math.random()*18+12}s;animation-delay:${Math.random()*14}s;background:${Math.random()>.5?'#3b8cf8':'#00f5d4'};opacity:${Math.random()*.15+.04};`;
    c.appendChild(p);
  }
})();

// REVEAL
const obs=new IntersectionObserver(e=>{e.forEach(x=>{if(x.isIntersecting){x.target.classList.add('visible');obs.unobserve(x.target);}});},{threshold:.1});
document.querySelectorAll('.reveal').forEach(el=>obs.observe(el));

// FAQ
function toggleFaq(el){
  const item=el.parentElement;
  const open=item.classList.contains('open');
  document.querySelectorAll('.faq-item.open').forEach(i=>i.classList.remove('open'));
  if(!open) item.classList.add('open');
}

// DOWNLOAD PROGRESS
function startProgress(e){
  const bar=document.getElementById('progressBar');
  const txt=document.getElementById('dlStatusText');
  if(!bar||!txt) return;
  const msgs=['🔗 Connecting to server...','📦 Preparing file...','⬇ Starting download...','✅ Download started!'];
  let i=0,w=0;
  txt.textContent=msgs[0];
  bar.style.width='0%';
  const iv=setInterval(()=>{
    w+=Math.random()*20+8;
    if(w>=100){w=100;clearInterval(iv);}
    bar.style.width=w+'%';
    const step=Math.floor(w/33);
    if(step<msgs.length) txt.textContent=msgs[step];
    if(w>=100) txt.textContent=msgs[3];
  },280);
}

// LIVE COUNTER
(function(){
  let n=10482359;
  const el=document.getElementById('dlCount');
  setInterval(()=>{n+=Math.floor(Math.random()*3+1);if(el)el.textContent=n.toLocaleString()+' downloads';},2800);
})();
</script>
</body>
</html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)