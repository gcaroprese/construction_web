configuration =
    defaults:
        slide: '.slide'
        autoplay: true
        autoplaySpeed: 2000
        accessibility: true
        slidesToShow: 1
        slidesToScroll: 1
        draggable: false
        speed: 300
        dots: false
        arrows: false

    dots:
        dots: true
        customPaging: (slider, i) ->
            return "<button type='button' data-role='none'><span>#{(i + 1)}</span></button>"

    arrows:
        arrows: true

    project:
        infinite: false
        arrows: false
        autoplay: false

Slider = (elem) ->
    element = $(elem)
    type = element.attr('data-slider-type')
    settings = _.extend {}, configuration.defaults, configuration[type]
    return element.slick(settings)


ProjectSlider = (elem, initial) ->
    settings = _.extend {}, configuration.defaults, configuration['project']
    slider = $(elem).slick(settings)

    slick = slider.getSlick()
    num_slides = slick.slideCount

    if initial == 'last'
        slick.changeSlide data: {message: 'index', index: (num_slides - 1)}, true

    slider.find('button').on 'click', ->
        button = $(@)
        current_slide = slick.currentSlide

        direction = button.attr('data-direction')
        if direction == 'next'
            if (current_slide + 1) == num_slides
                button.prop disabled: true
                location.href = slider.closest('#detail').attr('data-next-project')
            else
                slick.changeSlide data: {message: 'next'}
        if direction == 'previous'
            if (current_slide - 1) < 0
                button.prop disabled: true
                location.href = slider.closest('#detail').attr('data-previous-project') + '#last'
            else
                slick.changeSlide data: {message: 'previous'}
        return false

    # Left/Right arrow keys trigger button navigation
    $(document.documentElement).keyup (event) =>
        if event.keyCode == 37
            slider.find('[data-direction="previous"]').trigger('click')
        else if event.keyCode == 39
            slider.find('[data-direction="next"]').trigger('click')

    return slider


module.exports =
    Slider: Slider
    ProjectSlider: ProjectSlider
