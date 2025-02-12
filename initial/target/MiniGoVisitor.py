# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignment_stmt.
    def visitAssignment_stmt(self, ctx:MiniGoParser.Assignment_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ass_op.
    def visitAss_op(self, ctx:MiniGoParser.Ass_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_stmt.
    def visitIf_stmt(self, ctx:MiniGoParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_stmt.
    def visitElse_stmt(self, ctx:MiniGoParser.Else_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_stmt.
    def visitFor_stmt(self, ctx:MiniGoParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#basic_for.
    def visitBasic_for(self, ctx:MiniGoParser.Basic_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#with_init_con_upd.
    def visitWith_init_con_upd(self, ctx:MiniGoParser.With_init_con_updContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#range_for.
    def visitRange_for(self, ctx:MiniGoParser.Range_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#break_stmt.
    def visitBreak_stmt(self, ctx:MiniGoParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continue_stmt.
    def visitContinue_stmt(self, ctx:MiniGoParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#return_stmt.
    def visitReturn_stmt(self, ctx:MiniGoParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#call_stmt.
    def visitCall_stmt(self, ctx:MiniGoParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#end_stmt.
    def visitEnd_stmt(self, ctx:MiniGoParser.End_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#menthod_decl.
    def visitMenthod_decl(self, ctx:MiniGoParser.Menthod_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#parameter.
    def visitParameter(self, ctx:MiniGoParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#parameterlist.
    def visitParameterlist(self, ctx:MiniGoParser.ParameterlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#signature.
    def visitSignature(self, ctx:MiniGoParser.SignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_decl.
    def visitFunc_decl(self, ctx:MiniGoParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#block.
    def visitBlock(self, ctx:MiniGoParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_expression.
    def visitList_expression(self, ctx:MiniGoParser.List_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_statement.
    def visitList_statement(self, ctx:MiniGoParser.List_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#const_decl_stmt.
    def visitConst_decl_stmt(self, ctx:MiniGoParser.Const_decl_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_decl_stmt.
    def visitVar_decl_stmt(self, ctx:MiniGoParser.Var_decl_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression.
    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#term_1.
    def visitTerm_1(self, ctx:MiniGoParser.Term_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#term_2.
    def visitTerm_2(self, ctx:MiniGoParser.Term_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#term_3.
    def visitTerm_3(self, ctx:MiniGoParser.Term_3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#term_4.
    def visitTerm_4(self, ctx:MiniGoParser.Term_4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#term_5.
    def visitTerm_5(self, ctx:MiniGoParser.Term_5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#term_6.
    def visitTerm_6(self, ctx:MiniGoParser.Term_6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#term_7.
    def visitTerm_7(self, ctx:MiniGoParser.Term_7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primitive_type.
    def visitPrimitive_type(self, ctx:MiniGoParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_lit.
    def visitArray_lit(self, ctx:MiniGoParser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_array_elements.
    def visitList_array_elements(self, ctx:MiniGoParser.List_array_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_element.
    def visitArray_element(self, ctx:MiniGoParser.Array_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_access.
    def visitArray_access(self, ctx:MiniGoParser.Array_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#type_.
    def visitType_(self, ctx:MiniGoParser.Type_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_dimention.
    def visitList_dimention(self, ctx:MiniGoParser.List_dimentionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dimention.
    def visitDimention(self, ctx:MiniGoParser.DimentionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_access.
    def visitStruct_access(self, ctx:MiniGoParser.Struct_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_call.
    def visitFunc_call(self, ctx:MiniGoParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_lit.
    def visitStruct_lit(self, ctx:MiniGoParser.Struct_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_struct_elements.
    def visitList_struct_elements(self, ctx:MiniGoParser.List_struct_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_elements.
    def visitStruct_elements(self, ctx:MiniGoParser.Struct_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#type_decl.
    def visitType_decl(self, ctx:MiniGoParser.Type_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_decl.
    def visitInterface_decl(self, ctx:MiniGoParser.Interface_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_menthod.
    def visitList_menthod(self, ctx:MiniGoParser.List_menthodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#menthod.
    def visitMenthod(self, ctx:MiniGoParser.MenthodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struck_decl.
    def visitStruck_decl(self, ctx:MiniGoParser.Struck_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_field_decl.
    def visitList_field_decl(self, ctx:MiniGoParser.List_field_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field_decl.
    def visitField_decl(self, ctx:MiniGoParser.Field_declContext):
        return self.visitChildren(ctx)



del MiniGoParser