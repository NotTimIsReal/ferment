from index import Barrells
class test (Barrells):
    def __init__(self):
        Barrells.__init__(self)
        self.git=True
        self.url="https://github.com/NotTimIsReal/NotTimisReal"
        self.license="MIT"
        self.homepage="https://github.com/NotTimIsReal"
        self.dependencies=["curl", "git"]
        self.supported_OS=["1.0.0"]
    def install():
        pass