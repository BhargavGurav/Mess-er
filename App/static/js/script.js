// const successfulLookup = position => {   
//   const { latitude, longitude } = position.coords;  
//   fetch(`https://api.opencagedata.com/geocode/v1/json?q=${latitude}+${longitude}&key=1234`)
//   .then(response = response.json())
//   .then(console.log);  }
//   Window.navigator.geolocation.getCurrentPosition(successfulLookup,    console.log); 
// if ("geolocation" in navigator) {
//     // Prompt user for permission to access their location
//     navigator.geolocation.getCurrentPosition(
//       // Success callback function
//       (position) => {
//         // Get the user's latitude and longitude coordinates
//         const lat = position.coords.latitude;
//         const lng = position.coords.longitude;
  
//         // Do something with the location data, e.g. display on a map
//         console.log(`Latitude: ${lat}, longitude: ${lng}`);
//       },
//       // Error callback function
//       (error) => {
//         // Handle errors, e.g. user denied location sharing permissions
//         console.error("Error getting user location:", error);
//       }
//     );
//   } else {
//     // Geolocation is not supported by the browser
//     console.error("Geolocation is not supported by this browser.");
//   }

// var long = "";
// var lati = "";
// function Location(){
//     if(navigator.geolocation){
//         navigator.geolocation.getCurrentPosition((position) => {
//            long = position.coords.longitude;
//            lati = position.coords.latitude; 
// console.log(`Longitude : ${long} Latitude : ${lati}`);

//         });
//     }
// }
// Location();