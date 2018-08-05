import re
from django import template
from django.templatetags.static import static

register = template.Library()
staticPath = static('')

bbdata = {
    # (r'\[url\](.+?)\[/url\]', r'<a href="\1">\1</a>'),
    # (r'\[url=(.+?)\](.+?)\[/url\]', r'<a href="\1">\2</a>'),
    # (r'\[email\](.+?)\[/email\]', r'<a href="mailto:\1">\1</a>'),
    # (r'\[email=(.+?)\](.+?)\[/email\]', r'<a href="mailto:\1">\2</a>'),
    r'\[img\](.+?)\[/img\]': r'<img src="' + staticPath + r'\1">',
    r'\[img=(.+?)\](.+?)\[/img\]': r'<img src="' + staticPath + r'\1" alt="\2">',
    r'\[img w=(.+?)\ h=(.+?)](.+?)\[/img\]': r'<img src="' + staticPath + r'\3" weight="\1" height="\2">',
    r'\[spoil=(.+?)\](.+?)\[/spoil\]': r"""
            <div class="panel panel-default">
                <div class="panel-heading">
                  <h4 class="panel-title">
                    <a data-toggle="collapse" href="#\1Collapsable">
                        \1
                    </a>
                  </h4>
                </div>
                <div id="\1Collapsable" class="panel-collapse collapse in">
                  <div class="panel-body">
                      \2
                  </div>
                </div>
            </div>
        """,
    r'\[scratchBlocks\](.+?)\[/scratchBlocks\]': r"""
            <pre class="blocks">
                \1
            </pre>
        """,
    r'\[scratchBlock\](.+?)\[/scratchBlock\]': r"""
                <code class="blocksInline">\1</code>
        """,
    r'\[/scratchProject=(.+?)\]': r"""
                  <iframe allowtransparency="true" width="485" height="402" src="//scratch.mit.edu/projects/embed/\1/?autostart=false" frameborder="0" allowfullscreen>
                  </iframe>

        """,
    r'\[b\](.+?)\[/b\]': r'<b>\1</b>',
    r'\[i\](.+?)\[/i\]': r'<i>\1</i>',
    r'\[u\](.+?)\[/u\]': r'<u>\1</u>',
    # (r'\[quote\](.+?)\[/quote\]', r'<div style="margin-left: 1cm">\1</div>'),
    # (r'\[center\](.+?)\[/center\]', r'<div align="center">\1</div>'),
    # (r'\[code\](.+?)\[/code\]', r'<tt>\1</tt>'),
    # (r'\[big\](.+?)\[/big\]', r'<big>\1</big>'),
    # (r'\[small\](.+?)\[/small\]', r'<small>\1</small>'),
}

def word_replace(replace_dict, s):
    for key, val in replace_dict.items():
        s = s.replace(key, val)
    return s

@register.filter
def scratchBlocks(value):
     return replaceBBCodeContent(value, r'\[scratchBlocks\](.+?)\[/scratchBlocks\]')

@register.filter
def scratchBlock(value):
     return replaceBBCodeContent(value, r'\[scratchBlock\](.+?)\[/scratchBlock\]')


@register.filter
def scratchOnlineProject(value):
    return replaceBBCodeContent(value, r'\[/scratchProject=(.+?)\]')


def replaceBBCodeContent(value, bbdataKey):
    originalString = bbdata[bbdataKey]
    value = originalString.replace(r"\1", str(value))
    return value

@register.filter
def onlineProjectLink(value):
    return "https://scratch.mit.edu/projects/"+str(value)+"/#editor"

@register.filter
def replaceBBCode(value):

    for key, val in bbdata.items():
        p = re.compile(key, re.DOTALL)
        value = p.sub(val, value)

    return value

@register.filter
def createScratchWikiLink(value):
    preUrl = "https://fr.scratch-wiki.info/wiki/"
    postUrl = "_(bloc)"
    toReplace = {" ": "_", "[": "(", "]": ")"}
    value = word_replace(toReplace, value)
    return preUrl+value+postUrl

@register.filter
# Pas réussi à faire fonctionner correctement :(
def createBlocksTable(blocks):
    res = ""

    pre = """
    <table class="table table-bordered">
        <thead>
        <tr>
            <th scope="col">Bloc</th>
            <th scope="col">Description</th>
            <th scope="col">Doc</th>
        </tr>
        </thead>
        <tbody>
    """
    res += pre

    content = r"""
    <tr>
        <td>[blockJson]</td>
        <td>[blockDesc]</td>
        <td align="center">
            <a href="[blockWikiLink]" target="_blank">
              <span class="glyphicon glyphicon-link"></span>
            </a>
        </td>
    </tr>
    """
    print(blocks)
    for block in blocks:
        subDict = {
            "[blockJson]" : scratchBlock(block.blockJson),
            "[blockDesc]" : block.blockDescription,
            "[blockWikiLink]" : createScratchWikiLink(block.blockJson)
        }
        res += word_replace(subDict, content)

    post = """
        </tbody>
    </table>
    """
    res += post

    return res

