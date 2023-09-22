import json

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return {"real": obj.real, "imag": obj.imag}
        elif isinstance(obj, range):
            return {"start": obj.start, "stop": obj.stop, "step": obj.step}
        return super().default(obj)

def custom_dumps(obj, **kwargs):
    return json.dumps(obj, cls=CustomEncoder, **kwargs)

class CustomDecoder(json.JSONDecoder):
    def object_hook(self, obj):
        if "__complex__" in obj:
            return complex(obj["real"], obj["imag"])
        elif "__range__" in obj:
            return range(obj["start"], obj["stop"], obj["step"])
        return obj

def custom_loads(s, **kwargs):
    return json.loads(s, cls=CustomDecoder, **kwargs)
