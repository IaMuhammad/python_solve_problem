class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.browser = []

    def visit(self, url: str) -> None:
        self.browser = [url]

    def back(self, steps: int) -> str:
        return 'aw'

    def forward(self, steps: int) -> str:
        return 'as'

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)