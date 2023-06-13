#define _XOPEN_SOURCE 700

#include <stdio.h>
#include <Python.h>

void print_python_list_info(PyObject *p)
{
PyListObject *list = (PyListObject *)p;
Py_ssize_t size = Py_SIZE(list);
Py_ssize_t i;
PyObject *item;

printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", list->allocated);

for (i = 0; i < size; i++)
{
item = PyList_GET_ITEM(list, i);
printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
}
}
