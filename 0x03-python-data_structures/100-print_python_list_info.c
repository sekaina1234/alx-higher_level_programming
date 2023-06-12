#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
Py_ssize_t size, alloc, i;
PyObject *obj;

size = PyList_Size(p);
alloc = ((PyListObject *)p)->allocated;

printf("[*] Size of the Python List = %zd\n", size);
printf("[*] Allocated = %zd\n", alloc);

for (i = 0; i < size; i++)
{
printf("Element %zd: ", i);

obj = PyList_GetItem(p, i);
printf("%s\n", Py_TYPE(obj)->tp_name);
}
}
