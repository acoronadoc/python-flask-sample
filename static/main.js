var partHeaders={
		'Accept': 'application/json',
		'Content-Type': 'application/json'
		};
		
function init() {
	execute( "/list_images", "GET", {}, renderList );
	}

function analyse(uuid) {
	execute( "/analyse_image/"+uuid, "GET", {}, renderAnalyse );
	}
	
function renderList( data ) {
	var s="<tr><th>Image Id</th><th>Image name</th><th>Options</th></tr>";
	
	for ( var i=0; i<data.length; i++ ) 
		s+="<tr><td>"+data[i].id+"</td><td>"+data[i].name+"</td><td><button onclick=\"javascript: analyse('"+data[i].id+"');\">Analyse</button></td></tr>";
		
	document.getElementById("list").innerHTML=s;
	}

function renderAnalyse( data ) {
	var s="";
		
	s+="<p><strong>Name: </strong>"+data.name+"</p>";
	s+="<p><strong>Width: </strong>"+data.width+"</p>";
	s+="<p><strong>Height: </strong>"+data.height+"</p>";
	
	document.getElementById("infodata").innerHTML=s;
	}
	
function execute( url, method, reg, onSuccess ) {
	var post=JSON.stringify(reg);
	
	params={
		  method: method, 
		  headers: partHeaders,		  
		}
		
	if ( method=="POST" || method=="PUT" ) params.body=post;

	fetch( url, params ).then(function(response) {
			response.json().then(function(p) {
				onSuccess( p );
	        	});
	    });		
	}
