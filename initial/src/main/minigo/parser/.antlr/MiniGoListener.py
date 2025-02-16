# Generated from c:/Users/thinh/Documents/GitHub/PPL_1/initial/src/main/minigo/parser/MiniGo.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete listener for a parse tree produced by MiniGoParser.
class MiniGoListener(ParseTreeListener):

    # Enter a parse tree produced by MiniGoParser#program.
    def enterProgram(self, ctx:MiniGoParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniGoParser#program.
    def exitProgram(self, ctx:MiniGoParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniGoParser#statement.
    def enterStatement(self, ctx:MiniGoParser.StatementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#statement.
    def exitStatement(self, ctx:MiniGoParser.StatementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#assignment_stmt.
    def enterAssignment_stmt(self, ctx:MiniGoParser.Assignment_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#assignment_stmt.
    def exitAssignment_stmt(self, ctx:MiniGoParser.Assignment_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#ass_op.
    def enterAss_op(self, ctx:MiniGoParser.Ass_opContext):
        pass

    # Exit a parse tree produced by MiniGoParser#ass_op.
    def exitAss_op(self, ctx:MiniGoParser.Ass_opContext):
        pass


    # Enter a parse tree produced by MiniGoParser#if_stmt.
    def enterIf_stmt(self, ctx:MiniGoParser.If_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#if_stmt.
    def exitIf_stmt(self, ctx:MiniGoParser.If_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#else_stmt.
    def enterElse_stmt(self, ctx:MiniGoParser.Else_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#else_stmt.
    def exitElse_stmt(self, ctx:MiniGoParser.Else_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#for_stmt.
    def enterFor_stmt(self, ctx:MiniGoParser.For_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#for_stmt.
    def exitFor_stmt(self, ctx:MiniGoParser.For_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#basic_for.
    def enterBasic_for(self, ctx:MiniGoParser.Basic_forContext):
        pass

    # Exit a parse tree produced by MiniGoParser#basic_for.
    def exitBasic_for(self, ctx:MiniGoParser.Basic_forContext):
        pass


    # Enter a parse tree produced by MiniGoParser#with_init_con_upd.
    def enterWith_init_con_upd(self, ctx:MiniGoParser.With_init_con_updContext):
        pass

    # Exit a parse tree produced by MiniGoParser#with_init_con_upd.
    def exitWith_init_con_upd(self, ctx:MiniGoParser.With_init_con_updContext):
        pass


    # Enter a parse tree produced by MiniGoParser#range_for.
    def enterRange_for(self, ctx:MiniGoParser.Range_forContext):
        pass

    # Exit a parse tree produced by MiniGoParser#range_for.
    def exitRange_for(self, ctx:MiniGoParser.Range_forContext):
        pass


    # Enter a parse tree produced by MiniGoParser#break_stmt.
    def enterBreak_stmt(self, ctx:MiniGoParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#break_stmt.
    def exitBreak_stmt(self, ctx:MiniGoParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#continue_stmt.
    def enterContinue_stmt(self, ctx:MiniGoParser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#continue_stmt.
    def exitContinue_stmt(self, ctx:MiniGoParser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#return_stmt.
    def enterReturn_stmt(self, ctx:MiniGoParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#return_stmt.
    def exitReturn_stmt(self, ctx:MiniGoParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#call_stmt.
    def enterCall_stmt(self, ctx:MiniGoParser.Call_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#call_stmt.
    def exitCall_stmt(self, ctx:MiniGoParser.Call_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#end_stmt.
    def enterEnd_stmt(self, ctx:MiniGoParser.End_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#end_stmt.
    def exitEnd_stmt(self, ctx:MiniGoParser.End_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#menthod_decl.
    def enterMenthod_decl(self, ctx:MiniGoParser.Menthod_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#menthod_decl.
    def exitMenthod_decl(self, ctx:MiniGoParser.Menthod_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#parameter.
    def enterParameter(self, ctx:MiniGoParser.ParameterContext):
        pass

    # Exit a parse tree produced by MiniGoParser#parameter.
    def exitParameter(self, ctx:MiniGoParser.ParameterContext):
        pass


    # Enter a parse tree produced by MiniGoParser#parameterlist.
    def enterParameterlist(self, ctx:MiniGoParser.ParameterlistContext):
        pass

    # Exit a parse tree produced by MiniGoParser#parameterlist.
    def exitParameterlist(self, ctx:MiniGoParser.ParameterlistContext):
        pass


    # Enter a parse tree produced by MiniGoParser#signature.
    def enterSignature(self, ctx:MiniGoParser.SignatureContext):
        pass

    # Exit a parse tree produced by MiniGoParser#signature.
    def exitSignature(self, ctx:MiniGoParser.SignatureContext):
        pass


    # Enter a parse tree produced by MiniGoParser#func_decl.
    def enterFunc_decl(self, ctx:MiniGoParser.Func_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#func_decl.
    def exitFunc_decl(self, ctx:MiniGoParser.Func_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#block.
    def enterBlock(self, ctx:MiniGoParser.BlockContext):
        pass

    # Exit a parse tree produced by MiniGoParser#block.
    def exitBlock(self, ctx:MiniGoParser.BlockContext):
        pass


    # Enter a parse tree produced by MiniGoParser#list_expression.
    def enterList_expression(self, ctx:MiniGoParser.List_expressionContext):
        pass

    # Exit a parse tree produced by MiniGoParser#list_expression.
    def exitList_expression(self, ctx:MiniGoParser.List_expressionContext):
        pass


    # Enter a parse tree produced by MiniGoParser#list_statement.
    def enterList_statement(self, ctx:MiniGoParser.List_statementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#list_statement.
    def exitList_statement(self, ctx:MiniGoParser.List_statementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#const_decl_stmt.
    def enterConst_decl_stmt(self, ctx:MiniGoParser.Const_decl_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#const_decl_stmt.
    def exitConst_decl_stmt(self, ctx:MiniGoParser.Const_decl_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#var_decl_stmt.
    def enterVar_decl_stmt(self, ctx:MiniGoParser.Var_decl_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#var_decl_stmt.
    def exitVar_decl_stmt(self, ctx:MiniGoParser.Var_decl_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#expression.
    def enterExpression(self, ctx:MiniGoParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MiniGoParser#expression.
    def exitExpression(self, ctx:MiniGoParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MiniGoParser#term_1.
    def enterTerm_1(self, ctx:MiniGoParser.Term_1Context):
        pass

    # Exit a parse tree produced by MiniGoParser#term_1.
    def exitTerm_1(self, ctx:MiniGoParser.Term_1Context):
        pass


    # Enter a parse tree produced by MiniGoParser#term_2.
    def enterTerm_2(self, ctx:MiniGoParser.Term_2Context):
        pass

    # Exit a parse tree produced by MiniGoParser#term_2.
    def exitTerm_2(self, ctx:MiniGoParser.Term_2Context):
        pass


    # Enter a parse tree produced by MiniGoParser#term_3.
    def enterTerm_3(self, ctx:MiniGoParser.Term_3Context):
        pass

    # Exit a parse tree produced by MiniGoParser#term_3.
    def exitTerm_3(self, ctx:MiniGoParser.Term_3Context):
        pass


    # Enter a parse tree produced by MiniGoParser#term_4.
    def enterTerm_4(self, ctx:MiniGoParser.Term_4Context):
        pass

    # Exit a parse tree produced by MiniGoParser#term_4.
    def exitTerm_4(self, ctx:MiniGoParser.Term_4Context):
        pass


    # Enter a parse tree produced by MiniGoParser#term_5.
    def enterTerm_5(self, ctx:MiniGoParser.Term_5Context):
        pass

    # Exit a parse tree produced by MiniGoParser#term_5.
    def exitTerm_5(self, ctx:MiniGoParser.Term_5Context):
        pass


    # Enter a parse tree produced by MiniGoParser#term_6.
    def enterTerm_6(self, ctx:MiniGoParser.Term_6Context):
        pass

    # Exit a parse tree produced by MiniGoParser#term_6.
    def exitTerm_6(self, ctx:MiniGoParser.Term_6Context):
        pass


    # Enter a parse tree produced by MiniGoParser#term_7.
    def enterTerm_7(self, ctx:MiniGoParser.Term_7Context):
        pass

    # Exit a parse tree produced by MiniGoParser#term_7.
    def exitTerm_7(self, ctx:MiniGoParser.Term_7Context):
        pass


    # Enter a parse tree produced by MiniGoParser#primitive_type.
    def enterPrimitive_type(self, ctx:MiniGoParser.Primitive_typeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#primitive_type.
    def exitPrimitive_type(self, ctx:MiniGoParser.Primitive_typeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#array_lit.
    def enterArray_lit(self, ctx:MiniGoParser.Array_litContext):
        pass

    # Exit a parse tree produced by MiniGoParser#array_lit.
    def exitArray_lit(self, ctx:MiniGoParser.Array_litContext):
        pass


    # Enter a parse tree produced by MiniGoParser#list_array_elements.
    def enterList_array_elements(self, ctx:MiniGoParser.List_array_elementsContext):
        pass

    # Exit a parse tree produced by MiniGoParser#list_array_elements.
    def exitList_array_elements(self, ctx:MiniGoParser.List_array_elementsContext):
        pass


    # Enter a parse tree produced by MiniGoParser#array_element.
    def enterArray_element(self, ctx:MiniGoParser.Array_elementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#array_element.
    def exitArray_element(self, ctx:MiniGoParser.Array_elementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#array_access.
    def enterArray_access(self, ctx:MiniGoParser.Array_accessContext):
        pass

    # Exit a parse tree produced by MiniGoParser#array_access.
    def exitArray_access(self, ctx:MiniGoParser.Array_accessContext):
        pass


    # Enter a parse tree produced by MiniGoParser#type_.
    def enterType_(self, ctx:MiniGoParser.Type_Context):
        pass

    # Exit a parse tree produced by MiniGoParser#type_.
    def exitType_(self, ctx:MiniGoParser.Type_Context):
        pass


    # Enter a parse tree produced by MiniGoParser#list_dimention.
    def enterList_dimention(self, ctx:MiniGoParser.List_dimentionContext):
        pass

    # Exit a parse tree produced by MiniGoParser#list_dimention.
    def exitList_dimention(self, ctx:MiniGoParser.List_dimentionContext):
        pass


    # Enter a parse tree produced by MiniGoParser#dimention.
    def enterDimention(self, ctx:MiniGoParser.DimentionContext):
        pass

    # Exit a parse tree produced by MiniGoParser#dimention.
    def exitDimention(self, ctx:MiniGoParser.DimentionContext):
        pass


    # Enter a parse tree produced by MiniGoParser#struct_access.
    def enterStruct_access(self, ctx:MiniGoParser.Struct_accessContext):
        pass

    # Exit a parse tree produced by MiniGoParser#struct_access.
    def exitStruct_access(self, ctx:MiniGoParser.Struct_accessContext):
        pass


    # Enter a parse tree produced by MiniGoParser#func_call.
    def enterFunc_call(self, ctx:MiniGoParser.Func_callContext):
        pass

    # Exit a parse tree produced by MiniGoParser#func_call.
    def exitFunc_call(self, ctx:MiniGoParser.Func_callContext):
        pass


    # Enter a parse tree produced by MiniGoParser#struct_lit.
    def enterStruct_lit(self, ctx:MiniGoParser.Struct_litContext):
        pass

    # Exit a parse tree produced by MiniGoParser#struct_lit.
    def exitStruct_lit(self, ctx:MiniGoParser.Struct_litContext):
        pass


    # Enter a parse tree produced by MiniGoParser#list_struct_elements.
    def enterList_struct_elements(self, ctx:MiniGoParser.List_struct_elementsContext):
        pass

    # Exit a parse tree produced by MiniGoParser#list_struct_elements.
    def exitList_struct_elements(self, ctx:MiniGoParser.List_struct_elementsContext):
        pass


    # Enter a parse tree produced by MiniGoParser#struct_elements.
    def enterStruct_elements(self, ctx:MiniGoParser.Struct_elementsContext):
        pass

    # Exit a parse tree produced by MiniGoParser#struct_elements.
    def exitStruct_elements(self, ctx:MiniGoParser.Struct_elementsContext):
        pass


    # Enter a parse tree produced by MiniGoParser#type_decl.
    def enterType_decl(self, ctx:MiniGoParser.Type_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#type_decl.
    def exitType_decl(self, ctx:MiniGoParser.Type_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#interface_decl.
    def enterInterface_decl(self, ctx:MiniGoParser.Interface_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#interface_decl.
    def exitInterface_decl(self, ctx:MiniGoParser.Interface_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#list_menthod.
    def enterList_menthod(self, ctx:MiniGoParser.List_menthodContext):
        pass

    # Exit a parse tree produced by MiniGoParser#list_menthod.
    def exitList_menthod(self, ctx:MiniGoParser.List_menthodContext):
        pass


    # Enter a parse tree produced by MiniGoParser#menthod.
    def enterMenthod(self, ctx:MiniGoParser.MenthodContext):
        pass

    # Exit a parse tree produced by MiniGoParser#menthod.
    def exitMenthod(self, ctx:MiniGoParser.MenthodContext):
        pass


    # Enter a parse tree produced by MiniGoParser#struck_decl.
    def enterStruck_decl(self, ctx:MiniGoParser.Struck_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#struck_decl.
    def exitStruck_decl(self, ctx:MiniGoParser.Struck_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#list_field_decl.
    def enterList_field_decl(self, ctx:MiniGoParser.List_field_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#list_field_decl.
    def exitList_field_decl(self, ctx:MiniGoParser.List_field_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#field_decl.
    def enterField_decl(self, ctx:MiniGoParser.Field_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#field_decl.
    def exitField_decl(self, ctx:MiniGoParser.Field_declContext):
        pass



del MiniGoParser