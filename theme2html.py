#!/usr/bin/env python

class ThemePage(object):
    """docstring for ClassName"""
    def __init__(self):
        super(ThemePage, self).__init__()
        self.scopes = []
        self.sort_key = 'scope'

    def gen_header(self, line):
        pass
        
    def parse_file(self, file):
        lines = [line.strip() for line in open(file)];
        for line in lines:
            if line[0] == 'H':
                page.gen_header(line)
            if line[0] == 'M':
                page.gen_main(line)
            if line[0] == 'S':
                page.gen_scope(line)

    def gen_main(self, line):
        values = [x.lstrip() for x in line.split(',')]
        self.props = dict(zip(['bgcolor', 'fgcolor', 'caret', 'selection', 'invisibles', 'linehl'], values[1:])) 

    def gen_scope(self, line):
        values = [x.lstrip() for x in line.split(',')]
        scope = dict(zip(['name', 'bgcolor', 'fgcolor', 'style', 'scope'], values[1:]))
        self.scopes.append(scope)

    def scope_to_css(self, scope):
        # background-color:
        res = ""
        if scope['fgcolor'][0] == '#':
            # FIXME: transparency in scope['fgcolor'][7:9]
            res = "color:%s;" % (scope['fgcolor'][0:7])
        if scope['bgcolor'][0] == '#':
            # FIXME: transparency in scope['bgcolor'][7:9]
            res = res + "background-color:%s;" % (scope['bgcolor'][0:7])
        if res != "":
            return 'style ="%s"' % res
        else:
            return ''

    def render(self):
        self.preamble()
        
        print "<p>default</p>"
        
        for scope in self.scopes:
            print '<p %s>%s</p>' % (self.scope_to_css(scope), scope['scope'])
        
        self.postamble()
        
    def preamble(self):
        print '''
<!DOCTYPE html>
<html>
<style>
body {color:%s;}
</style>
<body style="background-color:%s;">
        ''' % (self.props['fgcolor'], self.props['bgcolor'])

    def postamble(self):
        print '''
</body>
</html>        
        '''
page = ThemePage()
page.parse_file('NorthernLights.tmcsv')
page.render()
