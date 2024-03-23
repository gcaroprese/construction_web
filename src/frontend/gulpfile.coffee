fs = require 'fs'
path = require 'path'
glob = require 'glob'
del = require 'del'
yargs = require 'yargs'
gulp = require 'gulp'
gutil = require 'gulp-util'
gulpif = require 'gulp-if'
plumber = require 'gulp-plumber'
size = require 'gulp-size'
rename = require 'gulp-rename'
tap = require 'gulp-tap'
changed = require 'gulp-changed'
concat = require 'gulp-concat'
lazypipe = require 'lazypipe'
runSequence = require 'run-sequence'
merge = require 'merge-stream'
transform = require 'vinyl-transform'
browserify = require 'browserify'
coffeeify = require 'coffeeify'
uglify = require 'gulp-uglify'
nunjucksify = require 'nunjucksify'
nunjucksRender = require 'gulp-nunjucks-render'
imagemin = require 'gulp-imagemin'
sprite = require('css-sprite').stream
stylus = require 'gulp-stylus'
koutoSwiss = require 'kouto-swiss'
iconfont = require 'gulp-iconfont'
bowerFiles = require 'main-bower-files'
browserSync = require 'browser-sync'

# -----------------------------------------------------------------------------

output = '../../static-compiled/'
bowerRoot = '../../'

isProduction = yargs.argv.production

imagePipe = lazypipe()
    .pipe -> gulpif isProduction, imagemin()
    .pipe gulp.dest, output + 'images/'

# -----------------------------------------------------------------------------

gulp.task 'scripts', ->
    browserifyLog = (file, msg, color='gray') ->
        gutil.log '[' + gutil.colors[color](path.basename file) + ']', msg

    browserified = transform (file) ->
        bundler = browserify
            extensions: ['.coffee']
            paths: ['scripts/']
            debug: not isProduction
            detectGlobals: false
            builtins: []

        bundler.add file
        bundler.transform coffeeify
        bundler.transform nunjucksify, extensions: ['.html']

        browserifyLog file, 'Creating bundle...'
        return bundler.bundle()
            .on 'end', -> browserifyLog file, 'Bundle created!'
            .on 'error', (e) ->
                browserifyLog file, e.message, 'red'
                @emit 'end'

    gulp.src ['./scripts/index.coffee', './scripts/admin.coffee']
        .pipe browserified
        .pipe rename extname: '.js'
        .pipe gulpif isProduction, uglify()
        .pipe gulp.dest output + 'scripts/'


gulp.task 'libs', (cb) ->
    gulp.src bowerFiles
            paths: bowerRoot
            filter: '**/*.js'
            checkExistence: true
        .pipe concat 'libs.js'
        .pipe gulpif isProduction, uglify()
        .pipe gulp.dest output + 'scripts/'


gulp.task 'styles', ->
    gulp.src 'styles/index.styl'
        .pipe plumber()
        .pipe tap (file) ->
            styleVarsJSON = JSON.parse fs.readFileSync 'styles/variables.json'
            styleVars = ''
            for key, value of styleVarsJSON
                styleVars += "$#{key} = #{value}\n"
            file.contents = Buffer.concat [new Buffer(styleVars), file.contents]
        .pipe stylus
            use: koutoSwiss()
            paths: [bowerRoot + 'bower_components/', 'tmp/']
            compress: isProduction
            sourcemap: do -> if not isProduction then inline: true
            'include css': true
        .pipe rename 'index.css'
        .pipe gulp.dest output + 'styles/'


gulp.task 'icons', ->
    gulp.src 'icons/*.svg'
        .pipe plumber()
        .pipe iconfont
            fontName: 'IconFont'
            appendCodepoints: false
            descent: 60
        .on 'codepoints', (codepoints, options) ->
            options.codepoints = codepoints
            iconsTemplate = 'styles/icons.styl.tpl'
            nunjucksRender.nunjucks.configure [iconsTemplate], watch: false
            gulp.src iconsTemplate
                .pipe nunjucksRender options
                .pipe rename 'icons.styl'
                .pipe gulp.dest 'tmp/'
        .pipe gulp.dest output + 'icons/'


gulp.task 'spritesheets', ->
    spritesheets = glob.sync 'spritesheets/*'
    merge spritesheets.map (spritesheet) ->
        name = path.basename spritesheet
        gulp.src "spritesheets/#{name}/*.{png,jpg}"
            .pipe plumber()
            .pipe rename prefix: "#{name}-"
            .pipe sprite
                name: "spritesheet-#{name}"
                prefix: "spritesheet-#{name}"
                style: "spritesheet-#{name}.styl"
                processor: 'stylus'
                cssPath: '../images'
                orientation: 'binary-tree'
                margin: 4
                retina: true
            .pipe gulpif '*.{png,jpg}', imagePipe(), gulp.dest 'tmp/'


gulp.task 'images', ->
    gulp.src 'images/**/*.{png,jpg}'
        .pipe plumber()
        .pipe gulpif not isProduction, changed output + 'images/'
        .pipe imagePipe()


gulp.task 'sizeReport', ->
    gulp.src output + '**'
        .pipe size showFiles: true, gzip: true


gulp.task 'clean', (cb) ->
    del [output + '*', 'tmp/'], force: true, cb


gulp.task 'build', (cb) ->
    runSequence \
        'clean',
        ['icons', 'spritesheets'],
        ['scripts', 'libs', 'styles', 'images'],
        'sizeReport',
        cb


gulp.task 'watchBuild', (cb) ->
    runSequence \
        ['icons', 'spritesheets'],
        ['scripts', 'libs', 'styles', 'images'],
        'browserSync',
        cb


gulp.task 'watch', ['watchBuild'], ->
    gulp.watch 'scripts/**/*.coffee', ['scripts', browserSync.reload]
    gulp.watch ['styles/**/*.{styl,json}', 'tmp/*.styl'], ['styles', browserSync.reload]
    gulp.watch 'images/**/*.{png,jpg}', ['images', browserSync.reload]
    gulp.watch ['icons/*.svg', 'styles/icons.styl.tpl'], ['icons']
    gulp.watch 'spritesheets/**', ['spritesheets']


gulp.task 'browserSync', ->
    bs = browserSync
        open: false
        notify: true
        online: false
        logSnippet: false
        logFileChanges: true
        ghostMode: false
