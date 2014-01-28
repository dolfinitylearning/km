#from imp import reload
import sys
# setdefaultencoding is removed during Python start. Get it back.
# See http://stackoverflow.com/questions/2276200/changing-default-encoding-of-python
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('utf-8')
# import codecs

from docutils import nodes, core, io
from docutils.parsers.rst import Directive, directives
from docutils.parsers.rst.roles import set_classes
from docutils.utils.code_analyzer import Lexer, LexerError, NumberLines

class Authornote(Directive):
    """
    Render author notes.
    """
    has_content = True
    required_arguments = 1
    final_argument_whitespace = True
    node_class = nodes.decoration
    def run(self):
        # Raise an error if the directive does not have contents.
        #self.assert_has_content()
        text = '\n'.join(self.content)
        # Make a node with the content
        content_node = self.node_class(rawsource=text)
        # Parse the directive contents into the new node.
        self.state.nested_parse(
            self.content,
            self.content_offset,
            content_node
        )
        # Create a new node with the prefix marker text for
        # Drupal custom filter to find.
        # Can apply permissions checks and other things on the
        # server side.
        prefix_text = '[[[cycoauthornote ' + self.arguments[0] + '|||\n'
        prefix_node = nodes.raw('', prefix_text, format='html')
        # Create a new node with the postfix marker text for
        # Cyco to find.
        postfix_text = ']]]\n'
        postfix_node = nodes.raw('', postfix_text, format='html')
        # Return the nodes in sequence.
        return [prefix_node, content_node, postfix_node]




class Exercise(Directive):
    """
    reStructuredText directive to show code listings with google-code-prettify
    """
    has_content = False
    required_arguments = 1

    def run(self):
        # Put in pattern that is replaced in Drupal by a custom filter.
        # Can apply permissions checks and other things on the
        # server side.
        result = '[[[cycoexercise ' + self.arguments[0] + ']]]\n'
        raw_node = nodes.raw('', result, format='html')
        return [raw_node]


class Pseudent(Directive):
    has_content = True
    required_arguments = 1
    #
    node_class = nodes.decoration

    def run(self):
        # Raise an error if the directive does not have contents.
        #self.assert_has_content()
        text = '\n'.join(self.content)
        # Make a node with the content
        content_node = self.node_class(rawsource=text)
        # Parse the directive contents into the new node.
        self.state.nested_parse(
            self.content,
            self.content_offset,
            content_node
        )
        # Create a new node with the prefix marker text for
        # Drupal custom filter to find.
        # Can apply permissions checks and other things on the
        # server side.
        prefix_text = '[[[cycopseudent ' + self.arguments[0] + '|||\n'
        prefix_node = nodes.raw('', prefix_text, format='html')
        # Create a new node with the postfix marker text for
        # Cyco to find.
        postfix_text = ']]]\n'
        postfix_node = nodes.raw('', postfix_text, format='html')
        # Return the nodes in sequence.
        return [prefix_node, content_node, postfix_node]

#Register the new directives.
directives.register_directive('exercise', Exercise)
directives.register_directive('pseudent', Pseudent)
directives.register_directive('authornote', Authornote)


##Create a new directive
#class Swear(Directive):
#
#    has_content = True
#
#    def run(self):
#        self.assert_has_content()
#        if cyco_user.can_swear:
#            target = ''.join(self.content.data)
#            text = '<p>FUCK ' + target.upper() + '</p>'
#        else:
#            text = '<p>You are not allowed to swear, fuckhead.</p>'
#        return [nodes.raw('', text, format='html')]
#
##Register the new directive.
#directives.register_directive('swear', Swear)

#Read the content to translate.
testing = False
if testing:
    f = open('in3.txt')
    content = f.readlines()
    f.close()
    data_in = ''.join(content)
else:
    # in_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
    # in_stream = codecs.getreader("utf-8")(sys.stdin)
    data_in = ''
    for line in sys.stdin:
#    for line in_stream:
        data_in += line

#Parse some content.
#thing = core.publish_parts(data_in, writer_name='html')
doc = core.publish_parts(data_in, writer_name='html')['html_body']
#out_stream = codecs.getwriter("utf-8")(sys.stdout)
print (doc)
