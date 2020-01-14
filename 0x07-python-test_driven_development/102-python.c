#include <Python.h>
#include <stdio.h>
#include <wchar.h>
/**
 * print_python_string -  print some basic info about Python bytes objects
 * @p: Pointer
 *
 * Return: the address of the new node, or NULL if it failed
 */
void print_python_string(PyObject *p);
{
	PyTypeObject *type =  p->ob_type;

	printf("[.] string object info\n");
	if (strcmp(type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
}

