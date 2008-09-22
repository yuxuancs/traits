#------------------------------------------------------------------------------
#
#  Copyright (c) 2008, Enthought, Inc.
#  All rights reserved.
#  
#  This software is provided without warranty under the terms of the BSD
#  license included in enthought/LICENSE.txt and may be redistributed only
#  under the conditions described in the aforementioned license.  The license
#  is also available online at http://www.enthought.com/licenses/BSD.txt
#
#  Thanks for using Enthought open source!
#  
#  Author: David C. Morrill
#  Date:   01/27/2006
#
#------------------------------------------------------------------------------

""" Defines the code editor factory for all traits toolkit backends, 
useful for tools such as debuggers.
"""

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from enthought.traits.api \
    import Instance, Str, Color, Enum, Bool
    
from enthought.traits.ui.editor_factory \
    import EditorFactory

#-------------------------------------------------------------------------------
#  'ToolkitEditorFactory' class:
#-------------------------------------------------------------------------------

class ToolkitEditorFactory ( EditorFactory ):
    """ Editor factory for code editors.
    """
    
    #---------------------------------------------------------------------------
    #  Trait definitions:
    #---------------------------------------------------------------------------
    
    # Object trait containing list of line numbers to mark (optional)
    mark_lines = Str
    
    # Background color for marking lines
    mark_color = Color( 0xECE9D8 )
    
    # Object trait containing the currently selected line (optional)
    selected_line = Str
    
    # Object trait containing the currently selected text (optional)
    selected_text = Str
    
    # Background color for selected lines
    selected_color = Color( 0xA4FFFF )
    
    # Where should the search toolbar be placed?
    search = Enum( 'top', 'bottom', 'none' )
    
    # Background color for lines that match the current search
    search_color = Color( 0xFFFF94 )
    
    # Current line
    line = Str
    
    # Current column
    column = Str
    
    # Should code folding be enabled?
    foldable = Bool( True )
    
    # Should line numbers be displayed in the margin?
    show_line_numbers = Bool( True )
    
    # Is user input set on every change?
    auto_set = Bool( True )
    
    # Should the editor auto-scroll when a new **selected_line** value is set?
    auto_scroll = Bool( True )

    # Optional key bindings associated with the editor    
    key_bindings = Instance( 'enthought.traits.ui.key_bindings.KeyBindings' )
    
    # Calltip clicked event
    calltip_clicked = Str
        

# Define the Code Editor class.
CodeEditor = ToolkitEditorFactory

### EOF #######################################################################