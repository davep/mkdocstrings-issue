class MyClass:
    """This is my test class.

    It has three different class attributes, all differently-cased
    variations on the same words. In Python these are totally different
    attributes.
    """

    MY_ATTR: str = ""
    """str: This is MY_ATTR -- it's an upper-case name."""

    my_attr: int = 0
    """int: This is my_attr -- it's a lower-case name."""

    My_Attr: bool = False
    """bool: This is My_Attr -- it's a mixed-case name."""

    MY_attr: float = 0.0
    """float: This is MY_attr -- it's also mentioned in __init__"""

    def __init__( self ):
        # This will cause MY_attr to not get documented.
        self.MY_attr = 0.0
        """I wonder if this documents it though."""
