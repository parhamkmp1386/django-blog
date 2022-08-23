function GetURL(){
	 var MyURL = document.URL;
	 var Lnk1 = document.querySelector('.link1');
	 var Lnk2 = document.querySelector('.link2');
	 var Lnk3 = document.querySelector('.link3');
	 if(MyURL == Lnk1)
	 {
	 	Lnk1.classList.add('active')
	 }

	 if(MyURL == Lnk2)
	 {
	 	Lnk2.classList.add('active')
	 }

	 if(MyURL == Lnk3)
	 {
	 	Lnk3.classList.add('active')
	 }
}

GetURL();

// ---------------------------------------------------------------------------------------------------------------------------

var CheckConnectionStatusBtn = document.querySelector('.check-connection-btn');
var ShowConnectionStatus = document.querySelector('.show-connection-status');
var ShowConnectionStatusText = document.querySelector('.show-connection-status h3');
var ShowConnectionStatusHideBtn = document.querySelector('.hide-btn');
var ShowConnectionStatusShowBtn = document.querySelector('.show-btn');
function CheckConnection(){
	if(navigator.onLine){
		ShowConnectionStatus.style.transition = '.5s';
		ShowConnectionStatus.style.backgroundColor = '#66FF00';
		ShowConnectionStatusText.innerText = 'You Connected to internet !';

	} 
	
	else{
		ShowConnectionStatus.style.transition = '.5s';
		ShowConnectionStatus.style.backgroundColor = '#fd5c63';
		ShowConnectionStatusText.innerText = 'You not connected to internet !';
	}


}
CheckConnectionStatusBtn.addEventListener('click', ()=>{
	CheckConnection();		
});

ShowConnectionStatusHideBtn.addEventListener('click', ()=>{
	ShowConnectionStatus.style.display = 'none';
	ShowConnectionStatusShowBtn.style.display = '';
	ShowConnectionStatusShowBtn.style.padding = '0px';
});

ShowConnectionStatusShowBtn.addEventListener('click', ()=>{
	ShowConnectionStatusShowBtn.style.display = 'none';
	ShowConnectionStatus.style.display = '';
	ShowConnectionStatus.style.transition = '.5s';
	ShowConnectionStatus.style.backgroundColor = 'yellow';
	ShowConnectionStatusText.innerText = 'click button for update connection status !';
});




// ---------------------------------------------------------
// const Seuucess_Close = document.querySelector('.Success_close');
// Success_close.addEventListener('click', ()=>{
// 	this.class
// });