"""
This type stub file was generated by pyright.
"""

from traitlets.config.configurable import Configurable
from traitlets import Integer

"""
Prefiltering components.

Prefilters transform user input before it is exec'd by Python.  These
transforms are used to implement additional syntax such as !ls and %magic.
"""
class PrefilterError(Exception):
    ...


re_fun_name = ...
re_exclude_auto = ...
def is_shadowed(identifier, ip):
    """Is the given identifier defined in one of the namespaces which shadow
    the alias and magic namespaces?  Note that an identifier is different
    than ifun, because it can not contain a '.' character."""
    ...

class PrefilterManager(Configurable):
    """Main prefilter component.

    The IPython prefilter is run on all user input before it is run.  The
    prefilter consumes lines of input and produces transformed lines of
    input.

    The implementation consists of two phases:

    1. Transformers
    2. Checkers and handlers

    Over time, we plan on deprecating the checkers and handlers and doing
    everything in the transformers.

    The transformers are instances of :class:`PrefilterTransformer` and have
    a single method :meth:`transform` that takes a line and returns a
    transformed line.  The transformation can be accomplished using any
    tool, but our current ones use regular expressions for speed.

    After all the transformers have been run, the line is fed to the checkers,
    which are instances of :class:`PrefilterChecker`.  The line is passed to
    the :meth:`check` method, which either returns `None` or a
    :class:`PrefilterHandler` instance.  If `None` is returned, the other
    checkers are tried.  If an :class:`PrefilterHandler` instance is returned,
    the line is passed to the :meth:`handle` method of the returned
    handler and no further checkers are tried.

    Both transformers and checkers have a `priority` attribute, that determines
    the order in which they are called.  Smaller priorities are tried first.

    Both transformers and checkers also have `enabled` attribute, which is
    a boolean that determines if the instance is used.

    Users or developers can change the priority or enabled attribute of
    transformers or checkers, but they must call the :meth:`sort_checkers`
    or :meth:`sort_transformers` method after changing the priority.
    """
    multi_line_specials = ...
    shell = ...
    def __init__(self, shell=..., **kwargs) -> None:
        ...
    
    def sort_transformers(self): # -> None:
        """Sort the transformers by priority.

        This must be called after the priority of a transformer is changed.
        The :meth:`register_transformer` method calls this automatically.
        """
        ...
    
    @property
    def transformers(self):
        """Return a list of checkers, sorted by priority."""
        ...
    
    def register_transformer(self, transformer): # -> None:
        """Register a transformer instance."""
        ...
    
    def unregister_transformer(self, transformer): # -> None:
        """Unregister a transformer instance."""
        ...
    
    def init_checkers(self): # -> None:
        """Create the default checkers."""
        ...
    
    def sort_checkers(self): # -> None:
        """Sort the checkers by priority.

        This must be called after the priority of a checker is changed.
        The :meth:`register_checker` method calls this automatically.
        """
        ...
    
    @property
    def checkers(self):
        """Return a list of checkers, sorted by priority."""
        ...
    
    def register_checker(self, checker): # -> None:
        """Register a checker instance."""
        ...
    
    def unregister_checker(self, checker): # -> None:
        """Unregister a checker instance."""
        ...
    
    def init_handlers(self): # -> None:
        """Create the default handlers."""
        ...
    
    @property
    def handlers(self):
        """Return a dict of all the handlers."""
        ...
    
    def register_handler(self, name, handler, esc_strings): # -> None:
        """Register a handler instance by name with esc_strings."""
        ...
    
    def unregister_handler(self, name, handler, esc_strings): # -> None:
        """Unregister a handler instance by name with esc_strings."""
        ...
    
    def get_handler_by_name(self, name):
        """Get a handler by its name."""
        ...
    
    def get_handler_by_esc(self, esc_str):
        """Get a handler by its escape string."""
        ...
    
    def prefilter_line_info(self, line_info):
        """Prefilter a line that has been converted to a LineInfo object.

        This implements the checker/handler part of the prefilter pipe.
        """
        ...
    
    def find_handler(self, line_info):
        """Find a handler for the line_info by trying checkers."""
        ...
    
    def transform_line(self, line, continue_prompt):
        """Calls the enabled transformers in order of increasing priority."""
        ...
    
    def prefilter_line(self, line, continue_prompt=...):
        """Prefilter a single input line as text.

        This method prefilters a single line of text by calling the
        transformers and then the checkers/handlers.
        """
        ...
    
    def prefilter_lines(self, lines, continue_prompt=...):
        """Prefilter multiple input lines of text.

        This is the main entry point for prefiltering multiple lines of
        input.  This simply calls :meth:`prefilter_line` for each line of
        input.

        This covers cases where there are multiple lines in the user entry,
        which is the case when the user goes back to a multiline history
        entry and presses enter.
        """
        ...
    


class PrefilterTransformer(Configurable):
    """Transform a line of user input."""
    priority = Integer(100).tag(config=True)
    shell = ...
    prefilter_manager = ...
    enabled = ...
    def __init__(self, shell=..., prefilter_manager=..., **kwargs) -> None:
        ...
    
    def transform(self, line, continue_prompt): # -> None:
        """Transform a line, returning the new one."""
        ...
    
    def __repr__(self):
        ...
    


class PrefilterChecker(Configurable):
    """Inspect an input line and return a handler for that line."""
    priority = Integer(100).tag(config=True)
    shell = ...
    prefilter_manager = ...
    enabled = ...
    def __init__(self, shell=..., prefilter_manager=..., **kwargs) -> None:
        ...
    
    def check(self, line_info): # -> None:
        """Inspect line_info and return a handler instance or None."""
        ...
    
    def __repr__(self):
        ...
    


class EmacsChecker(PrefilterChecker):
    priority = Integer(100).tag(config=True)
    enabled = ...
    def check(self, line_info): # -> None:
        "Emacs ipython-mode tags certain input lines."
        ...
    


class MacroChecker(PrefilterChecker):
    priority = Integer(250).tag(config=True)
    def check(self, line_info): # -> None:
        ...
    


class IPyAutocallChecker(PrefilterChecker):
    priority = Integer(300).tag(config=True)
    def check(self, line_info): # -> None:
        "Instances of IPyAutocall in user_ns get autocalled immediately"
        ...
    


class AssignmentChecker(PrefilterChecker):
    priority = Integer(600).tag(config=True)
    def check(self, line_info): # -> None:
        """Check to see if user is assigning to a var for the first time, in
        which case we want to avoid any sort of automagic / autocall games.

        This allows users to assign to either alias or magic names true python
        variables (the magic/alias systems always take second seat to true
        python code).  E.g. ls='hi', or ls,that=1,2"""
        ...
    


class AutoMagicChecker(PrefilterChecker):
    priority = Integer(700).tag(config=True)
    def check(self, line_info): # -> None:
        """If the ifun is magic, and automagic is on, run it.  Note: normal,
        non-auto magic would already have been triggered via '%' in
        check_esc_chars. This just checks for automagic.  Also, before
        triggering the magic handler, make sure that there is nothing in the
        user namespace which could shadow it."""
        ...
    


class PythonOpsChecker(PrefilterChecker):
    priority = Integer(900).tag(config=True)
    def check(self, line_info): # -> None:
        """If the 'rest' of the line begins with a function call or pretty much
        any python operator, we should simply execute the line (regardless of
        whether or not there's a possible autocall expansion).  This avoids
        spurious (and very confusing) geattr() accesses."""
        ...
    


class AutocallChecker(PrefilterChecker):
    priority = Integer(1000).tag(config=True)
    function_name_regexp = ...
    exclude_regexp = ...
    def check(self, line_info): # -> None:
        "Check if the initial word/function is callable and autocall is on."
        ...
    


class PrefilterHandler(Configurable):
    handler_name = ...
    esc_strings = ...
    shell = ...
    prefilter_manager = ...
    def __init__(self, shell=..., prefilter_manager=..., **kwargs) -> None:
        ...
    
    def handle(self, line_info):
        """Handle normal input lines. Use as a template for handlers."""
        ...
    
    def __str__(self) -> str:
        ...
    


class MacroHandler(PrefilterHandler):
    handler_name = ...
    def handle(self, line_info):
        ...
    


class MagicHandler(PrefilterHandler):
    handler_name = ...
    esc_strings = ...
    def handle(self, line_info):
        """Execute magic functions."""
        ...
    


class AutoHandler(PrefilterHandler):
    handler_name = ...
    esc_strings = ...
    def handle(self, line_info):
        """Handle lines which can be auto-executed, quoting if requested."""
        ...
    


class EmacsHandler(PrefilterHandler):
    handler_name = ...
    esc_strings = ...
    def handle(self, line_info):
        """Handle input lines marked by python-mode."""
        ...
    


_default_checkers = ...
_default_handlers = ...
