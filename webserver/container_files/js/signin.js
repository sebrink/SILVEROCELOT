document.getElementById("signin").onclick = function(){

var xhr = new XMLHttpRequest();

xhr.onreadystatechange = function () {
    if (this.readyState != 4) return;
    if (this.status == 200) {
	if(this.responseText.includes("Failed")){
		alert('Incorrect username and password combination')
		window.location.replace("/html/login.html");
	}else{
		window.location.replace("/python/index.py");
	};
    };
};


var username = document.getElementById("username").value;
var password = document.getElementById("password").value;

if(username == ""){
	alert('Enter a username');
}else if(password == ""){
	alert('Enter a password');
}else{
	xhr.open('GET', '/python/signin.py?username='+username+'&password='+password, true);
	xhr.send(null);
}
};
