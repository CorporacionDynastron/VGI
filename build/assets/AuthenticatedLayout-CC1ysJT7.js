import{r as d,j as t,L as g,e as Y}from"./app-BYNuh-Oo.js";import{K as Z}from"./transition-dT-xSinf.js";const H=d.createContext(),b=({children:e})=>{const[r,s]=d.useState(!1),i=()=>{s(l=>!l)};return t.jsx(H.Provider,{value:{open:r,setOpen:s,toggleOpen:i},children:t.jsx("div",{className:"relative",children:e})})},Q=({children:e})=>{const{open:r,setOpen:s,toggleOpen:i}=d.useContext(H);return t.jsxs(t.Fragment,{children:[t.jsx("div",{onClick:i,children:e}),r&&t.jsx("div",{className:"fixed inset-0 z-40",onClick:()=>s(!1)})]})},J=({align:e="right",width:r="48",contentClasses:s="py-1 bg-white dark:bg-gray-700",children:i})=>{const{open:l,setOpen:o}=d.useContext(H);let a="origin-top";e==="left"?a="ltr:origin-top-left rtl:origin-top-right start-0":e==="right"&&(a="ltr:origin-top-right rtl:origin-top-left end-0");let n="";return r==="48"&&(n="w-48"),t.jsx(t.Fragment,{children:t.jsx(Z,{show:l,enter:"transition ease-out duration-200",enterFrom:"opacity-0 scale-95",enterTo:"opacity-100 scale-100",leave:"transition ease-in duration-75",leaveFrom:"opacity-100 scale-100",leaveTo:"opacity-0 scale-95",children:t.jsx("div",{className:`absolute z-50 mt-2 rounded-md shadow-lg ${a} ${n}`,onClick:()=>o(!1),children:t.jsx("div",{className:"rounded-md ring-1 ring-black ring-opacity-5 "+s,children:i})})})})},X=({className:e="",children:r,...s})=>t.jsx(g,{...s,className:"block w-full px-4 py-2 text-start text-sm leading-5 text-gray-700 transition duration-150 ease-in-out hover:bg-gray-100 focus:bg-gray-100 focus:outline-none dark:text-gray-300 dark:hover:bg-gray-800 dark:focus:bg-gray-800 "+e,children:r});b.Trigger=Q;b.Content=J;b.Link=X;let ee={data:""},te=e=>{if(typeof window=="object"){let r=(e?e.querySelector("#_goober"):window._goober)||Object.assign(document.createElement("style"),{innerHTML:" ",id:"_goober"});return r.nonce=window.__nonce__,r.parentNode||(e||document.head).appendChild(r),r.firstChild}return e||ee},re=/(?:([\u0080-\uFFFF\w-%@]+) *:? *([^{;]+?);|([^;}{]*?) *{)|(}\s*)/g,se=/\/\*[^]*?\*\/|  +/g,I=/\n+/g,y=(e,r)=>{let s="",i="",l="";for(let o in e){let a=e[o];o[0]=="@"?o[1]=="i"?s=o+" "+a+";":i+=o[1]=="f"?y(a,o):o+"{"+y(a,o[1]=="k"?"":r)+"}":typeof a=="object"?i+=y(a,r?r.replace(/([^,])+/g,n=>o.replace(/([^,]*:\S+\([^)]*\))|([^,])+/g,c=>/&/.test(c)?c.replace(/&/g,n):n?n+" "+c:c)):o):a!=null&&(o=o[1]=="-"?o:o.replace(/[A-Z]/g,"-$&").toLowerCase(),l+=y.p?y.p(o,a):o+":"+a+";")}return s+(r&&l?r+"{"+l+"}":l)+i},k={},V=e=>{if(typeof e=="object"){let r="";for(let s in e)r+=s+V(e[s]);return r}return e},ae=(e,r,s,i,l)=>{let o=V(e),a=k[o]||(k[o]=(c=>{let m=0,u=11;for(;m<c.length;)u=101*u+c.charCodeAt(m++)>>>0;return"go"+u})(o));if(!k[a]){let c=o!==e?e:(m=>{let u,h,x=[{}];for(;u=re.exec(m.replace(se,""));)u[4]?x.shift():u[3]?(h=u[3].replace(I," ").trim(),x.unshift(x[0][h]=x[0][h]||{})):x[0][u[1]]=u[2].replace(I," ").trim();return x[0]})(e);k[a]=y(l?{["@keyframes "+a]:c}:c,s?"":"."+a)}let n=s&&k.g;return s&&(k.g=k[a]),((c,m,u,h)=>{h?m.data=m.data.replace(h,c):m.data.indexOf(c)===-1&&(m.data=u?c+m.data:m.data+c)})(k[a],r,i,n),a},oe=(e,r,s)=>e.reduce((i,l,o)=>{let a=r[o];if(a&&a.call){let n=a(s),c=n&&n.props&&n.props.className||/^go/.test(n)&&n;a=c?"."+c:n&&typeof n=="object"?n.props?"":y(n,""):n===!1?"":n}return i+l+(a??"")},"");function z(e){let r=this||{},s=e.call?e(r.p):e;return ae(s.unshift?s.raw?oe(s,[].slice.call(arguments,1),r.p):s.reduce((i,l)=>Object.assign(i,l&&l.call?l(r.p):l),{}):s,te(r.target),r.g,r.o,r.k)}let F,O,S;z.bind({g:1});let j=z.bind({k:1});function ne(e,r,s,i){y.p=r,F=e,O=s,S=i}function N(e,r){let s=this||{};return function(){let i=arguments;function l(o,a){let n=Object.assign({},o),c=n.className||l.className;s.p=Object.assign({theme:O&&O()},n),s.o=/go\d/.test(c),n.className=z.apply(s,i)+(c?" "+c:"");let m=e;return e[0]&&(m=n.as||e,delete n.as),S&&m[0]&&S(n),F(m,n)}return r?r(l):l}}var ie=e=>typeof e=="function",_=(e,r)=>ie(e)?e(r):e,le=(()=>{let e=0;return()=>(++e).toString()})(),P=(()=>{let e;return()=>{if(e===void 0&&typeof window<"u"){let r=matchMedia("(prefers-reduced-motion: reduce)");e=!r||r.matches}return e}})(),de=20,W="default",R=(e,r)=>{let{toastLimit:s}=e.settings;switch(r.type){case 0:return{...e,toasts:[r.toast,...e.toasts].slice(0,s)};case 1:return{...e,toasts:e.toasts.map(a=>a.id===r.toast.id?{...a,...r.toast}:a)};case 2:let{toast:i}=r;return R(e,{type:e.toasts.find(a=>a.id===i.id)?1:0,toast:i});case 3:let{toastId:l}=r;return{...e,toasts:e.toasts.map(a=>a.id===l||l===void 0?{...a,dismissed:!0,visible:!1}:a)};case 4:return r.toastId===void 0?{...e,toasts:[]}:{...e,toasts:e.toasts.filter(a=>a.id!==r.toastId)};case 5:return{...e,pausedAt:r.time};case 6:let o=r.time-(e.pausedAt||0);return{...e,pausedAt:void 0,toasts:e.toasts.map(a=>({...a,pauseDuration:a.pauseDuration+o}))}}},E=[],U={toasts:[],pausedAt:void 0,settings:{toastLimit:de}},w={},q=(e,r=W)=>{w[r]=R(w[r]||U,e),E.forEach(([s,i])=>{s===r&&i(w[r])})},G=e=>Object.keys(w).forEach(r=>q(e,r)),ce=e=>Object.keys(w).find(r=>w[r].toasts.some(s=>s.id===e)),D=(e=W)=>r=>{q(r,e)},he={blank:4e3,error:4e3,success:2e3,loading:1/0,custom:4e3},me=(e={},r=W)=>{let[s,i]=d.useState(w[r]||U),l=d.useRef(w[r]);d.useEffect(()=>(l.current!==w[r]&&i(w[r]),E.push([r,i]),()=>{let a=E.findIndex(([n])=>n===r);a>-1&&E.splice(a,1)}),[r]);let o=s.toasts.map(a=>{var n,c,m;return{...e,...e[a.type],...a,removeDelay:a.removeDelay||((n=e[a.type])==null?void 0:n.removeDelay)||e?.removeDelay,duration:a.duration||((c=e[a.type])==null?void 0:c.duration)||e?.duration||he[a.type],style:{...e.style,...(m=e[a.type])==null?void 0:m.style,...a.style}}});return{...s,toasts:o}},ue=(e,r="blank",s)=>({createdAt:Date.now(),visible:!0,dismissed:!1,type:r,ariaProps:{role:"status","aria-live":"polite"},message:e,pauseDuration:0,...s,id:s?.id||le()}),C=e=>(r,s)=>{let i=ue(r,e,s);return D(i.toasterId||ce(i.id))({type:2,toast:i}),i.id},p=(e,r)=>C("blank")(e,r);p.error=C("error");p.success=C("success");p.loading=C("loading");p.custom=C("custom");p.dismiss=(e,r)=>{let s={type:3,toastId:e};r?D(r)(s):G(s)};p.dismissAll=e=>p.dismiss(void 0,e);p.remove=(e,r)=>{let s={type:4,toastId:e};r?D(r)(s):G(s)};p.removeAll=e=>p.remove(void 0,e);p.promise=(e,r,s)=>{let i=p.loading(r.loading,{...s,...s?.loading});return typeof e=="function"&&(e=e()),e.then(l=>{let o=r.success?_(r.success,l):void 0;return o?p.success(o,{id:i,...s,...s?.success}):p.dismiss(i),l}).catch(l=>{let o=r.error?_(r.error,l):void 0;o?p.error(o,{id:i,...s,...s?.error}):p.dismiss(i)}),e};var xe=1e3,pe=(e,r="default")=>{let{toasts:s,pausedAt:i}=me(e,r),l=d.useRef(new Map).current,o=d.useCallback((h,x=xe)=>{if(l.has(h))return;let f=setTimeout(()=>{l.delete(h),a({type:4,toastId:h})},x);l.set(h,f)},[]);d.useEffect(()=>{if(i)return;let h=Date.now(),x=s.map(f=>{if(f.duration===1/0)return;let L=(f.duration||0)+f.pauseDuration-(h-f.createdAt);if(L<0){f.visible&&p.dismiss(f.id);return}return setTimeout(()=>p.dismiss(f.id,r),L)});return()=>{x.forEach(f=>f&&clearTimeout(f))}},[s,i,r]);let a=d.useCallback(D(r),[r]),n=d.useCallback(()=>{a({type:5,time:Date.now()})},[a]),c=d.useCallback((h,x)=>{a({type:1,toast:{id:h,height:x}})},[a]),m=d.useCallback(()=>{i&&a({type:6,time:Date.now()})},[i,a]),u=d.useCallback((h,x)=>{let{reverseOrder:f=!1,gutter:L=8,defaultPosition:M}=x||{},A=s.filter(v=>(v.position||M)===(h.position||M)&&v.height),K=A.findIndex(v=>v.id===h.id),T=A.filter((v,B)=>B<K&&v.visible).length;return A.filter(v=>v.visible).slice(...f?[T+1]:[0,T]).reduce((v,B)=>v+(B.height||0)+L,0)},[s]);return d.useEffect(()=>{s.forEach(h=>{if(h.dismissed)o(h.id,h.removeDelay);else{let x=l.get(h.id);x&&(clearTimeout(x),l.delete(h.id))}})},[s,o]),{toasts:s,handlers:{updateHeight:c,startPause:n,endPause:m,calculateOffset:u}}},fe=j`
from {
  transform: scale(0) rotate(45deg);
	opacity: 0;
}
to {
 transform: scale(1) rotate(45deg);
  opacity: 1;
}`,be=j`
from {
  transform: scale(0);
  opacity: 0;
}
to {
  transform: scale(1);
  opacity: 1;
}`,ge=j`
from {
  transform: scale(0) rotate(90deg);
	opacity: 0;
}
to {
  transform: scale(1) rotate(90deg);
	opacity: 1;
}`,ve=N("div")`
  width: 20px;
  opacity: 0;
  height: 20px;
  border-radius: 10px;
  background: ${e=>e.primary||"#ff4b4b"};
  position: relative;
  transform: rotate(45deg);

  animation: ${fe} 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275)
    forwards;
  animation-delay: 100ms;

  &:after,
  &:before {
    content: '';
    animation: ${be} 0.15s ease-out forwards;
    animation-delay: 150ms;
    position: absolute;
    border-radius: 3px;
    opacity: 0;
    background: ${e=>e.secondary||"#fff"};
    bottom: 9px;
    left: 4px;
    height: 2px;
    width: 12px;
  }

  &:before {
    animation: ${ge} 0.15s ease-out forwards;
    animation-delay: 180ms;
    transform: rotate(90deg);
  }
`,we=j`
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
`,je=N("div")`
  width: 12px;
  height: 12px;
  box-sizing: border-box;
  border: 2px solid;
  border-radius: 100%;
  border-color: ${e=>e.secondary||"#e0e0e0"};
  border-right-color: ${e=>e.primary||"#616161"};
  animation: ${we} 1s linear infinite;
`,ke=j`
from {
  transform: scale(0) rotate(45deg);
	opacity: 0;
}
to {
  transform: scale(1) rotate(45deg);
	opacity: 1;
}`,ye=j`
0% {
	height: 0;
	width: 0;
	opacity: 0;
}
40% {
  height: 0;
	width: 6px;
	opacity: 1;
}
100% {
  opacity: 1;
  height: 10px;
}`,Ne=N("div")`
  width: 20px;
  opacity: 0;
  height: 20px;
  border-radius: 10px;
  background: ${e=>e.primary||"#61d345"};
  position: relative;
  transform: rotate(45deg);

  animation: ${ke} 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275)
    forwards;
  animation-delay: 100ms;
  &:after {
    content: '';
    box-sizing: border-box;
    animation: ${ye} 0.2s ease-out forwards;
    opacity: 0;
    animation-delay: 200ms;
    position: absolute;
    border-right: 2px solid;
    border-bottom: 2px solid;
    border-color: ${e=>e.secondary||"#fff"};
    bottom: 6px;
    left: 6px;
    height: 10px;
    width: 6px;
  }
`,Le=N("div")`
  position: absolute;
`,Ce=N("div")`
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  min-width: 20px;
  min-height: 20px;
`,Me=j`
from {
  transform: scale(0.6);
  opacity: 0.4;
}
to {
  transform: scale(1);
  opacity: 1;
}`,$e=N("div")`
  position: relative;
  transform: scale(0.6);
  opacity: 0.4;
  min-width: 20px;
  animation: ${Me} 0.3s 0.12s cubic-bezier(0.175, 0.885, 0.32, 1.275)
    forwards;
`,Ee=({toast:e})=>{let{icon:r,type:s,iconTheme:i}=e;return r!==void 0?typeof r=="string"?d.createElement($e,null,r):r:s==="blank"?null:d.createElement(Ce,null,d.createElement(je,{...i}),s!=="loading"&&d.createElement(Le,null,s==="error"?d.createElement(ve,{...i}):d.createElement(Ne,{...i})))},_e=e=>`
0% {transform: translate3d(0,${e*-200}%,0) scale(.6); opacity:.5;}
100% {transform: translate3d(0,0,0) scale(1); opacity:1;}
`,ze=e=>`
0% {transform: translate3d(0,0,-1px) scale(1); opacity:1;}
100% {transform: translate3d(0,${e*-150}%,-1px) scale(.6); opacity:0;}
`,De="0%{opacity:0;} 100%{opacity:1;}",Ae="0%{opacity:1;} 100%{opacity:0;}",Be=N("div")`
  display: flex;
  align-items: center;
  background: #fff;
  color: #363636;
  line-height: 1.3;
  will-change: transform;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.1), 0 3px 3px rgba(0, 0, 0, 0.05);
  max-width: 350px;
  pointer-events: auto;
  padding: 8px 10px;
  border-radius: 8px;
`,Oe=N("div")`
  display: flex;
  justify-content: center;
  margin: 4px 10px;
  color: inherit;
  flex: 1 1 auto;
  white-space: pre-line;
`,Se=(e,r)=>{let s=e.includes("top")?1:-1,[i,l]=P()?[De,Ae]:[_e(s),ze(s)];return{animation:r?`${j(i)} 0.35s cubic-bezier(.21,1.02,.73,1) forwards`:`${j(l)} 0.4s forwards cubic-bezier(.06,.71,.55,1)`}},He=d.memo(({toast:e,position:r,style:s,children:i})=>{let l=e.height?Se(e.position||r||"top-center",e.visible):{opacity:0},o=d.createElement(Ee,{toast:e}),a=d.createElement(Oe,{...e.ariaProps},_(e.message,e));return d.createElement(Be,{className:e.className,style:{...l,...s,...e.style}},typeof i=="function"?i({icon:o,message:a}):d.createElement(d.Fragment,null,o,a))});ne(d.createElement);var We=({id:e,className:r,style:s,onHeightUpdate:i,children:l})=>{let o=d.useCallback(a=>{if(a){let n=()=>{let c=a.getBoundingClientRect().height;i(e,c)};n(),new MutationObserver(n).observe(a,{subtree:!0,childList:!0,characterData:!0})}},[e,i]);return d.createElement("div",{ref:o,className:r,style:s},l)},Te=(e,r)=>{let s=e.includes("top"),i=s?{top:0}:{bottom:0},l=e.includes("center")?{justifyContent:"center"}:e.includes("right")?{justifyContent:"flex-end"}:{};return{left:0,right:0,display:"flex",position:"absolute",transition:P()?void 0:"all 230ms cubic-bezier(.21,1.02,.73,1)",transform:`translateY(${r*(s?1:-1)}px)`,...i,...l}},Ie=z`
  z-index: 9999;
  > * {
    pointer-events: auto;
  }
`,$=16,Ve=({reverseOrder:e,position:r="top-center",toastOptions:s,gutter:i,children:l,toasterId:o,containerStyle:a,containerClassName:n})=>{let{toasts:c,handlers:m}=pe(s,o);return d.createElement("div",{"data-rht-toaster":o||"",style:{position:"fixed",zIndex:9999,top:$,left:$,right:$,bottom:$,pointerEvents:"none",...a},className:n,onMouseEnter:m.startPause,onMouseLeave:m.endPause},c.map(u=>{let h=u.position||r,x=m.calculateOffset(u,{reverseOrder:e,gutter:i,defaultPosition:r}),f=Te(h,x);return d.createElement(We,{id:u.id,key:u.id,onHeightUpdate:m.updateHeight,className:u.visible?Ie:"",style:f},u.type==="custom"?_(u.message,u):l?l(u):d.createElement(He,{toast:u,position:h}))}))};function Re({header:e,children:r}){const{auth:s,flash:i}=Y().props,l=s.user,[o,a]=d.useState(!1),[n,c]=d.useState(!1),[m,u]=d.useState(new Date),[h,x]=d.useState(()=>typeof window<"u"?localStorage.getItem("theme")==="light":!1);d.useEffect(()=>{h?(document.documentElement.classList.add("light-mode"),localStorage.setItem("theme","light")):(document.documentElement.classList.remove("light-mode"),localStorage.setItem("theme","dark"))},[h]),d.useEffect(()=>{const M=setInterval(()=>u(new Date),1e3);return()=>clearInterval(M)},[]),d.useEffect(()=>{i?.message&&p.success(i.message,{style:{background:"#0B111A",color:"#fff",border:"1px solid #D4AF37"},iconTheme:{primary:"#D4AF37",secondary:"#0B111A"}}),i?.error&&p.error(i.error,{style:{background:"#0B111A",color:"#fff",border:"1px solid #ef4444"}})},[i]);const f=m.toLocaleDateString("es-ES",{weekday:"short",day:"numeric",month:"short"}).toUpperCase(),L=m.toLocaleTimeString("es-ES",{hour:"2-digit",minute:"2-digit"});return t.jsxs("div",{className:"min-h-screen bg-brand-dark flex font-sans selection:bg-brand-gold selection:text-brand-dark",children:[t.jsx(Ve,{position:"top-right"}),t.jsxs("aside",{className:`fixed inset-y-0 left-0 z-50 bg-brand-dark transition-all duration-300 ease-in-out md:translate-x-0 flex flex-col border-r border-white/5 ${n?"w-20":"w-64"} ${o?"translate-x-0 w-64":"-translate-x-full md:w-[inherit]"}`,children:[t.jsxs("div",{className:"flex items-center justify-center h-20 relative overflow-hidden flex-shrink-0",children:[t.jsx("div",{className:"absolute inset-0 bg-blueprint opacity-20 pointer-events-none"}),t.jsxs("a",{href:"/",className:`flex items-center group relative z-10 ${n&&!o?"justify-center":"space-x-3 w-full px-6"}`,children:[t.jsx("div",{className:"w-8 h-8 flex-shrink-0 border border-brand-gold flex items-center justify-center rotate-45 transition-transform group-hover:rotate-0 duration-500 shadow-[0_0_15px_rgba(212,175,55,0.2)]",children:t.jsx("span",{className:"font-mono text-brand-gold font-bold -rotate-45 group-hover:rotate-0 duration-500 transition-transform",children:"V"})}),(!n||o)&&t.jsx("span",{className:"font-display font-bold text-xl uppercase tracking-widest text-white whitespace-nowrap overflow-hidden",children:"VADGOD"})]})]}),t.jsxs("nav",{className:"flex-1 overflow-y-auto custom-scrollbar py-4 space-y-1",children:[t.jsxs(g,{href:route("dashboard"),className:`flex items-center px-4 py-3 mx-2 rounded-none transition-colors group ${route().current("dashboard")?"bg-brand-gold text-brand-dark font-bold shadow-[0_0_15px_rgba(212,175,55,0.3)]":"text-brand-steel hover:bg-white/5 hover:text-white"}`,title:"Dashboard",children:[t.jsx("svg",{className:`flex-shrink-0 ${n&&!o?"mx-auto w-6 h-6":"w-5 h-5 mr-3"}`,fill:"none",stroke:"currentColor",viewBox:"0 0 24 24",children:t.jsx("path",{strokeLinecap:"round",strokeLinejoin:"round",strokeWidth:"2",d:"M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"})}),(!n||o)&&t.jsx("span",{className:"whitespace-nowrap",children:"Dashboard"})]}),!n||o?t.jsx("div",{className:"pt-6 pb-2 px-6",children:t.jsx("p",{className:"font-mono text-[10px] text-brand-steel uppercase tracking-[0.2em]",children:"Gestión General"})}):t.jsx("div",{className:"w-8 h-px bg-white/10 mx-auto my-4"}),t.jsxs(g,{href:route("admin.obras.index"),className:`flex items-center px-4 py-3 mx-2 rounded-none transition-colors group ${route().current("admin.obras.*")?"bg-brand-gold text-brand-dark font-bold shadow-[0_0_15px_rgba(212,175,55,0.3)]":"text-brand-steel hover:bg-white/5 hover:text-white"}`,title:"Portafolio / Obras",children:[t.jsx("svg",{className:`flex-shrink-0 ${n&&!o?"mx-auto w-6 h-6":"w-5 h-5 mr-3"}`,fill:"none",stroke:"currentColor",viewBox:"0 0 24 24",children:t.jsx("path",{strokeLinecap:"round",strokeLinejoin:"round",strokeWidth:"2",d:"M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"})}),(!n||o)&&t.jsx("span",{className:"whitespace-nowrap",children:"Portafolio / Obras"})]}),t.jsxs(g,{href:route("admin.banners.index"),className:`flex items-center px-4 py-3 mx-2 rounded-none transition-colors group ${route().current("admin.banners.*")?"bg-brand-gold text-brand-dark font-bold shadow-[0_0_15px_rgba(212,175,55,0.3)]":"text-brand-steel hover:bg-white/5 hover:text-white"}`,title:"Banners",children:[t.jsx("svg",{className:`flex-shrink-0 ${n&&!o?"mx-auto w-6 h-6":"w-5 h-5 mr-3"}`,fill:"none",stroke:"currentColor",viewBox:"0 0 24 24",children:t.jsx("path",{strokeLinecap:"round",strokeLinejoin:"round",strokeWidth:"2",d:"M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"})}),(!n||o)&&t.jsx("span",{className:"whitespace-nowrap",children:"Banners"})]}),t.jsxs(g,{href:route("admin.noticias.index"),className:`flex items-center px-4 py-3 mx-2 rounded-none transition-colors group ${route().current("admin.noticias.*")?"bg-brand-gold text-brand-dark font-bold shadow-[0_0_15px_rgba(212,175,55,0.3)]":"text-brand-steel hover:bg-white/5 hover:text-white"}`,title:"Noticias",children:[t.jsx("svg",{className:`flex-shrink-0 ${n&&!o?"mx-auto w-6 h-6":"w-5 h-5 mr-3"}`,fill:"none",stroke:"currentColor",viewBox:"0 0 24 24",children:t.jsx("path",{strokeLinecap:"round",strokeLinejoin:"round",strokeWidth:"2",d:"M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"})}),(!n||o)&&t.jsx("span",{className:"whitespace-nowrap",children:"Noticias"})]}),t.jsxs(g,{href:route("admin.trabajadores.index"),className:`flex items-center px-4 py-3 mx-2 rounded-none transition-colors group ${route().current("admin.trabajadores.*")?"bg-brand-gold text-brand-dark font-bold shadow-[0_0_15px_rgba(212,175,55,0.3)]":"text-brand-steel hover:bg-white/5 hover:text-white"}`,title:"El Equipo / Usuarios",children:[t.jsx("svg",{className:`flex-shrink-0 ${n&&!o?"mx-auto w-6 h-6":"w-5 h-5 mr-3"}`,fill:"none",stroke:"currentColor",viewBox:"0 0 24 24",children:t.jsx("path",{strokeLinecap:"round",strokeLinejoin:"round",strokeWidth:"2",d:"M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"})}),(!n||o)&&t.jsx("span",{className:"whitespace-nowrap",children:"El Equipo / Usuarios"})]}),t.jsxs(g,{href:route("admin.aliados.index"),className:`flex items-center px-4 py-3 mx-2 rounded-none transition-colors group ${route().current("admin.aliados.*")?"bg-brand-gold text-brand-dark font-bold shadow-[0_0_15px_rgba(212,175,55,0.3)]":"text-brand-steel hover:bg-white/5 hover:text-white"}`,title:"Alianzas",children:[t.jsx("svg",{className:`flex-shrink-0 ${n&&!o?"mx-auto w-6 h-6":"w-5 h-5 mr-3"}`,fill:"none",stroke:"currentColor",viewBox:"0 0 24 24",children:t.jsx("path",{strokeLinecap:"round",strokeLinejoin:"round",strokeWidth:"2",d:"M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"})}),(!n||o)&&t.jsx("span",{className:"whitespace-nowrap",children:"Alianzas"})]}),t.jsxs(g,{href:route("admin.usuarios.index"),className:`flex items-center px-4 py-3 mx-2 rounded-none transition-colors group ${route().current("admin.usuarios.*")?"bg-brand-gold text-brand-dark font-bold shadow-[0_0_15px_rgba(212,175,55,0.3)]":"text-brand-steel hover:bg-white/5 hover:text-white"}`,title:"Usuarios del Sistema",children:[t.jsx("svg",{className:`flex-shrink-0 ${n&&!o?"mx-auto w-6 h-6":"w-5 h-5 mr-3"}`,fill:"none",stroke:"currentColor",viewBox:"0 0 24 24",children:t.jsx("path",{strokeLinecap:"round",strokeLinejoin:"round",strokeWidth:"2",d:"M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"})}),(!n||o)&&t.jsx("span",{className:"whitespace-nowrap",children:"Usuarios"})]}),t.jsxs(g,{href:route("admin.mensajes.index"),className:`flex items-center px-4 py-3 mx-2 rounded-none transition-colors group ${route().current("admin.mensajes.*")?"bg-brand-gold text-brand-dark font-bold shadow-[0_0_15px_rgba(212,175,55,0.3)]":"text-brand-steel hover:bg-white/5 hover:text-white"}`,title:"Bandeja de Entrada",children:[t.jsx("svg",{className:`flex-shrink-0 ${n&&!o?"mx-auto w-6 h-6":"w-5 h-5 mr-3"}`,fill:"none",stroke:"currentColor",viewBox:"0 0 24 24",children:t.jsx("path",{strokeLinecap:"round",strokeLinejoin:"round",strokeWidth:"2",d:"M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"})}),(!n||o)&&t.jsx("span",{className:"whitespace-nowrap",children:"Bandeja de Entrada"})]}),t.jsxs(g,{href:route("admin.configuracion.index"),className:`flex items-center px-4 py-3 mx-2 rounded-none transition-colors group ${route().current("admin.configuracion.*")?"bg-brand-gold text-brand-dark font-bold shadow-[0_0_15px_rgba(212,175,55,0.3)]":"text-brand-steel hover:bg-white/5 hover:text-white"}`,title:"Configuración",children:[t.jsxs("svg",{className:`flex-shrink-0 ${n&&!o?"mx-auto w-6 h-6":"w-5 h-5 mr-3"}`,fill:"none",stroke:"currentColor",viewBox:"0 0 24 24",children:[t.jsx("path",{strokeLinecap:"round",strokeLinejoin:"round",strokeWidth:"2",d:"M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.065 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"}),t.jsx("path",{strokeLinecap:"round",strokeLinejoin:"round",strokeWidth:"2",d:"M15 12a3 3 0 11-6 0 3 3 0 016 0z"})]}),(!n||o)&&t.jsx("span",{className:"whitespace-nowrap",children:"Configuración"})]})]}),t.jsx("div",{className:"border-t border-white/5 p-4 flex justify-end",children:t.jsx("button",{onClick:()=>c(!n),className:"text-brand-steel hover:text-white p-2 hidden md:block transition-colors",children:t.jsx("svg",{className:`w-5 h-5 transition-transform duration-300 ${n?"rotate-180":""}`,fill:"none",stroke:"currentColor",viewBox:"0 0 24 24",children:t.jsx("path",{strokeLinecap:"round",strokeLinejoin:"round",strokeWidth:"2",d:"M11 19l-7-7 7-7m8 14l-7-7 7-7"})})})})]}),t.jsxs("div",{className:`flex-1 flex flex-col min-h-screen transition-all duration-300 ${n?"md:ml-20":"md:ml-64"}`,children:[t.jsx("header",{className:"bg-brand-surface2/80 backdrop-blur-md border-b border-white/5 sticky top-0 z-40",children:t.jsxs("div",{className:"flex items-center justify-between h-16 px-4 sm:px-6 lg:px-8",children:[t.jsxs("div",{className:"flex items-center",children:[t.jsx("button",{onClick:()=>a(!o),className:"md:hidden p-2 mr-2 rounded-md text-brand-steel hover:text-white hover:bg-white/5 transition-colors",children:t.jsx("svg",{className:"h-6 w-6",fill:"none",viewBox:"0 0 24 24",stroke:"currentColor",children:t.jsx("path",{strokeLinecap:"round",strokeLinejoin:"round",strokeWidth:"2",d:"M4 6h16M4 12h16M4 18h16"})})}),t.jsxs("div",{className:"hidden sm:flex items-center text-brand-steel font-mono text-xs uppercase tracking-widest gap-4",children:[t.jsxs("div",{className:"flex items-center gap-2",children:[t.jsx("svg",{className:"w-4 h-4 text-brand-gold",fill:"none",stroke:"currentColor",viewBox:"0 0 24 24",children:t.jsx("path",{strokeLinecap:"round",strokeLinejoin:"round",strokeWidth:"2",d:"M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"})}),f]}),t.jsxs("div",{className:"flex items-center gap-2",children:[t.jsx("svg",{className:"w-4 h-4 text-brand-gold",fill:"none",stroke:"currentColor",viewBox:"0 0 24 24",children:t.jsx("path",{strokeLinecap:"round",strokeLinejoin:"round",strokeWidth:"2",d:"M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"})}),L]})]})]}),t.jsxs("div",{className:"flex items-center gap-4",children:[t.jsx("button",{onClick:()=>x(!h),className:"text-brand-steel hover:text-brand-gold transition-colors p-2",title:"Cambiar Tema",children:h?t.jsx("svg",{className:"w-5 h-5",fill:"none",stroke:"currentColor",viewBox:"0 0 24 24",children:t.jsx("path",{strokeLinecap:"round",strokeLinejoin:"round",strokeWidth:"2",d:"M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"})}):t.jsx("svg",{className:"w-5 h-5",fill:"none",stroke:"currentColor",viewBox:"0 0 24 24",children:t.jsx("path",{strokeLinecap:"round",strokeLinejoin:"round",strokeWidth:"2",d:"M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"})})}),t.jsxs(b,{children:[t.jsx(b.Trigger,{children:t.jsxs("button",{className:"text-brand-steel hover:text-white transition-colors relative p-2",title:"Notificaciones",children:[t.jsx("span",{className:"absolute top-1 right-1 w-2 h-2 bg-red-500 rounded-full animate-pulse"}),t.jsx("svg",{className:"w-5 h-5",fill:"none",stroke:"currentColor",viewBox:"0 0 24 24",children:t.jsx("path",{strokeLinecap:"round",strokeLinejoin:"round",strokeWidth:"2",d:"M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"})})]})}),t.jsxs(b.Content,{children:[t.jsx("div",{className:"px-4 py-2 border-b border-white/10 bg-brand-dark/50",children:t.jsx("p",{className:"text-xs font-mono font-bold text-brand-gold uppercase tracking-widest",children:"Notificaciones"})}),t.jsxs("div",{className:"max-h-64 overflow-y-auto",children:[t.jsxs("div",{className:"px-4 py-3 border-b border-white/5 hover:bg-white/5 cursor-pointer transition-colors",children:[t.jsx("p",{className:"text-sm text-white",children:"Nuevo mensaje de contacto"}),t.jsx("p",{className:"text-xs text-brand-steel mt-1 font-mono",children:"Hace 5 minutos"})]}),t.jsxs("div",{className:"px-4 py-3 border-b border-white/5 hover:bg-white/5 cursor-pointer transition-colors",children:[t.jsx("p",{className:"text-sm text-white",children:"Actualización de sistema completada"}),t.jsx("p",{className:"text-xs text-brand-steel mt-1 font-mono",children:"Hace 2 horas"})]}),t.jsxs("div",{className:"px-4 py-3 border-b border-white/5 hover:bg-white/5 cursor-pointer transition-colors",children:[t.jsx("p",{className:"text-sm text-white",children:"Alerta: Respaldo programado"}),t.jsx("p",{className:"text-xs text-brand-steel mt-1 font-mono",children:"Hace 1 día"})]})]}),t.jsx("div",{className:"px-4 py-2 text-center border-t border-white/10",children:t.jsx(g,{href:"#",className:"text-xs font-mono text-brand-gold hover:text-white transition-colors",children:"Ver todas"})})]})]}),t.jsx("div",{className:"ml-2 flex items-center md:ml-4",children:t.jsxs(b,{children:[t.jsx(b.Trigger,{children:t.jsx("button",{className:"flex items-center text-sm focus:outline-none focus:ring-1 focus:ring-brand-gold transition-shadow",children:t.jsxs("div",{className:"flex items-center space-x-3 bg-brand-surface border border-white/5 pl-2 pr-4 py-1.5 rounded-full text-white hover:border-brand-gold/50 transition-colors shadow-lg",children:[t.jsx("div",{className:"w-8 h-8 rounded-full bg-brand-dark flex items-center justify-center border border-brand-gold/30 text-brand-gold font-bold font-mono text-xs",children:l.name.substring(0,2).toUpperCase()}),t.jsxs("div",{className:"flex flex-col items-start hidden sm:flex",children:[t.jsx("span",{className:"font-mono text-xs uppercase tracking-wider leading-none",children:l.name}),t.jsx("span",{className:"text-[9px] text-brand-gold tracking-widest mt-1 uppercase",children:"Administrador"})]}),t.jsx("svg",{className:"h-4 w-4 text-brand-steel ml-2",fill:"none",stroke:"currentColor",viewBox:"0 0 24 24",children:t.jsx("path",{strokeLinecap:"round",strokeLinejoin:"round",strokeWidth:"2",d:"M19 9l-7 7-7-7"})})]})})}),t.jsxs(b.Content,{contentClasses:"py-2 bg-brand-surface2 border border-brand-gold/20 text-white rounded-md shadow-2xl mt-2 w-56",children:[t.jsxs("div",{className:"px-4 py-3 border-b border-white/5 mb-1",children:[t.jsx("p",{className:"text-sm font-medium text-white",children:l.name}),t.jsx("p",{className:"text-xs text-brand-steel truncate",children:l.email})]}),t.jsxs(b.Link,{href:route("profile.edit"),className:"text-brand-steel hover:text-brand-gold hover:bg-brand-dark flex items-center gap-2",children:[t.jsx("svg",{className:"w-4 h-4",fill:"none",stroke:"currentColor",viewBox:"0 0 24 24",children:t.jsx("path",{strokeLinecap:"round",strokeLinejoin:"round",strokeWidth:"2",d:"M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"})}),"Perfil Administrativo"]}),t.jsxs(b.Link,{href:route("admin.configuracion.index"),className:"text-brand-steel hover:text-brand-gold hover:bg-brand-dark flex items-center gap-2",children:[t.jsxs("svg",{className:"w-4 h-4",fill:"none",stroke:"currentColor",viewBox:"0 0 24 24",children:[t.jsx("path",{strokeLinecap:"round",strokeLinejoin:"round",strokeWidth:"2",d:"M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"}),t.jsx("path",{strokeLinecap:"round",strokeLinejoin:"round",strokeWidth:"2",d:"M15 12a3 3 0 11-6 0 3 3 0 016 0z"})]}),"Configuración"]}),t.jsx("div",{className:"border-t border-white/5 my-1"}),t.jsxs(b.Link,{href:route("logout"),method:"post",as:"button",className:"text-red-400 hover:text-red-300 hover:bg-brand-dark flex items-center gap-2",children:[t.jsx("svg",{className:"w-4 h-4",fill:"none",stroke:"currentColor",viewBox:"0 0 24 24",children:t.jsx("path",{strokeLinecap:"round",strokeLinejoin:"round",strokeWidth:"2",d:"M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"})}),"Cerrar Sesión"]})]})]})})]})]})}),e&&t.jsx("div",{className:"bg-brand-dark border-b border-white/5",children:t.jsx("div",{className:"max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8",children:e})}),t.jsx("main",{className:"flex-1 overflow-y-auto p-4 sm:p-6 lg:p-8",children:r})]}),o&&t.jsx("div",{className:"fixed inset-0 bg-brand-dark/80 backdrop-blur-sm z-40 md:hidden",onClick:()=>a(!1)}),t.jsx("style",{children:`
                .custom-scrollbar::-webkit-scrollbar { width: 4px; }
                .custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
                .custom-scrollbar::-webkit-scrollbar-thumb { background: #161F2E; border-radius: 4px; }
                .custom-scrollbar::-webkit-scrollbar-thumb:hover { background: #D4AF37; }
            `})]})}export{Re as A};
