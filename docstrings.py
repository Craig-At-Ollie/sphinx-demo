class B:
    """
    This is class B, by default it's full of bs.
    A :meth:`make_bs` can be useful for making a list of bs.

    :ivar items: A list of b character strings
    :type items: list[str]
    """
    def __init__(self):
        self.items = self.make_bs(5)

    def __str__(self):
        return (
               "Empty b" if not self.items
                else "Bs" if len(self.items) > 1 
                else "single b"
        )

    @classmethod
    def make_bs(cls, count, user_lower=True):
        """
        Make some Bs, makes a list of Bs and returns them
        
        :param count: The count of how many Bs to make
        :type count: int

        :param user_lower: When True the bs will be lowercase, Defaults to true
        :type user_lower: bool, optional

        :return: The list of bs
        :rtype: list[str]
        """
        return  ["b" if user_lower else "B" for i in range(count)]



class C:
    """
    This is the C class.
    It contains a :attr:`thing` property and the method :meth:`set_b`.

    :param thing: The thing to set it to when initializing, defaults to None
    :type thing: object, optional

    :keyword stash: What to set the stash to, this is a keyword in kwargs
    :type stash: object, optional

    :cvar it: What it is. Note this is a class var, but it gets bundled with other vars
    :type it: object

    :ivar stash: A stash to store something, note this is an instance var
    :type stash: object

    """
    it=None

    def __init__(self, thing=None, **kwargs):
        """
        NOTE: dunder method docstrings are ignored and should be documented
        at the class level
        """
        if thing is not None:
            self.it = thing
        self.stash=kwargs.get("stash")

    def __call__(self, print_it=True):
        """
        Call the class to make it do something. This is displayed because it's
        called out in the autodoc call in the `index.rst` file
        
        :param print_it: When true, prints it, defaults to True
        :type print_it: bool, optional
        """
        if print_it:
            print(self.whatsit)
        else:
            raise NotImplementedError()

    def set_b(self, b):
        """
        set it to class :class:`B`

        :param b: An instance of the b class to use
        :type b: :class:`B`

        :raises TypeError: the parameter was not an instance of class B

        """
        if not isinstance(b, B):
            raise TypeError
        self.it = b

    @property
    def whatsit(self):
        """
        Read Only stringified version of what it is

        :rtype: str
        """
        return str(self.it)

    @property
    def thing(self):
        """
        What it is.

        :type: object
        """
        return self.it

    @thing.setter
    def thing(self, it):
        """
           Note that the setter is ignored
        """
        self.it = it


def work_it(set_it="flip it and reverse it"):
    """
    Create and run the C class

    :param set_it: What to set it to, defaults to a stribg of "thing"
    :type set_it: object, optional

    :return: The C class that was created and run
    :rtype: :class:`C`
    """
    c = C(stash="called from work it")
    c.thing = set_it
    c()
    c.set_b(B())
    return c

if __name__ == "__main__":
    worked_c = work_it()
    worked_c()
