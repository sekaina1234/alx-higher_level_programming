#include <Python.h>
#include <stdio.h>
/**
 * print_python_list - Prints information about a Python list object.
 * @p: Pointer to the PyObject representing the list.
 *
 * This function prints the size and allocated memory of the list, as well as
 * the type and content of each element in the list.
 */
void print_python_list(PyObject *p)
{
Py_ssize_t size, i;
PyObject *item;

if (!PyList_Check(p))
{
printf("[*] Invalid List Object\n");
return;
}

size = PyList_Size(p);

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

for (i = 0; i < size; i++)
{
item = PyList_GetItem(p, i);
printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
}
}
/**
 * print_python_bytes - Prints information about a Python bytes object.
 * @p: Pointer to the PyObject representing the bytes object.
 *
 * This function prints the size and contents of the bytes object.
 */
void print_python_bytes(PyObject *p)
{
Py_ssize_t size, i;
char *str;

if (!PyBytes_Check(p))
{
printf("[.] bytes object info\n");
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = PyBytes_Size(p);
str = PyBytes_AsString(p);

printf("[.] bytes object info\n");
printf("  size: %ld\n", size);
printf("  trying string: %s\n", str);

printf("  first %ld bytes: ", size + 1);
for (i = 0; i < size && i < 10; i++)
printf("%02x ", (unsigned char)str[i]);
printf("\n");
}
