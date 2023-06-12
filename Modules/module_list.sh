list of modules present in python:
__future__          argparse            help                sched
__main__ 

array 

# Help on built-in module array:

# NAME
#     array

# DESCRIPTION
#     This module defines an object type which can efficiently represent
#     an array of basic values: characters, integers, floating point
#     numbers.  Arrays are sequence types and behave very much like lists,
#     except that the type of objects stored in them is constrained.

# CLASSES
#     builtins.object
#         array
    
#     ArrayType = class array(builtins.object)
select |  array(typecode [, initializer]) -> array
#      |  
#      |  Return a new array whose items are restricted by typecode, and
#      |  initialized from the optional initializer value, which must be a list,
#      |  string or iterable over elements of the appropriate type.
#      |  
#      |  Arrays represent basic values and behave very much like lists, except
#      |  the type of objects stored in them is constrained. The type is specified
#      |  at object creation time by using a type code, which is a single character.
#      |  The following type codes are defined:
#      |  
select |      Type code   C Type             Minimum size in bytes
select |      'b'         signed integer     1
select |      'B'         unsigned integer   1
select |      'u'         Unicode character  2 (see note)
select |      'h'         signed integer     2
select |      'H'         unsigned integer   2
select |      'i'         signed integer     2
select |      'I'         unsigned integer   2
select |      'l'         signed integer     4
select |      'L'         unsigned integer   4
select |      'q'         signed integer     8 (see note)
select |      'Q'         unsigned integer   8 (see note)
select |      'f'         floating point     4
select |      'd'         floating point     8
#      |  
#      |  NOTE: The 'u' typecode corresponds to Python's unicode character. On
#      |  narrow builds this is 2-bytes on wide builds this is 4-bytes.
#      |  
#      |  NOTE: The 'q' and 'Q' type codes are only available if the platform
#      |  C compiler used to build Python supports 'long long', or, on Windows,
#      |  '__int64'.
#      |  
select |  Methods:
select |  
select |  append() -- append a new item to the end of the array
select |  buffer_info() -- return information giving the current memory info
select |  byteswap() -- byteswap all the items of the array
select |  count() -- return number of occurrences of an object
select |  extend() -- extend array by appending multiple elements from an iterable
select |  fromfile() -- read items from a file object
select |  fromlist() -- append items from the list
select |  frombytes() -- append items from the string
select |  index() -- return index of first occurrence of an object
select |  insert() -- insert a new item into the array at a provided position
select |  pop() -- remove and return item (default last)
select |  remove() -- remove first occurrence of an object
select |  reverse() -- reverse the order of the items in the array
select |  tofile() -- write all items to a file object
select |  tolist() -- return the array converted to an ordinary list
select |  tobytes() -- return the array converted to a string
#      |  
#      |  Attributes:
#      |  
#      |  typecode -- the typecode character used to create the array
#      |  itemsize -- the length in bytes of one array item
#      |  
#      |  Methods defined here:
#      |  
#      |  __add__(self, value, /)
#      |      Return self+value.
#      |  
#      |  __contains__(self, key, /)
#      |      Return key in self.
#      |  
#      |  __copy__(self, /)
#      |      Return a copy of the array.
#      |  
#      |  __deepcopy__(self, unused, /)
#      |      Return a copy of the array.
#      |  
#      |  __delitem__(self, key, /)
#      |      Delete self[key].
#      |  
#      |  __eq__(self, value, /)
#      |      Return self==value.
#      |  
#      |  __ge__(self, value, /)
#      |      Return self>=value.
#      |  
#      |  __getattribute__(self, name, /)
#      |      Return getattr(self, name).
#      |  
#      |  __getitem__(self, key, /)
#      |      Return self[key].
#      |  
#      |  __gt__(self, value, /)
#      |      Return self>value.
#      |  
#      |  __iadd__(self, value, /)
#      |      Implement self+=value.
#      |  
#      |  __imul__(self, value, /)
#      |      Implement self*=value.
#      |  
#      |  __iter__(self, /)
#      |      Implement iter(self).
#      |  
#      |  __le__(self, value, /)
#      |      Return self<=value.
#      |  
#      |  __len__(self, /)
#      |      Return len(self).
#      |  
#      |  __lt__(self, value, /)
#      |      Return self<value.
#      |  
#      |  __mul__(self, value, /)
#      |      Return self*value.
#      |  
#      |  __ne__(self, value, /)
#      |      Return self!=value.
#      |  
#      |  __reduce_ex__(self, value, /)
#      |      Return state information for pickling.
#      |  
#      |  __repr__(self, /)
#      |      Return repr(self).
#      |  
#      |  __rmul__(self, value, /)
#      |      Return value*self.
#      |  
#      |  __setitem__(self, key, value, /)
#      |      Set self[key] to value.
#      |  
#      |  __sizeof__(self, /)
#      |      Size of the array in memory, in bytes.
#      |  
#      |  append(self, v, /)
#      |      Append new value v to the end of the array.
#      |  
#      |  buffer_info(self, /)
#      |      Return a tuple (address, length) giving the current memory address and the length in items of the buffer used to hold array's contents.
#      |      
#      |      The length should be multiplied by the itemsize attribute to calculate
#      |      the buffer length in bytes.
#      |  
#      |  byteswap(self, /)
#      |      Byteswap all items of the array.
#      |      
#      |      If the items in the array are not 1, 2, 4, or 8 bytes in size, RuntimeError is
#      |      raised.
#      |  
#      |  count(self, v, /)
#      |      Return number of occurrences of v in the array.
#      |  
#      |  extend(self, bb, /)
#      |      Append items to the end of the array.
#      |  
#      |  frombytes(self, buffer, /)
#      |      Appends items from the string, interpreting it as an array of machine values, as if it had been read from a file using the fromfile() method.
#      |  
#      |  fromfile(self, f, n, /)
#      |      Read n objects from the file object f and append them to the end of the array.
#      |  
#      |  fromlist(self, list, /)
#      |      Append items to array from list.
#      |  
#      |  fromunicode(self, ustr, /)
#      |      Extends this array with data from the unicode string ustr.
#      |      
#      |      The array must be a unicode type array; otherwise a ValueError is raised.
#      |      Use array.frombytes(ustr.encode(...)) to append Unicode data to an array of
#      |      some other type.
#      |  
#      |  index(self, v, start=0, stop=9223372036854775807, /)
#      |      Return index of first occurrence of v in the array.
#      |      
#      |      Raise ValueError if the value is not present.
#      |  
#      |  insert(self, i, v, /)
#      |      Insert a new item v into the array before position i.
#      |  
#      |  pop(self, i=-1, /)
#      |      Return the i-th element and delete it from the array.
#      |      
#      |      i defaults to -1.
#      |  
#      |  remove(self, v, /)
#      |      Remove the first occurrence of v in the array.
#      |  
#      |  reverse(self, /)
#      |      Reverse the order of the items in the array.
#      |  
#      |  tobytes(self, /)
#      |      Convert the array to an array of machine values and return the bytes representation.
#      |  
#      |  tofile(self, f, /)
#      |      Write all items (as machine values) to the file object f.
#      |  
#      |  tolist(self, /)
#      |      Convert array to an ordinary list with the same items.
#      |  
#      |  tounicode(self, /)
#      |      Extends this array with data from the unicode string ustr.
#      |      
#      |      Convert the array to a unicode string.  The array must be a unicode type array;
#      |      otherwise a ValueError is raised.  Use array.tobytes().decode() to obtain a
#      |      unicode string from an array of some other type.
#      |  
#      |  ----------------------------------------------------------------------
#      |  Static methods defined here:
#      |  
#      |  __new__(*args, **kwargs) from builtins.type
#      |      Create and return a new object.  See help(type) for accurate signature.
#      |  
#      |  ----------------------------------------------------------------------
#      |  Data descriptors defined here:
#      |  
#      |  itemsize
#      |      the size, in bytes, of one array item
#      |  
#      |  typecode
#      |      the typecode character used to create the array
#      |  
#      |  ----------------------------------------------------------------------
#      |  Data and other attributes defined here:
#      |  
#      |  __hash__ = None
    
#     class array(builtins.object)
#      |  array(typecode [, initializer]) -> array
#      |  
#      |  Return a new array whose items are restricted by typecode, and
#      |  initialized from the optional initializer value, which must be a list,
#      |  string or iterable over elements of the appropriate type.
#      |  
#      |  Arrays represent basic values and behave very much like lists, except
#      |  the type of objects stored in them is constrained. The type is specified
#      |  at object creation time by using a type code, which is a single character.
#      |  The following type codes are defined:
#      |  
#      |      Type code   C Type             Minimum size in bytes
#      |      'b'         signed integer     1
#      |      'B'         unsigned integer   1
#      |      'u'         Unicode character  2 (see note)
#      |      'h'         signed integer     2
#      |      'H'         unsigned integer   2
#      |      'i'         signed integer     2
#      |      'I'         unsigned integer   2
#      |      'l'         signed integer     4
#      |      'L'         unsigned integer   4
#      |      'q'         signed integer     8 (see note)
#      |      'Q'         unsigned integer   8 (see note)
#      |      'f'         floating point     4
#      |      'd'         floating point     8
#      |  
#      |  NOTE: The 'u' typecode corresponds to Python's unicode character. On
#      |  narrow builds this is 2-bytes on wide builds this is 4-bytes.
#      |  
#      |  NOTE: The 'q' and 'Q' type codes are only available if the platform
#      |  C compiler used to build Python supports 'long long', or, on Windows,
#      |  '__int64'.
#      |  
#      |  Methods:
#      |  
#      |  append() -- append a new item to the end of the array
#      |  buffer_info() -- return information giving the current memory info
#      |  byteswap() -- byteswap all the items of the array
#      |  count() -- return number of occurrences of an object
#      |  extend() -- extend array by appending multiple elements from an iterable
#      |  fromfile() -- read items from a file object
#      |  fromlist() -- append items from the list
#      |  frombytes() -- append items from the string
#      |  index() -- return index of first occurrence of an object
#      |  insert() -- insert a new item into the array at a provided position
#      |  pop() -- remove and return item (default last)
#      |  remove() -- remove first occurrence of an object
#      |  reverse() -- reverse the order of the items in the array
#      |  tofile() -- write all items to a file object
#      |  tolist() -- return the array converted to an ordinary list
#      |  tobytes() -- return the array converted to a string
#      |  
#      |  Attributes:
#      |  
#      |  typecode -- the typecode character used to create the array
#      |  itemsize -- the length in bytes of one array item
#      |  
#      |  Methods defined here:
#      |  
#      |  __add__(self, value, /)
#      |      Return self+value.
#      |  
#      |  __contains__(self, key, /)
#      |      Return key in self.
#      |  
#      |  __copy__(self, /)
#      |      Return a copy of the array.
#      |  
#      |  __deepcopy__(self, unused, /)
#      |      Return a copy of the array.
#      |  
#      |  __delitem__(self, key, /)
#      |      Delete self[key].
#      |  
#      |  __eq__(self, value, /)
#      |      Return self==value.
#      |  
#      |  __ge__(self, value, /)
#      |      Return self>=value.
#      |  
#      |  __getattribute__(self, name, /)
#      |      Return getattr(self, name).
#      |  
#      |  __getitem__(self, key, /)
#      |      Return self[key].
#      |  
#      |  __gt__(self, value, /)
#      |      Return self>value.
#      |  
#      |  __iadd__(self, value, /)
#      |      Implement self+=value.
#      |  
#      |  __imul__(self, value, /)
#      |      Implement self*=value.
#      |  
#      |  __iter__(self, /)
#      |      Implement iter(self).
#      |  
#      |  __le__(self, value, /)
#      |      Return self<=value.
#      |  
#      |  __len__(self, /)
#      |      Return len(self).
#      |  
#      |  __lt__(self, value, /)
#      |      Return self<value.
#      |  
#      |  __mul__(self, value, /)
#      |      Return self*value.
#      |  
#      |  __ne__(self, value, /)
#      |      Return self!=value.
#      |  
#      |  __reduce_ex__(self, value, /)
#      |      Return state information for pickling.
#      |  
#      |  __repr__(self, /)
#      |      Return repr(self).
#      |  
#      |  __rmul__(self, value, /)
#      |      Return value*self.
#      |  
#      |  __setitem__(self, key, value, /)
#      |      Set self[key] to value.
#      |  
#      |  __sizeof__(self, /)
#      |      Size of the array in memory, in bytes.
#      |  
#      |  append(self, v, /)
#      |      Append new value v to the end of the array.
#      |  
#      |  buffer_info(self, /)
#      |      Return a tuple (address, length) giving the current memory address and the length in items of the buffer used to hold array's contents.
#      |      
#      |      The length should be multiplied by the itemsize attribute to calculate
#      |      the buffer length in bytes.
#      |  
#      |  byteswap(self, /)
#      |      Byteswap all items of the array.
#      |      
#      |      If the items in the array are not 1, 2, 4, or 8 bytes in size, RuntimeError is
#      |      raised.
#      |  
#      |  count(self, v, /)
#      |      Return number of occurrences of v in the array.
#      |  
#      |  extend(self, bb, /)
#      |      Append items to the end of the array.
#      |  
#      |  frombytes(self, buffer, /)
#      |      Appends items from the string, interpreting it as an array of machine values, as if it had been read from a file using the fromfile() method.
#      |  
#      |  fromfile(self, f, n, /)
#      |      Read n objects from the file object f and append them to the end of the array.
#      |  
#      |  fromlist(self, list, /)
#      |      Append items to array from list.
#      |  
#      |  fromunicode(self, ustr, /)
#      |      Extends this array with data from the unicode string ustr.
#      |      
#      |      The array must be a unicode type array; otherwise a ValueError is raised.
#      |      Use array.frombytes(ustr.encode(...)) to append Unicode data to an array of
#      |      some other type.
#      |  
#      |  index(self, v, start=0, stop=9223372036854775807, /)
#      |      Return index of first occurrence of v in the array.
#      |      
#      |      Raise ValueError if the value is not present.
#      |  
#      |  insert(self, i, v, /)
#      |      Insert a new item v into the array before position i.
#      |  
#      |  pop(self, i=-1, /)
#      |      Return the i-th element and delete it from the array.
#      |      
#      |      i defaults to -1.
#      |  
#      |  remove(self, v, /)
#      |      Remove the first occurrence of v in the array.
#      |  
#      |  reverse(self, /)
#      |      Reverse the order of the items in the array.
#      |  
#      |  tobytes(self, /)
#      |      Convert the array to an array of machine values and return the bytes representation.
#      |  
#      |  tofile(self, f, /)
#      |      Write all items (as machine values) to the file object f.
#      |  
#      |  tolist(self, /)
#      |      Convert array to an ordinary list with the same items.
#      |  
#      |  tounicode(self, /)
#      |      Extends this array with data from the unicode string ustr.
#      |      
#      |      Convert the array to a unicode string.  The array must be a unicode type array;
#      |      otherwise a ValueError is raised.  Use array.tobytes().decode() to obtain a
#      |      unicode string from an array of some other type.
#      |  
#      |  ----------------------------------------------------------------------
#      |  Static methods defined here:
#      |  
#      |  __new__(*args, **kwargs) from builtins.type
#      |      Create and return a new object.  See help(type) for accurate signature.
#      |  
#      |  ----------------------------------------------------------------------
#      |  Data descriptors defined here:
#      |  
#      |  itemsize
#      |      the size, in bytes, of one array item
#      |  
#      |  typecode
#      |      the typecode character used to create the array
#      |  
#      |  ----------------------------------------------------------------------
#      |  Data and other attributes defined here:
#      |  
#      |  __hash__ = None

# DATA
#     typecodes = 'bBuhHiIlLqQfd'

# FILE
#     (built-in)



help_about          scrolledlist
_abc                ast                 history             search
_aix_support        asynchat            hmac                searchbase
_ast                asyncio             html                searchengine
_asyncio            asyncore            http                secrets
_bisect             atexit              hyperparser         select
_blake2             audioop             idle                selectors
_bootsubprocess     autocomplete        idle_test           setuptools
_bz2                autocomplete_w      idlelib             shelve
_codecs             autoexpand          imaplib             shlex
_codecs_cn          base64              imghdr              shutil

os






imp

# help("imp")
  
# Help on module imp:

# NAME
#     imp

# MODULE REFERENCE
#     https://docs.python.org/3.10/library/imp.html
    
# DESCRIPTION
#     This module provides the components needed to build your own __import__
#     function.  Undocumented functions are obsolete.
    
#     In most cases it is preferred you consider using the importlib module's
#     functionality over this module.

# CLASSES
#     builtins.object
#         NullImporter
    
#     class NullImporter(builtins.object)
#      |  NullImporter(path)
#      |  
#      |  **DEPRECATED**
#      |  
#      |  Null import object.
#      |  
#      |  Methods defined here:
#      |  
#      |  __init__(self, path)
#      |      Initialize self.  See help(type(self)) for accurate signature.
#      |  
#      |  find_module(self, fullname)
#      |      Always returns None.
#      |  
#      |  ----------------------------------------------------------------------
#      |  Data descriptors defined here:
#      |  
#      |  __dict__
#      |      dictionary for instance variables (if defined)
#      |  
#      |  __weakref__
#      |      list of weak references to the object (if defined)

# FUNCTIONS
#     acquire_lock()
#         Acquires the interpreter's import lock for the current thread.
        
#         This lock should be used by import hooks to ensure thread-safety when importing
#         modules. On platforms without threads, this function does nothing.
    
#     cache_from_source(path, debug_override=None)
#         **DEPRECATED**
        
#         Given the path to a .py file, return the path to its .pyc file.
        
#         The .py file does not need to exist; this simply returns the path to the
#         .pyc file calculated as if the .py file were imported.
        
#         If debug_override is not None, then it must be a boolean and is used in
#         place of sys.flags.optimize.
        
#         If sys.implementation.cache_tag is None then NotImplementedError is raised.
    
    create_dynamic(...)
        Create an extension module.
    
#     find_module(name, path=None)
#         **DEPRECATED**
        
#         Search for a module.
        
#         If path is omitted or None, search for a built-in, frozen or special
#         module and continue search in sys.path. The module name cannot
#         contain '.'; to search for a submodule of a package, pass the
#         submodule name and the package's __path__.
    
#     get_frozen_object(name, /)
#         Create a code object for a frozen module.
    
#     get_magic()
#         **DEPRECATED**
        
#         Return the magic number for .pyc files.
    
#     get_suffixes()
#         **DEPRECATED**
    
#     get_tag()
#         Return the magic tag for .pyc files.
    
#     init_builtin(name)
#         **DEPRECATED**
        
#         Load and return a built-in module by name, or None is such module doesn't
#         exist
    
#     init_frozen(name, /)
#         Initializes a frozen module.
    
#     is_builtin(name, /)
#         Returns True if the module name corresponds to a built-in module.
    
#     is_frozen(name, /)
#         Returns True if the module name corresponds to a frozen module.
    
#     is_frozen_package(name, /)
#         Returns True if the module name is of a frozen package.
    
#     load_compiled(name, pathname, file=None)
#         **DEPRECATED**
    
#     load_dynamic(name, path, file=None)
#         **DEPRECATED**
        
#         Load an extension module.
    
#     load_module(name, file, filename, details)
#         **DEPRECATED**
        
#         Load a module, given information returned by find_module().
        
#         The module name must include the full package name, if any.
    
#     load_package(name, path)
#         **DEPRECATED**
    
#     load_source(name, pathname, file=None)
    
#     lock_held()
#         Return True if the import lock is currently held, else False.
        
#         On platforms without threads, return False.
    
#     new_module(name)
#         **DEPRECATED**
        
#         Create a new module.
        
#         The module is not entered into sys.modules.
    
#     release_lock()
#         Release the interpreter's import lock.
        
#         On platforms without threads, this function does nothing.
done >-------------------------------->
#     reload(module)
#         **DEPRECATED**
        
#         Reload the module and return it.
        
select    The module must have been successfully imported before.
<--------------------------------< done
#     source_from_cache(path)
#         **DEPRECATED**
        
#         Given the path to a .pyc. file, return the path to its .py file.
        
#         The .pyc file does not need to exist; this simply returns the path to
#         the .py file calculated to correspond to the .pyc file.  If path does
#         not conform to PEP 3147 format, ValueError will be raised. If
#         sys.implementation.cache_tag is None then NotImplementedError is raised.

# DATA
#     C_BUILTIN = 6
#     C_EXTENSION = 3
#     IMP_HOOK = 9
#     PKG_DIRECTORY = 5
#     PY_CODERESOURCE = 8
#     PY_COMPILED = 2
#     PY_FROZEN = 7
#     PY_RESOURCE = 4
#     PY_SOURCE = 1
#     SEARCH_ERROR = 0


_codecs_hk          bdb                 sidebar
_codecs_iso2022     binascii            importlib           signal
_codecs_jp          binhex              inspect             site
_codecs_kr          bisect              io                  smtpd
_codecs_tw          browser             iomenu              smtplib
_collections        builtins            ipaddress           sndhdr
_collections_abc    bz2                 itertools           socket
_compat_pickle      cProfile            json                socketserver
_compression        calendar            keyword             sqlite3
_contextvars        calltip             lib2to3             squeezer
_csv                calltip_w           linecache           sre_compile
_ctypes             cgi                 locale              sre_constants
_ctypes_test        cgitb               logging             sre_parse
_datetime           chunk               lzma                ssl
_decimal            

cmath

# Help on built-in module cmath:

# NAME
#     cmath

# DESCRIPTION
#     This module provides access to mathematical functions for complex
#     numbers.

select all FUNCTIONS
#     acos(z, /)
#         Return the arc cosine of z.
    
#     acosh(z, /)
#         Return the inverse hyperbolic cosine of z.
    
#     asin(z, /)
#         Return the arc sine of z.
    
#     asinh(z, /)
#         Return the inverse hyperbolic sine of z.
    
#     atan(z, /)
#         Return the arc tangent of z.
    
#     atanh(z, /)
#         Return the inverse hyperbolic tangent of z.
    
#     cos(z, /)
#         Return the cosine of z.
    
#     cosh(z, /)
#         Return the hyperbolic cosine of z.
    
#     exp(z, /)
#         Return the exponential value e**z.
    
#     isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
#         Determine whether two complex numbers are close in value.
        
#           rel_tol
#             maximum difference for being considered "close", relative to the
#             magnitude of the input values
#           abs_tol
#             maximum difference for being considered "close", regardless of the
#             magnitude of the input values
        
#         Return True if a is close in value to b, and False otherwise.
        
#         For the values to be considered close, the difference between them must be
#         smaller than at least one of the tolerances.
        
#         -inf, inf and NaN behave similarly to the IEEE 754 Standard. That is, NaN is
#         not close to anything, even itself. inf and -inf are only close to themselves.
    
#     isfinite(z, /)
#         Return True if both the real and imaginary parts of z are finite, else False.
    
#     isinf(z, /)
#         Checks if the real or imaginary part of z is infinite.
    
#     isnan(z, /)
#         Checks if the real or imaginary part of z not a number (NaN).
    
#     log(...)
#         log(z[, base]) -> the logarithm of z to the given base.
        
#         If the base not specified, returns the natural logarithm (base e) of z.
    
#     log10(z, /)
#         Return the base-10 logarithm of z.
    
#     phase(z, /)
#         Return argument, also known as the phase angle, of a complex.
    
#     polar(z, /)
#         Convert a complex from rectangular coordinates to polar coordinates.
        
#         r is the distance from 0 and phi the phase angle.
    
#     rect(r, phi, /)
#         Convert from polar coordinates to rectangular coordinates.
    
#     sin(z, /)
#         Return the sine of z.
    
#     sinh(z, /)
#         Return the hyperbolic sine of z.
    
#     sqrt(z, /)
#         Return the square root of z.
    
#     tan(z, /)
#         Return the tangent of z.
    
#     tanh(z, /)
#         Return the hyperbolic tangent of z.

# DATA
#     e = 2.718281828459045
#     inf = inf
#     infj = infj
#     nan = nan
#     nanj = nanj
#     pi = 3.141592653589793
#     tau = 6.283185307179586

# FILE
#     (built-in)

macosx              stackviewer
_distutils_hack     cmd                 mailbox             stat
_elementtree        code                mailcap             statistics
_functools          codecontext         mainmenu            statusbar
_hashlib            codecs              marshal             string
_heapq              codeop              math                stringprep
_imp                collections         mimetypes           struct
_io                 colorizer           mmap                subprocess
_json               colorsys            modulefinder        sunau
_locale             compileall          msilib              symtable
_lsprof             concurrent          msvcrt              sys
_lzma               config              multicall           sysconfig
_markupbase         config_key          multiprocessing     tabnanny
_md5                configdialog        netrc               tarfile
_msi                configparser        nntplib             telnetlib
_multibytecodec     contextlib          nt                  tempfile
_multiprocessing    contextvars         ntpath              test
_opcode             copy                nturl2path          textview
_operator           copyreg             numbers             textwrap
_osx_support        crypt               opcode              this
_overlapped         csv                 operator            threading
_pickle             ctypes              optparse            time
_py_abc             curses              os select           timeit
_pydecimal          dataclasses         outwin              tkinter
_pyio               datetime            parenmatch          token
_queue              dbm                 pathbrowser         tokenize
_random             debugger            pathlib             tooltip
_sha1               debugger_r          pdb                 trace
_sha256             debugobj            percolator          traceback
_sha3               debugobj_r          pickle              tracemalloc
_sha512             decimal             pickletools         tree
_signal             delegator           pip                 tty
_sitebuiltins       difflib             pipes               turtle
_socket             dis                 pkg_resources       turtledemo
_sqlite3            distutils           pkgutil             types
_sre                doctest             platform            typing
_ssl                dynoption           plistlib            undo
_stat               editor              poplib              unicodedata
_statistics         email               posixpath           unittest
_string             encodings           pprint              urllib
_strptime           ensurepip           profile             uu
_struct             enum                pstats              uuid
_symtable           errno               pty                 venv
_testbuffer         faulthandler        py_compile          warnings
_testcapi           filecmp             pyclbr              wave
_testconsole        fileinput           pydoc               weakref
_testimportmultiple filelist            pydoc_data          webbrowser
_testinternalcapi   fnmatch             pyexpat             window
_testmultiphase     format              pyparse             winreg
_thread             fractions           pyshell             winsound
_threading_local    ftplib              query               wsgiref
_tkinter            functools           queue               xdrlib
_tracemalloc        gc                  quopri              xml
_uuid               genericpath         random              xmlrpc
_warnings           getopt              re                  xxsubtype
_weakref            getpass             redirector          zipapp
_weakrefset         gettext             replace             zipfile
_winapi             glob                reprlib             zipimport
_xxsubinterpreters  graphlib            rlcompleter         zlib
_zoneinfo           grep                rpc                 zoneinfo
abc                 gzip                run                 zoomheight
aifc                hashlib             runpy               zzdummy
antigravity         heapq               runscript           

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

