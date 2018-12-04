window.onload = init;

function init(){
  const root = document.getElementsByTagName("nav")[0];
  const main = document.getElementsByTagName("main")[0];
  for (child of main.children) {
    if(child.tagName === "H2" || child.tagName === "H3")
      root.appendChild(child.cloneNode(true));
  }
}
