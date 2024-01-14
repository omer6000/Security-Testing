from typing import Any

ops = ['__add__', '__sub__', '__mul__', '__matmul__', '__truediv__',
       '__floordiv__', '__mod__', '__divmod__', '__pow__', '__lshift__', 
       '__rshift__', '__and__', '__xor__', '__or__', '__lt__', '__le__',
       '__gt__', '__ge__','__eq__', '__ne__']

rops = ['__radd__', '__rsub__', '__rmul__', '__rmatmul__', '__rtruediv__',
        '__rfloordiv__', '__rmod__', '__rdivmod__', '__rpow__', '__rlshift__', 
        '__rrshift__', '__rand__', '__rxor__', '__ror__', '__rlt__', '__rle__',
        '__rgt__', '__rge__','__req__', '__rne__']

number_ops = ['__neg__', '__pos__', '__abs__', '__invert__', 
             '__round__', '__int__', '__float__', '__complex__']

str_ops = ['__repr__', '__str__', 'capitalize', 'casefold', 'center', 'encode', 
           'expandtabs', 'format', 'format_map', 'join', 'ljust', 
           'lower', 'lstrip', 'replace', 'rjust', 'rstrip', 'strip', 
           'swapcase', 'title', 'translate', 'upper', 'startswith', 'split',
           'isupper', 'isspace', 'istitle', 'isprintable', 'isnumeric', 'islower',
           'isidentifier', 'isdigit', 'isdecimal', 'isalpha', 'isalnum']

container_ops = ['__len__', '__getitem__', '__iter__', '__next__', '__reversed__', 
                 '__missing__', 'append', 'extend', 'insert', 'remove', 'pop', 
                 'clear', 'index', 'count', 'sort', 'reverse', 'copy']

container_ops_unchanged = ['__setitem__', '__delitem__', '__contains__']


class tany(object):
    
    def __init__(self, value: Any, taint: Any = None, **kwargs):
        """Constructor.
        `value` is the string value the `tstr` object is to be constructed from.
        `taint` is an (optional) taint to be propagated to derived strings."""
        self. value = value
        self.taint = taint
        
    def __add__(self, other):
        if isinstance(other, tany) == False:
            other = self.create(other)
        if isinstance(self.value,str) or isinstance(other.value,str):
            return tany(str(self.value)+str(other.value),'str')
        else:
            return tany(self.value+other.value,'int')
    def __radd__(self, other):
        if isinstance(other, tany) == False:
            other = self.create(other)
        if isinstance(self.value,str) or isinstance(other.value,str):
            return tany(str(other.value)+str(self.value),'str')
        else:
            return tany(self.value+other.value,'int')

    def __sub__(self, other):
        if isinstance(other, tany) == False:
            other = self.create(other)
        return tany(self.value-other.value,'int')
    def __rsub__(self, other):
        if isinstance(other, tany) == False:
            other = self.create(other)
        return tany(other.value-self.value,'int')

    def __mul__(self, other):
        if isinstance(other, tany) == False:
            other = self.create(other)
        if isinstance(self.value,str):
            res = ""
            for _ in range(other.value):
                res += self.value
            return tany(res,'str')
        else:
            return tany(self.value*other.value,self.taint)
    def __rmul__(self, other):
        return self.__mul__(other)
    def __truediv__(self,other):
        return tany(self.value/other,self.taint)
    def __rtruediv__(self,other):
        return tany(other/self.value,self.taint)
    def __floordiv__(self,other):
        return tany(self.value//other,self.taint)
    def __rfloordiv__(self,other):
        return tany(other//self.value,self.taint)
    def __divmod__(self,other):
        return tany(divmod(self.value,other),self.taint)
    def __rdivmod__(self,other):
        return tany(divmod(other,self.value),self.taint)
    def __mod__(self,other):
        return tany(self.value%other,self.taint)
    def __rmod__(self,other):
        return tany(other%self.value,self.taint)
    def __lshift__(self,other):
        return tany(self.value<<other,self.taint)
    def __rlshift__(self,other):
        return tany(other<<self.value,self.taint)
    def __rshift__(self,other):
        return tany(self.value>>other,self.taint)
    def __rrshift__(self,other):
        return tany(other>>self.value,self.taint)
    def __and__(self,other):
        return tany(self.value&other,self.taint)
    def __rand__(self,other):
        return tany(other&self.value,self.taint)
    def __or__(self,other):
        return tany(self.value|other,self.taint)
    def __ror__(self,other):
        return tany(other|self.value,self.taint)
    def __xor__(self,other):
        return tany(self.value^other,self.taint)
    def __rxor__(self,other):
        return tany(other^self.value,self.taint)
    def __lt__(self,other):
        return tany(self.value<other,self.taint)
    def __rlt__(self,other):
        return tany(other<self.value,self.taint)
    def __le__(self,other):
        return tany(self.value<=other,self.taint)
    def __rle__(self,other):
        return tany(other<=self.value,self.taint)
    def __gt__(self,other):
        return tany(self.value>other,self.taint)
    def __rgt__(self,other):
        return tany(other>self.value,self.taint)
    def __ge__(self,other):
        return tany(self.value>=other,self.taint)
    def __rge__(self,other):
        return tany(other>=self.value,self.taint)
    def __eq__(self,other):
        return tany(self.value==other,self.taint)
    def __req__(self,other):
        return tany(self.value==other,self.taint)
    def __ne__(self,other):
        return tany(self.value!=other,self.taint)
    def __rne__(self,other):
        return tany(self.value!=other,self.taint)
    def __repr__(self):
        return self.value.__repr__()
    def __neg__(self):
        return tany(-1*self.value,self.taint)
    def __pos__(self):
        return tany(self.value,self.taint)
    def __invert__(self):
        return tany(~self.value,self.taint)
    def __round__(self):
        return tany(round(self.value),self.taint)
    def __abs__(self):
        return tany(abs(self.value),self.taint)
    def capitalize(self):
        return tany(self.value.capitalize(),self.taint)
    def casefold(self):
        return tany(self.value.casefold(),self.taint)

    def center(self,input):
        return tany(self.value.center(input),self.taint)

    def encode(self):
        return tany(self.value.encode(),self.taint)

    def expandtabs(self):
        return tany(self.value.expandtabs(),self.taint)

    def format(self):
        return tany(self.value.format(),self.taint)

    def format_map(self,input):
        return tany(self.value.format_map(input),self.taint)

    def join(self,input):
        return tany(self.value.join(input),self.taint)

    def ljust(self,input):
        return tany(self.value.ljust(input),self.taint)

    def rjust(self,input):
        return tany(self.value.rjust(input),self.taint)

    def lstrip(self,input):
        return tany(self.value.lstrip(input),self.taint)

    def rstrip(self,input):
        return tany(self.value.rstrip(input),self.taint)

    def strip(self,input):
        return tany(self.value.strip(input),self.taint)

    def replace(self,x,y):
        return tany(self.value.replace(x,y),self.taint)
    def swapcase(self):
        return tany(self.value.swapcase(),self.taint)
    def startswith(self,input):
        return tany(self.value.startswith(input),self.taint)
    def split(self,input):
        return tany(self.value.split(input),self.taint)
    def lower(self):
        return tany(self.value.lower(),self.taint)    
    def upper(self):
        return tany(self.value.upper(),self.taint)
    def title(self):
        return tany(self.value.title(),self.taint)
    def isupper(self):
        return tany(self.value.isupper(),self.taint)
    def isspace(self):
        return tany(self.value.isspace(),self.taint)
    def istitle(self):
        return tany(self.value.istitle(),self.taint)
    def isprintable(self):
        return tany(self.value.isprintable(),self.taint)
    def isnumeric(self):
        return tany(self.value.isnumeric(),self.taint)
    def islower(self):
        return tany(self.value.islower(),self.taint)
    def isidentifier(self):
        return tany(self.value.isidentifier(),self.taint)
    def isdigit(self):
        return tany(self.value.isdigit(),self.taint)
    def isdecimal(self):
        return tany(self.value.isdecimal(),self.taint)
    def isalpha(self):
        return tany(self.value.isalpha(),self.taint)
    def isalnum(self):
        return tany(self.value.isalnum(),self.taint)
    def __len__(self):
        return tany(len(self.value), self.taint)

    def __getitem__(self, key):
        return tany(self.value[key], self.taint)

    def __iter__(self):
        return tany(iter(self.value),self.taint)

    def __next__(self):
        return tany(next(self.value), self.taint)

    def __reversed__(self):
        return tany(reversed(self.value), self.taint)

    def __missing__(self, key):
        return tany(self.value.get(key), self.taint)

    def append(self, item):
        self.value.append(item)
        return tany(self.value, self.taint)

    def extend(self, iterable):
        self.value.extend(iterable)
        return tany(self.value, self.taint)

    def insert(self, index, item):
        self.value.insert(index, item)
        return tany(self.value, self.taint)

    def remove(self, item):
        self.value.remove(item)
        return tany(self.value, self.taint)

    def pop(self, index=-1):
        return tany(self.value.pop(index), self.taint)

    def clear(self):
        self.value.clear()
        return tany(self.value, self.taint)

    def index(self, item, start=0, end=None):
        if end is not None:
            return tany(self.value.index(item, start, end), self.taint)
        else:
            return tany(self.value.index(item, start), self.taint)
    def count(self, item):
        return tany(self.value.count(item), self.taint)

    def sort(self, key=None, reverse=False):
        self.value.sort(key=key, reverse=reverse)
        return tany(self.value, self.taint)

    def reverse(self):
        self.value.reverse()
        return tany(self.value, self.taint)

    def copy(self):
        return tany(self.value.copy(), self.taint)

    def __setitem__(self, key, value):
        self.value[key] = value
        return tany(self.value, self.taint)

    def __delitem__(self, key):
        del self.value[key]
        return tany(self.value, self.taint)

    def __contains__(self, item):
        return item in self.value

    def clear_taint(self):
        """Remove taint"""
        self.taint = None
        return self

    def has_taint(self):
        """Check if taint is present"""
        return self.taint is not None
    
    def create(self, x: Any):
        return tany(x,self.taint)
    
    @staticmethod
    def make_wrapper(fun_name: str):
        """Make `fun_name` from any class a method in `tany`"""
        def proxy(self, *args, **kwargs):
            args = list(args)
            for i in range(len(args)):
                if isinstance(args[i], tany):
                    args[i] = args[i].value
            for k in kwargs:
                if isinstance(kwargs[k], tany):
                    kwargs[k] = kwargs[k].value
            try:
                res = getattr(self.value, fun_name)(*args, **kwargs)
            except AttributeError:
                res = getattr(args[0], fun_name.replace('__r', '__'))(self.value, *args[1:], **kwargs) 
            return self.create(res)

        return proxy
    
    @staticmethod
    def make_wrapper_unchanged_return(fun_name: str):
        """Make `fun_name` from any class a method in `tany` but returns a not tainted object"""
        def proxy(self, *args, **kwargs):
            args = list(args)
            for i in range(len(args)):
                if isinstance(args[i], tany):
                    args[i] = args[i].value
            for k in kwargs:
                if isinstance(kwargs[k], tany):
                    kwargs[k] = kwargs[k].value
            res = getattr(self.value, fun_name)(*args, **kwargs)
            return res

        return proxy


# Wrappers
original_repr = repr
original_len = len

def repr_wrapper(x):
    if isinstance(x, tany):
        return x.create(original_repr(x.value))
    else:
        return original_repr(x)
    
    
def len_wrapper(x):
    if isinstance(x, tany):
        return x.create(original_len(x.value))
    else:
        return original_len(x)

    
repr = repr_wrapper
len = len_wrapper


# Casts    
def tint(x):
    if isinstance(x, tany):
        return x.create(int(x.value))
    else:
        return int(x)


def tfloat(x):
    if isinstance(x, tany):
        return x.create(float(x.value))
    else:
        return float(x)

    
def tstr(x):
    if isinstance(x, tany):
        return x.create(str(x.value))
    else:
        return str(x)
    

def tcomplex(x):
    if isinstance(x, tany):
        return tany(complex(x.value),x.taint)
    else:
        return complex(x)