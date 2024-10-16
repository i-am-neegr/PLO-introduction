class ProductNotFoundException(Exception):
    def __init__(self, *args, **kwargs):
        self.message = str(args[0]) if args else "No Product Found"

    def __str__(self):
        return self.message
