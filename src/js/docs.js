window.onload = init;
const main = document.getElementsByTagName("main")[0];
main.addEventListener("scroll",scroll);
let elems = [];

function init(){
  const root = document.getElementsByTagName("nav")[0];
  for (child of main.children) {
    if(child.tagName === "H2" || child.tagName === "H3") {
      let clone = child.cloneNode(true);
      elems.push([child,clone])
      root.appendChild(clone);
    }
  }
  elems.map(x=>x[1].addEventListener("click", _=>main.scrollTop=x[0].offsetTop-100));

  // Magic formatting
  for (list of document.getElementsByTagName("CMDS")) formatCmdList(list);
}
function formatCmdList(list) {
  const children = [];
  for (child of list.children) children.push(child.cloneNode(true));
  list.innerHTML = "";
  for (child of children) {
    let container = document.createElement("div");
    let img = document.createElement("div")
    if (child.tagName === "C") {
      container.className = "speech-bubble";
      img.className = "acc-img";
      container.appendChild(img);
      container.appendChild(child);
    }
    else {
      container.className = "speech-bubble response";
      img.className = "hp-img";
      container.appendChild(child);
      container.appendChild(img);
    }
    list.appendChild(container);
  }


}
function backActivate(elems, i) {
  while (i>=0) {
    if (elems[i][1].tagName === "H2") {
      elems[i][1].classList.add("active");
      break;
    }
    i--;
  }
}
function scroll(){
  let delta = elems.map(x=>x[0].offsetTop-main.scrollTop);
  let i = 0;
  elems.map(x=>x[1].classList.remove("active"));
  while (i < elems.length) {
    if (delta[i] >= 0){
      elems[i][1].classList.add("active");
      if (elems[i][1].tagName === "H3") backActivate(elems,i-1);
      break;
    }
    i++;
  }
}
