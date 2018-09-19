#include <Python.h>
#include <stdio.h>


// original function
int calc(int x, int a, int b){
return a*x+b;
}

// wrap the original function
// kwargs are args with default value.
PyObject* calc_(PyObject* self, PyObject* args, PyObject* kwargs){

    // Parse args from python object
    int x, a = 0, b = 0;
    static char *kwlist[]  = {'x', 'a', 'b', NULL}; // must end with NULL
    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "i|ii", kwlist, &x, &a, &b)) {
    return NULL;
    }

    // call original function
    int ret;
    ret = calc(x,a,b);


    // wrap the ret value to python object
    return Py_BuildValue("i", ret);

}


// tell python what is the keywords to call functions
static PyMethodDef SpeedupPerformanceMethods[] = {
  {"calc", (PyCFunction) calc_, METH_VARARGS | METH_KEYWORDS, "A slow calculation method."},
  {NULL, NULL, 0, NULL}  // must end with NULLs
};


