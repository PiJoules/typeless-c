from lang_ast import *
from cparse import Parser

import os


INIT_TYPES = {"int", "float", "void", "char"}


class Inferer:
    ######### Interface ########

    def __init__(self, init_variables=None, init_types=INIT_TYPES,
                 source_dir=None):
        self.__variables = init_variables or {}
        self.__types = init_types or set()
        self.__source_dir = source_dir or os.getcwd()

    def variables(self):
        return self.__variables

    def types(self):
        return self.__types

    def bind(self, varname, type):
        self.assert_type_exists(type)
        if varname in self.__variables:
            assert self.__variables[varname] == type
        else:
            self.__variables[varname] = type

    def assert_type_exists(self, type):
        if isinstance(type, (Array, Pointer)):
            self.assert_type_exists(type.contents)
        elif not type in self.types():
            raise RuntimeError("Type '{}' not previously declared.".format(type))

    def add_type(self, type):
        self.__types.add(type)

    ######## Type inference ###########

    def infer(self, expr):
        raise NotImplementedError("Unable to infer type for expression {}".format(type(expr)))

    ######## Node checking ###########

    def check_define(self, node):
        if node.value:
            expected_t = self.infer(node.value)
            if node.type:
                assert expected_t == node.type
            else:
                node.type = expected_t
            self.bind(node.name, node.type)

    def check_struct_decl(self, node):
        # Check struct members
        self.add_type(node.struct.name)
        for member, type in node.struct.members().items():
            self.assert_type_exists(type)

    def check_func_decl(self, node):
        func_t = node.type()
        self.assert_type_exists(func_t.returns)
        for param in func_t.params:
            self.assert_type_exists(param)
        self.add_type(func_t)
        self.bind(node.name, func_t)

    def check_include_local(self, node):
        parser = Parser()
        path = os.path.join(self.__source_dir, node.path.s)
        with open(path, "r") as f:
            module_ast = parser.parse(f.read())
            self.check_module(module_ast)

    def check_func_def(self, node):
        name = node.name

        if name in self.variables():
            # Check and match parameters and types
            pass
        else:
            pass

        raise NotImplementedError

    def check(self, node):
        if isinstance(node, Module):
            self.check_module(node)
        elif isinstance(node, list):
            self.check_sequence(node)
        elif isinstance(node, Define):
            self.check_define(node)
        elif isinstance(node, StructDecl):
            self.check_struct_decl(node)
        elif isinstance(node, FuncDecl):
            self.check_func_decl(node)
        elif isinstance(node, IncludeLocal):
            self.check_include_local(node)
        elif isinstance(node, FuncDef):
            self.check_func_def(node)
        elif isinstance(node, (Ifndef, Endif)):
            pass
        else:
            raise RuntimeError("Unable to check node {}".format(type(node)))

    def check_sequence(self, seq):
        for node in seq:
            self.check(node)

    def check_module(self, node):
        self.check_sequence(node.body)
