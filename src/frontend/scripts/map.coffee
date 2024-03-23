{Map, Marker, LatLng, InfoWindow} = google.maps
geocoder = new google.maps.Geocoder

class MapView extends Backbone.Marionette.View
    ui:
        toggle: '#map-overlay'
        canvas: '#map-canvas'

    events:
        'click @ui.toggle': 'onToggleClick'

    initialize: ->
        @bindUIElements()
        @delegateEvents()

        @address = @options.address
        @infoWindow = @options.infoWindow
        @setCoordinates(@address)

        defaults = {zoom: 13, center: new LatLng 0, 0}
        config = _.extend {}, defaults, @options?.config
        @map = new Map @ui.canvas[0], config

    onToggleClick: (e) ->
        if @coordinates?
            return @showMap()
        return false

    onResize: ->
        google.maps.event.trigger @map, 'resize'

    setCenter: ->
        @map.setCenter @coordinates

    placeMarker: ->
        @marker = new Marker
            map: @map
            position: @coordinates
            title: @address
            description: @address

    placeInfoWindow: (marker) ->
        infoWindow = new InfoWindow content: @infoWindow

        infoWindow.open(@map, @marker)
        google.maps.event.addListener @marker, 'click', =>
            infoWindow.open(@map, @marker)

    showMap: ->
        @$el.addClass('map-active')
        @ui.canvas.fadeIn =>
            @setupMap()

    setupMap: ->
        @placeMarker()
        @placeInfoWindow()
        google.maps.event.trigger @map, 'resize'
        @setCenter()

    setCoordinates: ->
        geocoder.geocode address: @address, (results, status) =>
            if status == google.maps.GeocoderStatus.OK
                @coordinates = results[0].geometry.location
            return null


module.exports = MapView
