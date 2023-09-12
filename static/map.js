$(document).ready(function () {
  

  // Coordinate of Makkah & Maddinah
  var MakkahCoordinate = {
    latitude: 21.423064802559917,
    longitude: 39.82498712936757,
  };
  var MadinahCoordinate = { latitude: 24.4672018, longitude: 39.6156392 };

  // Check the selected city
  var city = "{{ request.session.main_search_params.city}}";

  // Exract Selected City from Session
  var selectedCityCoordinate =
    city == "Makkah" ? MakkahCoordinate : MadinahCoordinate;


    
    // Initialize Map
    var map = L.map("map").setView(
    [selectedCityCoordinate.latitude, selectedCityCoordinate.longitude],
    8
  );

  L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 19,
    attribution:
      '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
  }).addTo(map);

  // Markers

  var hotels = [];
  $(".hotel-location-group").each(function () {
    hotels.push({
      name: $(this).find(".hotel-name").text(),
      slug: $(this).find(".hotel-slug").text(),
      hrm: $(this).find(".hotel-hrm").text(),
      long: $(this).find(".hotel-longitude").text(),
      lat: $(this).find(".hotel-latitude").text(),
    });
  });
  
  hotels.forEach((hotel) => {
    if (hotel.lat && hotel.long){
        var linkToHotel = `<a href="/hotels/hotel_detail/${hotel.slug}/"><b>${hotel.name}</b><br>يبعد ${hotel.hrm} كيلو.</a>`;
        var popup = L.popup().setContent(linkToHotel);
    L.marker([ hotel.lat,hotel.long]).bindPopup(popup).addTo(map).openPopup();}
  });

  console.log(hotels)

});
