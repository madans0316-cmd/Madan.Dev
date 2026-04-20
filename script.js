// WHATSAPP LINK (number encoded for security - not visible in source)
(function(){
  const w=document.getElementById('wa-link');
  if(w){
    const _n=atob('OTE5NDQ5ODg3Njc4');
    const _m='Hi%20Madan%2C%20I%20found%20your%20portfolio%20and%20would%20like%20to%20connect!';
    w.href='https://wa.me/'+_n+'?text='+_m;
  }
})();

// PROJECT TOGGLE SWITCH
(function(){
  const sw=document.getElementById('projSwitch');
  const hwLabel=document.getElementById('hw-label');
  const swLabel=document.getElementById('sw-label');
  if(!sw)return;
  sw.addEventListener('change',()=>{
    const isSw=sw.checked;
    document.getElementById('grid-hardware').classList.toggle('proj-grid-hidden',isSw);
    document.getElementById('grid-software').classList.toggle('proj-grid-hidden',!isSw);
    hwLabel.classList.toggle('hw-active',!isSw);
    swLabel.classList.toggle('sw-active',isSw);
  });
})();

// NAV GLIDER
function moveNavGlider(section){
  const links=document.querySelectorAll('.nav-link');
  const glider=document.getElementById('navGlider');
  if(!glider)return;
  links.forEach(a=>a.classList.remove('nav-active'));
  const active=document.querySelector(`.nav-link[data-section="${section}"]`);
  if(!active)return;
  active.classList.add('nav-active');
  const li=active.closest('li');
  glider.style.width=active.offsetWidth+'px';
  glider.style.left=li.offsetLeft+'px';
}
// Init glider on page load
window.addEventListener('load',()=>moveNavGlider('about'));
// Click to move glider
document.querySelectorAll('.nav-link').forEach(a=>{
  a.addEventListener('click',()=>moveNavGlider(a.dataset.section));
});

// LOADER
(function(){
  const bar=document.getElementById('loaderBar');
  const pct=document.getElementById('loaderPct');
  const loader=document.getElementById('intro-loader');
  let p=0;
  const iv=setInterval(()=>{
    p+=Math.random()*3.5+1;
    if(p>=100){
      p=100;clearInterval(iv);
      setTimeout(()=>{
        loader.style.opacity='0';loader.style.transition='opacity 0.6s';
        setTimeout(()=>{loader.style.display='none';},600);
      },300);
    }
    bar.style.width=p+'%';
    pct.textContent=Math.floor(p)+'%';
  },50);
})();

// THEME
const themeBtn=document.getElementById('themeBtn');
let dark=true;
themeBtn.addEventListener('click',()=>{
  dark=!dark;
  document.documentElement.dataset.theme=dark?'':'light';
  themeBtn.textContent=dark?'🌙':'☀️';
});

// HAMBURGER
const ham=document.getElementById('hamburger');
const mob=document.getElementById('mobileMenu');
ham.addEventListener('click',()=>mob.classList.toggle('open'));
mob.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>mob.classList.remove('open')));

// CURSOR
const glow=document.getElementById('cursorGlow');
const trail=document.getElementById('cursorTrail');
let tx=0,ty=0,cx=0,cy=0;
document.addEventListener('mousemove',e=>{
  tx=e.clientX;ty=e.clientY;
  glow.style.left=tx+'px';glow.style.top=ty+'px';
});
(function animT(){
  cx+=(tx-cx)*0.15;cy+=(ty-cy)*0.15;
  trail.style.left=cx+'px';trail.style.top=cy+'px';
  requestAnimationFrame(animT);
})();

// REVEAL ON SCROLL
const revealSections=()=>{
  document.querySelectorAll('.reveal').forEach(el=>{
    if(el.getBoundingClientRect().top<window.innerHeight-150)
      el.classList.add('active');
  });
};
window.addEventListener('scroll',revealSections,{passive:true});
revealSections();

// MAGNETIC BUTTONS
document.querySelectorAll('.magnetic-btn').forEach(btn=>{
  btn.addEventListener('mousemove',e=>{
    const r=btn.getBoundingClientRect();
    const x=e.clientX-r.left-r.width/2;
    const y=e.clientY-r.top-r.height/2;
    btn.style.transform=`translate(${x*0.3}px,${y*0.3}px)`;
  });
  btn.addEventListener('mouseleave',()=>{btn.style.transform='translate(0,0)';});
});

// FLOATING NAV DOTS
const sections=['home','about','skills','career','education','projects','contact'];
const dots=document.querySelectorAll('.nav-dot');
dots.forEach(d=>d.addEventListener('click',()=>{
  const t=document.getElementById(d.dataset.target);
  if(t)t.scrollIntoView({behavior:'smooth'});
}));
window.addEventListener('scroll',()=>{
  let cur='home';
  sections.forEach(id=>{
    const el=document.getElementById(id);
    if(el&&window.scrollY>=el.offsetTop-200)cur=id;
  });
  dots.forEach(d=>d.classList.toggle('active',d.dataset.target===cur));
  // Update nav glider on scroll
  const navSections=['about','skills','career','education','projects','contact'];
  const inView=navSections.find(id=>{
    const el=document.getElementById(id);
    return el&&window.scrollY>=el.offsetTop-200;
  });
  if(inView)moveNavGlider(inView);
},{passive:true});

// BINARY RUNNER
(function(){
  const el=document.getElementById('binaryRunner');
  const w=['01001011','01000001','01001100','01001001','01001110','01010101','01011000',
    'EMBEDDED','SYSTEM','SIGNAL','PROCESS','01000001','01010010','01000011','01001000',
    'MADAN','ECE','01001001','01001111','01010100','SECURITY','ETHICAL',
    '01000001','01000011','01001011','MICROCON','TROLLER','KALI','LINUX','ARCH'];
  let s='';
  for(let i=0;i<65;i++)s+=w[Math.floor(Math.random()*w.length)]+'  ';
  el.textContent=s;
})();

// PROJECT OPEN
function openProject(url){
  const ph=['https://your-project-1-url.com','https://your-project-2-url.com','https://your-project-3-url.com'];
  if(url&&!ph.includes(url))window.open(url,'_blank');
}
