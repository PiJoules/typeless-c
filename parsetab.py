
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftEQGTLTleftPLUSMINUSleftMULTDIVNAME INT FLOAT STRING LPAR RPAR LBRACKET RBRACKET LBRACE RBRACE COLON EQ ASSIGN ARROW LT GT PLUS MINUS MULT DIV WS NEWLINE COMMA INDENT DEDENT RETURN DEF DEFINE ENUM INCLUDE INCLUDE_LOCAL IFmodule : stmt_listmodule : emptystmt_list : stmt_list NEWLINEstmt_list : stmt_list stmtstmt_list : NEWLINEstmt_list : stmtfuncdef : DEF NAME parameters COLON suiteparameters : LPAR RPARparameters : LPAR varargslist RPARvarargslist : name_or_var_declname_or_var_decl : NAME\n                        | var_declvarargslist : varargslist COMMA name_or_var_declstmt : simple_stmt\n            | compound_stmtsimple_stmt : small_stmt NEWLINEsmall_stmt : return_stmt\n                  | include_stmt\n                  | define_stmt\n                  | expr_stmt\n                  | assign_stmt\n                  | func_decl\n                  | var_decl\n                  | enum_declenum_decl : ENUM NAME LBRACE enum_name_list RBRACEenum_name_list : NAMEenum_name_list : enum_name_list COMMA NAMEfunc_decl : DEF NAME parametersfunc_decl : DEF NAME parameters ARROW type_declarationvar_decl : NAME COLON type_declarationvar_decl : NAME COLON type_declaration ASSIGN exprtype_declaration : NAMEtype_declaration : LBRACE type_declaration RBRACEtype_declaration : inline_func_declinline_func_decl : param_type_list ARROW type_declarationparam_type_list : LPAR RPARparam_type_list : LPAR param_list_contents RPARparam_list_contents : type_declarationparam_list_contents : param_list_contents COMMA type_declarationtype_declaration : type_declaration bracket_listpointer_or_array : pointer\n                        | arraybracket_list : pointer_or_arraybracket_list : bracket_list pointer_or_arraypointer : LBRACKET RBRACKETarray : LBRACKET expr RBRACKETinclude_stmt : INCLUDE STRINGinclude_stmt : INCLUDE_LOCAL STRINGexpr_stmt : exprassign_stmt : expr ASSIGN exprreturn_stmt : RETURN exprdefine_stmt : DEFINE NAME exprdefine_stmt : DEFINE NAMEcompound_stmt : if_stmt\n                     | funcdefif_stmt : IF expr COLON suitesuite : NEWLINE INDENT stmts DEDENTstmts : stmtstmts : stmts stmtexpr : expr PLUS expr\n            | expr MINUS expr\n            | expr MULT expr\n            | expr DIV expr\n            | expr LT expr\n            | expr EQ expr\n            | expr GT expr\n            | powerexpr : LPAR expr RPARexpr : LPAR type_declaration RPAR exprexpr : PLUS exprexpr : MINUS exprpower : atompower : atom traileratom : NAMEatom : INTatom : FLOATatom : STRINGatom : LBRACKET RBRACKETatom : LBRACKET array_contents RBRACKETarray_contents : exprarray_contents : array_contents COMMA exprtrailer : LPAR arglist RPARtrailer : LPAR RPARtestlist : testlist_multi COMMA\n                | testlist_multi testlist_multi : testlist_multi COMMA expr\n                      | exprarglist : arglist COMMA argument\n               | argumentargument : exprempty : '
    
_lr_action_items = {'IF':([0,2,6,21,23,25,32,33,37,66,67,124,131,137,142,143,144,145,],[28,-6,-5,-55,-54,-14,-15,28,-16,-4,-3,-56,-7,28,-58,28,-59,-57,]),'GT':([7,10,12,16,24,30,36,38,39,48,52,55,58,60,61,63,65,71,72,73,74,75,76,77,78,83,96,98,102,103,111,112,123,127,139,],[41,-76,-77,-75,-67,-72,-74,-71,-74,41,41,-74,-70,41,-78,41,-73,-63,-66,-62,-65,41,-60,-64,-61,-68,41,-79,41,-83,41,41,41,-82,41,]),'FLOAT':([0,2,5,6,8,9,18,21,23,25,26,28,32,33,37,40,41,42,43,44,45,46,47,53,59,64,66,67,88,91,97,124,126,128,131,137,142,143,144,145,],[10,-6,10,-5,10,10,10,-55,-54,-14,10,10,-15,10,-16,10,10,10,10,10,10,10,10,10,10,10,-4,-3,10,10,10,-56,10,10,-7,10,-58,10,-59,-57,]),'PLUS':([0,2,5,6,7,8,9,10,12,16,18,21,23,24,25,26,28,30,32,33,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,55,58,59,60,61,63,64,65,66,67,71,72,73,74,75,76,77,78,83,88,91,96,97,98,102,103,111,112,123,124,126,127,128,131,137,139,142,143,144,145,],[18,-6,18,-5,45,18,18,-76,-77,-75,18,-55,-54,-67,-14,18,18,-72,-15,18,-74,-16,-71,-74,18,18,18,18,18,18,18,18,45,45,18,-74,-70,18,45,-78,45,18,-73,-4,-3,-63,45,-62,45,45,-60,45,-61,-68,18,18,45,18,-79,45,-83,45,45,45,-56,18,-82,18,-7,18,45,-58,18,-59,-57,]),'INT':([0,2,5,6,8,9,18,21,23,25,26,28,32,33,37,40,41,42,43,44,45,46,47,53,59,64,66,67,88,91,97,124,126,128,131,137,142,143,144,145,],[16,-6,16,-5,16,16,16,-55,-54,-14,16,16,-15,16,-16,16,16,16,16,16,16,16,16,16,16,16,-4,-3,16,16,16,-56,16,16,-7,16,-58,16,-59,-57,]),'ARROW':([49,85,93,109,120,134,],[79,-36,115,-37,-8,-9,]),'RBRACE':([50,80,82,87,89,90,92,105,106,110,113,121,122,130,141,],[-34,106,-32,-43,-41,-42,-40,-35,-33,-45,-44,135,-26,-46,-27,]),'DEFINE':([0,2,6,21,23,25,32,33,37,66,67,124,131,137,142,143,144,145,],[22,-6,-5,-55,-54,-14,-15,22,-16,-4,-3,-56,-7,22,-58,22,-59,-57,]),'EQ':([7,10,12,16,24,30,36,38,39,48,52,55,58,60,61,63,65,71,72,73,74,75,76,77,78,83,96,98,102,103,111,112,123,127,139,],[43,-76,-77,-75,-67,-72,-74,-71,-74,43,43,-74,-70,43,-78,43,-73,-63,-66,-62,-65,43,-60,-64,-61,-68,43,-79,43,-83,43,43,43,-82,43,]),'MINUS':([0,2,5,6,7,8,9,10,12,16,18,21,23,24,25,26,28,30,32,33,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,55,58,59,60,61,63,64,65,66,67,71,72,73,74,75,76,77,78,83,88,91,96,97,98,102,103,111,112,123,124,126,127,128,131,137,139,142,143,144,145,],[5,-6,5,-5,47,5,5,-76,-77,-75,5,-55,-54,-67,-14,5,5,-72,-15,5,-74,-16,-71,-74,5,5,5,5,5,5,5,5,47,47,5,-74,-70,5,47,-78,47,5,-73,-4,-3,-63,47,-62,47,47,-60,47,-61,-68,5,5,47,5,-79,47,-83,47,47,47,-56,5,-82,5,-7,5,47,-58,5,-59,-57,]),'LBRACE':([9,51,53,57,70,79,81,108,115,],[51,51,51,95,51,51,51,51,51,]),'COMMA':([10,12,16,24,30,38,39,50,55,58,60,61,62,65,71,72,73,74,76,77,78,82,83,84,86,87,89,90,92,98,100,101,102,103,104,105,106,107,110,112,113,116,117,118,119,121,122,123,127,129,130,138,139,140,141,],[-76,-77,-75,-67,-72,-71,-74,-34,-32,-70,-80,-78,97,-73,-63,-66,-62,-65,-60,-64,-61,-32,-68,108,-38,-43,-41,-42,-40,-79,-89,126,-90,-83,-30,-35,-33,-38,-45,-69,-44,133,-12,-11,-10,136,-26,-81,-82,-39,-46,-88,-31,-13,-27,]),'RBRACKET':([10,12,16,24,26,30,38,39,58,60,61,62,65,71,72,73,74,76,77,78,83,88,98,103,111,112,123,127,],[-76,-77,-75,-67,61,-72,-71,-74,-70,-80,-78,98,-73,-63,-66,-62,-65,-60,-64,-61,-68,110,-79,-83,130,-69,-81,-82,]),'NEWLINE':([0,1,2,3,4,6,7,10,11,12,15,16,19,20,21,23,24,25,29,30,31,32,33,36,37,38,39,48,50,58,59,61,65,66,67,68,69,71,72,73,74,75,76,77,78,82,83,87,89,90,92,93,96,98,99,103,104,105,106,110,112,113,114,120,124,127,130,131,132,134,135,139,145,],[6,-24,-6,37,-18,-5,-49,-76,-21,-77,-17,-75,-19,-23,-55,-54,-67,-14,-22,-72,-20,-15,67,-74,-16,-71,-74,-51,-34,-70,-53,-78,-73,-4,-3,-48,-47,-63,-66,-62,-65,-50,-60,-64,-61,-32,-68,-43,-41,-42,-40,-28,-52,-79,125,-83,-30,-35,-33,-45,-69,-44,125,-8,-56,-82,-46,-7,-29,-9,-25,-31,-57,]),'LBRACKET':([0,2,5,6,8,9,18,21,23,25,26,28,32,33,37,40,41,42,43,44,45,46,47,50,53,54,55,59,64,66,67,80,82,86,87,88,89,90,91,92,97,104,105,106,107,110,113,124,126,128,129,130,131,132,137,142,143,144,145,],[26,-6,26,-5,26,26,26,-55,-54,-14,26,26,-15,26,-16,26,26,26,26,26,26,26,26,-34,26,88,-32,26,26,-4,-3,88,-32,88,-43,26,-41,-42,26,88,26,88,88,-33,88,-45,-44,-56,26,26,88,-46,-7,88,26,-58,26,-59,-57,]),'RETURN':([0,2,6,21,23,25,32,33,37,66,67,124,131,137,142,143,144,145,],[8,-6,-5,-55,-54,-14,-15,8,-16,-4,-3,-56,-7,8,-58,8,-59,-57,]),'COLON':([10,12,16,24,30,36,38,39,58,61,63,65,71,72,73,74,76,77,78,83,93,98,103,112,118,120,127,134,],[-76,-77,-75,-67,-72,70,-71,-74,-70,-78,99,-73,-63,-66,-62,-65,-60,-64,-61,-68,114,-79,-83,-69,70,-8,-82,-9,]),'ASSIGN':([7,10,12,16,24,30,36,38,39,50,58,61,65,71,72,73,74,76,77,78,82,83,87,89,90,92,98,103,104,105,106,110,112,113,127,130,],[44,-76,-77,-75,-67,-72,-74,-71,-74,-34,-70,-78,-73,-63,-66,-62,-65,-60,-64,-61,-32,-68,-43,-41,-42,-40,-79,-83,128,-35,-33,-45,-69,-44,-82,-46,]),'INDENT':([125,],[137,]),'LT':([7,10,12,16,24,30,36,38,39,48,52,55,58,60,61,63,65,71,72,73,74,75,76,77,78,83,96,98,102,103,111,112,123,127,139,],[46,-76,-77,-75,-67,-72,-74,-71,-74,46,46,-74,-70,46,-78,46,-73,-63,-66,-62,-65,46,-60,-64,-61,-68,46,-79,46,-83,46,46,46,-82,46,]),'RPAR':([10,12,16,24,30,38,39,50,52,53,54,55,58,61,64,65,71,72,73,74,76,77,78,81,82,83,84,86,87,89,90,92,94,98,100,101,102,103,104,105,106,107,110,112,113,116,117,118,119,127,129,130,138,139,140,],[-76,-77,-75,-67,-72,-71,-74,-34,83,85,91,-32,-70,-78,103,-73,-63,-66,-62,-65,-60,-64,-61,85,-32,-68,109,91,-43,-41,-42,-40,120,-79,-89,127,-90,-83,-30,-35,-33,-38,-45,-69,-44,134,-12,-11,-10,-82,-39,-46,-88,-31,-13,]),'DIV':([7,10,12,16,24,30,36,38,39,48,52,55,58,60,61,63,65,71,72,73,74,75,76,77,78,83,96,98,102,103,111,112,123,127,139,],[40,-76,-77,-75,-67,-72,-74,40,-74,40,40,-74,40,40,-78,40,-73,-63,40,-62,40,40,40,40,40,-68,40,-79,40,-83,40,40,40,-82,40,]),'LPAR':([0,2,5,6,8,9,10,12,16,18,21,23,25,26,28,30,32,33,36,37,39,40,41,42,43,44,45,46,47,51,53,55,56,59,61,64,66,67,70,79,81,88,91,97,98,108,115,124,126,128,131,137,142,143,144,145,],[9,-6,9,-5,9,53,-76,-77,-75,9,-55,-54,-14,9,9,64,-15,9,-74,-16,-74,9,9,9,9,9,9,9,9,81,53,-74,94,9,-78,9,-4,-3,81,81,81,9,9,9,-79,81,81,-56,9,9,-7,9,-58,9,-59,-57,]),'STRING':([0,2,5,6,8,9,18,21,23,25,26,28,32,33,34,35,37,40,41,42,43,44,45,46,47,53,59,64,66,67,88,91,97,124,126,128,131,137,142,143,144,145,],[12,-6,12,-5,12,12,12,-55,-54,-14,12,12,-15,12,68,69,-16,12,12,12,12,12,12,12,12,12,12,12,-4,-3,12,12,12,-56,12,12,-7,12,-58,12,-59,-57,]),'MULT':([7,10,12,16,24,30,36,38,39,48,52,55,58,60,61,63,65,71,72,73,74,75,76,77,78,83,96,98,102,103,111,112,123,127,139,],[42,-76,-77,-75,-67,-72,-74,42,-74,42,42,-74,42,42,-78,42,-73,-63,42,-62,42,42,42,42,42,-68,42,-79,42,-83,42,42,42,-82,42,]),'DEDENT':([21,23,25,32,37,124,131,142,143,144,145,],[-55,-54,-14,-15,-16,-56,-7,-58,145,-59,-57,]),'DEF':([0,2,6,21,23,25,32,33,37,66,67,124,131,137,142,143,144,145,],[13,-6,-5,-55,-54,-14,-15,13,-16,-4,-3,-56,-7,13,-58,13,-59,-57,]),'$end':([0,2,6,17,21,23,25,27,32,33,37,66,67,124,131,145,],[-91,-6,-5,0,-55,-54,-14,-2,-15,-1,-16,-4,-3,-56,-7,-57,]),'ENUM':([0,2,6,21,23,25,32,33,37,66,67,124,131,137,142,143,144,145,],[14,-6,-5,-55,-54,-14,-15,14,-16,-4,-3,-56,-7,14,-58,14,-59,-57,]),'INCLUDE_LOCAL':([0,2,6,21,23,25,32,33,37,66,67,124,131,137,142,143,144,145,],[34,-6,-5,-55,-54,-14,-15,34,-16,-4,-3,-56,-7,34,-58,34,-59,-57,]),'INCLUDE':([0,2,6,21,23,25,32,33,37,66,67,124,131,137,142,143,144,145,],[35,-6,-5,-55,-54,-14,-15,35,-16,-4,-3,-56,-7,35,-58,35,-59,-57,]),'NAME':([0,2,5,6,8,9,13,14,18,21,22,23,25,26,28,32,33,37,40,41,42,43,44,45,46,47,51,53,59,64,66,67,70,79,81,88,91,94,95,97,108,115,124,126,128,131,133,136,137,142,143,144,145,],[36,-6,39,-5,39,55,56,57,39,-55,59,-54,-14,39,39,-15,36,-16,39,39,39,39,39,39,39,39,82,55,39,39,-4,-3,82,82,82,39,39,118,122,39,82,82,-56,39,39,-7,118,141,36,-58,36,-59,-57,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'return_stmt':([0,33,137,143,],[15,15,15,15,]),'enum_name_list':([95,],[121,]),'enum_decl':([0,33,137,143,],[1,1,1,1,]),'stmt':([0,33,137,143,],[2,66,142,144,]),'argument':([64,126,],[100,138,]),'func_decl':([0,33,137,143,],[29,29,29,29,]),'trailer':([30,],[65,]),'define_stmt':([0,33,137,143,],[19,19,19,19,]),'var_decl':([0,33,94,133,137,143,],[20,20,117,117,20,20,]),'small_stmt':([0,33,137,143,],[3,3,3,3,]),'array':([54,80,86,92,104,105,107,129,132,],[90,90,90,90,90,90,90,90,90,]),'assign_stmt':([0,33,137,143,],[11,11,11,11,]),'if_stmt':([0,33,137,143,],[23,23,23,23,]),'include_stmt':([0,33,137,143,],[4,4,4,4,]),'param_list_contents':([53,81,],[84,84,]),'power':([0,5,8,9,18,26,28,33,40,41,42,43,44,45,46,47,53,59,64,88,91,97,126,128,137,143,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'param_type_list':([9,51,53,70,79,81,108,115,],[49,49,49,49,49,49,49,49,]),'inline_func_decl':([9,51,53,70,79,81,108,115,],[50,50,50,50,50,50,50,50,]),'simple_stmt':([0,33,137,143,],[25,25,25,25,]),'funcdef':([0,33,137,143,],[21,21,21,21,]),'suite':([99,114,],[124,131,]),'expr':([0,5,8,9,18,26,28,33,40,41,42,43,44,45,46,47,53,59,64,88,91,97,126,128,137,143,],[7,38,48,52,58,60,63,7,71,72,73,74,75,76,77,78,52,96,102,111,112,123,102,139,7,7,]),'parameters':([56,],[93,]),'empty':([0,],[27,]),'array_contents':([26,],[62,]),'atom':([0,5,8,9,18,26,28,33,40,41,42,43,44,45,46,47,53,59,64,88,91,97,126,128,137,143,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'arglist':([64,],[101,]),'name_or_var_decl':([94,133,],[119,140,]),'expr_stmt':([0,33,137,143,],[31,31,31,31,]),'module':([0,],[17,]),'bracket_list':([54,80,86,104,105,107,129,132,],[92,92,92,92,92,92,92,92,]),'pointer_or_array':([54,80,86,92,104,105,107,129,132,],[87,87,87,113,87,87,87,87,87,]),'type_declaration':([9,51,53,70,79,81,108,115,],[54,80,86,104,105,107,129,132,]),'compound_stmt':([0,33,137,143,],[32,32,32,32,]),'pointer':([54,80,86,92,104,105,107,129,132,],[89,89,89,89,89,89,89,89,89,]),'stmts':([137,],[143,]),'stmt_list':([0,],[33,]),'varargslist':([94,],[116,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> module","S'",1,None,None,None),
  ('module -> stmt_list','module',1,'p_module','cparse.py',16),
  ('module -> empty','module',1,'p_empty_module','cparse.py',20),
  ('stmt_list -> stmt_list NEWLINE','stmt_list',2,'p_stmt_list_1','cparse.py',26),
  ('stmt_list -> stmt_list stmt','stmt_list',2,'p_stmt_list_2','cparse.py',31),
  ('stmt_list -> NEWLINE','stmt_list',1,'p_stmt_list_3','cparse.py',37),
  ('stmt_list -> stmt','stmt_list',1,'p_stmt_list_4','cparse.py',42),
  ('funcdef -> DEF NAME parameters COLON suite','funcdef',5,'p_funcdef','cparse.py',93),
  ('parameters -> LPAR RPAR','parameters',2,'p_parameters_empty','cparse.py',105),
  ('parameters -> LPAR varargslist RPAR','parameters',3,'p_parameters_exist','cparse.py',110),
  ('varargslist -> name_or_var_decl','varargslist',1,'p_varargslist_one','cparse.py',117),
  ('name_or_var_decl -> NAME','name_or_var_decl',1,'p_name_or_var_decl','cparse.py',121),
  ('name_or_var_decl -> var_decl','name_or_var_decl',1,'p_name_or_var_decl','cparse.py',122),
  ('varargslist -> varargslist COMMA name_or_var_decl','varargslist',3,'p_varargslist_many','cparse.py',126),
  ('stmt -> simple_stmt','stmt',1,'p_stmt','cparse.py',131),
  ('stmt -> compound_stmt','stmt',1,'p_stmt','cparse.py',132),
  ('simple_stmt -> small_stmt NEWLINE','simple_stmt',2,'p_simple_stmt','cparse.py',139),
  ('small_stmt -> return_stmt','small_stmt',1,'p_small_stmt','cparse.py',149),
  ('small_stmt -> include_stmt','small_stmt',1,'p_small_stmt','cparse.py',150),
  ('small_stmt -> define_stmt','small_stmt',1,'p_small_stmt','cparse.py',151),
  ('small_stmt -> expr_stmt','small_stmt',1,'p_small_stmt','cparse.py',152),
  ('small_stmt -> assign_stmt','small_stmt',1,'p_small_stmt','cparse.py',153),
  ('small_stmt -> func_decl','small_stmt',1,'p_small_stmt','cparse.py',154),
  ('small_stmt -> var_decl','small_stmt',1,'p_small_stmt','cparse.py',155),
  ('small_stmt -> enum_decl','small_stmt',1,'p_small_stmt','cparse.py',156),
  ('enum_decl -> ENUM NAME LBRACE enum_name_list RBRACE','enum_decl',5,'p_enum_decl','cparse.py',161),
  ('enum_name_list -> NAME','enum_name_list',1,'p_enum_name_list','cparse.py',165),
  ('enum_name_list -> enum_name_list COMMA NAME','enum_name_list',3,'p_enum_name_list_many','cparse.py',169),
  ('func_decl -> DEF NAME parameters','func_decl',3,'p_func_decl','cparse.py',175),
  ('func_decl -> DEF NAME parameters ARROW type_declaration','func_decl',5,'p_func_declwith_ret','cparse.py',181),
  ('var_decl -> NAME COLON type_declaration','var_decl',3,'p_vardecl','cparse.py',187),
  ('var_decl -> NAME COLON type_declaration ASSIGN expr','var_decl',5,'p_vardecl_assign','cparse.py',192),
  ('type_declaration -> NAME','type_declaration',1,'p_declaration_name','cparse.py',197),
  ('type_declaration -> LBRACE type_declaration RBRACE','type_declaration',3,'p_type_declaration_scoped','cparse.py',201),
  ('type_declaration -> inline_func_decl','type_declaration',1,'p_function_declaration','cparse.py',208),
  ('inline_func_decl -> param_type_list ARROW type_declaration','inline_func_decl',3,'p_inline_func_decl','cparse.py',212),
  ('param_type_list -> LPAR RPAR','param_type_list',2,'p_param_type_list_empty','cparse.py',216),
  ('param_type_list -> LPAR param_list_contents RPAR','param_type_list',3,'p_param_type_list_something','cparse.py',220),
  ('param_list_contents -> type_declaration','param_list_contents',1,'p_param_list_contents','cparse.py',224),
  ('param_list_contents -> param_list_contents COMMA type_declaration','param_list_contents',3,'p_param_list_contents_many','cparse.py',228),
  ('type_declaration -> type_declaration bracket_list','type_declaration',2,'p_declaration_array','cparse.py',235),
  ('pointer_or_array -> pointer','pointer_or_array',1,'p_pointer_or_array','cparse.py',251),
  ('pointer_or_array -> array','pointer_or_array',1,'p_pointer_or_array','cparse.py',252),
  ('bracket_list -> pointer_or_array','bracket_list',1,'p_bracket_list_one','cparse.py',256),
  ('bracket_list -> bracket_list pointer_or_array','bracket_list',2,'p_bracket_list_many','cparse.py',260),
  ('pointer -> LBRACKET RBRACKET','pointer',2,'p_pointer','cparse.py',264),
  ('array -> LBRACKET expr RBRACKET','array',3,'p_array','cparse.py',268),
  ('include_stmt -> INCLUDE STRING','include_stmt',2,'p_include_standard','cparse.py',273),
  ('include_stmt -> INCLUDE_LOCAL STRING','include_stmt',2,'p_include_local','cparse.py',278),
  ('expr_stmt -> expr','expr_stmt',1,'p_expr_stmt','cparse.py',283),
  ('assign_stmt -> expr ASSIGN expr','assign_stmt',3,'p_assign','cparse.py',288),
  ('return_stmt -> RETURN expr','return_stmt',2,'p_return_stmt','cparse.py',293),
  ('define_stmt -> DEFINE NAME expr','define_stmt',3,'p_define_stmt','cparse.py',298),
  ('define_stmt -> DEFINE NAME','define_stmt',2,'p_define_stmt_empty','cparse.py',303),
  ('compound_stmt -> if_stmt','compound_stmt',1,'p_compound_stmt','cparse.py',310),
  ('compound_stmt -> funcdef','compound_stmt',1,'p_compound_stmt','cparse.py',311),
  ('if_stmt -> IF expr COLON suite','if_stmt',4,'p_if_stmt','cparse.py',316),
  ('suite -> NEWLINE INDENT stmts DEDENT','suite',4,'p_suite','cparse.py',321),
  ('stmts -> stmt','stmts',1,'p_stmts_1','cparse.py',326),
  ('stmts -> stmts stmt','stmts',2,'p_stmts_2','cparse.py',331),
  ('expr -> expr PLUS expr','expr',3,'p_comparison','cparse.py',361),
  ('expr -> expr MINUS expr','expr',3,'p_comparison','cparse.py',362),
  ('expr -> expr MULT expr','expr',3,'p_comparison','cparse.py',363),
  ('expr -> expr DIV expr','expr',3,'p_comparison','cparse.py',364),
  ('expr -> expr LT expr','expr',3,'p_comparison','cparse.py',365),
  ('expr -> expr EQ expr','expr',3,'p_comparison','cparse.py',366),
  ('expr -> expr GT expr','expr',3,'p_comparison','cparse.py',367),
  ('expr -> power','expr',1,'p_comparison','cparse.py',368),
  ('expr -> LPAR expr RPAR','expr',3,'p_comparison_scoped','cparse.py',375),
  ('expr -> LPAR type_declaration RPAR expr','expr',4,'p_comparison_cast','cparse.py',379),
  ('expr -> PLUS expr','expr',2,'p_comparison_uadd','cparse.py',384),
  ('expr -> MINUS expr','expr',2,'p_comparison_usub','cparse.py',389),
  ('power -> atom','power',1,'p_power_1','cparse.py',399),
  ('power -> atom trailer','power',2,'p_power_2','cparse.py',404),
  ('atom -> NAME','atom',1,'p_atom_name','cparse.py',409),
  ('atom -> INT','atom',1,'p_atom_int','cparse.py',414),
  ('atom -> FLOAT','atom',1,'p_atom_float','cparse.py',418),
  ('atom -> STRING','atom',1,'p_atom_str','cparse.py',423),
  ('atom -> LBRACKET RBRACKET','atom',2,'p_atom_array_empty','cparse.py',427),
  ('atom -> LBRACKET array_contents RBRACKET','atom',3,'p_atom_array','cparse.py',431),
  ('array_contents -> expr','array_contents',1,'p_array_litral_contents','cparse.py',435),
  ('array_contents -> array_contents COMMA expr','array_contents',3,'p_array_litral_contents_2','cparse.py',439),
  ('trailer -> LPAR arglist RPAR','trailer',3,'p_trailer','cparse.py',451),
  ('trailer -> LPAR RPAR','trailer',2,'p_trailer_empty','cparse.py',455),
  ('testlist -> testlist_multi COMMA','testlist',2,'p_testlist','cparse.py',463),
  ('testlist -> testlist_multi','testlist',1,'p_testlist','cparse.py',464),
  ('testlist_multi -> testlist_multi COMMA expr','testlist_multi',3,'p_testlist_multi','cparse.py',479),
  ('testlist_multi -> expr','testlist_multi',1,'p_testlist_multi','cparse.py',480),
  ('arglist -> arglist COMMA argument','arglist',3,'p_arglist','cparse.py',495),
  ('arglist -> argument','arglist',1,'p_arglist','cparse.py',496),
  ('argument -> expr','argument',1,'p_argument','cparse.py',505),
  ('empty -> <empty>','empty',0,'p_empty','cparse.py',509),
]
