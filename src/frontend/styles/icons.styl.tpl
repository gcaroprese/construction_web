@font-face
    font-family: '{{ fontName }}'
    src: url('../icons/{{ fontName }}.eot')
    src: url('../icons/{{ fontName }}.eot?#iefix') format('eot'),
         url('../icons/{{ fontName }}.woff') format('woff'),
         url('../icons/{{ fontName }}.ttf') format('truetype'),
         url('../icons/{{ fontName }}.svg#{{ fontName }}') format('svg')
    font-weight: normal
    font-style: normal

.icon
    display: inline-block
    font-family: '{{ fontName }}'
    font-size: 1em
    font-style: normal
    font-weight: normal
    line-height: 1

.icon-lg
    font-size: 1.2em

.icon-fw
    width: 1.2857142857142858em
    text-align: center

{% for codepoint in codepoints %}
$icon-{{ codepoint.name }} = '\{{ codepoint.codepoint.toString(16).toUpperCase() }}'
.icon-{{ codepoint.name }}:before
    content: $icon-{{ codepoint.name }}
{% endfor %}
