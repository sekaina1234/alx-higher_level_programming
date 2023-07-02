#include <Python.h>

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    unsigned char *bytes;

    if (!PyBytes_Check(p)) {
        printf("[.] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    bytes = (unsigned char *)PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", PyBytes_AsString(p));

    printf("  first %ld bytes: ", (size < 10) ? size + 1 : 10);
    for (i = 0; i < size && i < 10; i++) {
        printf("%02x", bytes[i]);
        if (i + 1 < size && i + 1 < 10)
            printf(" ");
    }
    printf("\n");
}
