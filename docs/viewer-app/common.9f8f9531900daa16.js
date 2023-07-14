"use strict";(self.webpackChunkviewer_app=self.webpackChunkviewer_app||[]).push([[592],{3575:(C,g,o)=>{o.d(g,{M:()=>s});var t=o(2082),d=o(8590),l=o(2504),a=o(1179),_=o(2134);let s=(()=>{class c{constructor(e,i,n){this.router=e,this.commonService=i,this.modal=n,this.page=1,this.size=2,this.keywords="",this.totalElements=0,this.type=t.Z.APPLICATIONS,this.items=[]}ngOnInit(){this.searchDashboardItems(this.page,1)}searchDashboardItems(e,i,n){this.commonService.fetchDashboardItems(this.type,e-1,this.size,n).subscribe(r=>{this.items=r.content,this.totalElements=r.totalElements})}onTypeChange(e){e===t.Z.APPLICATIONS?this.type=t.Z.APPLICATIONS:e===t.Z.TERRITORIES&&(this.type=t.Z.TERRITORIES),this.items=[],this.page=1,this.searchDashboardItems(this.page)}openModal(e,i){this.modal.open(d.k,{data:{id:e,type:this.type,items:i}}).afterClosed.subscribe(({applicationId:r,territoryId:h})=>{r&&h&&this.navigateToMap(r,h)})}switchLength(e,i){if(1===e.length){let n,r;this.type===t.Z.APPLICATIONS?(n=i,r=e[0].id):this.type===t.Z.TERRITORIES&&(n=e[0].id,r=i),this.navigateToMap(n,r)}else this.type===t.Z.TERRITORIES&&(e=e.map(n=>({id:n.id,name:n.title}))),this.openModal(i,e)}onCardClicked(e){let i;this.type===t.Z.APPLICATIONS?i=this.commonService.fetchTerritoriesByApplication(e):this.type===t.Z.TERRITORIES&&(i=this.commonService.fetchApplicationsByTerritory(e)),i?.subscribe(n=>{n.content&&n.content.length&&this.switchLength(n.content,e)})}onKeywordsSearch(e){this.page=1,this.searchDashboardItems(this.page,this.size,e)}onPageChange(e){this.page=e,this.searchDashboardItems(e,this.size,this.keywords)}}return c.\u0275fac=function(e){return new(e||c)(l.Y36(a.F0),l.Y36(t.v),l.Y36(_.V))},c.\u0275dir=l.lG2({type:c}),c})()},2863:(C,g,o)=>{o.d(g,{G:()=>m});var t=o(2438),d=o(4755),l=o(5885),a=o(2504),_=o(5099),p=o(1179),s=o(2082),c=o(2134);let m=(()=>{class e extends t.R{constructor(n,r,h,u,P,O,E,M,b){super(n,r,h,u,P,O,E,M,b)}navigateToMap(){this.router.navigateByUrl(l.Ft.Section.User.Map(this.applicationId,this.territoryId))}}return e.\u0275fac=function(n){return new(n||e)(a.Y36(_.sK),a.Y36(d.Ye),a.Y36(p.gz),a.Y36(p.F0),a.Y36(s.v),a.Y36(c.V),a.Y36(a.Qsj),a.Y36(a.SBq),a.Y36(d.K0))},e.\u0275cmp=a.Xpm({type:e,selectors:[["app-map"]],features:[a.qOj],decls:3,vars:0,consts:[[1,"map"],[1,"map-container"],["id","mapa"]],template:function(n,r){1&n&&(a.TgZ(0,"div",0)(1,"div",1),a._UZ(2,"div",2),a.qZA()())},styles:[".map[_ngcontent-%COMP%]{display:flex;flex-direction:column}.map[_ngcontent-%COMP%]   .map-options[_ngcontent-%COMP%]{display:flex;justify-content:right;position:relative;bottom:60px;margin-right:600px}.map[_ngcontent-%COMP%]   .map-options[_ngcontent-%COMP%]   button[_ngcontent-%COMP%]{height:35px;width:80px;margin:0 10px;background:white}.map[_ngcontent-%COMP%]   .map-container[_ngcontent-%COMP%]{position:absolute;height:calc(100% - 80px);width:100%}"]}),e})()},2730:(C,g,o)=>{o.d(g,{O:()=>a});var t=o(2504),d=o(2082),l=o(5099);let a=(()=>{class _{constructor(){this.type=new t.vpe,this.DashboardTypes=d.Z,this.applicationSelected=!0,this.territoriesSelected=!1,this.type.emit(d.Z.APPLICATIONS)}onClick(s){s===d.Z.APPLICATIONS?(this.applicationSelected=!0,this.territoriesSelected=!1):s===d.Z.TERRITORIES&&(this.territoriesSelected=!0,this.applicationSelected=!1),this.type.emit(s)}}return _.\u0275fac=function(s){return new(s||_)},_.\u0275cmp=t.Xpm({type:_,selectors:[["app-dashboard-buttons"]],outputs:{type:"type"},decls:7,vars:10,consts:[[1,"dashboard-buttons"],["type","button",3,"click"]],template:function(s,c){1&s&&(t.TgZ(0,"div",0)(1,"button",1),t.NdJ("click",function(){return c.onClick(c.DashboardTypes.APPLICATIONS)}),t._uU(2),t.ALo(3,"translate"),t.qZA(),t.TgZ(4,"button",1),t.NdJ("click",function(){return c.onClick(c.DashboardTypes.TERRITORIES)}),t._uU(5),t.ALo(6,"translate"),t.qZA()()),2&s&&(t.xp6(1),t.ekj("selected",c.applicationSelected),t.xp6(1),t.hij(" ",t.lcZ(3,6,"dashboardPage.applicationsTitle")," "),t.xp6(2),t.ekj("selected",c.territoriesSelected),t.xp6(1),t.hij(" ",t.lcZ(6,8,"dashboardPage.territoriesTitle")," "))},dependencies:[l.X$],styles:[".dashboard-buttons[_ngcontent-%COMP%]{display:flex;flex-wrap:wrap;flex-direction:row;align-items:center;justify-content:space-between;margin:80px 20px 0}.dashboard-buttons[_ngcontent-%COMP%]   .selected[_ngcontent-%COMP%]{color:#27187e;border-color:#27187e}.dashboard-buttons[_ngcontent-%COMP%]   button[_ngcontent-%COMP%]{font-weight:700;font-size:30px;color:#758bfd;background:white;border:none;border-bottom:3px solid #758BFD;padding-bottom:5px}.dashboard-buttons[_ngcontent-%COMP%]   button[_ngcontent-%COMP%]:hover{color:#27187e;border-color:#27187e}.dashboard-buttons[_ngcontent-%COMP%]   button[_ngcontent-%COMP%]:focus{color:#27187e;border-color:#27187e}"]}),_})()},8056:(C,g,o)=>{o.d(g,{W:()=>m});var t=o(2504),d=o(4755),l=o(5099),a=o(4333);function _(e,i){if(1&e&&(t.ynx(0),t.TgZ(1,"div",6),t._UZ(2,"img",7),t.qZA(),t.BQk()),2&e){const n=t.oxw().$implicit;t.xp6(2),t.Q6J("src",n.img,t.LSH)}}function p(e,i){1&e&&(t.TgZ(0,"div",6),t._UZ(1,"img",8),t.qZA())}function s(e,i){if(1&e){const n=t.EpF();t.TgZ(0,"div",2),t.NdJ("click",function(){const u=t.CHM(n).$implicit,P=t.oxw();return t.KtG(P.onCardClicked(u.id))}),t.YNc(1,_,3,1,"ng-container",3),t.YNc(2,p,2,0,"ng-template",null,4,t.W1O),t.TgZ(4,"div",5)(5,"label"),t._uU(6),t.ALo(7,"translate"),t.qZA(),t.TgZ(8,"label"),t._uU(9),t.ALo(10,"translate"),t.qZA()()()}if(2&e){const n=i.$implicit,r=t.MAs(3);t.xp6(1),t.Q6J("ngIf",n.img)("ngIfElse",r),t.xp6(5),t.lnq("",t.lcZ(7,7,"dashboardPage.name"),": ",n.title," ",n.name,""),t.xp6(3),t.AsE("",t.lcZ(10,9,"dashboardPage.id"),": ",n.id,"")}}const c=function(e,i,n){return{currentPage:e,itemsPerPage:i,totalItems:n,id:"pagination_dashboard"}};let m=(()=>{class e{constructor(){this.items=[],this.page=0,this.size=0,this.totalElements=0,this.id=new t.vpe}onCardClicked(n){this.id.emit(n)}}return e.\u0275fac=function(n){return new(n||e)},e.\u0275cmp=t.Xpm({type:e,selectors:[["app-dashboard-items"]],inputs:{items:"items",page:"page",size:"size",totalElements:"totalElements"},outputs:{id:"id"},decls:3,vars:8,consts:[[1,"cards-container"],["class","card",3,"click",4,"ngFor","ngForOf"],[1,"card",3,"click"],[4,"ngIf","ngIfElse"],["noimg",""],[1,"card-titles"],[1,"card-img"],[3,"src"],["src","assets/img/card-no-image.svg"]],template:function(n,r){1&n&&(t.TgZ(0,"div",0),t.YNc(1,s,11,11,"div",1),t.ALo(2,"paginate"),t.qZA()),2&n&&(t.xp6(1),t.Q6J("ngForOf",t.xi3(2,1,r.items,t.kEZ(4,c,r.page.toString(),r.size,r.totalElements))))},dependencies:[d.sg,d.O5,l.X$,a._s],styles:[".cards-container[_ngcontent-%COMP%]{display:flex;flex-wrap:wrap;justify-content:flex-start}.cards-container[_ngcontent-%COMP%]   .card[_ngcontent-%COMP%]{display:flex;width:21%;min-width:384px;max-width:-moz-fit-content;max-width:fit-content;align-items:center;margin:8px;color:#1a0e00;background:white;border:3px solid #27187e;border-radius:15px}.cards-container[_ngcontent-%COMP%]   .card[_ngcontent-%COMP%]:hover{border:3px solid #758BFD}.cards-container[_ngcontent-%COMP%]   .card[_ngcontent-%COMP%]:hover   .card-img[_ngcontent-%COMP%]   img[_ngcontent-%COMP%]{background-color:#758bfd;opacity:100%}.cards-container[_ngcontent-%COMP%]   .card-img[_ngcontent-%COMP%]{display:flex;justify-content:center;align-items:center;width:-moz-fit-content;width:fit-content;margin:8px;border-radius:10px}.cards-container[_ngcontent-%COMP%]   .card-img[_ngcontent-%COMP%]   img[_ngcontent-%COMP%]{width:96px;height:96px;border-radius:20px;opacity:50%}.cards-container[_ngcontent-%COMP%]   .card-titles[_ngcontent-%COMP%]{display:flex;flex-direction:column;margin:8px}.cards-container[_ngcontent-%COMP%]   .card-titles[_ngcontent-%COMP%]   label[_ngcontent-%COMP%]{margin:4px}"]}),e})()},57:(C,g,o)=>{o.d(g,{z:()=>a});var t=o(2504),d=o(4333),l=o(5099);let a=(()=>{class _{constructor(){this.page=new t.vpe}handlePageChange(s){this.page.emit(s)}}return _.\u0275fac=function(s){return new(s||_)},_.\u0275cmp=t.Xpm({type:_,selectors:[["app-dashboard-pagination"]],outputs:{page:"page"},decls:4,vars:6,consts:[[1,"dashboard-pagination"],["id","pagination_dashboard",3,"previousLabel","nextLabel","pageChange"]],template:function(s,c){1&s&&(t.TgZ(0,"div",0)(1,"pagination-controls",1),t.NdJ("pageChange",function(e){return c.handlePageChange(e)}),t.ALo(2,"translate"),t.ALo(3,"translate"),t.qZA()()),2&s&&(t.xp6(1),t.s9C("previousLabel",t.lcZ(2,2,"paginate.previous")),t.s9C("nextLabel",t.lcZ(3,4,"paginate.next")))},dependencies:[d.LS,l.X$],styles:[".ngx-pagination{display:flex;justify-content:center;align-items:center}  .ngx-pagination .current{background:#FF9300!important}"]}),_})()}}]);