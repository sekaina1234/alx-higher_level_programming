#include <Python.h>
#include <stdio.h>
/**
 * print_python_list - Prints information about a Python list object.
 * @p: Pointer to the Python list object.
 */
void print_python_list(PyObject *p)
{
Py_ssize_t size, i;
PyObject *item;

size = PyList_Size(p);

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %zd\n", size);
printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

for (i = 0; i < size; i++)
{
item = PyList_GetItem(p, i);
printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
}
}
/**
 * print_python_bytes - Prints information about a Python bytes object.
 * @p: Pointer to the Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
Py_ssize_t size, i;
char *string;

printf("[.] bytes object info\n");

if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = PyBytes_Size(p);
string = PyBytes_AsString(p);

printf("  size: %zd\n", size);
printf("  trying string: %s\n", string);

printf("  first %zd bytes: ", (size < 10) ? size + 1 : 10);
for (i = 0; i < ((size < 10) ? size : 10); i++)
{
printf("%02x%c", (unsigned char)string[i],
(i == 9 || i == size - 1) ? '\n' : ' ');
}
}
