import random
import string


class ShortnerService:
    url_store: dict[str, str] = {}
    
    def generate_code(self) -> str:
        alphabet = string.ascii_letters + string.digits
        while True:
            code = "".join(random.choices(alphabet, k=6))
            if code not in self.url_store:
                break
        return code

    def save_url(self, long_url: str) -> str:
        code = self.generate_code()
        self.url_store[code] = long_url
        return code

    def get_long_url(self, code: str) -> str | None:
        return self.url_store.get(code)

