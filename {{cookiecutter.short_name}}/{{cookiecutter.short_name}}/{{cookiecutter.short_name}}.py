"""
TODO: Write a description of what this XBlock is
"""
import pkg_resources

from xblock.core import XBlock
from xblock.fields import Integer, Scope
from xblock.fragment import Fragment


def resource_string(path):
    """Handy helper for getting resources from our kit."""
    data = pkg_resources.resource_string(__name__, path)
    return data.decode("utf8")


# pylint: disable=too-many-ancestors
class {{cookiecutter.class_name}}(XBlock):
    """
    TODO: Document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TODO: delete count, and define your own fields.
    count = Integer(
        default=0, scope=Scope.user_state,
        help="A simple counter, to show something happening",
    )

    # TODO: change this view to display your data your own way.
    # pylint: disable=unused-argument
    def student_view(self, context=None):
        """
        The primary view of the {{cookiecutter.class_name}}, shown to students
        when viewing courses.
        """
        html = resource_string("public/{{cookiecutter.short_name|lower}}.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(resource_string("public/{{cookiecutter.short_name|lower}}.css"))
        frag.add_javascript(resource_string("public/{{cookiecutter.short_name|lower}}.js"))
        frag.initialize_js('{{cookiecutter.class_name}}')
        return frag
    # pylint: enable=unused-argument

    # TODO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    # pylint: disable=unused-argument
    @XBlock.json_handler
    def increment_count(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        assert data['hello'] == 'world'
        self.count += 1
        return {"count": self.count}
    # pylint: enable=unused-argument

    # TODO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("{{cookiecutter.class_name}}",
             """<{{cookiecutter.short_name|lower}}/>
             """),
            ("Multiple {{cookiecutter.class_name}}",
             """<vertical_demo>
                <{{cookiecutter.short_name|lower}}/>
                <{{cookiecutter.short_name|lower}}/>
                <{{cookiecutter.short_name|lower}}/>
                </vertical_demo>
             """),
        ]
# pylint: enable=too-many-ancestors
