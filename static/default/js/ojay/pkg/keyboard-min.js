/*
Copyright (c) 2007-2008 the OTHER media Limited
Licensed under the BSD license, http://ojay.othermedia.org/license.html
*/
// @require ojay/core-min
eval(function(p,a,c,k,e,r){e=function(c){return(c<62?'':e(parseInt(c/62)))+((c=c%62)>35?String.fromCharCode(c+29):c.toString(36))};if('0'.replace(0,e)==0){while(c--)r[e(c)]=k[c];k=[function(e){return r[e]||e}];e=function(){return'([2-9t-zA-Z]|1\\w)'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('(3(m,h,k){5 i=m.KEY;5 r=3(a){a=a.trim();4 a?a.split(/\\s+/):[]},o=3(a,b){4 a-b},p=3(a){4 a&&15(a).14().charCodeAt(0)},l=3(c){7(Z c==\'Y\')c=r(c);4 c.map(3(a){5 b=G;7(b=i[15(a).14()])a=b;7(Z a==\'Y\')a=p(a);4 a}).1a(o)},s=3(c){4 c.reduce(3(a,b){switch(b){D i.CONTROL:a.ctrl=u;C;D i.SHIFT:a.shift=u;C;D i.ALT:a.alt=u;C;default:a.T.L(b)}4 a},{T:[]})},j=3(a){4 a.1a(o).join(\':\')};5 q=R.Keyboard=8 v.N({listen:3(a,b,c,e){5 g=8 n(a,b,c,e);g.x();4 g},isPressed:3(a){4 l(a).every(f.method(\'J\'))}});5 n=8 v.11({12:3(a,b,c,e){a=R(a).node;7(e)c=c.bind(e);2.E=l(b);2.I=8 m(a,s(2.E),c)},x:3(){2.B=u;2.I.x();2.z&&d.P(2);4 2},A:3(){2.B=O;2.I.A();2.z&&d.K(2);4 2},10:3(){2.z=u;2.B&&d.P(2);4 2},allowDefault:3(){2.z=O;2.B&&d.K(2);4 2},9:3(){5 a=j(2.E);2.9=3(){4 a};4 a}});q.RuleSet=8 v.11({12:3(a){2.6={};5 b,c;M(b Q a){c=8 n(S,b,a[b]);2.6[c.9()]=c}},w:3(a,b){a=Function.from(a);M(5 c Q 2.6)a.call(b||G,2.6[c])},x:3(){2.w(\'x\');4 2},A:3(){2.w(\'A\');4 2},get:3(a){4 2.6[j(l(a))]||G},merge:3(b){5 c={},e=3(a){c[a.9()]=a};[2,b].w({w:e});5 g=8 2.klass({});g.6=c;4 g}});5 f=8 v.N({t:[],U:3(a){7(!2.J(a))2.t.L(a)},V:3(b){2.t=2.t.19(3(a){4 a!=b})},J:3(a){4 2.t.indexOf(a)!=-1},9:3(){4 j(2.t)}});5 d=8 v.N({6:[],P:3(a){2.6.L(a)},K:3(b){2.6=2.6.19(3(a){4 a!=b})},F:3(a,b){7(2.W(b))h.10(a)},W:3(a){M(5 b=0,c=2.6.length;b<c;b++){7(2.6[b].9()==a)4 u}4 O}});h.H(k,\'keydown\',3(a){f.U(a.X);7(y.13.ua.ie)d.F(a,f.9())});7(!y.13.ua.ie){h.H(k,\'keypress\',3(a){d.F(a,f.9())})}h.H(k,\'keyup\',3(a){f.V(a.X)})})(y.18.KeyListener,y.18.Event,S);',[],74,'||this|function|return|var|_0|if|new|getSignature||||||||||||||||||||_1|true|JS|forEach|enable|YAHOO|_3|disable|_2|break|case|_7|_6|null|on|_4|_8|_9|push|for|Singleton|false|_5|in|Ojay|document|keys|_b|_a|_c|keyCode|string|typeof|preventDefault|Class|initialize|env|toUpperCase|String|||util|filter|sort'.split('|'),0,{}))