class MyClass:
    """This is my test class.

    It has three different class attributes, all differently-cased
    variations on the same words. In Python these are totally different
    attributes.
    """

    MY_ATTR: str = ""
    """str: This is MY_ATTR -- it's an upper-case name."""

    my_attr: int = 0
    """str: This is my_attr -- it's a lower-case name."""

    My_Attr: bool = False
    """str: This is My_Attr -- it's a mixed-case name."""
