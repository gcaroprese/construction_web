



class AdminProjectsGrid extends Backbone.Marionette.View
    ui:
        projects: '.project'
        size: "[name='project-size']"
        badge: "[name='project-badge-position']"

    events:
        'change @ui.size': 'onSizeChange'
        'change @ui.badge': 'onBadgeChange'

    initialize: ->
        _.bindAll @, 'generate', 'resizeProject', 'commit', 'onPositionChange', 'onSizeChange'

        @bindUIElements()
        @delegateEvents()

        defaults =
            rows: 2
            onChange: @onPositionChange

        @settings = _.extend {}, defaults, @options?.rows

        @fields =
            badge:
                position: '.field-grid_badge_position select'
            size:
                w: '.field-grid_w input'
                h: '.field-grid_h input'
            position:
                x: '.field-grid_x input'
                y: '.field-grid_y input'

        @generate()

    generate: ->
        @$el.gridList(@settings)

    commit: (projectID, property, values) ->
        row = $(".action-checkbox .action-select[value=#{projectID}]").closest('.grp-row')
        for attr, field of @fields[property]
            value = values[attr]
            row.find(field).val(value)

    resizeProject: (projectID, size) ->
        project = @ui.projects.filter("[data-id=#{projectID}]").first()

        for attr, value of size
            data = "data-#{attr}"
            project.attr data, value

        # TODO: Try to extend GridList to handle Width & Height resizing
        # @$el.gridList('resizeItem', project, size)

    getProjectID: (element) ->
        return element.closest('.project').attr('data-id')

    onPositionChange: (items) ->
        for item in items
            position =
                x: item.x
                y: item.y

            @commit(item.id, 'position', position)

    onSizeChange: (e) ->
        input = $(e.target)
        projectID = @getProjectID(input)

        size =
            w: input.find('option:selected').attr("data-w")
            h: input.find('option:selected').attr("data-h")

        @commit(projectID, 'size', size)
        @resizeProject(projectID, size)

    onBadgeChange: (e) ->
        input = $(e.target)
        projectID = @getProjectID(input)
        values =
            position: input.val()

        @commit(projectID, 'badge', values)


#---------------------------------------------------------------------------------------------------
# Views: Site
#---------------------------------------------------------------------------------------------------

class SiteProjectsGrid extends Backbone.Marionette.View

    ui:
        grid: '#grid'
        projects: '#grid .project'
        pager: '.pager a'

    events:
        'click @ui.pager': 'onPagerClick'

    initialize: ->
        _.bindAll @, 'generate', 'onMouseWheel','move'

        @bindUIElements()
        @delegateEvents()

        @isMoving = false
        @animationTime = 300

        @settings =
            columns: @options.columns or 4
            rows: @options.rows or 2

        @columns = @calculateColumns() - @settings.columns
        @generate()

        @move = _.debounce @move, (40), true

        $(window).on 'resize',
            _.throttle @generate, @animationTime, true

        $(document.documentElement).keyup (event) =>
            if event.keyCode == 37
                @move(-1)
            else if event.keyCode == 39
                @move(1)

        @ui.grid.on 'mousewheel',
            @onMouseWheel

    generate: ->
        for project in @ui.projects
            @positionProject $(project)

    calculateCellSize: ->
        return [
            @$el.width() * (1 / @settings.columns),
            @$el.height() * (1 / @settings.rows)
        ]

    calculateColumns: ->
        dimensions = _.map @ui.projects, (project) =>
            data = @getProjectData $(project)
            return parseInt(data.x) + parseInt(data.w)
        return _.max(dimensions)

    calculateCurrentColumn: ->
        cellWidth = parseFloat(@calculateCellSize()[0])
        return Math.ceil @ui.grid.scrollLeft() / cellWidth

    onPagerClick: (event) ->
        event.preventDefault()
        event.stopPropagation()

        direction = $(event.currentTarget).attr('data-direction')
        @move(direction)

    onMouseWheel: (event) ->

        getDeltaKey = (delta) ->
            if Math.abs(delta.x) > Math.abs(delta.y)
                return 'x'
            return 'y'

        delta =
            x: event.deltaX
            y: event.deltaY
        deltaKey = getDeltaKey(delta)

        if deltaKey == 'y'
            event.preventDefault()
            event.stopPropagation()

            direction = (delta.y / Math.abs(delta.y)) * -1
            @move(direction)

    move: (direction) ->
        column = @calculateCurrentColumn() + parseInt(direction)

        if not (0 <= column <= @columns)
            return

        # Don't make it infinite
        # if column < 0
        #     column = @columns # Last
        # else if column > @columns
        #     column = 0 # First

        offset = (column * @calculateCellSize()[0])
        @ui.grid
            .animate {scrollLeft: offset}, @animationTime

    getProjectData: (project) ->
        return {} =
            w: project.attr('data-w')
            h: project.attr('data-h')
            x: project.attr('data-x')
            y: project.attr('data-y')

    positionProject: (project) ->
        cellSize = @calculateCellSize()
        projectData = @getProjectData(project)

        position =
            width: projectData.w * cellSize[0]
            height: projectData.h * cellSize[1]
            left: projectData.x * cellSize[0]
            top: projectData.y * cellSize[1]

        project.css(position)


#---------------------------------------------------------------------------------------------------
# Exports
#---------------------------------------------------------------------------------------------------
module.exports =
    SiteProjectsGrid: SiteProjectsGrid
    AdminProjectsGrid: AdminProjectsGrid
