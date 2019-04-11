document.getElementById("createAccount").onclick = function(){

var xhr = new XMLHttpRequest();

xhr.onreadystatechange = function () {
    if (this.readyState != 4) return;
    if (this.status == 200) {
	if(this.responseText.includes("User Created")){
		alert('Account Created! Please now log into your account')
		window.location.replace("/");
	}else{
		alert('Username already taken');
	};
    };
};


var username = document.getElementById("username").value;
var password = document.getElementById("password").value;
var confirmPassword = document.getElementById("confirmPassword").value;
var displayName = document.getElementById("displayName").value;

if(username == ""){
	alert('Enter a username');
}else if(displayName == ""){
	alert('Enter a display name')
}else if(password != confirmPassword){
	alert('Passwords do not match');
}else if(password == ""){
	alert('You need a password');
}else{
	xhr.open('GET', '/python/newAccount.py?username='+username+'&displayName='+displayName+'&password='+password, true);
	xhr.send(null);
}
};
