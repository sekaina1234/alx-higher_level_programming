#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - Prints basic information about a Python list
 * @p: Pointer to the Python list object
 *
 * This function prints the size of the Python list, the allocated size,
 * and the type of each element in the list.
 */
void print_python_list_info(PyObject *p)
{
PyListObject *list = (PyListObject *)p;
Py_ssize_t size = PyList_Size(p);
Py_ssize_t allocated = list->allocated;
Py_ssize_t i;
PyObject *element;
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", allocated);
for (i = 0; i < size; i++)
{
element = PyList_GetItem(p, i);
printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
}
}
