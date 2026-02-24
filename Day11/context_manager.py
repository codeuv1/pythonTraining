import urllib.request
from types import TracebackType
from typing import Optional, Type


class URLResource:
    def __init__(self, url: str) -> None:
        self.url = url
        self.response = None

    def __enter__(self) -> urllib.request.addinfourl:
        print(f"[INFO] Opening connection to {self.url}")
        self.response = urllib.request.urlopen(self.url)
        return self.response

    def __exit__(self,exc_type: Optional[Type[BaseException]],exc_value: Optional[BaseException],traceback: Optional[TracebackType],
    ) -> None:
        if self.response:
            self.response.close()
            print("[INFO] Connection closed")

with URLResource("https://example.com") as response:
    content = response.read(100)  # read first 100 bytes
    print(content.decode("utf-8"))