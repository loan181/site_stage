import re
from django import template
from django.templatetags.static import static

register = template.Library()
staticPath = static('')

# All BB data string regex
class BbRegex :
    bold = r'\[b\](.+?)\[/b\]'
    italic = r'\[i\](.+?)\[/i\]'
    underline = r'\[u\](.+?)\[/u\]'
    img = r'\[img\](.+?)\[/img\]'
    imgAlt = r'\[img=(.+?)\](.+?)\[/img\]'
    imgSize = r'\[img w=(.+?)\ h=(.+?)](.+?)\[/img\]'
    spoil = r'\[spoil title=(.+?) id=(.+?)\](.+?)\[/spoil\]'
    scratchBlock = r'\[scratchBlock\](.+?)\[/scratchBlock\]'
    scratchBlocks = r'\[scratchBlocks\](.+?)\[/scratchBlocks\]'
    scratchProject = r'\[/scratchProject=(.+?)\]'


bbdata = {
    # (r'\[url\](.+?)\[/url\]', r'<a href="\1">\1</a>'),
    # (r'\[url=(.+?)\](.+?)\[/url\]', r'<a href="\1">\2</a>'),
    # (r'\[email\](.+?)\[/email\]', r'<a href="mailto:\1">\1</a>'),
    # (r'\[email=(.+?)\](.+?)\[/email\]', r'<a href="mailto:\1">\2</a>'),
    BbRegex.img: r'<img src="' + staticPath + r'img/' + r'\1">',
    BbRegex.imgAlt: r'<img src="' + staticPath + r'img/' + r'\1" alt="\2">',
    BbRegex.imgSize: r'<img src="' + staticPath + r'img/' + r'\3" weight="\1" height="\2">',
    BbRegex.spoil: r"""
            <div class="card">
                <div class="card-header" data-toggle="collapse" data-target="#\2Collapsable">
                  <h5 class="mb-0">
                    <button class="btn btn-link" type="button">
                        \1
                    </button>
                  </h5>
                </div>
                <div id="\2Collapsable" class="collapse">
                  <div class="card-body">
                      \3
                  </div>
                </div>
            </div>
        """,
    BbRegex.scratchBlocks: r"""
            <pre class="blocks">
                \1
            </pre>
        """,
    BbRegex.scratchBlock: r'<code class="blocksInline">\1</code>',
    BbRegex.scratchProject: r"""
        <div class="embed-responsive embed-responsive-4by3">
            <iframe allowtransparency="true" src="//scratch.mit.edu/projects/embed/\1/?autostart=false" frameborder="0" allowfullscreen>
            </iframe>
        </div>
        """,
    BbRegex.bold: r'<b>\1</b>',
    BbRegex.italic: r'<i>\1</i>',
    BbRegex.underline: r'<u>\1</u>',
    # (r'\[quote\](.+?)\[/quote\]', r'<div style="margin-left: 1cm">\1</div>'),
    # (r'\[center\](.+?)\[/center\]', r'<div align="center">\1</div>'),
    # (r'\[code\](.+?)\[/code\]', r'<tt>\1</tt>'),
    # (r'\[big\](.+?)\[/big\]', r'<big>\1</big>'),
    # (r'\[small\](.+?)\[/small\]', r'<small>\1</small>'),
}


@register.filter
def addStr(arg1, arg2):
    """concatenate arg1 & arg2"""
    return str(arg1) + str(arg2)


@register.filter
def orderQueryBy(value, orderByStr):
    return value.order_by(orderByStr)




def word_replace(replace_dict, s):
    for key, val in replace_dict.items():
        s = s.replace(key, val)
    return s


def indexReplace(BbRegexData, datas):
    ret = BbRegexData
    for i in range(len(datas)):
        ret = ret.replace('\\'+str(i+1), str(datas[i]))
    return ret


@register.filter
def replaceBBCode(value):
    for key, val in bbdata.items():
        p = re.compile(key, re.DOTALL)
        value = p.sub(val, value)
    return value




@register.filter
def scratchBlocks(value):
    return indexReplace(bbdata[BbRegex.scratchBlocks], (value,))


@register.filter
def scratchBlock(value):
    return indexReplace(bbdata[BbRegex.scratchBlock], (value,))


@register.filter
def scratchOnlineProject(value):
    return indexReplace(bbdata[BbRegex.scratchProject], (value,))


@register.simple_tag
def spoil(title, content, visible=True, idTitle=None):
    modSpoil = bbdata[BbRegex.spoil]
    # TODO correct here for fit for bootstrap 4.1.x
    if not visible:
        modSpoil = modSpoil.replace(
            'class="panel-collapse collapse in"',
            'class="panel-collapse collapse"'
        )
    # Generate an id title for the spoiler automatically if not provided using the title
    if idTitle is None:
        idTitle = title
    idTitle = word_replace({" ": "_"}, idTitle)
    return indexReplace(modSpoil, (title, idTitle, content))

@register.simple_tag
def scratchOfflineProject(filePath, showEditor=False):
    ret = ""
    generatedID = "scratch-flash-"+filePath.replace("/", "-")
    scratchPath = staticPath+"scratch/Scratch.swf"
    ret += '<embed id={} class="embed-responsive embed-responsive-4by3" src="{}" data-sbFile={} data-editMode={}>'.format(generatedID, scratchPath, filePath, showEditor)
    return ret

@register.filter
def onlineProjectLink(value):
    return "https://scratch.mit.edu/projects/"+str(value)+"/#editor"


@register.filter
def createScratchWikiLink(value):
    preUrl = "https://fr.scratch-wiki.info/wiki/"
    postUrl = "_(bloc)"
    toReplace = {" ": "_", "[": "(", "]": ")"}
    value = word_replace(toReplace, value)
    return preUrl+value+postUrl


@register.filter
def createBlocksTable(blocks):
    res = ""

    pre = '\
    <table class="table table-bordered">\
        <thead>\
        <tr>\
            <th scope="col">Bloc</th>\
            <th scope="col">Description</th>\
            <th scope="col">Doc</th>\
        </tr>\
        </thead>\
        <tbody>\
     '
    res += pre

    content = '\
    <tr>\
        <td>[blockJson]</td>\
        <td>[blockDesc]</td>\
        <td align="center">\
            <a href="[blockWikiLink]" target="_blank">\
              [LIEN]🔗\
            </a>\
        </td>\
    </tr>\
    '
    for block in blocks:
        # TODO : issues in domr blocksJson using line breaks (use blocks istead of inline notation ?)
        subDict = {
            "[blockJson]" : scratchBlock(block.blockJson),
            "[blockDesc]" : block.blockDescription,
            "[blockWikiLink]" : createScratchWikiLink(block.blockJson)
        }

        res += word_replace(subDict, content)

    post = '\
        </tbody>\
    </table>\
    '
    res += post
    return res

