import json

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return {"complex": True, "real": obj.real, "imag": obj.imag}
        if isinstance(obj, range):
            return {"range": True, "start": obj.start, "stop": obj.stop, "step": obj.step}
        return super().default(obj)

def dumps(obj, *args, **kwargs):
    return json.dumps(obj, cls=CustomEncoder, *args, **kwargs)

def loads(s, *args, **kwargs):
    return json.loads(s, *args, **kwargs)