construction_site_sample = window.construction_site_sample
{Slider, ProjectSlider} = require 'slider'
Map = require 'map'
{SiteProjectsGrid} = require 'projects'

#---------------------------------------------------------------------------------------------------
# Globals
#---------------------------------------------------------------------------------------------------
$ ->
    $('[data-target="blank"]').on 'click', (e) ->
        e.preventDefault()
        window.open $(e.target).attr('href')

#---------------------------------------------------------------------------------------------------
# Mobile
#---------------------------------------------------------------------------------------------------

$ ->
    $('[data-role="navigation-toggle"]').on 'click', (e) ->
        $('nav').toggleClass('opened')
        $('body').toggleClass('navigation-opened')


    $('[data-role="mobile-projects-pager"]').on 'click', (e) ->
        e.preventDefault()
        target = $(e.currentTarget)

        project_url_attr = 'data-next-project'
        if target.attr('[data-direction]') < 0
            project_url_attr = 'data-previous-project'

        location.href = $('#detail').attr(project_url_attr)

#---------------------------------------------------------------------------------------------------
# Sliders
#---------------------------------------------------------------------------------------------------
$ ->
    sliders = [
        selector: '[data-slider]'
        klass: Slider
    ]

    for config in sliders
        for element in $(config.selector)
            slider = config.klass
            slider(element)

#---------------------------------------------------------------------------------------------------
# Contact: Map
#---------------------------------------------------------------------------------------------------

address = 'Miguel de Azcuénaga 1496, Vicente López, Buenos Aires, Argentina'
infoWindow = '<div class="info-window">'
infoWindow += '<h1>Aulet Abiega | Arquitectos</h1>'
infoWindow += '<div>'
infoWindow += '<p>Azcuénaga 1496 4B - Vicente Lopez - CP 1638 - Buenos Aires - Argentina.</p>'
infoWindow += '<p>5411 6841.0445 - info@construction_site_sample.com</p>'
infoWindow += '</div>'
infoWindow += '</div>'

$ ->
    map_container = $('#contact #map-container')
    if map_container.length

        map_view = new Map
            el: map_container
            address: address,
            infoWindow: infoWindow


#---------------------------------------------------------------------------------------------------
# Projects: Grid
#---------------------------------------------------------------------------------------------------
$ ->

    project_grid = $('#projects #projects-grid')

    if project_grid.length
        isMac = navigator.platform.toLowerCase().indexOf('mac') >= 0
        hasTouch = ('ontouchstart' in window) or
            (window.DocumentTouch and document instanceof DocumentTouch)

        grid = project_grid.find('#grid')

        if hasTouch or isMac
            grid.css('overflow', 'auto')

        project_grid_view = new SiteProjectsGrid
            el: project_grid
            columns: 5
            rows: 2


#---------------------------------------------------------------------------------------------------
# Projects: Detail
#---------------------------------------------------------------------------------------------------
$ ->
    project_detail = $('#projects #detail')

    toggle_badge = (badge) ->
        badge.toggleClass('closed')

    if project_detail.length

        badge = project_detail.find('.badge')

        badge.on 'click', (event) ->
            event.stopPropagation()
            event.preventDefault()

            if badge.is('.closed')
                return toggle_badge(badge)

        badge.find('.toggle').on 'click', (event) ->
            event.stopPropagation()
            event.preventDefault()

            toggle_badge(badge)

        initial_slide = 'first'
        if (window.location.hash.replace('#', '') == 'last')
            initial_slide = 'last'

        project_slider = ProjectSlider(project_detail.find('.slider'), initial_slide)

#---------------------------------------------------------------------------------------------------
# Landing: Redirect
#---------------------------------------------------------------------------------------------------
$ ->
    $('#landing').on 'click', (event) ->
        location.href = construction_site_sample.home
        event.preventDefault()

