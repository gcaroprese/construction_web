{AdminProjectsGrid} = require 'projects'


$ ->

    if $('.grid-container #projects-grid').length
        grid = new AdminProjectsGrid
            el: '.grid-container #projects-grid'
            rows: 2
