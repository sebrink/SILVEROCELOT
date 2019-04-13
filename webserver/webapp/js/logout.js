document.getElementById("logout").onclick = function(){

var xhr = new XMLHttpRequest();

xhr.onreadystatechange = function () {
    if (this.readyState != 4) return;
    if (this.status == 200) {
      	if(this.responseText.includes("invalid")){
          document.cookie = "session=; max-age=-9999; path=/;";
      		window.location.replace("/html/login.html");
      	}else{
      		// document.cookie = this.responseText.replace(/(\r\n|\n|\r)/gm, "");
          document.cookie = "session=; max-age=-9999; path=/;";
      		window.location.replace("/html/login.html");
      	};
    };
};



xhr.open('GET', '/python/logout.py', true);
xhr.send(null);

}
