function volumecylinder() {
  var pi=3.14;
  var r=document.getElementById("radius").value;
  var h=document.getElementById("height").value;
  var volume=pi*r*h**2;
  var outbox=document.getElementById("outbox").value = volume;
}
function modifyDom() {
  var bait = "lol its actually this one";
  document.getElementById("changeText").innerHTML = bait;
}
function searchTeams(){
	var team=!!document.getElementById("teamSearch");
	if (team==false){
		alert("true")
	}
	
}