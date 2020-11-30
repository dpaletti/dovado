// Generated from /home/danielepaletti/Nextcloud/POLIMI_disroot/advanced_computer_architectures/project/dovado-rtl/src/dovado_rtl/antlr/grammars/vhdlParser.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class vhdlParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		KW_PROCESS=1, KW_CONTEXT=2, KW_POSTPONED=3, KW_LINKAGE=4, KW_COMPONENT=5, 
		KW_ABS=6, KW_DEFAULT=7, KW_THEN=8, KW_BLOCK=9, KW_REM=10, KW_INERTIAL=11, 
		KW_NEXT=12, KW_ENTITY=13, KW_ON=14, KW_GROUP=15, KW_XNOR=16, KW_FILE=17, 
		KW_PURE=18, KW_GUARDED=19, KW_GENERIC=20, KW_RANGE=21, KW_ELSE=22, KW_USE=23, 
		KW_SHARED=24, KW_MOD=25, KW_LOOP=26, KW_RECORD=27, KW_SIGNAL=28, KW_REJECT=29, 
		KW_BEGIN=30, KW_SLA=31, KW_DISCONNECT=32, KW_OF=33, KW_PROCEDURE=34, KW_SRL=35, 
		KW_VUNIT=36, KW_ATTRIBUTE=37, KW_VARIABLE=38, KW_PROPERTY=39, KW_UNAFFECTED=40, 
		KW_XOR=41, KW_REGISTER=42, KW_SUBTYPE=43, KW_TO=44, KW_NEW=45, KW_REPORT=46, 
		KW_CONSTANT=47, KW_BUFFER=48, KW_BODY=49, KW_AFTER=50, KW_TRANSPORT=51, 
		KW_FUNCTION=52, KW_END=53, KW_SELECT=54, KW_OR=55, KW_LIBRARY=56, KW_ELSIF=57, 
		KW_SLL=58, KW_MAP=59, KW_SRA=60, KW_PROTECTED=61, KW_DOWNTO=62, KW_LABEL=63, 
		KW_ALL=64, KW_ALIAS=65, KW_GENERATE=66, KW_NOR=67, KW_IN=68, KW_RELEASE=69, 
		KW_EXIT=70, KW_RETURN=71, KW_WITH=72, KW_UNTIL=73, KW_AND=74, KW_INOUT=75, 
		KW_WAIT=76, KW_NAND=77, KW_ARRAY=78, KW_FORCE=79, KW_WHILE=80, KW_IMPURE=81, 
		KW_PACKAGE=82, KW_UNITS=83, KW_ASSERT=84, KW_PARAMETER=85, KW_SEVERITY=86, 
		KW_LITERAL=87, KW_FOR=88, KW_ROR=89, KW_IF=90, KW_OUT=91, KW_ROL=92, KW_IS=93, 
		KW_SEQUENCE=94, KW_OTHERS=95, KW_TYPE=96, KW_CASE=97, KW_NOT=98, KW_CONFIGURATION=99, 
		KW_OPEN=100, KW_ARCHITECTURE=101, KW_BUS=102, KW_ACCESS=103, KW_WHEN=104, 
		KW_PORT=105, KW_NULL=106, BASIC_IDENTIFIER=107, EXTENDED_IDENTIFIER=108, 
		DECIMAL_LITERAL=109, INTEGER=110, EXPONENT=111, BASED_LITERAL=112, CHARACTER_LITERAL=113, 
		STRING_LITERAL=114, BIT_STRING_LITERAL=115, COMMENT=116, BLOCK_COMMENT=117, 
		TAB=118, SPACE=119, NEWLINE=120, CR=121, SPACE_CHARACTER=122, DBLQUOTE=123, 
		UNDERSCORE=124, DIGIT=125, SEMI=126, LPAREN=127, RPAREN=128, LSQUARE_BR=129, 
		RSQUARE_BR=130, APOSTROPHE=131, SHIFT_LEFT=132, SHIFT_RIGHT=133, AT=134, 
		HASHTAG=135, COMMA=136, DOT=137, QUESTIONMARK=138, COLON=139, EQ=140, 
		NE=141, LT=142, GT=143, GE=144, EQ_MATCH=145, NE_MATCH=146, LT_MATCH=147, 
		LE_MATCH=148, GT_MATCH=149, GE_MATCH=150, PLUS=151, MINUS=152, AMPERSAND=153, 
		BAR=154, BACKSLASH=155, MUL=156, DIV=157, DOUBLESTAR=158, CONASGN=159, 
		GRAVE_ACCENT=160, UP=161, VARASGN=162, BOX=163, ARROW=164, COND_OP=165;
	public static final int
		RULE_any_keyword = 0, RULE_name_literal = 1, RULE_name = 2, RULE_name_slice_part = 3, 
		RULE_name_attribute_part = 4, RULE_attribute_name = 5, RULE_suffix = 6, 
		RULE_explicit_range = 7, RULE_selected_name = 8, RULE_entity_declaration = 9, 
		RULE_entity_declarative_item = 10, RULE_entity_statement = 11, RULE_architecture_body = 12, 
		RULE_block_declarative_item = 13, RULE_configuration_declaration = 14, 
		RULE_configuration_declarative_item = 15, RULE_block_configuration = 16, 
		RULE_block_specification = 17, RULE_generate_specification = 18, RULE_configuration_item = 19, 
		RULE_component_configuration = 20, RULE_subprogram_declaration = 21, RULE_subprogram_specification = 22, 
		RULE_procedure_specification = 23, RULE_function_specification = 24, RULE_subprogram_header = 25, 
		RULE_designator = 26, RULE_operator_symbol = 27, RULE_formal_parameter_list = 28, 
		RULE_subprogram_body = 29, RULE_subprogram_kind = 30, RULE_subprogram_instantiation_declaration = 31, 
		RULE_signature = 32, RULE_package_declaration = 33, RULE_package_declarative_item = 34, 
		RULE_package_body = 35, RULE_package_instantiation_declaration = 36, RULE_scalar_type_definition = 37, 
		RULE_range_constraint = 38, RULE_range_ = 39, RULE_direction = 40, RULE_enumeration_type_definition = 41, 
		RULE_enumeration_literal = 42, RULE_integer_type_definition = 43, RULE_physical_type_definition = 44, 
		RULE_primary_unit_declaration = 45, RULE_secondary_unit_declaration = 46, 
		RULE_floating_type_definition = 47, RULE_composite_type_definition = 48, 
		RULE_array_type_definition = 49, RULE_unbounded_array_definition = 50, 
		RULE_constrained_array_definition = 51, RULE_index_subtype_definition = 52, 
		RULE_array_constraint = 53, RULE_array_element_constraint = 54, RULE_index_constraint = 55, 
		RULE_discrete_range = 56, RULE_record_type_definition = 57, RULE_element_declaration = 58, 
		RULE_identifier_list = 59, RULE_element_subtype_definition = 60, RULE_record_constraint = 61, 
		RULE_record_element_constraint = 62, RULE_access_type_definition = 63, 
		RULE_incomplete_type_declaration = 64, RULE_file_type_definition = 65, 
		RULE_protected_type_definition = 66, RULE_protected_type_declaration = 67, 
		RULE_protected_type_declarative_item = 68, RULE_protected_type_body = 69, 
		RULE_type_declaration = 70, RULE_full_type_declaration = 71, RULE_type_definition = 72, 
		RULE_subtype_declaration = 73, RULE_subtype_indication = 74, RULE_resolution_indication = 75, 
		RULE_element_resolution = 76, RULE_array_element_resolution = 77, RULE_record_resolution = 78, 
		RULE_record_element_resolution = 79, RULE_type_mark = 80, RULE_constraint = 81, 
		RULE_element_constraint = 82, RULE_object_declaration = 83, RULE_constant_declaration = 84, 
		RULE_signal_declaration = 85, RULE_signal_kind = 86, RULE_variable_declaration = 87, 
		RULE_file_declaration = 88, RULE_file_open_information = 89, RULE_file_logical_name = 90, 
		RULE_interface_declaration = 91, RULE_interface_object_declaration = 92, 
		RULE_interface_constant_declaration = 93, RULE_interface_signal_declaration = 94, 
		RULE_interface_variable_declaration = 95, RULE_interface_file_declaration = 96, 
		RULE_signal_mode = 97, RULE_interface_type_declaration = 98, RULE_interface_incomplete_type_declaration = 99, 
		RULE_interface_subprogram_declaration = 100, RULE_interface_subprogram_specification = 101, 
		RULE_interface_procedure_specification = 102, RULE_interface_function_specification = 103, 
		RULE_interface_subprogram_default = 104, RULE_interface_package_declaration = 105, 
		RULE_interface_package_generic_map_aspect = 106, RULE_interface_list = 107, 
		RULE_interface_element = 108, RULE_generic_clause = 109, RULE_generic_list = 110, 
		RULE_port_clause = 111, RULE_port_list = 112, RULE_association_list = 113, 
		RULE_association_element = 114, RULE_formal_part = 115, RULE_actual_part = 116, 
		RULE_actual_designator = 117, RULE_generic_map_aspect = 118, RULE_port_map_aspect = 119, 
		RULE_alias_declaration = 120, RULE_alias_designator = 121, RULE_attribute_declaration = 122, 
		RULE_component_declaration = 123, RULE_group_template_declaration = 124, 
		RULE_entity_class_entry_list = 125, RULE_entity_class_entry = 126, RULE_group_declaration = 127, 
		RULE_group_constituent_list = 128, RULE_group_constituent = 129, RULE_attribute_specification = 130, 
		RULE_entity_specification = 131, RULE_entity_class = 132, RULE_entity_name_list = 133, 
		RULE_entity_designator = 134, RULE_entity_tag = 135, RULE_configuration_specification = 136, 
		RULE_simple_configuration_specification = 137, RULE_compound_configuration_specification = 138, 
		RULE_component_specification = 139, RULE_instantiation_list = 140, RULE_binding_indication = 141, 
		RULE_entity_aspect = 142, RULE_verification_unit_binding_indication = 143, 
		RULE_verification_unit_list = 144, RULE_disconnection_specification = 145, 
		RULE_guarded_signal_specification = 146, RULE_signal_list = 147, RULE_attribute_designator = 148, 
		RULE_external_name = 149, RULE_external_pathname = 150, RULE_package_pathname = 151, 
		RULE_absolute_pathname = 152, RULE_relative_pathname = 153, RULE_partial_pathname = 154, 
		RULE_pathname_element = 155, RULE_expression = 156, RULE_simple_expression = 157, 
		RULE_primary = 158, RULE_logical_operator = 159, RULE_relational_operator = 160, 
		RULE_shift_operator = 161, RULE_adding_operator = 162, RULE_sign = 163, 
		RULE_multiplying_operator = 164, RULE_miscellaneous_operator = 165, RULE_numeric_literal = 166, 
		RULE_physical_literal = 167, RULE_aggregate = 168, RULE_element_association = 169, 
		RULE_choices = 170, RULE_choice = 171, RULE_qualified_expression = 172, 
		RULE_allocator = 173, RULE_sequence_of_statements = 174, RULE_sequential_statement = 175, 
		RULE_wait_statement = 176, RULE_sensitivity_clause = 177, RULE_sensitivity_list = 178, 
		RULE_condition_clause = 179, RULE_condition = 180, RULE_timeout_clause = 181, 
		RULE_assertion_statement = 182, RULE_assertion = 183, RULE_report_statement = 184, 
		RULE_signal_assignment_statement = 185, RULE_simple_signal_assignment = 186, 
		RULE_simple_waveform_assignment = 187, RULE_simple_force_assignment = 188, 
		RULE_simple_release_assignment = 189, RULE_force_mode = 190, RULE_delay_mechanism = 191, 
		RULE_target = 192, RULE_waveform = 193, RULE_waveform_element = 194, RULE_conditional_signal_assignment = 195, 
		RULE_conditional_waveform_assignment = 196, RULE_conditional_waveforms = 197, 
		RULE_conditional_force_assignment = 198, RULE_conditional_expressions = 199, 
		RULE_selected_signal_assignment = 200, RULE_selected_waveform_assignment = 201, 
		RULE_selected_waveforms = 202, RULE_selected_force_assignment = 203, RULE_selected_expressions = 204, 
		RULE_variable_assignment_statement = 205, RULE_simple_variable_assignment = 206, 
		RULE_conditional_variable_assignment = 207, RULE_selected_variable_assignment = 208, 
		RULE_procedure_call_statement = 209, RULE_procedure_call = 210, RULE_if_statement = 211, 
		RULE_case_statement = 212, RULE_case_statement_alternative = 213, RULE_loop_statement = 214, 
		RULE_iteration_scheme = 215, RULE_parameter_specification = 216, RULE_next_statement = 217, 
		RULE_exit_statement = 218, RULE_return_statement = 219, RULE_null_statement = 220, 
		RULE_concurrent_statement_with_optional_label = 221, RULE_concurrent_statement = 222, 
		RULE_block_statement = 223, RULE_block_header = 224, RULE_process_statement = 225, 
		RULE_process_sensitivity_list = 226, RULE_process_or_package_declarative_item = 227, 
		RULE_process_declarative_item = 228, RULE_concurrent_procedure_call_statement = 229, 
		RULE_concurrent_assertion_statement = 230, RULE_concurrent_signal_assignment_statement = 231, 
		RULE_concurrent_signal_assignment_any = 232, RULE_concurrent_selected_signal_assignment = 233, 
		RULE_component_instantiation_statement = 234, RULE_instantiated_unit = 235, 
		RULE_generate_statement = 236, RULE_for_generate_statement = 237, RULE_if_generate_statement = 238, 
		RULE_case_generate_statement = 239, RULE_case_generate_alternative = 240, 
		RULE_generate_statement_body_with_begin_end = 241, RULE_generate_statement_body = 242, 
		RULE_label = 243, RULE_use_clause = 244, RULE_design_file = 245, RULE_design_unit = 246, 
		RULE_library_unit = 247, RULE_primary_unit = 248, RULE_secondary_unit = 249, 
		RULE_library_clause = 250, RULE_logical_name_list = 251, RULE_context_declaration = 252, 
		RULE_context_clause = 253, RULE_context_item = 254, RULE_context_reference = 255, 
		RULE_identifier = 256;
	private static String[] makeRuleNames() {
		return new String[] {
			"any_keyword", "name_literal", "name", "name_slice_part", "name_attribute_part", 
			"attribute_name", "suffix", "explicit_range", "selected_name", "entity_declaration", 
			"entity_declarative_item", "entity_statement", "architecture_body", "block_declarative_item", 
			"configuration_declaration", "configuration_declarative_item", "block_configuration", 
			"block_specification", "generate_specification", "configuration_item", 
			"component_configuration", "subprogram_declaration", "subprogram_specification", 
			"procedure_specification", "function_specification", "subprogram_header", 
			"designator", "operator_symbol", "formal_parameter_list", "subprogram_body", 
			"subprogram_kind", "subprogram_instantiation_declaration", "signature", 
			"package_declaration", "package_declarative_item", "package_body", "package_instantiation_declaration", 
			"scalar_type_definition", "range_constraint", "range_", "direction", 
			"enumeration_type_definition", "enumeration_literal", "integer_type_definition", 
			"physical_type_definition", "primary_unit_declaration", "secondary_unit_declaration", 
			"floating_type_definition", "composite_type_definition", "array_type_definition", 
			"unbounded_array_definition", "constrained_array_definition", "index_subtype_definition", 
			"array_constraint", "array_element_constraint", "index_constraint", "discrete_range", 
			"record_type_definition", "element_declaration", "identifier_list", "element_subtype_definition", 
			"record_constraint", "record_element_constraint", "access_type_definition", 
			"incomplete_type_declaration", "file_type_definition", "protected_type_definition", 
			"protected_type_declaration", "protected_type_declarative_item", "protected_type_body", 
			"type_declaration", "full_type_declaration", "type_definition", "subtype_declaration", 
			"subtype_indication", "resolution_indication", "element_resolution", 
			"array_element_resolution", "record_resolution", "record_element_resolution", 
			"type_mark", "constraint", "element_constraint", "object_declaration", 
			"constant_declaration", "signal_declaration", "signal_kind", "variable_declaration", 
			"file_declaration", "file_open_information", "file_logical_name", "interface_declaration", 
			"interface_object_declaration", "interface_constant_declaration", "interface_signal_declaration", 
			"interface_variable_declaration", "interface_file_declaration", "signal_mode", 
			"interface_type_declaration", "interface_incomplete_type_declaration", 
			"interface_subprogram_declaration", "interface_subprogram_specification", 
			"interface_procedure_specification", "interface_function_specification", 
			"interface_subprogram_default", "interface_package_declaration", "interface_package_generic_map_aspect", 
			"interface_list", "interface_element", "generic_clause", "generic_list", 
			"port_clause", "port_list", "association_list", "association_element", 
			"formal_part", "actual_part", "actual_designator", "generic_map_aspect", 
			"port_map_aspect", "alias_declaration", "alias_designator", "attribute_declaration", 
			"component_declaration", "group_template_declaration", "entity_class_entry_list", 
			"entity_class_entry", "group_declaration", "group_constituent_list", 
			"group_constituent", "attribute_specification", "entity_specification", 
			"entity_class", "entity_name_list", "entity_designator", "entity_tag", 
			"configuration_specification", "simple_configuration_specification", 
			"compound_configuration_specification", "component_specification", "instantiation_list", 
			"binding_indication", "entity_aspect", "verification_unit_binding_indication", 
			"verification_unit_list", "disconnection_specification", "guarded_signal_specification", 
			"signal_list", "attribute_designator", "external_name", "external_pathname", 
			"package_pathname", "absolute_pathname", "relative_pathname", "partial_pathname", 
			"pathname_element", "expression", "simple_expression", "primary", "logical_operator", 
			"relational_operator", "shift_operator", "adding_operator", "sign", "multiplying_operator", 
			"miscellaneous_operator", "numeric_literal", "physical_literal", "aggregate", 
			"element_association", "choices", "choice", "qualified_expression", "allocator", 
			"sequence_of_statements", "sequential_statement", "wait_statement", "sensitivity_clause", 
			"sensitivity_list", "condition_clause", "condition", "timeout_clause", 
			"assertion_statement", "assertion", "report_statement", "signal_assignment_statement", 
			"simple_signal_assignment", "simple_waveform_assignment", "simple_force_assignment", 
			"simple_release_assignment", "force_mode", "delay_mechanism", "target", 
			"waveform", "waveform_element", "conditional_signal_assignment", "conditional_waveform_assignment", 
			"conditional_waveforms", "conditional_force_assignment", "conditional_expressions", 
			"selected_signal_assignment", "selected_waveform_assignment", "selected_waveforms", 
			"selected_force_assignment", "selected_expressions", "variable_assignment_statement", 
			"simple_variable_assignment", "conditional_variable_assignment", "selected_variable_assignment", 
			"procedure_call_statement", "procedure_call", "if_statement", "case_statement", 
			"case_statement_alternative", "loop_statement", "iteration_scheme", "parameter_specification", 
			"next_statement", "exit_statement", "return_statement", "null_statement", 
			"concurrent_statement_with_optional_label", "concurrent_statement", "block_statement", 
			"block_header", "process_statement", "process_sensitivity_list", "process_or_package_declarative_item", 
			"process_declarative_item", "concurrent_procedure_call_statement", "concurrent_assertion_statement", 
			"concurrent_signal_assignment_statement", "concurrent_signal_assignment_any", 
			"concurrent_selected_signal_assignment", "component_instantiation_statement", 
			"instantiated_unit", "generate_statement", "for_generate_statement", 
			"if_generate_statement", "case_generate_statement", "case_generate_alternative", 
			"generate_statement_body_with_begin_end", "generate_statement_body", 
			"label", "use_clause", "design_file", "design_unit", "library_unit", 
			"primary_unit", "secondary_unit", "library_clause", "logical_name_list", 
			"context_declaration", "context_clause", "context_item", "context_reference", 
			"identifier"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			"'\n'", "'\r'", "' '", "'\"'", "'_'", null, "';'", "'('", "')'", "'['", 
			"']'", "'''", "'<<'", "'>>'", "'@'", "'#'", "','", "'.'", "'?'", "':'", 
			"'='", "'/='", "'<'", "'>'", "'>='", "'?='", "'?/='", "'?<'", "'?<='", 
			"'?>'", "'?>='", "'+'", "'-'", "'&'", "'|'", "'\\'", "'*'", "'/'", "'**'", 
			"'<='", "'`'", "'^'", "':='", "'<>'", "'=>'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "KW_PROCESS", "KW_CONTEXT", "KW_POSTPONED", "KW_LINKAGE", "KW_COMPONENT", 
			"KW_ABS", "KW_DEFAULT", "KW_THEN", "KW_BLOCK", "KW_REM", "KW_INERTIAL", 
			"KW_NEXT", "KW_ENTITY", "KW_ON", "KW_GROUP", "KW_XNOR", "KW_FILE", "KW_PURE", 
			"KW_GUARDED", "KW_GENERIC", "KW_RANGE", "KW_ELSE", "KW_USE", "KW_SHARED", 
			"KW_MOD", "KW_LOOP", "KW_RECORD", "KW_SIGNAL", "KW_REJECT", "KW_BEGIN", 
			"KW_SLA", "KW_DISCONNECT", "KW_OF", "KW_PROCEDURE", "KW_SRL", "KW_VUNIT", 
			"KW_ATTRIBUTE", "KW_VARIABLE", "KW_PROPERTY", "KW_UNAFFECTED", "KW_XOR", 
			"KW_REGISTER", "KW_SUBTYPE", "KW_TO", "KW_NEW", "KW_REPORT", "KW_CONSTANT", 
			"KW_BUFFER", "KW_BODY", "KW_AFTER", "KW_TRANSPORT", "KW_FUNCTION", "KW_END", 
			"KW_SELECT", "KW_OR", "KW_LIBRARY", "KW_ELSIF", "KW_SLL", "KW_MAP", "KW_SRA", 
			"KW_PROTECTED", "KW_DOWNTO", "KW_LABEL", "KW_ALL", "KW_ALIAS", "KW_GENERATE", 
			"KW_NOR", "KW_IN", "KW_RELEASE", "KW_EXIT", "KW_RETURN", "KW_WITH", "KW_UNTIL", 
			"KW_AND", "KW_INOUT", "KW_WAIT", "KW_NAND", "KW_ARRAY", "KW_FORCE", "KW_WHILE", 
			"KW_IMPURE", "KW_PACKAGE", "KW_UNITS", "KW_ASSERT", "KW_PARAMETER", "KW_SEVERITY", 
			"KW_LITERAL", "KW_FOR", "KW_ROR", "KW_IF", "KW_OUT", "KW_ROL", "KW_IS", 
			"KW_SEQUENCE", "KW_OTHERS", "KW_TYPE", "KW_CASE", "KW_NOT", "KW_CONFIGURATION", 
			"KW_OPEN", "KW_ARCHITECTURE", "KW_BUS", "KW_ACCESS", "KW_WHEN", "KW_PORT", 
			"KW_NULL", "BASIC_IDENTIFIER", "EXTENDED_IDENTIFIER", "DECIMAL_LITERAL", 
			"INTEGER", "EXPONENT", "BASED_LITERAL", "CHARACTER_LITERAL", "STRING_LITERAL", 
			"BIT_STRING_LITERAL", "COMMENT", "BLOCK_COMMENT", "TAB", "SPACE", "NEWLINE", 
			"CR", "SPACE_CHARACTER", "DBLQUOTE", "UNDERSCORE", "DIGIT", "SEMI", "LPAREN", 
			"RPAREN", "LSQUARE_BR", "RSQUARE_BR", "APOSTROPHE", "SHIFT_LEFT", "SHIFT_RIGHT", 
			"AT", "HASHTAG", "COMMA", "DOT", "QUESTIONMARK", "COLON", "EQ", "NE", 
			"LT", "GT", "GE", "EQ_MATCH", "NE_MATCH", "LT_MATCH", "LE_MATCH", "GT_MATCH", 
			"GE_MATCH", "PLUS", "MINUS", "AMPERSAND", "BAR", "BACKSLASH", "MUL", 
			"DIV", "DOUBLESTAR", "CONASGN", "GRAVE_ACCENT", "UP", "VARASGN", "BOX", 
			"ARROW", "COND_OP"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "vhdlParser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public vhdlParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class Any_keywordContext extends ParserRuleContext {
		public TerminalNode KW_PROCESS() { return getToken(vhdlParser.KW_PROCESS, 0); }
		public TerminalNode KW_CONTEXT() { return getToken(vhdlParser.KW_CONTEXT, 0); }
		public TerminalNode KW_POSTPONED() { return getToken(vhdlParser.KW_POSTPONED, 0); }
		public TerminalNode KW_LINKAGE() { return getToken(vhdlParser.KW_LINKAGE, 0); }
		public TerminalNode KW_COMPONENT() { return getToken(vhdlParser.KW_COMPONENT, 0); }
		public TerminalNode KW_ABS() { return getToken(vhdlParser.KW_ABS, 0); }
		public TerminalNode KW_DEFAULT() { return getToken(vhdlParser.KW_DEFAULT, 0); }
		public TerminalNode KW_THEN() { return getToken(vhdlParser.KW_THEN, 0); }
		public TerminalNode KW_BLOCK() { return getToken(vhdlParser.KW_BLOCK, 0); }
		public TerminalNode KW_REM() { return getToken(vhdlParser.KW_REM, 0); }
		public TerminalNode KW_INERTIAL() { return getToken(vhdlParser.KW_INERTIAL, 0); }
		public TerminalNode KW_NEXT() { return getToken(vhdlParser.KW_NEXT, 0); }
		public TerminalNode KW_ENTITY() { return getToken(vhdlParser.KW_ENTITY, 0); }
		public TerminalNode KW_ON() { return getToken(vhdlParser.KW_ON, 0); }
		public TerminalNode KW_GROUP() { return getToken(vhdlParser.KW_GROUP, 0); }
		public TerminalNode KW_XNOR() { return getToken(vhdlParser.KW_XNOR, 0); }
		public TerminalNode KW_FILE() { return getToken(vhdlParser.KW_FILE, 0); }
		public TerminalNode KW_PURE() { return getToken(vhdlParser.KW_PURE, 0); }
		public TerminalNode KW_GUARDED() { return getToken(vhdlParser.KW_GUARDED, 0); }
		public TerminalNode KW_GENERIC() { return getToken(vhdlParser.KW_GENERIC, 0); }
		public TerminalNode KW_RANGE() { return getToken(vhdlParser.KW_RANGE, 0); }
		public TerminalNode KW_ELSE() { return getToken(vhdlParser.KW_ELSE, 0); }
		public TerminalNode KW_USE() { return getToken(vhdlParser.KW_USE, 0); }
		public TerminalNode KW_SHARED() { return getToken(vhdlParser.KW_SHARED, 0); }
		public TerminalNode KW_MOD() { return getToken(vhdlParser.KW_MOD, 0); }
		public TerminalNode KW_LOOP() { return getToken(vhdlParser.KW_LOOP, 0); }
		public TerminalNode KW_RECORD() { return getToken(vhdlParser.KW_RECORD, 0); }
		public TerminalNode KW_SIGNAL() { return getToken(vhdlParser.KW_SIGNAL, 0); }
		public TerminalNode KW_REJECT() { return getToken(vhdlParser.KW_REJECT, 0); }
		public TerminalNode KW_BEGIN() { return getToken(vhdlParser.KW_BEGIN, 0); }
		public TerminalNode KW_SLA() { return getToken(vhdlParser.KW_SLA, 0); }
		public TerminalNode KW_DISCONNECT() { return getToken(vhdlParser.KW_DISCONNECT, 0); }
		public TerminalNode KW_OF() { return getToken(vhdlParser.KW_OF, 0); }
		public TerminalNode KW_PROCEDURE() { return getToken(vhdlParser.KW_PROCEDURE, 0); }
		public TerminalNode KW_SRL() { return getToken(vhdlParser.KW_SRL, 0); }
		public TerminalNode KW_VUNIT() { return getToken(vhdlParser.KW_VUNIT, 0); }
		public TerminalNode KW_ATTRIBUTE() { return getToken(vhdlParser.KW_ATTRIBUTE, 0); }
		public TerminalNode KW_VARIABLE() { return getToken(vhdlParser.KW_VARIABLE, 0); }
		public TerminalNode KW_PROPERTY() { return getToken(vhdlParser.KW_PROPERTY, 0); }
		public TerminalNode KW_UNAFFECTED() { return getToken(vhdlParser.KW_UNAFFECTED, 0); }
		public TerminalNode KW_XOR() { return getToken(vhdlParser.KW_XOR, 0); }
		public TerminalNode KW_REGISTER() { return getToken(vhdlParser.KW_REGISTER, 0); }
		public TerminalNode KW_SUBTYPE() { return getToken(vhdlParser.KW_SUBTYPE, 0); }
		public TerminalNode KW_TO() { return getToken(vhdlParser.KW_TO, 0); }
		public TerminalNode KW_NEW() { return getToken(vhdlParser.KW_NEW, 0); }
		public TerminalNode KW_REPORT() { return getToken(vhdlParser.KW_REPORT, 0); }
		public TerminalNode KW_CONSTANT() { return getToken(vhdlParser.KW_CONSTANT, 0); }
		public TerminalNode KW_BUFFER() { return getToken(vhdlParser.KW_BUFFER, 0); }
		public TerminalNode KW_BODY() { return getToken(vhdlParser.KW_BODY, 0); }
		public TerminalNode KW_AFTER() { return getToken(vhdlParser.KW_AFTER, 0); }
		public TerminalNode KW_TRANSPORT() { return getToken(vhdlParser.KW_TRANSPORT, 0); }
		public TerminalNode KW_FUNCTION() { return getToken(vhdlParser.KW_FUNCTION, 0); }
		public TerminalNode KW_END() { return getToken(vhdlParser.KW_END, 0); }
		public TerminalNode KW_SELECT() { return getToken(vhdlParser.KW_SELECT, 0); }
		public TerminalNode KW_OR() { return getToken(vhdlParser.KW_OR, 0); }
		public TerminalNode KW_LIBRARY() { return getToken(vhdlParser.KW_LIBRARY, 0); }
		public TerminalNode KW_ELSIF() { return getToken(vhdlParser.KW_ELSIF, 0); }
		public TerminalNode KW_SLL() { return getToken(vhdlParser.KW_SLL, 0); }
		public TerminalNode KW_MAP() { return getToken(vhdlParser.KW_MAP, 0); }
		public TerminalNode KW_SRA() { return getToken(vhdlParser.KW_SRA, 0); }
		public TerminalNode KW_PROTECTED() { return getToken(vhdlParser.KW_PROTECTED, 0); }
		public TerminalNode KW_DOWNTO() { return getToken(vhdlParser.KW_DOWNTO, 0); }
		public TerminalNode KW_LABEL() { return getToken(vhdlParser.KW_LABEL, 0); }
		public TerminalNode KW_ALL() { return getToken(vhdlParser.KW_ALL, 0); }
		public TerminalNode KW_ALIAS() { return getToken(vhdlParser.KW_ALIAS, 0); }
		public TerminalNode KW_GENERATE() { return getToken(vhdlParser.KW_GENERATE, 0); }
		public TerminalNode KW_NOR() { return getToken(vhdlParser.KW_NOR, 0); }
		public TerminalNode KW_IN() { return getToken(vhdlParser.KW_IN, 0); }
		public TerminalNode KW_RELEASE() { return getToken(vhdlParser.KW_RELEASE, 0); }
		public TerminalNode KW_EXIT() { return getToken(vhdlParser.KW_EXIT, 0); }
		public TerminalNode KW_RETURN() { return getToken(vhdlParser.KW_RETURN, 0); }
		public TerminalNode KW_WITH() { return getToken(vhdlParser.KW_WITH, 0); }
		public TerminalNode KW_UNTIL() { return getToken(vhdlParser.KW_UNTIL, 0); }
		public TerminalNode KW_AND() { return getToken(vhdlParser.KW_AND, 0); }
		public TerminalNode KW_INOUT() { return getToken(vhdlParser.KW_INOUT, 0); }
		public TerminalNode KW_WAIT() { return getToken(vhdlParser.KW_WAIT, 0); }
		public TerminalNode KW_NAND() { return getToken(vhdlParser.KW_NAND, 0); }
		public TerminalNode KW_ARRAY() { return getToken(vhdlParser.KW_ARRAY, 0); }
		public TerminalNode KW_FORCE() { return getToken(vhdlParser.KW_FORCE, 0); }
		public TerminalNode KW_WHILE() { return getToken(vhdlParser.KW_WHILE, 0); }
		public TerminalNode KW_IMPURE() { return getToken(vhdlParser.KW_IMPURE, 0); }
		public TerminalNode KW_PACKAGE() { return getToken(vhdlParser.KW_PACKAGE, 0); }
		public TerminalNode KW_UNITS() { return getToken(vhdlParser.KW_UNITS, 0); }
		public TerminalNode KW_ASSERT() { return getToken(vhdlParser.KW_ASSERT, 0); }
		public TerminalNode KW_PARAMETER() { return getToken(vhdlParser.KW_PARAMETER, 0); }
		public TerminalNode KW_SEVERITY() { return getToken(vhdlParser.KW_SEVERITY, 0); }
		public TerminalNode KW_LITERAL() { return getToken(vhdlParser.KW_LITERAL, 0); }
		public TerminalNode KW_FOR() { return getToken(vhdlParser.KW_FOR, 0); }
		public TerminalNode KW_ROR() { return getToken(vhdlParser.KW_ROR, 0); }
		public TerminalNode KW_IF() { return getToken(vhdlParser.KW_IF, 0); }
		public TerminalNode KW_OUT() { return getToken(vhdlParser.KW_OUT, 0); }
		public TerminalNode KW_ROL() { return getToken(vhdlParser.KW_ROL, 0); }
		public TerminalNode KW_IS() { return getToken(vhdlParser.KW_IS, 0); }
		public TerminalNode KW_SEQUENCE() { return getToken(vhdlParser.KW_SEQUENCE, 0); }
		public TerminalNode KW_OTHERS() { return getToken(vhdlParser.KW_OTHERS, 0); }
		public TerminalNode KW_TYPE() { return getToken(vhdlParser.KW_TYPE, 0); }
		public TerminalNode KW_CASE() { return getToken(vhdlParser.KW_CASE, 0); }
		public TerminalNode KW_NOT() { return getToken(vhdlParser.KW_NOT, 0); }
		public TerminalNode KW_CONFIGURATION() { return getToken(vhdlParser.KW_CONFIGURATION, 0); }
		public TerminalNode KW_OPEN() { return getToken(vhdlParser.KW_OPEN, 0); }
		public TerminalNode KW_ARCHITECTURE() { return getToken(vhdlParser.KW_ARCHITECTURE, 0); }
		public TerminalNode KW_BUS() { return getToken(vhdlParser.KW_BUS, 0); }
		public TerminalNode KW_ACCESS() { return getToken(vhdlParser.KW_ACCESS, 0); }
		public TerminalNode KW_WHEN() { return getToken(vhdlParser.KW_WHEN, 0); }
		public TerminalNode KW_PORT() { return getToken(vhdlParser.KW_PORT, 0); }
		public TerminalNode KW_NULL() { return getToken(vhdlParser.KW_NULL, 0); }
		public Any_keywordContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_any_keyword; }
	}

	public final Any_keywordContext any_keyword() throws RecognitionException {
		Any_keywordContext _localctx = new Any_keywordContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_any_keyword);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(514);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << KW_PROCESS) | (1L << KW_CONTEXT) | (1L << KW_POSTPONED) | (1L << KW_LINKAGE) | (1L << KW_COMPONENT) | (1L << KW_ABS) | (1L << KW_DEFAULT) | (1L << KW_THEN) | (1L << KW_BLOCK) | (1L << KW_REM) | (1L << KW_INERTIAL) | (1L << KW_NEXT) | (1L << KW_ENTITY) | (1L << KW_ON) | (1L << KW_GROUP) | (1L << KW_XNOR) | (1L << KW_FILE) | (1L << KW_PURE) | (1L << KW_GUARDED) | (1L << KW_GENERIC) | (1L << KW_RANGE) | (1L << KW_ELSE) | (1L << KW_USE) | (1L << KW_SHARED) | (1L << KW_MOD) | (1L << KW_LOOP) | (1L << KW_RECORD) | (1L << KW_SIGNAL) | (1L << KW_REJECT) | (1L << KW_BEGIN) | (1L << KW_SLA) | (1L << KW_DISCONNECT) | (1L << KW_OF) | (1L << KW_PROCEDURE) | (1L << KW_SRL) | (1L << KW_VUNIT) | (1L << KW_ATTRIBUTE) | (1L << KW_VARIABLE) | (1L << KW_PROPERTY) | (1L << KW_UNAFFECTED) | (1L << KW_XOR) | (1L << KW_REGISTER) | (1L << KW_SUBTYPE) | (1L << KW_TO) | (1L << KW_NEW) | (1L << KW_REPORT) | (1L << KW_CONSTANT) | (1L << KW_BUFFER) | (1L << KW_BODY) | (1L << KW_AFTER) | (1L << KW_TRANSPORT) | (1L << KW_FUNCTION) | (1L << KW_END) | (1L << KW_SELECT) | (1L << KW_OR) | (1L << KW_LIBRARY) | (1L << KW_ELSIF) | (1L << KW_SLL) | (1L << KW_MAP) | (1L << KW_SRA) | (1L << KW_PROTECTED) | (1L << KW_DOWNTO) | (1L << KW_LABEL))) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & ((1L << (KW_ALL - 64)) | (1L << (KW_ALIAS - 64)) | (1L << (KW_GENERATE - 64)) | (1L << (KW_NOR - 64)) | (1L << (KW_IN - 64)) | (1L << (KW_RELEASE - 64)) | (1L << (KW_EXIT - 64)) | (1L << (KW_RETURN - 64)) | (1L << (KW_WITH - 64)) | (1L << (KW_UNTIL - 64)) | (1L << (KW_AND - 64)) | (1L << (KW_INOUT - 64)) | (1L << (KW_WAIT - 64)) | (1L << (KW_NAND - 64)) | (1L << (KW_ARRAY - 64)) | (1L << (KW_FORCE - 64)) | (1L << (KW_WHILE - 64)) | (1L << (KW_IMPURE - 64)) | (1L << (KW_PACKAGE - 64)) | (1L << (KW_UNITS - 64)) | (1L << (KW_ASSERT - 64)) | (1L << (KW_PARAMETER - 64)) | (1L << (KW_SEVERITY - 64)) | (1L << (KW_LITERAL - 64)) | (1L << (KW_FOR - 64)) | (1L << (KW_ROR - 64)) | (1L << (KW_IF - 64)) | (1L << (KW_OUT - 64)) | (1L << (KW_ROL - 64)) | (1L << (KW_IS - 64)) | (1L << (KW_SEQUENCE - 64)) | (1L << (KW_OTHERS - 64)) | (1L << (KW_TYPE - 64)) | (1L << (KW_CASE - 64)) | (1L << (KW_NOT - 64)) | (1L << (KW_CONFIGURATION - 64)) | (1L << (KW_OPEN - 64)) | (1L << (KW_ARCHITECTURE - 64)) | (1L << (KW_BUS - 64)) | (1L << (KW_ACCESS - 64)) | (1L << (KW_WHEN - 64)) | (1L << (KW_PORT - 64)) | (1L << (KW_NULL - 64)))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Name_literalContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public Operator_symbolContext operator_symbol() {
			return getRuleContext(Operator_symbolContext.class,0);
		}
		public TerminalNode CHARACTER_LITERAL() { return getToken(vhdlParser.CHARACTER_LITERAL, 0); }
		public Name_literalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_name_literal; }
	}

	public final Name_literalContext name_literal() throws RecognitionException {
		Name_literalContext _localctx = new Name_literalContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_name_literal);
		try {
			setState(519);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BASIC_IDENTIFIER:
			case EXTENDED_IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(516);
				identifier();
				}
				break;
			case STRING_LITERAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(517);
				operator_symbol();
				}
				break;
			case CHARACTER_LITERAL:
				enterOuterAlt(_localctx, 3);
				{
				setState(518);
				match(CHARACTER_LITERAL);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NameContext extends ParserRuleContext {
		public Name_literalContext name_literal() {
			return getRuleContext(Name_literalContext.class,0);
		}
		public External_nameContext external_name() {
			return getRuleContext(External_nameContext.class,0);
		}
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public Name_slice_partContext name_slice_part() {
			return getRuleContext(Name_slice_partContext.class,0);
		}
		public Name_attribute_partContext name_attribute_part() {
			return getRuleContext(Name_attribute_partContext.class,0);
		}
		public Association_listContext association_list() {
			return getRuleContext(Association_listContext.class,0);
		}
		public TerminalNode DOT() { return getToken(vhdlParser.DOT, 0); }
		public SuffixContext suffix() {
			return getRuleContext(SuffixContext.class,0);
		}
		public NameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_name; }
	}

	public final NameContext name() throws RecognitionException {
		return name(0);
	}

	private NameContext name(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		NameContext _localctx = new NameContext(_ctx, _parentState);
		NameContext _prevctx = _localctx;
		int _startState = 4;
		enterRecursionRule(_localctx, 4, RULE_name, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(524);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BASIC_IDENTIFIER:
			case EXTENDED_IDENTIFIER:
			case CHARACTER_LITERAL:
			case STRING_LITERAL:
				{
				setState(522);
				name_literal();
				}
				break;
			case SHIFT_LEFT:
				{
				setState(523);
				external_name();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(536);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new NameContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_name);
					setState(526);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(532);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
					case 1:
						{
						setState(527);
						name_slice_part();
						}
						break;
					case 2:
						{
						setState(528);
						name_attribute_part();
						}
						break;
					case 3:
						{
						setState(529);
						association_list();
						}
						break;
					case 4:
						{
						setState(530);
						match(DOT);
						setState(531);
						suffix();
						}
						break;
					}
					}
					} 
				}
				setState(538);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Name_slice_partContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(vhdlParser.LPAREN, 0); }
		public Explicit_rangeContext explicit_range() {
			return getRuleContext(Explicit_rangeContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(vhdlParser.RPAREN, 0); }
		public Name_slice_partContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_name_slice_part; }
	}

	public final Name_slice_partContext name_slice_part() throws RecognitionException {
		Name_slice_partContext _localctx = new Name_slice_partContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_name_slice_part);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(539);
			match(LPAREN);
			setState(540);
			explicit_range();
			setState(541);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Name_attribute_partContext extends ParserRuleContext {
		public TerminalNode APOSTROPHE() { return getToken(vhdlParser.APOSTROPHE, 0); }
		public Attribute_designatorContext attribute_designator() {
			return getRuleContext(Attribute_designatorContext.class,0);
		}
		public SignatureContext signature() {
			return getRuleContext(SignatureContext.class,0);
		}
		public Name_attribute_partContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_name_attribute_part; }
	}

	public final Name_attribute_partContext name_attribute_part() throws RecognitionException {
		Name_attribute_partContext _localctx = new Name_attribute_partContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_name_attribute_part);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(544);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LSQUARE_BR) {
				{
				setState(543);
				signature();
				}
			}

			setState(546);
			match(APOSTROPHE);
			setState(547);
			attribute_designator();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Attribute_nameContext extends ParserRuleContext {
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public Name_attribute_partContext name_attribute_part() {
			return getRuleContext(Name_attribute_partContext.class,0);
		}
		public Attribute_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attribute_name; }
	}

	public final Attribute_nameContext attribute_name() throws RecognitionException {
		Attribute_nameContext _localctx = new Attribute_nameContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_attribute_name);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(549);
			name(0);
			setState(550);
			name_attribute_part();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SuffixContext extends ParserRuleContext {
		public Name_literalContext name_literal() {
			return getRuleContext(Name_literalContext.class,0);
		}
		public TerminalNode KW_ALL() { return getToken(vhdlParser.KW_ALL, 0); }
		public SuffixContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_suffix; }
	}

	public final SuffixContext suffix() throws RecognitionException {
		SuffixContext _localctx = new SuffixContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_suffix);
		try {
			setState(554);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BASIC_IDENTIFIER:
			case EXTENDED_IDENTIFIER:
			case CHARACTER_LITERAL:
			case STRING_LITERAL:
				enterOuterAlt(_localctx, 1);
				{
				setState(552);
				name_literal();
				}
				break;
			case KW_ALL:
				enterOuterAlt(_localctx, 2);
				{
				setState(553);
				match(KW_ALL);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Explicit_rangeContext extends ParserRuleContext {
		public List<Simple_expressionContext> simple_expression() {
			return getRuleContexts(Simple_expressionContext.class);
		}
		public Simple_expressionContext simple_expression(int i) {
			return getRuleContext(Simple_expressionContext.class,i);
		}
		public DirectionContext direction() {
			return getRuleContext(DirectionContext.class,0);
		}
		public Explicit_rangeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_explicit_range; }
	}

	public final Explicit_rangeContext explicit_range() throws RecognitionException {
		Explicit_rangeContext _localctx = new Explicit_rangeContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_explicit_range);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(556);
			simple_expression(0);
			setState(557);
			direction();
			setState(558);
			simple_expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Selected_nameContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public List<TerminalNode> DOT() { return getTokens(vhdlParser.DOT); }
		public TerminalNode DOT(int i) {
			return getToken(vhdlParser.DOT, i);
		}
		public List<SuffixContext> suffix() {
			return getRuleContexts(SuffixContext.class);
		}
		public SuffixContext suffix(int i) {
			return getRuleContext(SuffixContext.class,i);
		}
		public Selected_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_selected_name; }
	}

	public final Selected_nameContext selected_name() throws RecognitionException {
		Selected_nameContext _localctx = new Selected_nameContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_selected_name);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(560);
			identifier();
			setState(565);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==DOT) {
				{
				{
				setState(561);
				match(DOT);
				setState(562);
				suffix();
				}
				}
				setState(567);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Entity_declarationContext extends ParserRuleContext {
		public List<TerminalNode> KW_ENTITY() { return getTokens(vhdlParser.KW_ENTITY); }
		public TerminalNode KW_ENTITY(int i) {
			return getToken(vhdlParser.KW_ENTITY, i);
		}
		public List<IdentifierContext> identifier() {
			return getRuleContexts(IdentifierContext.class);
		}
		public IdentifierContext identifier(int i) {
			return getRuleContext(IdentifierContext.class,i);
		}
		public TerminalNode KW_IS() { return getToken(vhdlParser.KW_IS, 0); }
		public TerminalNode KW_END() { return getToken(vhdlParser.KW_END, 0); }
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public Generic_clauseContext generic_clause() {
			return getRuleContext(Generic_clauseContext.class,0);
		}
		public Port_clauseContext port_clause() {
			return getRuleContext(Port_clauseContext.class,0);
		}
		public List<Entity_declarative_itemContext> entity_declarative_item() {
			return getRuleContexts(Entity_declarative_itemContext.class);
		}
		public Entity_declarative_itemContext entity_declarative_item(int i) {
			return getRuleContext(Entity_declarative_itemContext.class,i);
		}
		public TerminalNode KW_BEGIN() { return getToken(vhdlParser.KW_BEGIN, 0); }
		public List<Entity_statementContext> entity_statement() {
			return getRuleContexts(Entity_statementContext.class);
		}
		public Entity_statementContext entity_statement(int i) {
			return getRuleContext(Entity_statementContext.class,i);
		}
		public Entity_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entity_declaration; }
	}

	public final Entity_declarationContext entity_declaration() throws RecognitionException {
		Entity_declarationContext _localctx = new Entity_declarationContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_entity_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(568);
			match(KW_ENTITY);
			setState(569);
			identifier();
			setState(570);
			match(KW_IS);
			setState(572);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_GENERIC) {
				{
				setState(571);
				generic_clause();
				}
			}

			setState(575);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_PORT) {
				{
				setState(574);
				port_clause();
				}
			}

			setState(580);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << KW_GROUP) | (1L << KW_FILE) | (1L << KW_PURE) | (1L << KW_USE) | (1L << KW_SHARED) | (1L << KW_SIGNAL) | (1L << KW_DISCONNECT) | (1L << KW_PROCEDURE) | (1L << KW_ATTRIBUTE) | (1L << KW_VARIABLE) | (1L << KW_SUBTYPE) | (1L << KW_CONSTANT) | (1L << KW_FUNCTION))) != 0) || ((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & ((1L << (KW_ALIAS - 65)) | (1L << (KW_IMPURE - 65)) | (1L << (KW_PACKAGE - 65)) | (1L << (KW_TYPE - 65)))) != 0)) {
				{
				{
				setState(577);
				entity_declarative_item();
				}
				}
				setState(582);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(590);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_BEGIN) {
				{
				setState(583);
				match(KW_BEGIN);
				setState(587);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==KW_PROCESS || _la==KW_POSTPONED || ((((_la - 84)) & ~0x3f) == 0 && ((1L << (_la - 84)) & ((1L << (KW_ASSERT - 84)) | (1L << (BASIC_IDENTIFIER - 84)) | (1L << (EXTENDED_IDENTIFIER - 84)) | (1L << (CHARACTER_LITERAL - 84)) | (1L << (STRING_LITERAL - 84)) | (1L << (SHIFT_LEFT - 84)))) != 0)) {
					{
					{
					setState(584);
					entity_statement();
					}
					}
					setState(589);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(592);
			match(KW_END);
			setState(594);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_ENTITY) {
				{
				setState(593);
				match(KW_ENTITY);
				}
			}

			setState(597);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==BASIC_IDENTIFIER || _la==EXTENDED_IDENTIFIER) {
				{
				setState(596);
				identifier();
				}
			}

			setState(599);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Entity_declarative_itemContext extends ParserRuleContext {
		public Signal_declarationContext signal_declaration() {
			return getRuleContext(Signal_declarationContext.class,0);
		}
		public Process_declarative_itemContext process_declarative_item() {
			return getRuleContext(Process_declarative_itemContext.class,0);
		}
		public Disconnection_specificationContext disconnection_specification() {
			return getRuleContext(Disconnection_specificationContext.class,0);
		}
		public Entity_declarative_itemContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entity_declarative_item; }
	}

	public final Entity_declarative_itemContext entity_declarative_item() throws RecognitionException {
		Entity_declarative_itemContext _localctx = new Entity_declarative_itemContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_entity_declarative_item);
		try {
			setState(604);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KW_SIGNAL:
				enterOuterAlt(_localctx, 1);
				{
				setState(601);
				signal_declaration();
				}
				break;
			case KW_GROUP:
			case KW_FILE:
			case KW_PURE:
			case KW_USE:
			case KW_SHARED:
			case KW_PROCEDURE:
			case KW_ATTRIBUTE:
			case KW_VARIABLE:
			case KW_SUBTYPE:
			case KW_CONSTANT:
			case KW_FUNCTION:
			case KW_ALIAS:
			case KW_IMPURE:
			case KW_PACKAGE:
			case KW_TYPE:
				enterOuterAlt(_localctx, 2);
				{
				setState(602);
				process_declarative_item();
				}
				break;
			case KW_DISCONNECT:
				enterOuterAlt(_localctx, 3);
				{
				setState(603);
				disconnection_specification();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Entity_statementContext extends ParserRuleContext {
		public Concurrent_assertion_statementContext concurrent_assertion_statement() {
			return getRuleContext(Concurrent_assertion_statementContext.class,0);
		}
		public Concurrent_procedure_call_statementContext concurrent_procedure_call_statement() {
			return getRuleContext(Concurrent_procedure_call_statementContext.class,0);
		}
		public Process_statementContext process_statement() {
			return getRuleContext(Process_statementContext.class,0);
		}
		public LabelContext label() {
			return getRuleContext(LabelContext.class,0);
		}
		public TerminalNode COLON() { return getToken(vhdlParser.COLON, 0); }
		public Entity_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entity_statement; }
	}

	public final Entity_statementContext entity_statement() throws RecognitionException {
		Entity_statementContext _localctx = new Entity_statementContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_entity_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(609);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				{
				setState(606);
				label();
				setState(607);
				match(COLON);
				}
				break;
			}
			setState(614);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				{
				setState(611);
				concurrent_assertion_statement();
				}
				break;
			case 2:
				{
				setState(612);
				concurrent_procedure_call_statement();
				}
				break;
			case 3:
				{
				setState(613);
				process_statement();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Architecture_bodyContext extends ParserRuleContext {
		public List<TerminalNode> KW_ARCHITECTURE() { return getTokens(vhdlParser.KW_ARCHITECTURE); }
		public TerminalNode KW_ARCHITECTURE(int i) {
			return getToken(vhdlParser.KW_ARCHITECTURE, i);
		}
		public List<IdentifierContext> identifier() {
			return getRuleContexts(IdentifierContext.class);
		}
		public IdentifierContext identifier(int i) {
			return getRuleContext(IdentifierContext.class,i);
		}
		public TerminalNode KW_OF() { return getToken(vhdlParser.KW_OF, 0); }
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public TerminalNode KW_IS() { return getToken(vhdlParser.KW_IS, 0); }
		public TerminalNode KW_BEGIN() { return getToken(vhdlParser.KW_BEGIN, 0); }
		public TerminalNode KW_END() { return getToken(vhdlParser.KW_END, 0); }
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public List<Block_declarative_itemContext> block_declarative_item() {
			return getRuleContexts(Block_declarative_itemContext.class);
		}
		public Block_declarative_itemContext block_declarative_item(int i) {
			return getRuleContext(Block_declarative_itemContext.class,i);
		}
		public List<Concurrent_statementContext> concurrent_statement() {
			return getRuleContexts(Concurrent_statementContext.class);
		}
		public Concurrent_statementContext concurrent_statement(int i) {
			return getRuleContext(Concurrent_statementContext.class,i);
		}
		public Architecture_bodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_architecture_body; }
	}

	public final Architecture_bodyContext architecture_body() throws RecognitionException {
		Architecture_bodyContext _localctx = new Architecture_bodyContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_architecture_body);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(616);
			match(KW_ARCHITECTURE);
			setState(617);
			identifier();
			setState(618);
			match(KW_OF);
			setState(619);
			name(0);
			setState(620);
			match(KW_IS);
			setState(624);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << KW_COMPONENT) | (1L << KW_GROUP) | (1L << KW_FILE) | (1L << KW_PURE) | (1L << KW_USE) | (1L << KW_SHARED) | (1L << KW_SIGNAL) | (1L << KW_DISCONNECT) | (1L << KW_PROCEDURE) | (1L << KW_ATTRIBUTE) | (1L << KW_VARIABLE) | (1L << KW_SUBTYPE) | (1L << KW_CONSTANT) | (1L << KW_FUNCTION))) != 0) || ((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & ((1L << (KW_ALIAS - 65)) | (1L << (KW_IMPURE - 65)) | (1L << (KW_PACKAGE - 65)) | (1L << (KW_FOR - 65)) | (1L << (KW_TYPE - 65)))) != 0)) {
				{
				{
				setState(621);
				block_declarative_item();
				}
				}
				setState(626);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(627);
			match(KW_BEGIN);
			setState(631);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==KW_PROCESS || _la==KW_POSTPONED || ((((_la - 72)) & ~0x3f) == 0 && ((1L << (_la - 72)) & ((1L << (KW_WITH - 72)) | (1L << (KW_ASSERT - 72)) | (1L << (BASIC_IDENTIFIER - 72)) | (1L << (EXTENDED_IDENTIFIER - 72)) | (1L << (CHARACTER_LITERAL - 72)) | (1L << (STRING_LITERAL - 72)) | (1L << (LPAREN - 72)) | (1L << (SHIFT_LEFT - 72)))) != 0)) {
				{
				{
				setState(628);
				concurrent_statement();
				}
				}
				setState(633);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(634);
			match(KW_END);
			setState(636);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_ARCHITECTURE) {
				{
				setState(635);
				match(KW_ARCHITECTURE);
				}
			}

			setState(639);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==BASIC_IDENTIFIER || _la==EXTENDED_IDENTIFIER) {
				{
				setState(638);
				identifier();
				}
			}

			setState(641);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Block_declarative_itemContext extends ParserRuleContext {
		public Entity_declarative_itemContext entity_declarative_item() {
			return getRuleContext(Entity_declarative_itemContext.class,0);
		}
		public Component_declarationContext component_declaration() {
			return getRuleContext(Component_declarationContext.class,0);
		}
		public Configuration_specificationContext configuration_specification() {
			return getRuleContext(Configuration_specificationContext.class,0);
		}
		public Block_declarative_itemContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block_declarative_item; }
	}

	public final Block_declarative_itemContext block_declarative_item() throws RecognitionException {
		Block_declarative_itemContext _localctx = new Block_declarative_itemContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_block_declarative_item);
		try {
			setState(646);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KW_GROUP:
			case KW_FILE:
			case KW_PURE:
			case KW_USE:
			case KW_SHARED:
			case KW_SIGNAL:
			case KW_DISCONNECT:
			case KW_PROCEDURE:
			case KW_ATTRIBUTE:
			case KW_VARIABLE:
			case KW_SUBTYPE:
			case KW_CONSTANT:
			case KW_FUNCTION:
			case KW_ALIAS:
			case KW_IMPURE:
			case KW_PACKAGE:
			case KW_TYPE:
				enterOuterAlt(_localctx, 1);
				{
				setState(643);
				entity_declarative_item();
				}
				break;
			case KW_COMPONENT:
				enterOuterAlt(_localctx, 2);
				{
				setState(644);
				component_declaration();
				}
				break;
			case KW_FOR:
				enterOuterAlt(_localctx, 3);
				{
				setState(645);
				configuration_specification();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Configuration_declarationContext extends ParserRuleContext {
		public List<TerminalNode> KW_CONFIGURATION() { return getTokens(vhdlParser.KW_CONFIGURATION); }
		public TerminalNode KW_CONFIGURATION(int i) {
			return getToken(vhdlParser.KW_CONFIGURATION, i);
		}
		public List<IdentifierContext> identifier() {
			return getRuleContexts(IdentifierContext.class);
		}
		public IdentifierContext identifier(int i) {
			return getRuleContext(IdentifierContext.class,i);
		}
		public TerminalNode KW_OF() { return getToken(vhdlParser.KW_OF, 0); }
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public TerminalNode KW_IS() { return getToken(vhdlParser.KW_IS, 0); }
		public Block_configurationContext block_configuration() {
			return getRuleContext(Block_configurationContext.class,0);
		}
		public TerminalNode KW_END() { return getToken(vhdlParser.KW_END, 0); }
		public List<TerminalNode> SEMI() { return getTokens(vhdlParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(vhdlParser.SEMI, i);
		}
		public List<Configuration_declarative_itemContext> configuration_declarative_item() {
			return getRuleContexts(Configuration_declarative_itemContext.class);
		}
		public Configuration_declarative_itemContext configuration_declarative_item(int i) {
			return getRuleContext(Configuration_declarative_itemContext.class,i);
		}
		public List<Verification_unit_binding_indicationContext> verification_unit_binding_indication() {
			return getRuleContexts(Verification_unit_binding_indicationContext.class);
		}
		public Verification_unit_binding_indicationContext verification_unit_binding_indication(int i) {
			return getRuleContext(Verification_unit_binding_indicationContext.class,i);
		}
		public Configuration_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_configuration_declaration; }
	}

	public final Configuration_declarationContext configuration_declaration() throws RecognitionException {
		Configuration_declarationContext _localctx = new Configuration_declarationContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_configuration_declaration);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(648);
			match(KW_CONFIGURATION);
			setState(649);
			identifier();
			setState(650);
			match(KW_OF);
			setState(651);
			name(0);
			setState(652);
			match(KW_IS);
			setState(656);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(653);
					configuration_declarative_item();
					}
					} 
				}
				setState(658);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			}
			setState(664);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==KW_USE) {
				{
				{
				setState(659);
				verification_unit_binding_indication();
				setState(660);
				match(SEMI);
				}
				}
				setState(666);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(667);
			block_configuration();
			setState(668);
			match(KW_END);
			setState(670);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_CONFIGURATION) {
				{
				setState(669);
				match(KW_CONFIGURATION);
				}
			}

			setState(673);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==BASIC_IDENTIFIER || _la==EXTENDED_IDENTIFIER) {
				{
				setState(672);
				identifier();
				}
			}

			setState(675);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Configuration_declarative_itemContext extends ParserRuleContext {
		public Use_clauseContext use_clause() {
			return getRuleContext(Use_clauseContext.class,0);
		}
		public Attribute_specificationContext attribute_specification() {
			return getRuleContext(Attribute_specificationContext.class,0);
		}
		public Group_declarationContext group_declaration() {
			return getRuleContext(Group_declarationContext.class,0);
		}
		public Configuration_declarative_itemContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_configuration_declarative_item; }
	}

	public final Configuration_declarative_itemContext configuration_declarative_item() throws RecognitionException {
		Configuration_declarative_itemContext _localctx = new Configuration_declarative_itemContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_configuration_declarative_item);
		try {
			setState(680);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KW_USE:
				enterOuterAlt(_localctx, 1);
				{
				setState(677);
				use_clause();
				}
				break;
			case KW_ATTRIBUTE:
				enterOuterAlt(_localctx, 2);
				{
				setState(678);
				attribute_specification();
				}
				break;
			case KW_GROUP:
				enterOuterAlt(_localctx, 3);
				{
				setState(679);
				group_declaration();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Block_configurationContext extends ParserRuleContext {
		public List<TerminalNode> KW_FOR() { return getTokens(vhdlParser.KW_FOR); }
		public TerminalNode KW_FOR(int i) {
			return getToken(vhdlParser.KW_FOR, i);
		}
		public Block_specificationContext block_specification() {
			return getRuleContext(Block_specificationContext.class,0);
		}
		public TerminalNode KW_END() { return getToken(vhdlParser.KW_END, 0); }
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public List<Use_clauseContext> use_clause() {
			return getRuleContexts(Use_clauseContext.class);
		}
		public Use_clauseContext use_clause(int i) {
			return getRuleContext(Use_clauseContext.class,i);
		}
		public List<Configuration_itemContext> configuration_item() {
			return getRuleContexts(Configuration_itemContext.class);
		}
		public Configuration_itemContext configuration_item(int i) {
			return getRuleContext(Configuration_itemContext.class,i);
		}
		public Block_configurationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block_configuration; }
	}

	public final Block_configurationContext block_configuration() throws RecognitionException {
		Block_configurationContext _localctx = new Block_configurationContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_block_configuration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(682);
			match(KW_FOR);
			setState(683);
			block_specification();
			setState(687);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==KW_USE) {
				{
				{
				setState(684);
				use_clause();
				}
				}
				setState(689);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(693);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==KW_FOR) {
				{
				{
				setState(690);
				configuration_item();
				}
				}
				setState(695);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(696);
			match(KW_END);
			setState(697);
			match(KW_FOR);
			setState(698);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Block_specificationContext extends ParserRuleContext {
		public LabelContext label() {
			return getRuleContext(LabelContext.class,0);
		}
		public TerminalNode LPAREN() { return getToken(vhdlParser.LPAREN, 0); }
		public Generate_specificationContext generate_specification() {
			return getRuleContext(Generate_specificationContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(vhdlParser.RPAREN, 0); }
		public Block_specificationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block_specification; }
	}

	public final Block_specificationContext block_specification() throws RecognitionException {
		Block_specificationContext _localctx = new Block_specificationContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_block_specification);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(700);
			label();
			setState(705);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LPAREN) {
				{
				setState(701);
				match(LPAREN);
				setState(702);
				generate_specification();
				setState(703);
				match(RPAREN);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Generate_specificationContext extends ParserRuleContext {
		public Discrete_rangeContext discrete_range() {
			return getRuleContext(Discrete_rangeContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public LabelContext label() {
			return getRuleContext(LabelContext.class,0);
		}
		public Generate_specificationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_generate_specification; }
	}

	public final Generate_specificationContext generate_specification() throws RecognitionException {
		Generate_specificationContext _localctx = new Generate_specificationContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_generate_specification);
		try {
			setState(710);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,30,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(707);
				discrete_range();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(708);
				expression(0);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(709);
				label();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Configuration_itemContext extends ParserRuleContext {
		public Block_configurationContext block_configuration() {
			return getRuleContext(Block_configurationContext.class,0);
		}
		public Component_configurationContext component_configuration() {
			return getRuleContext(Component_configurationContext.class,0);
		}
		public Configuration_itemContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_configuration_item; }
	}

	public final Configuration_itemContext configuration_item() throws RecognitionException {
		Configuration_itemContext _localctx = new Configuration_itemContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_configuration_item);
		try {
			setState(714);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,31,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(712);
				block_configuration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(713);
				component_configuration();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Component_configurationContext extends ParserRuleContext {
		public List<TerminalNode> KW_FOR() { return getTokens(vhdlParser.KW_FOR); }
		public TerminalNode KW_FOR(int i) {
			return getToken(vhdlParser.KW_FOR, i);
		}
		public Component_specificationContext component_specification() {
			return getRuleContext(Component_specificationContext.class,0);
		}
		public TerminalNode KW_END() { return getToken(vhdlParser.KW_END, 0); }
		public List<TerminalNode> SEMI() { return getTokens(vhdlParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(vhdlParser.SEMI, i);
		}
		public Binding_indicationContext binding_indication() {
			return getRuleContext(Binding_indicationContext.class,0);
		}
		public List<Verification_unit_binding_indicationContext> verification_unit_binding_indication() {
			return getRuleContexts(Verification_unit_binding_indicationContext.class);
		}
		public Verification_unit_binding_indicationContext verification_unit_binding_indication(int i) {
			return getRuleContext(Verification_unit_binding_indicationContext.class,i);
		}
		public Block_configurationContext block_configuration() {
			return getRuleContext(Block_configurationContext.class,0);
		}
		public Component_configurationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_component_configuration; }
	}

	public final Component_configurationContext component_configuration() throws RecognitionException {
		Component_configurationContext _localctx = new Component_configurationContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_component_configuration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(716);
			match(KW_FOR);
			setState(717);
			component_specification();
			setState(721);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,32,_ctx) ) {
			case 1:
				{
				setState(718);
				binding_indication();
				setState(719);
				match(SEMI);
				}
				break;
			}
			setState(728);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==KW_USE) {
				{
				{
				setState(723);
				verification_unit_binding_indication();
				setState(724);
				match(SEMI);
				}
				}
				setState(730);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(732);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_FOR) {
				{
				setState(731);
				block_configuration();
				}
			}

			setState(734);
			match(KW_END);
			setState(735);
			match(KW_FOR);
			setState(736);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Subprogram_declarationContext extends ParserRuleContext {
		public Subprogram_specificationContext subprogram_specification() {
			return getRuleContext(Subprogram_specificationContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public Subprogram_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subprogram_declaration; }
	}

	public final Subprogram_declarationContext subprogram_declaration() throws RecognitionException {
		Subprogram_declarationContext _localctx = new Subprogram_declarationContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_subprogram_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(738);
			subprogram_specification();
			setState(739);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Subprogram_specificationContext extends ParserRuleContext {
		public Procedure_specificationContext procedure_specification() {
			return getRuleContext(Procedure_specificationContext.class,0);
		}
		public Function_specificationContext function_specification() {
			return getRuleContext(Function_specificationContext.class,0);
		}
		public Subprogram_specificationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subprogram_specification; }
	}

	public final Subprogram_specificationContext subprogram_specification() throws RecognitionException {
		Subprogram_specificationContext _localctx = new Subprogram_specificationContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_subprogram_specification);
		try {
			setState(743);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KW_PROCEDURE:
				enterOuterAlt(_localctx, 1);
				{
				setState(741);
				procedure_specification();
				}
				break;
			case KW_PURE:
			case KW_FUNCTION:
			case KW_IMPURE:
				enterOuterAlt(_localctx, 2);
				{
				setState(742);
				function_specification();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Procedure_specificationContext extends ParserRuleContext {
		public TerminalNode KW_PROCEDURE() { return getToken(vhdlParser.KW_PROCEDURE, 0); }
		public DesignatorContext designator() {
			return getRuleContext(DesignatorContext.class,0);
		}
		public Subprogram_headerContext subprogram_header() {
			return getRuleContext(Subprogram_headerContext.class,0);
		}
		public TerminalNode LPAREN() { return getToken(vhdlParser.LPAREN, 0); }
		public Formal_parameter_listContext formal_parameter_list() {
			return getRuleContext(Formal_parameter_listContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(vhdlParser.RPAREN, 0); }
		public TerminalNode KW_PARAMETER() { return getToken(vhdlParser.KW_PARAMETER, 0); }
		public Procedure_specificationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_procedure_specification; }
	}

	public final Procedure_specificationContext procedure_specification() throws RecognitionException {
		Procedure_specificationContext _localctx = new Procedure_specificationContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_procedure_specification);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(745);
			match(KW_PROCEDURE);
			setState(746);
			designator();
			setState(748);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_GENERIC) {
				{
				setState(747);
				subprogram_header();
				}
			}

			setState(757);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_PARAMETER || _la==LPAREN) {
				{
				setState(751);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==KW_PARAMETER) {
					{
					setState(750);
					match(KW_PARAMETER);
					}
				}

				setState(753);
				match(LPAREN);
				setState(754);
				formal_parameter_list();
				setState(755);
				match(RPAREN);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_specificationContext extends ParserRuleContext {
		public TerminalNode KW_FUNCTION() { return getToken(vhdlParser.KW_FUNCTION, 0); }
		public DesignatorContext designator() {
			return getRuleContext(DesignatorContext.class,0);
		}
		public TerminalNode KW_RETURN() { return getToken(vhdlParser.KW_RETURN, 0); }
		public Type_markContext type_mark() {
			return getRuleContext(Type_markContext.class,0);
		}
		public Subprogram_headerContext subprogram_header() {
			return getRuleContext(Subprogram_headerContext.class,0);
		}
		public TerminalNode LPAREN() { return getToken(vhdlParser.LPAREN, 0); }
		public Formal_parameter_listContext formal_parameter_list() {
			return getRuleContext(Formal_parameter_listContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(vhdlParser.RPAREN, 0); }
		public TerminalNode KW_PURE() { return getToken(vhdlParser.KW_PURE, 0); }
		public TerminalNode KW_IMPURE() { return getToken(vhdlParser.KW_IMPURE, 0); }
		public TerminalNode KW_PARAMETER() { return getToken(vhdlParser.KW_PARAMETER, 0); }
		public Function_specificationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_specification; }
	}

	public final Function_specificationContext function_specification() throws RecognitionException {
		Function_specificationContext _localctx = new Function_specificationContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_function_specification);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(760);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_PURE || _la==KW_IMPURE) {
				{
				setState(759);
				_la = _input.LA(1);
				if ( !(_la==KW_PURE || _la==KW_IMPURE) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
			}

			setState(762);
			match(KW_FUNCTION);
			setState(763);
			designator();
			setState(765);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_GENERIC) {
				{
				setState(764);
				subprogram_header();
				}
			}

			setState(774);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_PARAMETER || _la==LPAREN) {
				{
				setState(768);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==KW_PARAMETER) {
					{
					setState(767);
					match(KW_PARAMETER);
					}
				}

				setState(770);
				match(LPAREN);
				setState(771);
				formal_parameter_list();
				setState(772);
				match(RPAREN);
				}
			}

			setState(776);
			match(KW_RETURN);
			setState(777);
			type_mark();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Subprogram_headerContext extends ParserRuleContext {
		public TerminalNode KW_GENERIC() { return getToken(vhdlParser.KW_GENERIC, 0); }
		public TerminalNode LPAREN() { return getToken(vhdlParser.LPAREN, 0); }
		public Generic_listContext generic_list() {
			return getRuleContext(Generic_listContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(vhdlParser.RPAREN, 0); }
		public Generic_map_aspectContext generic_map_aspect() {
			return getRuleContext(Generic_map_aspectContext.class,0);
		}
		public Subprogram_headerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subprogram_header; }
	}

	public final Subprogram_headerContext subprogram_header() throws RecognitionException {
		Subprogram_headerContext _localctx = new Subprogram_headerContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_subprogram_header);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(779);
			match(KW_GENERIC);
			setState(780);
			match(LPAREN);
			setState(781);
			generic_list();
			setState(782);
			match(RPAREN);
			setState(784);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_GENERIC) {
				{
				setState(783);
				generic_map_aspect();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DesignatorContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public Operator_symbolContext operator_symbol() {
			return getRuleContext(Operator_symbolContext.class,0);
		}
		public DesignatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_designator; }
	}

	public final DesignatorContext designator() throws RecognitionException {
		DesignatorContext _localctx = new DesignatorContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_designator);
		try {
			setState(788);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BASIC_IDENTIFIER:
			case EXTENDED_IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(786);
				identifier();
				}
				break;
			case STRING_LITERAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(787);
				operator_symbol();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Operator_symbolContext extends ParserRuleContext {
		public TerminalNode STRING_LITERAL() { return getToken(vhdlParser.STRING_LITERAL, 0); }
		public Operator_symbolContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operator_symbol; }
	}

	public final Operator_symbolContext operator_symbol() throws RecognitionException {
		Operator_symbolContext _localctx = new Operator_symbolContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_operator_symbol);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(790);
			match(STRING_LITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Formal_parameter_listContext extends ParserRuleContext {
		public Interface_listContext interface_list() {
			return getRuleContext(Interface_listContext.class,0);
		}
		public Formal_parameter_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_formal_parameter_list; }
	}

	public final Formal_parameter_listContext formal_parameter_list() throws RecognitionException {
		Formal_parameter_listContext _localctx = new Formal_parameter_listContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_formal_parameter_list);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(792);
			interface_list();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Subprogram_bodyContext extends ParserRuleContext {
		public Subprogram_specificationContext subprogram_specification() {
			return getRuleContext(Subprogram_specificationContext.class,0);
		}
		public TerminalNode KW_IS() { return getToken(vhdlParser.KW_IS, 0); }
		public TerminalNode KW_BEGIN() { return getToken(vhdlParser.KW_BEGIN, 0); }
		public TerminalNode KW_END() { return getToken(vhdlParser.KW_END, 0); }
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public List<Process_declarative_itemContext> process_declarative_item() {
			return getRuleContexts(Process_declarative_itemContext.class);
		}
		public Process_declarative_itemContext process_declarative_item(int i) {
			return getRuleContext(Process_declarative_itemContext.class,i);
		}
		public List<Sequential_statementContext> sequential_statement() {
			return getRuleContexts(Sequential_statementContext.class);
		}
		public Sequential_statementContext sequential_statement(int i) {
			return getRuleContext(Sequential_statementContext.class,i);
		}
		public Subprogram_kindContext subprogram_kind() {
			return getRuleContext(Subprogram_kindContext.class,0);
		}
		public DesignatorContext designator() {
			return getRuleContext(DesignatorContext.class,0);
		}
		public Subprogram_bodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subprogram_body; }
	}

	public final Subprogram_bodyContext subprogram_body() throws RecognitionException {
		Subprogram_bodyContext _localctx = new Subprogram_bodyContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_subprogram_body);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(794);
			subprogram_specification();
			setState(795);
			match(KW_IS);
			setState(799);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << KW_GROUP) | (1L << KW_FILE) | (1L << KW_PURE) | (1L << KW_USE) | (1L << KW_SHARED) | (1L << KW_PROCEDURE) | (1L << KW_ATTRIBUTE) | (1L << KW_VARIABLE) | (1L << KW_SUBTYPE) | (1L << KW_CONSTANT) | (1L << KW_FUNCTION))) != 0) || ((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & ((1L << (KW_ALIAS - 65)) | (1L << (KW_IMPURE - 65)) | (1L << (KW_PACKAGE - 65)) | (1L << (KW_TYPE - 65)))) != 0)) {
				{
				{
				setState(796);
				process_declarative_item();
				}
				}
				setState(801);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(802);
			match(KW_BEGIN);
			setState(806);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << KW_NEXT) | (1L << KW_LOOP) | (1L << KW_REPORT))) != 0) || ((((_la - 70)) & ~0x3f) == 0 && ((1L << (_la - 70)) & ((1L << (KW_EXIT - 70)) | (1L << (KW_RETURN - 70)) | (1L << (KW_WITH - 70)) | (1L << (KW_WAIT - 70)) | (1L << (KW_WHILE - 70)) | (1L << (KW_ASSERT - 70)) | (1L << (KW_FOR - 70)) | (1L << (KW_IF - 70)) | (1L << (KW_CASE - 70)) | (1L << (KW_NULL - 70)) | (1L << (BASIC_IDENTIFIER - 70)) | (1L << (EXTENDED_IDENTIFIER - 70)) | (1L << (CHARACTER_LITERAL - 70)) | (1L << (STRING_LITERAL - 70)) | (1L << (LPAREN - 70)) | (1L << (SHIFT_LEFT - 70)))) != 0)) {
				{
				{
				setState(803);
				sequential_statement();
				}
				}
				setState(808);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(809);
			match(KW_END);
			setState(811);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_PROCEDURE || _la==KW_FUNCTION) {
				{
				setState(810);
				subprogram_kind();
				}
			}

			setState(814);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 107)) & ~0x3f) == 0 && ((1L << (_la - 107)) & ((1L << (BASIC_IDENTIFIER - 107)) | (1L << (EXTENDED_IDENTIFIER - 107)) | (1L << (STRING_LITERAL - 107)))) != 0)) {
				{
				setState(813);
				designator();
				}
			}

			setState(816);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Subprogram_kindContext extends ParserRuleContext {
		public TerminalNode KW_PROCEDURE() { return getToken(vhdlParser.KW_PROCEDURE, 0); }
		public TerminalNode KW_FUNCTION() { return getToken(vhdlParser.KW_FUNCTION, 0); }
		public Subprogram_kindContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subprogram_kind; }
	}

	public final Subprogram_kindContext subprogram_kind() throws RecognitionException {
		Subprogram_kindContext _localctx = new Subprogram_kindContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_subprogram_kind);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(818);
			_la = _input.LA(1);
			if ( !(_la==KW_PROCEDURE || _la==KW_FUNCTION) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Subprogram_instantiation_declarationContext extends ParserRuleContext {
		public Subprogram_kindContext subprogram_kind() {
			return getRuleContext(Subprogram_kindContext.class,0);
		}
		public DesignatorContext designator() {
			return getRuleContext(DesignatorContext.class,0);
		}
		public TerminalNode KW_IS() { return getToken(vhdlParser.KW_IS, 0); }
		public TerminalNode KW_NEW() { return getToken(vhdlParser.KW_NEW, 0); }
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public SignatureContext signature() {
			return getRuleContext(SignatureContext.class,0);
		}
		public Generic_map_aspectContext generic_map_aspect() {
			return getRuleContext(Generic_map_aspectContext.class,0);
		}
		public Subprogram_instantiation_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subprogram_instantiation_declaration; }
	}

	public final Subprogram_instantiation_declarationContext subprogram_instantiation_declaration() throws RecognitionException {
		Subprogram_instantiation_declarationContext _localctx = new Subprogram_instantiation_declarationContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_subprogram_instantiation_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(820);
			subprogram_kind();
			setState(821);
			designator();
			setState(822);
			match(KW_IS);
			setState(823);
			match(KW_NEW);
			setState(824);
			name(0);
			setState(826);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LSQUARE_BR) {
				{
				setState(825);
				signature();
				}
			}

			setState(829);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_GENERIC) {
				{
				setState(828);
				generic_map_aspect();
				}
			}

			setState(831);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SignatureContext extends ParserRuleContext {
		public TerminalNode LSQUARE_BR() { return getToken(vhdlParser.LSQUARE_BR, 0); }
		public TerminalNode RSQUARE_BR() { return getToken(vhdlParser.RSQUARE_BR, 0); }
		public List<Type_markContext> type_mark() {
			return getRuleContexts(Type_markContext.class);
		}
		public Type_markContext type_mark(int i) {
			return getRuleContext(Type_markContext.class,i);
		}
		public TerminalNode KW_RETURN() { return getToken(vhdlParser.KW_RETURN, 0); }
		public List<TerminalNode> COMMA() { return getTokens(vhdlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(vhdlParser.COMMA, i);
		}
		public SignatureContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_signature; }
	}

	public final SignatureContext signature() throws RecognitionException {
		SignatureContext _localctx = new SignatureContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_signature);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(833);
			match(LSQUARE_BR);
			setState(842);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 107)) & ~0x3f) == 0 && ((1L << (_la - 107)) & ((1L << (BASIC_IDENTIFIER - 107)) | (1L << (EXTENDED_IDENTIFIER - 107)) | (1L << (CHARACTER_LITERAL - 107)) | (1L << (STRING_LITERAL - 107)) | (1L << (SHIFT_LEFT - 107)))) != 0)) {
				{
				setState(834);
				type_mark();
				setState(839);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(835);
					match(COMMA);
					setState(836);
					type_mark();
					}
					}
					setState(841);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(846);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_RETURN) {
				{
				setState(844);
				match(KW_RETURN);
				setState(845);
				type_mark();
				}
			}

			setState(848);
			match(RSQUARE_BR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Package_declarationContext extends ParserRuleContext {
		public List<TerminalNode> KW_PACKAGE() { return getTokens(vhdlParser.KW_PACKAGE); }
		public TerminalNode KW_PACKAGE(int i) {
			return getToken(vhdlParser.KW_PACKAGE, i);
		}
		public List<IdentifierContext> identifier() {
			return getRuleContexts(IdentifierContext.class);
		}
		public IdentifierContext identifier(int i) {
			return getRuleContext(IdentifierContext.class,i);
		}
		public TerminalNode KW_IS() { return getToken(vhdlParser.KW_IS, 0); }
		public TerminalNode KW_END() { return getToken(vhdlParser.KW_END, 0); }
		public List<TerminalNode> SEMI() { return getTokens(vhdlParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(vhdlParser.SEMI, i);
		}
		public Generic_clauseContext generic_clause() {
			return getRuleContext(Generic_clauseContext.class,0);
		}
		public List<Package_declarative_itemContext> package_declarative_item() {
			return getRuleContexts(Package_declarative_itemContext.class);
		}
		public Package_declarative_itemContext package_declarative_item(int i) {
			return getRuleContext(Package_declarative_itemContext.class,i);
		}
		public Generic_map_aspectContext generic_map_aspect() {
			return getRuleContext(Generic_map_aspectContext.class,0);
		}
		public Package_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_package_declaration; }
	}

	public final Package_declarationContext package_declaration() throws RecognitionException {
		Package_declarationContext _localctx = new Package_declarationContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_package_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(850);
			match(KW_PACKAGE);
			setState(851);
			identifier();
			setState(852);
			match(KW_IS);
			setState(859);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_GENERIC) {
				{
				setState(853);
				generic_clause();
				setState(857);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==KW_GENERIC) {
					{
					setState(854);
					generic_map_aspect();
					setState(855);
					match(SEMI);
					}
				}

				}
			}

			setState(864);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << KW_COMPONENT) | (1L << KW_GROUP) | (1L << KW_FILE) | (1L << KW_PURE) | (1L << KW_USE) | (1L << KW_SHARED) | (1L << KW_SIGNAL) | (1L << KW_DISCONNECT) | (1L << KW_PROCEDURE) | (1L << KW_ATTRIBUTE) | (1L << KW_VARIABLE) | (1L << KW_SUBTYPE) | (1L << KW_CONSTANT) | (1L << KW_FUNCTION))) != 0) || ((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & ((1L << (KW_ALIAS - 65)) | (1L << (KW_IMPURE - 65)) | (1L << (KW_PACKAGE - 65)) | (1L << (KW_TYPE - 65)))) != 0)) {
				{
				{
				setState(861);
				package_declarative_item();
				}
				}
				setState(866);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(867);
			match(KW_END);
			setState(869);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_PACKAGE) {
				{
				setState(868);
				match(KW_PACKAGE);
				}
			}

			setState(872);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==BASIC_IDENTIFIER || _la==EXTENDED_IDENTIFIER) {
				{
				setState(871);
				identifier();
				}
			}

			setState(874);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Package_declarative_itemContext extends ParserRuleContext {
		public Process_or_package_declarative_itemContext process_or_package_declarative_item() {
			return getRuleContext(Process_or_package_declarative_itemContext.class,0);
		}
		public Signal_declarationContext signal_declaration() {
			return getRuleContext(Signal_declarationContext.class,0);
		}
		public Component_declarationContext component_declaration() {
			return getRuleContext(Component_declarationContext.class,0);
		}
		public Disconnection_specificationContext disconnection_specification() {
			return getRuleContext(Disconnection_specificationContext.class,0);
		}
		public Package_declarative_itemContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_package_declarative_item; }
	}

	public final Package_declarative_itemContext package_declarative_item() throws RecognitionException {
		Package_declarative_itemContext _localctx = new Package_declarative_itemContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_package_declarative_item);
		try {
			setState(880);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KW_GROUP:
			case KW_FILE:
			case KW_PURE:
			case KW_USE:
			case KW_SHARED:
			case KW_PROCEDURE:
			case KW_ATTRIBUTE:
			case KW_VARIABLE:
			case KW_SUBTYPE:
			case KW_CONSTANT:
			case KW_FUNCTION:
			case KW_ALIAS:
			case KW_IMPURE:
			case KW_PACKAGE:
			case KW_TYPE:
				enterOuterAlt(_localctx, 1);
				{
				setState(876);
				process_or_package_declarative_item();
				}
				break;
			case KW_SIGNAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(877);
				signal_declaration();
				}
				break;
			case KW_COMPONENT:
				enterOuterAlt(_localctx, 3);
				{
				setState(878);
				component_declaration();
				}
				break;
			case KW_DISCONNECT:
				enterOuterAlt(_localctx, 4);
				{
				setState(879);
				disconnection_specification();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Package_bodyContext extends ParserRuleContext {
		public List<TerminalNode> KW_PACKAGE() { return getTokens(vhdlParser.KW_PACKAGE); }
		public TerminalNode KW_PACKAGE(int i) {
			return getToken(vhdlParser.KW_PACKAGE, i);
		}
		public List<TerminalNode> KW_BODY() { return getTokens(vhdlParser.KW_BODY); }
		public TerminalNode KW_BODY(int i) {
			return getToken(vhdlParser.KW_BODY, i);
		}
		public List<IdentifierContext> identifier() {
			return getRuleContexts(IdentifierContext.class);
		}
		public IdentifierContext identifier(int i) {
			return getRuleContext(IdentifierContext.class,i);
		}
		public TerminalNode KW_IS() { return getToken(vhdlParser.KW_IS, 0); }
		public TerminalNode KW_END() { return getToken(vhdlParser.KW_END, 0); }
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public List<Process_declarative_itemContext> process_declarative_item() {
			return getRuleContexts(Process_declarative_itemContext.class);
		}
		public Process_declarative_itemContext process_declarative_item(int i) {
			return getRuleContext(Process_declarative_itemContext.class,i);
		}
		public Package_bodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_package_body; }
	}

	public final Package_bodyContext package_body() throws RecognitionException {
		Package_bodyContext _localctx = new Package_bodyContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_package_body);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(882);
			match(KW_PACKAGE);
			setState(883);
			match(KW_BODY);
			setState(884);
			identifier();
			setState(885);
			match(KW_IS);
			setState(889);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << KW_GROUP) | (1L << KW_FILE) | (1L << KW_PURE) | (1L << KW_USE) | (1L << KW_SHARED) | (1L << KW_PROCEDURE) | (1L << KW_ATTRIBUTE) | (1L << KW_VARIABLE) | (1L << KW_SUBTYPE) | (1L << KW_CONSTANT) | (1L << KW_FUNCTION))) != 0) || ((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & ((1L << (KW_ALIAS - 65)) | (1L << (KW_IMPURE - 65)) | (1L << (KW_PACKAGE - 65)) | (1L << (KW_TYPE - 65)))) != 0)) {
				{
				{
				setState(886);
				process_declarative_item();
				}
				}
				setState(891);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(892);
			match(KW_END);
			setState(895);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_PACKAGE) {
				{
				setState(893);
				match(KW_PACKAGE);
				setState(894);
				match(KW_BODY);
				}
			}

			setState(898);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==BASIC_IDENTIFIER || _la==EXTENDED_IDENTIFIER) {
				{
				setState(897);
				identifier();
				}
			}

			setState(900);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Package_instantiation_declarationContext extends ParserRuleContext {
		public TerminalNode KW_PACKAGE() { return getToken(vhdlParser.KW_PACKAGE, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode KW_IS() { return getToken(vhdlParser.KW_IS, 0); }
		public TerminalNode KW_NEW() { return getToken(vhdlParser.KW_NEW, 0); }
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public Generic_map_aspectContext generic_map_aspect() {
			return getRuleContext(Generic_map_aspectContext.class,0);
		}
		public Package_instantiation_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_package_instantiation_declaration; }
	}

	public final Package_instantiation_declarationContext package_instantiation_declaration() throws RecognitionException {
		Package_instantiation_declarationContext _localctx = new Package_instantiation_declarationContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_package_instantiation_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(902);
			match(KW_PACKAGE);
			setState(903);
			identifier();
			setState(904);
			match(KW_IS);
			setState(905);
			match(KW_NEW);
			setState(906);
			name(0);
			setState(908);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_GENERIC) {
				{
				setState(907);
				generic_map_aspect();
				}
			}

			setState(910);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Scalar_type_definitionContext extends ParserRuleContext {
		public Enumeration_type_definitionContext enumeration_type_definition() {
			return getRuleContext(Enumeration_type_definitionContext.class,0);
		}
		public Integer_type_definitionContext integer_type_definition() {
			return getRuleContext(Integer_type_definitionContext.class,0);
		}
		public Floating_type_definitionContext floating_type_definition() {
			return getRuleContext(Floating_type_definitionContext.class,0);
		}
		public Physical_type_definitionContext physical_type_definition() {
			return getRuleContext(Physical_type_definitionContext.class,0);
		}
		public Scalar_type_definitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_scalar_type_definition; }
	}

	public final Scalar_type_definitionContext scalar_type_definition() throws RecognitionException {
		Scalar_type_definitionContext _localctx = new Scalar_type_definitionContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_scalar_type_definition);
		try {
			setState(916);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,64,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(912);
				enumeration_type_definition();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(913);
				integer_type_definition();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(914);
				floating_type_definition();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(915);
				physical_type_definition();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Range_constraintContext extends ParserRuleContext {
		public TerminalNode KW_RANGE() { return getToken(vhdlParser.KW_RANGE, 0); }
		public Range_Context range_() {
			return getRuleContext(Range_Context.class,0);
		}
		public Range_constraintContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_range_constraint; }
	}

	public final Range_constraintContext range_constraint() throws RecognitionException {
		Range_constraintContext _localctx = new Range_constraintContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_range_constraint);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(918);
			match(KW_RANGE);
			setState(919);
			range_();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Range_Context extends ParserRuleContext {
		public Attribute_nameContext attribute_name() {
			return getRuleContext(Attribute_nameContext.class,0);
		}
		public List<Simple_expressionContext> simple_expression() {
			return getRuleContexts(Simple_expressionContext.class);
		}
		public Simple_expressionContext simple_expression(int i) {
			return getRuleContext(Simple_expressionContext.class,i);
		}
		public DirectionContext direction() {
			return getRuleContext(DirectionContext.class,0);
		}
		public Range_Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_range_; }
	}

	public final Range_Context range_() throws RecognitionException {
		Range_Context _localctx = new Range_Context(_ctx, getState());
		enterRule(_localctx, 78, RULE_range_);
		try {
			setState(926);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,65,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(921);
				attribute_name();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(922);
				simple_expression(0);
				setState(923);
				direction();
				setState(924);
				simple_expression(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DirectionContext extends ParserRuleContext {
		public TerminalNode KW_TO() { return getToken(vhdlParser.KW_TO, 0); }
		public TerminalNode KW_DOWNTO() { return getToken(vhdlParser.KW_DOWNTO, 0); }
		public DirectionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_direction; }
	}

	public final DirectionContext direction() throws RecognitionException {
		DirectionContext _localctx = new DirectionContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_direction);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(928);
			_la = _input.LA(1);
			if ( !(_la==KW_TO || _la==KW_DOWNTO) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Enumeration_type_definitionContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(vhdlParser.LPAREN, 0); }
		public List<Enumeration_literalContext> enumeration_literal() {
			return getRuleContexts(Enumeration_literalContext.class);
		}
		public Enumeration_literalContext enumeration_literal(int i) {
			return getRuleContext(Enumeration_literalContext.class,i);
		}
		public TerminalNode RPAREN() { return getToken(vhdlParser.RPAREN, 0); }
		public List<TerminalNode> COMMA() { return getTokens(vhdlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(vhdlParser.COMMA, i);
		}
		public Enumeration_type_definitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_enumeration_type_definition; }
	}

	public final Enumeration_type_definitionContext enumeration_type_definition() throws RecognitionException {
		Enumeration_type_definitionContext _localctx = new Enumeration_type_definitionContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_enumeration_type_definition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(930);
			match(LPAREN);
			setState(931);
			enumeration_literal();
			setState(936);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(932);
				match(COMMA);
				setState(933);
				enumeration_literal();
				}
				}
				setState(938);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(939);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Enumeration_literalContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode CHARACTER_LITERAL() { return getToken(vhdlParser.CHARACTER_LITERAL, 0); }
		public Enumeration_literalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_enumeration_literal; }
	}

	public final Enumeration_literalContext enumeration_literal() throws RecognitionException {
		Enumeration_literalContext _localctx = new Enumeration_literalContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_enumeration_literal);
		try {
			setState(943);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BASIC_IDENTIFIER:
			case EXTENDED_IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(941);
				identifier();
				}
				break;
			case CHARACTER_LITERAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(942);
				match(CHARACTER_LITERAL);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Integer_type_definitionContext extends ParserRuleContext {
		public Range_constraintContext range_constraint() {
			return getRuleContext(Range_constraintContext.class,0);
		}
		public Integer_type_definitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_integer_type_definition; }
	}

	public final Integer_type_definitionContext integer_type_definition() throws RecognitionException {
		Integer_type_definitionContext _localctx = new Integer_type_definitionContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_integer_type_definition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(945);
			range_constraint();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Physical_type_definitionContext extends ParserRuleContext {
		public Range_constraintContext range_constraint() {
			return getRuleContext(Range_constraintContext.class,0);
		}
		public List<TerminalNode> KW_UNITS() { return getTokens(vhdlParser.KW_UNITS); }
		public TerminalNode KW_UNITS(int i) {
			return getToken(vhdlParser.KW_UNITS, i);
		}
		public Primary_unit_declarationContext primary_unit_declaration() {
			return getRuleContext(Primary_unit_declarationContext.class,0);
		}
		public TerminalNode KW_END() { return getToken(vhdlParser.KW_END, 0); }
		public List<Secondary_unit_declarationContext> secondary_unit_declaration() {
			return getRuleContexts(Secondary_unit_declarationContext.class);
		}
		public Secondary_unit_declarationContext secondary_unit_declaration(int i) {
			return getRuleContext(Secondary_unit_declarationContext.class,i);
		}
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public Physical_type_definitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_physical_type_definition; }
	}

	public final Physical_type_definitionContext physical_type_definition() throws RecognitionException {
		Physical_type_definitionContext _localctx = new Physical_type_definitionContext(_ctx, getState());
		enterRule(_localctx, 88, RULE_physical_type_definition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(947);
			range_constraint();
			setState(948);
			match(KW_UNITS);
			setState(949);
			primary_unit_declaration();
			setState(953);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==BASIC_IDENTIFIER || _la==EXTENDED_IDENTIFIER) {
				{
				{
				setState(950);
				secondary_unit_declaration();
				}
				}
				setState(955);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(956);
			match(KW_END);
			setState(957);
			match(KW_UNITS);
			setState(959);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==BASIC_IDENTIFIER || _la==EXTENDED_IDENTIFIER) {
				{
				setState(958);
				identifier();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Primary_unit_declarationContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public Primary_unit_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primary_unit_declaration; }
	}

	public final Primary_unit_declarationContext primary_unit_declaration() throws RecognitionException {
		Primary_unit_declarationContext _localctx = new Primary_unit_declarationContext(_ctx, getState());
		enterRule(_localctx, 90, RULE_primary_unit_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(961);
			identifier();
			setState(962);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Secondary_unit_declarationContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode EQ() { return getToken(vhdlParser.EQ, 0); }
		public Physical_literalContext physical_literal() {
			return getRuleContext(Physical_literalContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public Secondary_unit_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_secondary_unit_declaration; }
	}

	public final Secondary_unit_declarationContext secondary_unit_declaration() throws RecognitionException {
		Secondary_unit_declarationContext _localctx = new Secondary_unit_declarationContext(_ctx, getState());
		enterRule(_localctx, 92, RULE_secondary_unit_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(964);
			identifier();
			setState(965);
			match(EQ);
			setState(966);
			physical_literal();
			setState(967);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Floating_type_definitionContext extends ParserRuleContext {
		public Range_constraintContext range_constraint() {
			return getRuleContext(Range_constraintContext.class,0);
		}
		public Floating_type_definitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_floating_type_definition; }
	}

	public final Floating_type_definitionContext floating_type_definition() throws RecognitionException {
		Floating_type_definitionContext _localctx = new Floating_type_definitionContext(_ctx, getState());
		enterRule(_localctx, 94, RULE_floating_type_definition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(969);
			range_constraint();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Composite_type_definitionContext extends ParserRuleContext {
		public Array_type_definitionContext array_type_definition() {
			return getRuleContext(Array_type_definitionContext.class,0);
		}
		public Record_type_definitionContext record_type_definition() {
			return getRuleContext(Record_type_definitionContext.class,0);
		}
		public Composite_type_definitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_composite_type_definition; }
	}

	public final Composite_type_definitionContext composite_type_definition() throws RecognitionException {
		Composite_type_definitionContext _localctx = new Composite_type_definitionContext(_ctx, getState());
		enterRule(_localctx, 96, RULE_composite_type_definition);
		try {
			setState(973);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KW_ARRAY:
				enterOuterAlt(_localctx, 1);
				{
				setState(971);
				array_type_definition();
				}
				break;
			case KW_RECORD:
				enterOuterAlt(_localctx, 2);
				{
				setState(972);
				record_type_definition();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Array_type_definitionContext extends ParserRuleContext {
		public Unbounded_array_definitionContext unbounded_array_definition() {
			return getRuleContext(Unbounded_array_definitionContext.class,0);
		}
		public Constrained_array_definitionContext constrained_array_definition() {
			return getRuleContext(Constrained_array_definitionContext.class,0);
		}
		public Array_type_definitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_type_definition; }
	}

	public final Array_type_definitionContext array_type_definition() throws RecognitionException {
		Array_type_definitionContext _localctx = new Array_type_definitionContext(_ctx, getState());
		enterRule(_localctx, 98, RULE_array_type_definition);
		try {
			setState(977);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,71,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(975);
				unbounded_array_definition();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(976);
				constrained_array_definition();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Unbounded_array_definitionContext extends ParserRuleContext {
		public TerminalNode KW_ARRAY() { return getToken(vhdlParser.KW_ARRAY, 0); }
		public TerminalNode LPAREN() { return getToken(vhdlParser.LPAREN, 0); }
		public List<Index_subtype_definitionContext> index_subtype_definition() {
			return getRuleContexts(Index_subtype_definitionContext.class);
		}
		public Index_subtype_definitionContext index_subtype_definition(int i) {
			return getRuleContext(Index_subtype_definitionContext.class,i);
		}
		public TerminalNode RPAREN() { return getToken(vhdlParser.RPAREN, 0); }
		public TerminalNode KW_OF() { return getToken(vhdlParser.KW_OF, 0); }
		public Subtype_indicationContext subtype_indication() {
			return getRuleContext(Subtype_indicationContext.class,0);
		}
		public List<TerminalNode> COMMA() { return getTokens(vhdlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(vhdlParser.COMMA, i);
		}
		public Unbounded_array_definitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unbounded_array_definition; }
	}

	public final Unbounded_array_definitionContext unbounded_array_definition() throws RecognitionException {
		Unbounded_array_definitionContext _localctx = new Unbounded_array_definitionContext(_ctx, getState());
		enterRule(_localctx, 100, RULE_unbounded_array_definition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(979);
			match(KW_ARRAY);
			setState(980);
			match(LPAREN);
			setState(981);
			index_subtype_definition();
			setState(986);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(982);
				match(COMMA);
				setState(983);
				index_subtype_definition();
				}
				}
				setState(988);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(989);
			match(RPAREN);
			setState(990);
			match(KW_OF);
			setState(991);
			subtype_indication();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Constrained_array_definitionContext extends ParserRuleContext {
		public TerminalNode KW_ARRAY() { return getToken(vhdlParser.KW_ARRAY, 0); }
		public Index_constraintContext index_constraint() {
			return getRuleContext(Index_constraintContext.class,0);
		}
		public TerminalNode KW_OF() { return getToken(vhdlParser.KW_OF, 0); }
		public Subtype_indicationContext subtype_indication() {
			return getRuleContext(Subtype_indicationContext.class,0);
		}
		public Constrained_array_definitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constrained_array_definition; }
	}

	public final Constrained_array_definitionContext constrained_array_definition() throws RecognitionException {
		Constrained_array_definitionContext _localctx = new Constrained_array_definitionContext(_ctx, getState());
		enterRule(_localctx, 102, RULE_constrained_array_definition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(993);
			match(KW_ARRAY);
			setState(994);
			index_constraint();
			setState(995);
			match(KW_OF);
			setState(996);
			subtype_indication();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Index_subtype_definitionContext extends ParserRuleContext {
		public Type_markContext type_mark() {
			return getRuleContext(Type_markContext.class,0);
		}
		public TerminalNode KW_RANGE() { return getToken(vhdlParser.KW_RANGE, 0); }
		public TerminalNode BOX() { return getToken(vhdlParser.BOX, 0); }
		public Index_subtype_definitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_index_subtype_definition; }
	}

	public final Index_subtype_definitionContext index_subtype_definition() throws RecognitionException {
		Index_subtype_definitionContext _localctx = new Index_subtype_definitionContext(_ctx, getState());
		enterRule(_localctx, 104, RULE_index_subtype_definition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(998);
			type_mark();
			setState(999);
			match(KW_RANGE);
			setState(1000);
			match(BOX);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Array_constraintContext extends ParserRuleContext {
		public Index_constraintContext index_constraint() {
			return getRuleContext(Index_constraintContext.class,0);
		}
		public Array_element_constraintContext array_element_constraint() {
			return getRuleContext(Array_element_constraintContext.class,0);
		}
		public TerminalNode LPAREN() { return getToken(vhdlParser.LPAREN, 0); }
		public TerminalNode KW_OPEN() { return getToken(vhdlParser.KW_OPEN, 0); }
		public TerminalNode RPAREN() { return getToken(vhdlParser.RPAREN, 0); }
		public Array_constraintContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_constraint; }
	}

	public final Array_constraintContext array_constraint() throws RecognitionException {
		Array_constraintContext _localctx = new Array_constraintContext(_ctx, getState());
		enterRule(_localctx, 106, RULE_array_constraint);
		try {
			setState(1012);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,75,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(1002);
				index_constraint();
				setState(1004);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,73,_ctx) ) {
				case 1:
					{
					setState(1003);
					array_element_constraint();
					}
					break;
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(1006);
				match(LPAREN);
				setState(1007);
				match(KW_OPEN);
				setState(1008);
				match(RPAREN);
				setState(1010);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,74,_ctx) ) {
				case 1:
					{
					setState(1009);
					array_element_constraint();
					}
					break;
				}
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Array_element_constraintContext extends ParserRuleContext {
		public Element_constraintContext element_constraint() {
			return getRuleContext(Element_constraintContext.class,0);
		}
		public Array_element_constraintContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_element_constraint; }
	}

	public final Array_element_constraintContext array_element_constraint() throws RecognitionException {
		Array_element_constraintContext _localctx = new Array_element_constraintContext(_ctx, getState());
		enterRule(_localctx, 108, RULE_array_element_constraint);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1014);
			element_constraint();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Index_constraintContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(vhdlParser.LPAREN, 0); }
		public List<Discrete_rangeContext> discrete_range() {
			return getRuleContexts(Discrete_rangeContext.class);
		}
		public Discrete_rangeContext discrete_range(int i) {
			return getRuleContext(Discrete_rangeContext.class,i);
		}
		public TerminalNode RPAREN() { return getToken(vhdlParser.RPAREN, 0); }
		public List<TerminalNode> COMMA() { return getTokens(vhdlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(vhdlParser.COMMA, i);
		}
		public Index_constraintContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_index_constraint; }
	}

	public final Index_constraintContext index_constraint() throws RecognitionException {
		Index_constraintContext _localctx = new Index_constraintContext(_ctx, getState());
		enterRule(_localctx, 110, RULE_index_constraint);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1016);
			match(LPAREN);
			setState(1017);
			discrete_range();
			setState(1022);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(1018);
				match(COMMA);
				setState(1019);
				discrete_range();
				}
				}
				setState(1024);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(1025);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Discrete_rangeContext extends ParserRuleContext {
		public Subtype_indicationContext subtype_indication() {
			return getRuleContext(Subtype_indicationContext.class,0);
		}
		public Range_Context range_() {
			return getRuleContext(Range_Context.class,0);
		}
		public Discrete_rangeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_discrete_range; }
	}

	public final Discrete_rangeContext discrete_range() throws RecognitionException {
		Discrete_rangeContext _localctx = new Discrete_rangeContext(_ctx, getState());
		enterRule(_localctx, 112, RULE_discrete_range);
		try {
			setState(1029);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,77,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(1027);
				subtype_indication();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(1028);
				range_();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Record_type_definitionContext extends ParserRuleContext {
		public List<TerminalNode> KW_RECORD() { return getTokens(vhdlParser.KW_RECORD); }
		public TerminalNode KW_RECORD(int i) {
			return getToken(vhdlParser.KW_RECORD, i);
		}
		public TerminalNode KW_END() { return getToken(vhdlParser.KW_END, 0); }
		public List<Element_declarationContext> element_declaration() {
			return getRuleContexts(Element_declarationContext.class);
		}
		public Element_declarationContext element_declaration(int i) {
			return getRuleContext(Element_declarationContext.class,i);
		}
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public Record_type_definitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_record_type_definition; }
	}

	public final Record_type_definitionContext record_type_definition() throws RecognitionException {
		Record_type_definitionContext _localctx = new Record_type_definitionContext(_ctx, getState());
		enterRule(_localctx, 114, RULE_record_type_definition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1031);
			match(KW_RECORD);
			setState(1033); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(1032);
				element_declaration();
				}
				}
				setState(1035); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==BASIC_IDENTIFIER || _la==EXTENDED_IDENTIFIER );
			setState(1037);
			match(KW_END);
			setState(1038);
			match(KW_RECORD);
			setState(1040);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==BASIC_IDENTIFIER || _la==EXTENDED_IDENTIFIER) {
				{
				setState(1039);
				identifier();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Element_declarationContext extends ParserRuleContext {
		public Identifier_listContext identifier_list() {
			return getRuleContext(Identifier_listContext.class,0);
		}
		public TerminalNode COLON() { return getToken(vhdlParser.COLON, 0); }
		public Element_subtype_definitionContext element_subtype_definition() {
			return getRuleContext(Element_subtype_definitionContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public Element_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_element_declaration; }
	}

	public final Element_declarationContext element_declaration() throws RecognitionException {
		Element_declarationContext _localctx = new Element_declarationContext(_ctx, getState());
		enterRule(_localctx, 116, RULE_element_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1042);
			identifier_list();
			setState(1043);
			match(COLON);
			setState(1044);
			element_subtype_definition();
			setState(1045);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Identifier_listContext extends ParserRuleContext {
		public List<IdentifierContext> identifier() {
			return getRuleContexts(IdentifierContext.class);
		}
		public IdentifierContext identifier(int i) {
			return getRuleContext(IdentifierContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(vhdlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(vhdlParser.COMMA, i);
		}
		public Identifier_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifier_list; }
	}

	public final Identifier_listContext identifier_list() throws RecognitionException {
		Identifier_listContext _localctx = new Identifier_listContext(_ctx, getState());
		enterRule(_localctx, 118, RULE_identifier_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1047);
			identifier();
			setState(1052);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(1048);
				match(COMMA);
				setState(1049);
				identifier();
				}
				}
				setState(1054);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Element_subtype_definitionContext extends ParserRuleContext {
		public Subtype_indicationContext subtype_indication() {
			return getRuleContext(Subtype_indicationContext.class,0);
		}
		public Element_subtype_definitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_element_subtype_definition; }
	}

	public final Element_subtype_definitionContext element_subtype_definition() throws RecognitionException {
		Element_subtype_definitionContext _localctx = new Element_subtype_definitionContext(_ctx, getState());
		enterRule(_localctx, 120, RULE_element_subtype_definition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1055);
			subtype_indication();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Record_constraintContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(vhdlParser.LPAREN, 0); }
		public List<Record_element_constraintContext> record_element_constraint() {
			return getRuleContexts(Record_element_constraintContext.class);
		}
		public Record_element_constraintContext record_element_constraint(int i) {
			return getRuleContext(Record_element_constraintContext.class,i);
		}
		public TerminalNode RPAREN() { return getToken(vhdlParser.RPAREN, 0); }
		public List<TerminalNode> COMMA() { return getTokens(vhdlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(vhdlParser.COMMA, i);
		}
		public Record_constraintContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_record_constraint; }
	}

	public final Record_constraintContext record_constraint() throws RecognitionException {
		Record_constraintContext _localctx = new Record_constraintContext(_ctx, getState());
		enterRule(_localctx, 122, RULE_record_constraint);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1057);
			match(LPAREN);
			setState(1058);
			record_element_constraint();
			setState(1063);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(1059);
				match(COMMA);
				setState(1060);
				record_element_constraint();
				}
				}
				setState(1065);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(1066);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Record_element_constraintContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public Element_constraintContext element_constraint() {
			return getRuleContext(Element_constraintContext.class,0);
		}
		public Record_element_constraintContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_record_element_constraint; }
	}

	public final Record_element_constraintContext record_element_constraint() throws RecognitionException {
		Record_element_constraintContext _localctx = new Record_element_constraintContext(_ctx, getState());
		enterRule(_localctx, 124, RULE_record_element_constraint);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1068);
			identifier();
			setState(1069);
			element_constraint();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Access_type_definitionContext extends ParserRuleContext {
		public TerminalNode KW_ACCESS() { return getToken(vhdlParser.KW_ACCESS, 0); }
		public Subtype_indicationContext subtype_indication() {
			return getRuleContext(Subtype_indicationContext.class,0);
		}
		public Access_type_definitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_access_type_definition; }
	}

	public final Access_type_definitionContext access_type_definition() throws RecognitionException {
		Access_type_definitionContext _localctx = new Access_type_definitionContext(_ctx, getState());
		enterRule(_localctx, 126, RULE_access_type_definition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1071);
			match(KW_ACCESS);
			setState(1072);
			subtype_indication();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Incomplete_type_declarationContext extends ParserRuleContext {
		public TerminalNode KW_TYPE() { return getToken(vhdlParser.KW_TYPE, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public Incomplete_type_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_incomplete_type_declaration; }
	}

	public final Incomplete_type_declarationContext incomplete_type_declaration() throws RecognitionException {
		Incomplete_type_declarationContext _localctx = new Incomplete_type_declarationContext(_ctx, getState());
		enterRule(_localctx, 128, RULE_incomplete_type_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1074);
			match(KW_TYPE);
			setState(1075);
			identifier();
			setState(1076);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class File_type_definitionContext extends ParserRuleContext {
		public TerminalNode KW_FILE() { return getToken(vhdlParser.KW_FILE, 0); }
		public TerminalNode KW_OF() { return getToken(vhdlParser.KW_OF, 0); }
		public Type_markContext type_mark() {
			return getRuleContext(Type_markContext.class,0);
		}
		public File_type_definitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_file_type_definition; }
	}

	public final File_type_definitionContext file_type_definition() throws RecognitionException {
		File_type_definitionContext _localctx = new File_type_definitionContext(_ctx, getState());
		enterRule(_localctx, 130, RULE_file_type_definition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1078);
			match(KW_FILE);
			setState(1079);
			match(KW_OF);
			setState(1080);
			type_mark();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Protected_type_definitionContext extends ParserRuleContext {
		public Protected_type_declarationContext protected_type_declaration() {
			return getRuleContext(Protected_type_declarationContext.class,0);
		}
		public Protected_type_bodyContext protected_type_body() {
			return getRuleContext(Protected_type_bodyContext.class,0);
		}
		public Protected_type_definitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_protected_type_definition; }
	}

	public final Protected_type_definitionContext protected_type_definition() throws RecognitionException {
		Protected_type_definitionContext _localctx = new Protected_type_definitionContext(_ctx, getState());
		enterRule(_localctx, 132, RULE_protected_type_definition);
		try {
			setState(1084);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,82,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(1082);
				protected_type_declaration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(1083);
				protected_type_body();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Protected_type_declarationContext extends ParserRuleContext {
		public List<TerminalNode> KW_PROTECTED() { return getTokens(vhdlParser.KW_PROTECTED); }
		public TerminalNode KW_PROTECTED(int i) {
			return getToken(vhdlParser.KW_PROTECTED, i);
		}
		public TerminalNode KW_END() { return getToken(vhdlParser.KW_END, 0); }
		public List<Protected_type_declarative_itemContext> protected_type_declarative_item() {
			return getRuleContexts(Protected_type_declarative_itemContext.class);
		}
		public Protected_type_declarative_itemContext protected_type_declarative_item(int i) {
			return getRuleContext(Protected_type_declarative_itemContext.class,i);
		}
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public Protected_type_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_protected_type_declaration; }
	}

	public final Protected_type_declarationContext protected_type_declaration() throws RecognitionException {
		Protected_type_declarationContext _localctx = new Protected_type_declarationContext(_ctx, getState());
		enterRule(_localctx, 134, RULE_protected_type_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1086);
			match(KW_PROTECTED);
			setState(1090);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 18)) & ~0x3f) == 0 && ((1L << (_la - 18)) & ((1L << (KW_PURE - 18)) | (1L << (KW_USE - 18)) | (1L << (KW_PROCEDURE - 18)) | (1L << (KW_ATTRIBUTE - 18)) | (1L << (KW_FUNCTION - 18)) | (1L << (KW_IMPURE - 18)))) != 0)) {
				{
				{
				setState(1087);
				protected_type_declarative_item();
				}
				}
				setState(1092);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(1093);
			match(KW_END);
			setState(1094);
			match(KW_PROTECTED);
			setState(1096);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==BASIC_IDENTIFIER || _la==EXTENDED_IDENTIFIER) {
				{
				setState(1095);
				identifier();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Protected_type_declarative_itemContext extends ParserRuleContext {
		public Subprogram_declarationContext subprogram_declaration() {
			return getRuleContext(Subprogram_declarationContext.class,0);
		}
		public Subprogram_instantiation_declarationContext subprogram_instantiation_declaration() {
			return getRuleContext(Subprogram_instantiation_declarationContext.class,0);
		}
		public Attribute_specificationContext attribute_specification() {
			return getRuleContext(Attribute_specificationContext.class,0);
		}
		public Use_clauseContext use_clause() {
			return getRuleContext(Use_clauseContext.class,0);
		}
		public Protected_type_declarative_itemContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_protected_type_declarative_item; }
	}

	public final Protected_type_declarative_itemContext protected_type_declarative_item() throws RecognitionException {
		Protected_type_declarative_itemContext _localctx = new Protected_type_declarative_itemContext(_ctx, getState());
		enterRule(_localctx, 136, RULE_protected_type_declarative_item);
		try {
			setState(1102);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,85,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(1098);
				subprogram_declaration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(1099);
				subprogram_instantiation_declaration();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(1100);
				attribute_specification();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(1101);
				use_clause();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Protected_type_bodyContext extends ParserRuleContext {
		public List<TerminalNode> KW_PROTECTED() { return getTokens(vhdlParser.KW_PROTECTED); }
		public TerminalNode KW_PROTECTED(int i) {
			return getToken(vhdlParser.KW_PROTECTED, i);
		}
		public List<TerminalNode> KW_BODY() { return getTokens(vhdlParser.KW_BODY); }
		public TerminalNode KW_BODY(int i) {
			return getToken(vhdlParser.KW_BODY, i);
		}
		public TerminalNode KW_END() { return getToken(vhdlParser.KW_END, 0); }
		public List<Process_declarative_itemContext> process_declarative_item() {
			return getRuleContexts(Process_declarative_itemContext.class);
		}
		public Process_declarative_itemContext process_declarative_item(int i) {
			return getRuleContext(Process_declarative_itemContext.class,i);
		}
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public Protected_type_bodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_protected_type_body; }
	}

	public final Protected_type_bodyContext protected_type_body() throws RecognitionException {
		Protected_type_bodyContext _localctx = new Protected_type_bodyContext(_ctx, getState());
		enterRule(_localctx, 138, RULE_protected_type_body);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1104);
			match(KW_PROTECTED);
			setState(1105);
			match(KW_BODY);
			setState(1109);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << KW_GROUP) | (1L << KW_FILE) | (1L << KW_PURE) | (1L << KW_USE) | (1L << KW_SHARED) | (1L << KW_PROCEDURE) | (1L << KW_ATTRIBUTE) | (1L << KW_VARIABLE) | (1L << KW_SUBTYPE) | (1L << KW_CONSTANT) | (1L << KW_FUNCTION))) != 0) || ((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & ((1L << (KW_ALIAS - 65)) | (1L << (KW_IMPURE - 65)) | (1L << (KW_PACKAGE - 65)) | (1L << (KW_TYPE - 65)))) != 0)) {
				{
				{
				setState(1106);
				process_declarative_item();
				}
				}
				setState(1111);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(1112);
			match(KW_END);
			setState(1113);
			match(KW_PROTECTED);
			setState(1114);
			match(KW_BODY);
			setState(1116);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==BASIC_IDENTIFIER || _la==EXTENDED_IDENTIFIER) {
				{
				setState(1115);
				identifier();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Type_declarationContext extends ParserRuleContext {
		public Full_type_declarationContext full_type_declaration() {
			return getRuleContext(Full_type_declarationContext.class,0);
		}
		public Incomplete_type_declarationContext incomplete_type_declaration() {
			return getRuleContext(Incomplete_type_declarationContext.class,0);
		}
		public Type_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type_declaration; }
	}

	public final Type_declarationContext type_declaration() throws RecognitionException {
		Type_declarationContext _localctx = new Type_declarationContext(_ctx, getState());
		enterRule(_localctx, 140, RULE_type_declaration);
		try {
			setState(1120);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,88,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(1118);
				full_type_declaration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(1119);
				incomplete_type_declaration();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Full_type_declarationContext extends ParserRuleContext {
		public TerminalNode KW_TYPE() { return getToken(vhdlParser.KW_TYPE, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode KW_IS() { return getToken(vhdlParser.KW_IS, 0); }
		public Type_definitionContext type_definition() {
			return getRuleContext(Type_definitionContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public Full_type_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_full_type_declaration; }
	}

	public final Full_type_declarationContext full_type_declaration() throws RecognitionException {
		Full_type_declarationContext _localctx = new Full_type_declarationContext(_ctx, getState());
		enterRule(_localctx, 142, RULE_full_type_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1122);
			match(KW_TYPE);
			setState(1123);
			identifier();
			setState(1124);
			match(KW_IS);
			setState(1125);
			type_definition();
			setState(1126);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Type_definitionContext extends ParserRuleContext {
		public Scalar_type_definitionContext scalar_type_definition() {
			return getRuleContext(Scalar_type_definitionContext.class,0);
		}
		public Composite_type_definitionContext composite_type_definition() {
			return getRuleContext(Composite_type_definitionContext.class,0);
		}
		public Access_type_definitionContext access_type_definition() {
			return getRuleContext(Access_type_definitionContext.class,0);
		}
		public File_type_definitionContext file_type_definition() {
			return getRuleContext(File_type_definitionContext.class,0);
		}
		public Protected_type_definitionContext protected_type_definition() {
			return getRuleContext(Protected_type_definitionContext.class,0);
		}
		public Type_definitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type_definition; }
	}

	public final Type_definitionContext type_definition() throws RecognitionException {
		Type_definitionContext _localctx = new Type_definitionContext(_ctx, getState());
		enterRule(_localctx, 144, RULE_type_definition);
		try {
			setState(1133);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KW_RANGE:
			case LPAREN:
				enterOuterAlt(_localctx, 1);
				{
				setState(1128);
				scalar_type_definition();
				}
				break;
			case KW_RECORD:
			case KW_ARRAY:
				enterOuterAlt(_localctx, 2);
				{
				setState(1129);
				composite_type_definition();
				}
				break;
			case KW_ACCESS:
				enterOuterAlt(_localctx, 3);
				{
				setState(1130);
				access_type_definition();
				}
				break;
			case KW_FILE:
				enterOuterAlt(_localctx, 4);
				{
				setState(1131);
				file_type_definition();
				}
				break;
			case KW_PROTECTED:
				enterOuterAlt(_localctx, 5);
				{
				setState(1132);
				protected_type_definition();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Subtype_declarationContext extends ParserRuleContext {
		public TerminalNode KW_SUBTYPE() { return getToken(vhdlParser.KW_SUBTYPE, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode KW_IS() { return getToken(vhdlParser.KW_IS, 0); }
		public Subtype_indicationContext subtype_indication() {
			return getRuleContext(Subtype_indicationContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public Subtype_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subtype_declaration; }
	}

	public final Subtype_declarationContext subtype_declaration() throws RecognitionException {
		Subtype_declarationContext _localctx = new Subtype_declarationContext(_ctx, getState());
		enterRule(_localctx, 146, RULE_subtype_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1135);
			match(KW_SUBTYPE);
			setState(1136);
			identifier();
			setState(1137);
			match(KW_IS);
			setState(1138);
			subtype_indication();
			setState(1139);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Subtype_indicationContext extends ParserRuleContext {
		public Type_markContext type_mark() {
			return getRuleContext(Type_markContext.class,0);
		}
		public Resolution_indicationContext resolution_indication() {
			return getRuleContext(Resolution_indicationContext.class,0);
		}
		public ConstraintContext constraint() {
			return getRuleContext(ConstraintContext.class,0);
		}
		public Subtype_indicationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subtype_indication; }
	}

	public final Subtype_indicationContext subtype_indication() throws RecognitionException {
		Subtype_indicationContext _localctx = new Subtype_indicationContext(_ctx, getState());
		enterRule(_localctx, 148, RULE_subtype_indication);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1142);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,90,_ctx) ) {
			case 1:
				{
				setState(1141);
				resolution_indication();
				}
				break;
			}
			setState(1144);
			type_mark();
			setState(1146);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,91,_ctx) ) {
			case 1:
				{
				setState(1145);
				constraint();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Resolution_indicationContext extends ParserRuleContext {
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public TerminalNode LPAREN() { return getToken(vhdlParser.LPAREN, 0); }
		public Element_resolutionContext element_resolution() {
			return getRuleContext(Element_resolutionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(vhdlParser.RPAREN, 0); }
		public Resolution_indicationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_resolution_indication; }
	}

	public final Resolution_indicationContext resolution_indication() throws RecognitionException {
		Resolution_indicationContext _localctx = new Resolution_indicationContext(_ctx, getState());
		enterRule(_localctx, 150, RULE_resolution_indication);
		try {
			setState(1153);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BASIC_IDENTIFIER:
			case EXTENDED_IDENTIFIER:
			case CHARACTER_LITERAL:
			case STRING_LITERAL:
			case SHIFT_LEFT:
				enterOuterAlt(_localctx, 1);
				{
				setState(1148);
				name(0);
				}
				break;
			case LPAREN:
				enterOuterAlt(_localctx, 2);
				{
				setState(1149);
				match(LPAREN);
				setState(1150);
				element_resolution();
				setState(1151);
				match(RPAREN);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Element_resolutionContext extends ParserRuleContext {
		public Array_element_resolutionContext array_element_resolution() {
			return getRuleContext(Array_element_resolutionContext.class,0);
		}
		public Record_resolutionContext record_resolution() {
			return getRuleContext(Record_resolutionContext.class,0);
		}
		public Element_resolutionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_element_resolution; }
	}

	public final Element_resolutionContext element_resolution() throws RecognitionException {
		Element_resolutionContext _localctx = new Element_resolutionContext(_ctx, getState());
		enterRule(_localctx, 152, RULE_element_resolution);
		try {
			setState(1157);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,93,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(1155);
				array_element_resolution();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(1156);
				record_resolution();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Array_element_resolutionContext extends ParserRuleContext {
		public Resolution_indicationContext resolution_indication() {
			return getRuleContext(Resolution_indicationContext.class,0);
		}
		public Array_element_resolutionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_element_resolution; }
	}

	public final Array_element_resolutionContext array_element_resolution() throws RecognitionException {
		Array_element_resolutionContext _localctx = new Array_element_resolutionContext(_ctx, getState());
		enterRule(_localctx, 154, RULE_array_element_resolution);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1159);
			resolution_indication();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Record_resolutionContext extends ParserRuleContext {
		public List<Record_element_resolutionContext> record_element_resolution() {
			return getRuleContexts(Record_element_resolutionContext.class);
		}
		public Record_element_resolutionContext record_element_resolution(int i) {
			return getRuleContext(Record_element_resolutionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(vhdlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(vhdlParser.COMMA, i);
		}
		public Record_resolutionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_record_resolution; }
	}

	public final Record_resolutionContext record_resolution() throws RecognitionException {
		Record_resolutionContext _localctx = new Record_resolutionContext(_ctx, getState());
		enterRule(_localctx, 156, RULE_record_resolution);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1161);
			record_element_resolution();
			setState(1166);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(1162);
				match(COMMA);
				setState(1163);
				record_element_resolution();
				}
				}
				setState(1168);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Record_element_resolutionContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public Resolution_indicationContext resolution_indication() {
			return getRuleContext(Resolution_indicationContext.class,0);
		}
		public Record_element_resolutionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_record_element_resolution; }
	}

	public final Record_element_resolutionContext record_element_resolution() throws RecognitionException {
		Record_element_resolutionContext _localctx = new Record_element_resolutionContext(_ctx, getState());
		enterRule(_localctx, 158, RULE_record_element_resolution);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1169);
			identifier();
			setState(1170);
			resolution_indication();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Type_markContext extends ParserRuleContext {
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public Type_markContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type_mark; }
	}

	public final Type_markContext type_mark() throws RecognitionException {
		Type_markContext _localctx = new Type_markContext(_ctx, getState());
		enterRule(_localctx, 160, RULE_type_mark);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1172);
			name(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ConstraintContext extends ParserRuleContext {
		public Range_constraintContext range_constraint() {
			return getRuleContext(Range_constraintContext.class,0);
		}
		public Element_constraintContext element_constraint() {
			return getRuleContext(Element_constraintContext.class,0);
		}
		public ConstraintContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constraint; }
	}

	public final ConstraintContext constraint() throws RecognitionException {
		ConstraintContext _localctx = new ConstraintContext(_ctx, getState());
		enterRule(_localctx, 162, RULE_constraint);
		try {
			setState(1176);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KW_RANGE:
				enterOuterAlt(_localctx, 1);
				{
				setState(1174);
				range_constraint();
				}
				break;
			case LPAREN:
				enterOuterAlt(_localctx, 2);
				{
				setState(1175);
				element_constraint();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Element_constraintContext extends ParserRuleContext {
		public Array_constraintContext array_constraint() {
			return getRuleContext(Array_constraintContext.class,0);
		}
		public Record_constraintContext record_constraint() {
			return getRuleContext(Record_constraintContext.class,0);
		}
		public Element_constraintContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_element_constraint; }
	}

	public final Element_constraintContext element_constraint() throws RecognitionException {
		Element_constraintContext _localctx = new Element_constraintContext(_ctx, getState());
		enterRule(_localctx, 164, RULE_element_constraint);
		try {
			setState(1180);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,96,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(1178);
				array_constraint();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(1179);
				record_constraint();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Object_declarationContext extends ParserRuleContext {
		public Constant_declarationContext constant_declaration() {
			return getRuleContext(Constant_declarationContext.class,0);
		}
		public Signal_declarationContext signal_declaration() {
			return getRuleContext(Signal_declarationContext.class,0);
		}
		public Variable_declarationContext variable_declaration() {
			return getRuleContext(Variable_declarationContext.class,0);
		}
		public File_declarationContext file_declaration() {
			return getRuleContext(File_declarationContext.class,0);
		}
		public Object_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_object_declaration; }
	}

	public final Object_declarationContext object_declaration() throws RecognitionException {
		Object_declarationContext _localctx = new Object_declarationContext(_ctx, getState());
		enterRule(_localctx, 166, RULE_object_declaration);
		try {
			setState(1186);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KW_CONSTANT:
				enterOuterAlt(_localctx, 1);
				{
				setState(1182);
				constant_declaration();
				}
				break;
			case KW_SIGNAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(1183);
				signal_declaration();
				}
				break;
			case KW_SHARED:
			case KW_VARIABLE:
				enterOuterAlt(_localctx, 3);
				{
				setState(1184);
				variable_declaration();
				}
				break;
			case KW_FILE:
				enterOuterAlt(_localctx, 4);
				{
				setState(1185);
				file_declaration();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Constant_declarationContext extends ParserRuleContext {
		public TerminalNode KW_CONSTANT() { return getToken(vhdlParser.KW_CONSTANT, 0); }
		public Identifier_listContext identifier_list() {
			return getRuleContext(Identifier_listContext.class,0);
		}
		public TerminalNode COLON() { return getToken(vhdlParser.COLON, 0); }
		public Subtype_indicationContext subtype_indication() {
			return getRuleContext(Subtype_indicationContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public TerminalNode VARASGN() { return getToken(vhdlParser.VARASGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Constant_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constant_declaration; }
	}

	public final Constant_declarationContext constant_declaration() throws RecognitionException {
		Constant_declarationContext _localctx = new Constant_declarationContext(_ctx, getState());
		enterRule(_localctx, 168, RULE_constant_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1188);
			match(KW_CONSTANT);
			setState(1189);
			identifier_list();
			setState(1190);
			match(COLON);
			setState(1191);
			subtype_indication();
			setState(1194);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==VARASGN) {
				{
				setState(1192);
				match(VARASGN);
				setState(1193);
				expression(0);
				}
			}

			setState(1196);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Signal_declarationContext extends ParserRuleContext {
		public TerminalNode KW_SIGNAL() { return getToken(vhdlParser.KW_SIGNAL, 0); }
		public Identifier_listContext identifier_list() {
			return getRuleContext(Identifier_listContext.class,0);
		}
		public TerminalNode COLON() { return getToken(vhdlParser.COLON, 0); }
		public Subtype_indicationContext subtype_indication() {
			return getRuleContext(Subtype_indicationContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public Signal_kindContext signal_kind() {
			return getRuleContext(Signal_kindContext.class,0);
		}
		public TerminalNode VARASGN() { return getToken(vhdlParser.VARASGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Signal_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_signal_declaration; }
	}

	public final Signal_declarationContext signal_declaration() throws RecognitionException {
		Signal_declarationContext _localctx = new Signal_declarationContext(_ctx, getState());
		enterRule(_localctx, 170, RULE_signal_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1198);
			match(KW_SIGNAL);
			setState(1199);
			identifier_list();
			setState(1200);
			match(COLON);
			setState(1201);
			subtype_indication();
			setState(1203);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_REGISTER || _la==KW_BUS) {
				{
				setState(1202);
				signal_kind();
				}
			}

			setState(1207);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==VARASGN) {
				{
				setState(1205);
				match(VARASGN);
				setState(1206);
				expression(0);
				}
			}

			setState(1209);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Signal_kindContext extends ParserRuleContext {
		public TerminalNode KW_REGISTER() { return getToken(vhdlParser.KW_REGISTER, 0); }
		public TerminalNode KW_BUS() { return getToken(vhdlParser.KW_BUS, 0); }
		public Signal_kindContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_signal_kind; }
	}

	public final Signal_kindContext signal_kind() throws RecognitionException {
		Signal_kindContext _localctx = new Signal_kindContext(_ctx, getState());
		enterRule(_localctx, 172, RULE_signal_kind);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1211);
			_la = _input.LA(1);
			if ( !(_la==KW_REGISTER || _la==KW_BUS) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Variable_declarationContext extends ParserRuleContext {
		public TerminalNode KW_VARIABLE() { return getToken(vhdlParser.KW_VARIABLE, 0); }
		public Identifier_listContext identifier_list() {
			return getRuleContext(Identifier_listContext.class,0);
		}
		public TerminalNode COLON() { return getToken(vhdlParser.COLON, 0); }
		public Subtype_indicationContext subtype_indication() {
			return getRuleContext(Subtype_indicationContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public TerminalNode KW_SHARED() { return getToken(vhdlParser.KW_SHARED, 0); }
		public TerminalNode VARASGN() { return getToken(vhdlParser.VARASGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Variable_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable_declaration; }
	}

	public final Variable_declarationContext variable_declaration() throws RecognitionException {
		Variable_declarationContext _localctx = new Variable_declarationContext(_ctx, getState());
		enterRule(_localctx, 174, RULE_variable_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1214);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_SHARED) {
				{
				setState(1213);
				match(KW_SHARED);
				}
			}

			setState(1216);
			match(KW_VARIABLE);
			setState(1217);
			identifier_list();
			setState(1218);
			match(COLON);
			setState(1219);
			subtype_indication();
			setState(1222);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==VARASGN) {
				{
				setState(1220);
				match(VARASGN);
				setState(1221);
				expression(0);
				}
			}

			setState(1224);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class File_declarationContext extends ParserRuleContext {
		public TerminalNode KW_FILE() { return getToken(vhdlParser.KW_FILE, 0); }
		public Identifier_listContext identifier_list() {
			return getRuleContext(Identifier_listContext.class,0);
		}
		public TerminalNode COLON() { return getToken(vhdlParser.COLON, 0); }
		public Subtype_indicationContext subtype_indication() {
			return getRuleContext(Subtype_indicationContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public File_open_informationContext file_open_information() {
			return getRuleContext(File_open_informationContext.class,0);
		}
		public File_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_file_declaration; }
	}

	public final File_declarationContext file_declaration() throws RecognitionException {
		File_declarationContext _localctx = new File_declarationContext(_ctx, getState());
		enterRule(_localctx, 176, RULE_file_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1226);
			match(KW_FILE);
			setState(1227);
			identifier_list();
			setState(1228);
			match(COLON);
			setState(1229);
			subtype_indication();
			setState(1231);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_IS || _la==KW_OPEN) {
				{
				setState(1230);
				file_open_information();
				}
			}

			setState(1233);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class File_open_informationContext extends ParserRuleContext {
		public TerminalNode KW_IS() { return getToken(vhdlParser.KW_IS, 0); }
		public File_logical_nameContext file_logical_name() {
			return getRuleContext(File_logical_nameContext.class,0);
		}
		public TerminalNode KW_OPEN() { return getToken(vhdlParser.KW_OPEN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode KW_IN() { return getToken(vhdlParser.KW_IN, 0); }
		public TerminalNode KW_OUT() { return getToken(vhdlParser.KW_OUT, 0); }
		public File_open_informationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_file_open_information; }
	}

	public final File_open_informationContext file_open_information() throws RecognitionException {
		File_open_informationContext _localctx = new File_open_informationContext(_ctx, getState());
		enterRule(_localctx, 178, RULE_file_open_information);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1237);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_OPEN) {
				{
				setState(1235);
				match(KW_OPEN);
				setState(1236);
				expression(0);
				}
			}

			setState(1239);
			match(KW_IS);
			setState(1241);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_IN || _la==KW_OUT) {
				{
				setState(1240);
				_la = _input.LA(1);
				if ( !(_la==KW_IN || _la==KW_OUT) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
			}

			setState(1243);
			file_logical_name();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class File_logical_nameContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public File_logical_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_file_logical_name; }
	}

	public final File_logical_nameContext file_logical_name() throws RecognitionException {
		File_logical_nameContext _localctx = new File_logical_nameContext(_ctx, getState());
		enterRule(_localctx, 180, RULE_file_logical_name);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1245);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Interface_declarationContext extends ParserRuleContext {
		public Interface_object_declarationContext interface_object_declaration() {
			return getRuleContext(Interface_object_declarationContext.class,0);
		}
		public Interface_type_declarationContext interface_type_declaration() {
			return getRuleContext(Interface_type_declarationContext.class,0);
		}
		public Interface_subprogram_declarationContext interface_subprogram_declaration() {
			return getRuleContext(Interface_subprogram_declarationContext.class,0);
		}
		public Interface_package_declarationContext interface_package_declaration() {
			return getRuleContext(Interface_package_declarationContext.class,0);
		}
		public Interface_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_interface_declaration; }
	}

	public final Interface_declarationContext interface_declaration() throws RecognitionException {
		Interface_declarationContext _localctx = new Interface_declarationContext(_ctx, getState());
		enterRule(_localctx, 182, RULE_interface_declaration);
		try {
			setState(1251);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KW_FILE:
			case KW_SIGNAL:
			case KW_VARIABLE:
			case KW_CONSTANT:
			case BASIC_IDENTIFIER:
			case EXTENDED_IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(1247);
				interface_object_declaration();
				}
				break;
			case KW_TYPE:
				enterOuterAlt(_localctx, 2);
				{
				setState(1248);
				interface_type_declaration();
				}
				break;
			case KW_PURE:
			case KW_PROCEDURE:
			case KW_FUNCTION:
			case KW_IMPURE:
				enterOuterAlt(_localctx, 3);
				{
				setState(1249);
				interface_subprogram_declaration();
				}
				break;
			case KW_PACKAGE:
				enterOuterAlt(_localctx, 4);
				{
				setState(1250);
				interface_package_declaration();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Interface_object_declarationContext extends ParserRuleContext {
		public Interface_constant_declarationContext interface_constant_declaration() {
			return getRuleContext(Interface_constant_declarationContext.class,0);
		}
		public Interface_signal_declarationContext interface_signal_declaration() {
			return getRuleContext(Interface_signal_declarationContext.class,0);
		}
		public Interface_variable_declarationContext interface_variable_declaration() {
			return getRuleContext(Interface_variable_declarationContext.class,0);
		}
		public Interface_file_declarationContext interface_file_declaration() {
			return getRuleContext(Interface_file_declarationContext.class,0);
		}
		public Interface_object_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_interface_object_declaration; }
	}

	public final Interface_object_declarationContext interface_object_declaration() throws RecognitionException {
		Interface_object_declarationContext _localctx = new Interface_object_declarationContext(_ctx, getState());
		enterRule(_localctx, 184, RULE_interface_object_declaration);
		try {
			setState(1257);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KW_CONSTANT:
				enterOuterAlt(_localctx, 1);
				{
				setState(1253);
				interface_constant_declaration();
				}
				break;
			case KW_SIGNAL:
			case BASIC_IDENTIFIER:
			case EXTENDED_IDENTIFIER:
				enterOuterAlt(_localctx, 2);
				{
				setState(1254);
				interface_signal_declaration();
				}
				break;
			case KW_VARIABLE:
				enterOuterAlt(_localctx, 3);
				{
				setState(1255);
				interface_variable_declaration();
				}
				break;
			case KW_FILE:
				enterOuterAlt(_localctx, 4);
				{
				setState(1256);
				interface_file_declaration();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Interface_constant_declarationContext extends ParserRuleContext {
		public TerminalNode KW_CONSTANT() { return getToken(vhdlParser.KW_CONSTANT, 0); }
		public Identifier_listContext identifier_list() {
			return getRuleContext(Identifier_listContext.class,0);
		}
		public TerminalNode COLON() { return getToken(vhdlParser.COLON, 0); }
		public Subtype_indicationContext subtype_indication() {
			return getRuleContext(Subtype_indicationContext.class,0);
		}
		public TerminalNode KW_IN() { return getToken(vhdlParser.KW_IN, 0); }
		public TerminalNode VARASGN() { return getToken(vhdlParser.VARASGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Interface_constant_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_interface_constant_declaration; }
	}

	public final Interface_constant_declarationContext interface_constant_declaration() throws RecognitionException {
		Interface_constant_declarationContext _localctx = new Interface_constant_declarationContext(_ctx, getState());
		enterRule(_localctx, 186, RULE_interface_constant_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1259);
			match(KW_CONSTANT);
			setState(1260);
			identifier_list();
			setState(1261);
			match(COLON);
			setState(1263);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_IN) {
				{
				setState(1262);
				match(KW_IN);
				}
			}

			setState(1265);
			subtype_indication();
			setState(1268);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==VARASGN) {
				{
				setState(1266);
				match(VARASGN);
				setState(1267);
				expression(0);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Interface_signal_declarationContext extends ParserRuleContext {
		public Identifier_listContext identifier_list() {
			return getRuleContext(Identifier_listContext.class,0);
		}
		public TerminalNode COLON() { return getToken(vhdlParser.COLON, 0); }
		public Subtype_indicationContext subtype_indication() {
			return getRuleContext(Subtype_indicationContext.class,0);
		}
		public TerminalNode KW_SIGNAL() { return getToken(vhdlParser.KW_SIGNAL, 0); }
		public Signal_modeContext signal_mode() {
			return getRuleContext(Signal_modeContext.class,0);
		}
		public TerminalNode KW_BUS() { return getToken(vhdlParser.KW_BUS, 0); }
		public TerminalNode VARASGN() { return getToken(vhdlParser.VARASGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Interface_signal_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_interface_signal_declaration; }
	}

	public final Interface_signal_declarationContext interface_signal_declaration() throws RecognitionException {
		Interface_signal_declarationContext _localctx = new Interface_signal_declarationContext(_ctx, getState());
		enterRule(_localctx, 188, RULE_interface_signal_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1271);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_SIGNAL) {
				{
				setState(1270);
				match(KW_SIGNAL);
				}
			}

			setState(1273);
			identifier_list();
			setState(1274);
			match(COLON);
			setState(1276);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_LINKAGE || _la==KW_BUFFER || ((((_la - 68)) & ~0x3f) == 0 && ((1L << (_la - 68)) & ((1L << (KW_IN - 68)) | (1L << (KW_INOUT - 68)) | (1L << (KW_OUT - 68)))) != 0)) {
				{
				setState(1275);
				signal_mode();
				}
			}

			setState(1278);
			subtype_indication();
			setState(1280);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_BUS) {
				{
				setState(1279);
				match(KW_BUS);
				}
			}

			setState(1284);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==VARASGN) {
				{
				setState(1282);
				match(VARASGN);
				setState(1283);
				expression(0);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Interface_variable_declarationContext extends ParserRuleContext {
		public TerminalNode KW_VARIABLE() { return getToken(vhdlParser.KW_VARIABLE, 0); }
		public Identifier_listContext identifier_list() {
			return getRuleContext(Identifier_listContext.class,0);
		}
		public TerminalNode COLON() { return getToken(vhdlParser.COLON, 0); }
		public Subtype_indicationContext subtype_indication() {
			return getRuleContext(Subtype_indicationContext.class,0);
		}
		public Signal_modeContext signal_mode() {
			return getRuleContext(Signal_modeContext.class,0);
		}
		public TerminalNode VARASGN() { return getToken(vhdlParser.VARASGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Interface_variable_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_interface_variable_declaration; }
	}

	public final Interface_variable_declarationContext interface_variable_declaration() throws RecognitionException {
		Interface_variable_declarationContext _localctx = new Interface_variable_declarationContext(_ctx, getState());
		enterRule(_localctx, 190, RULE_interface_variable_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1286);
			match(KW_VARIABLE);
			setState(1287);
			identifier_list();
			setState(1288);
			match(COLON);
			setState(1290);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_LINKAGE || _la==KW_BUFFER || ((((_la - 68)) & ~0x3f) == 0 && ((1L << (_la - 68)) & ((1L << (KW_IN - 68)) | (1L << (KW_INOUT - 68)) | (1L << (KW_OUT - 68)))) != 0)) {
				{
				setState(1289);
				signal_mode();
				}
			}

			setState(1292);
			subtype_indication();
			setState(1295);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==VARASGN) {
				{
				setState(1293);
				match(VARASGN);
				setState(1294);
				expression(0);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Interface_file_declarationContext extends ParserRuleContext {
		public TerminalNode KW_FILE() { return getToken(vhdlParser.KW_FILE, 0); }
		public Identifier_listContext identifier_list() {
			return getRuleContext(Identifier_listContext.class,0);
		}
		public TerminalNode COLON() { return getToken(vhdlParser.COLON, 0); }
		public Subtype_indicationContext subtype_indication() {
			return getRuleContext(Subtype_indicationContext.class,0);
		}
		public Interface_file_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_interface_file_declaration; }
	}

	public final Interface_file_declarationContext interface_file_declaration() throws RecognitionException {
		Interface_file_declarationContext _localctx = new Interface_file_declarationContext(_ctx, getState());
		enterRule(_localctx, 192, RULE_interface_file_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1297);
			match(KW_FILE);
			setState(1298);
			identifier_list();
			setState(1299);
			match(COLON);
			setState(1300);
			subtype_indication();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Signal_modeContext extends ParserRuleContext {
		public TerminalNode KW_IN() { return getToken(vhdlParser.KW_IN, 0); }
		public TerminalNode KW_OUT() { return getToken(vhdlParser.KW_OUT, 0); }
		public TerminalNode KW_INOUT() { return getToken(vhdlParser.KW_INOUT, 0); }
		public TerminalNode KW_BUFFER() { return getToken(vhdlParser.KW_BUFFER, 0); }
		public TerminalNode KW_LINKAGE() { return getToken(vhdlParser.KW_LINKAGE, 0); }
		public Signal_modeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_signal_mode; }
	}

	public final Signal_modeContext signal_mode() throws RecognitionException {
		Signal_modeContext _localctx = new Signal_modeContext(_ctx, getState());
		enterRule(_localctx, 194, RULE_signal_mode);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1302);
			_la = _input.LA(1);
			if ( !(_la==KW_LINKAGE || _la==KW_BUFFER || ((((_la - 68)) & ~0x3f) == 0 && ((1L << (_la - 68)) & ((1L << (KW_IN - 68)) | (1L << (KW_INOUT - 68)) | (1L << (KW_OUT - 68)))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Interface_type_declarationContext extends ParserRuleContext {
		public Interface_incomplete_type_declarationContext interface_incomplete_type_declaration() {
			return getRuleContext(Interface_incomplete_type_declarationContext.class,0);
		}
		public Interface_type_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_interface_type_declaration; }
	}

	public final Interface_type_declarationContext interface_type_declaration() throws RecognitionException {
		Interface_type_declarationContext _localctx = new Interface_type_declarationContext(_ctx, getState());
		enterRule(_localctx, 196, RULE_interface_type_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1304);
			interface_incomplete_type_declaration();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Interface_incomplete_type_declarationContext extends ParserRuleContext {
		public TerminalNode KW_TYPE() { return getToken(vhdlParser.KW_TYPE, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public Interface_incomplete_type_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_interface_incomplete_type_declaration; }
	}

	public final Interface_incomplete_type_declarationContext interface_incomplete_type_declaration() throws RecognitionException {
		Interface_incomplete_type_declarationContext _localctx = new Interface_incomplete_type_declarationContext(_ctx, getState());
		enterRule(_localctx, 198, RULE_interface_incomplete_type_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1306);
			match(KW_TYPE);
			setState(1307);
			identifier();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Interface_subprogram_declarationContext extends ParserRuleContext {
		public Interface_subprogram_specificationContext interface_subprogram_specification() {
			return getRuleContext(Interface_subprogram_specificationContext.class,0);
		}
		public TerminalNode KW_IS() { return getToken(vhdlParser.KW_IS, 0); }
		public Interface_subprogram_defaultContext interface_subprogram_default() {
			return getRuleContext(Interface_subprogram_defaultContext.class,0);
		}
		public Interface_subprogram_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_interface_subprogram_declaration; }
	}

	public final Interface_subprogram_declarationContext interface_subprogram_declaration() throws RecognitionException {
		Interface_subprogram_declarationContext _localctx = new Interface_subprogram_declarationContext(_ctx, getState());
		enterRule(_localctx, 200, RULE_interface_subprogram_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1309);
			interface_subprogram_specification();
			setState(1312);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_IS) {
				{
				setState(1310);
				match(KW_IS);
				setState(1311);
				interface_subprogram_default();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Interface_subprogram_specificationContext extends ParserRuleContext {
		public Interface_procedure_specificationContext interface_procedure_specification() {
			return getRuleContext(Interface_procedure_specificationContext.class,0);
		}
		public Interface_function_specificationContext interface_function_specification() {
			return getRuleContext(Interface_function_specificationContext.class,0);
		}
		public Interface_subprogram_specificationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_interface_subprogram_specification; }
	}

	public final Interface_subprogram_specificationContext interface_subprogram_specification() throws RecognitionException {
		Interface_subprogram_specificationContext _localctx = new Interface_subprogram_specificationContext(_ctx, getState());
		enterRule(_localctx, 202, RULE_interface_subprogram_specification);
		try {
			setState(1316);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KW_PROCEDURE:
				enterOuterAlt(_localctx, 1);
				{
				setState(1314);
				interface_procedure_specification();
				}
				break;
			case KW_PURE:
			case KW_FUNCTION:
			case KW_IMPURE:
				enterOuterAlt(_localctx, 2);
				{
				setState(1315);
				interface_function_specification();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Interface_procedure_specificationContext extends ParserRuleContext {
		public TerminalNode KW_PROCEDURE() { return getToken(vhdlParser.KW_PROCEDURE, 0); }
		public DesignatorContext designator() {
			return getRuleContext(DesignatorContext.class,0);
		}
		public TerminalNode LPAREN() { return getToken(vhdlParser.LPAREN, 0); }
		public Formal_parameter_listContext formal_parameter_list() {
			return getRuleContext(Formal_parameter_listContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(vhdlParser.RPAREN, 0); }
		public TerminalNode KW_PARAMETER() { return getToken(vhdlParser.KW_PARAMETER, 0); }
		public Interface_procedure_specificationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_interface_procedure_specification; }
	}

	public final Interface_procedure_specificationContext interface_procedure_specification() throws RecognitionException {
		Interface_procedure_specificationContext _localctx = new Interface_procedure_specificationContext(_ctx, getState());
		enterRule(_localctx, 204, RULE_interface_procedure_specification);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1318);
			match(KW_PROCEDURE);
			setState(1319);
			designator();
			setState(1327);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_PARAMETER || _la==LPAREN) {
				{
				setState(1321);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==KW_PARAMETER) {
					{
					setState(1320);
					match(KW_PARAMETER);
					}
				}

				setState(1323);
				match(LPAREN);
				setState(1324);
				formal_parameter_list();
				setState(1325);
				match(RPAREN);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Interface_function_specificationContext extends ParserRuleContext {
		public TerminalNode KW_FUNCTION() { return getToken(vhdlParser.KW_FUNCTION, 0); }
		public DesignatorContext designator() {
			return getRuleContext(DesignatorContext.class,0);
		}
		public TerminalNode KW_RETURN() { return getToken(vhdlParser.KW_RETURN, 0); }
		public Type_markContext type_mark() {
			return getRuleContext(Type_markContext.class,0);
		}
		public TerminalNode LPAREN() { return getToken(vhdlParser.LPAREN, 0); }
		public Formal_parameter_listContext formal_parameter_list() {
			return getRuleContext(Formal_parameter_listContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(vhdlParser.RPAREN, 0); }
		public TerminalNode KW_PURE() { return getToken(vhdlParser.KW_PURE, 0); }
		public TerminalNode KW_IMPURE() { return getToken(vhdlParser.KW_IMPURE, 0); }
		public TerminalNode KW_PARAMETER() { return getToken(vhdlParser.KW_PARAMETER, 0); }
		public Interface_function_specificationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_interface_function_specification; }
	}

	public final Interface_function_specificationContext interface_function_specification() throws RecognitionException {
		Interface_function_specificationContext _localctx = new Interface_function_specificationContext(_ctx, getState());
		enterRule(_localctx, 206, RULE_interface_function_specification);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1330);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_PURE || _la==KW_IMPURE) {
				{
				setState(1329);
				_la = _input.LA(1);
				if ( !(_la==KW_PURE || _la==KW_IMPURE) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
			}

			setState(1332);
			match(KW_FUNCTION);
			setState(1333);
			designator();
			setState(1341);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_PARAMETER || _la==LPAREN) {
				{
				setState(1335);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==KW_PARAMETER) {
					{
					setState(1334);
					match(KW_PARAMETER);
					}
				}

				setState(1337);
				match(LPAREN);
				setState(1338);
				formal_parameter_list();
				setState(1339);
				match(RPAREN);
				}
			}

			setState(1343);
			match(KW_RETURN);
			setState(1344);
			type_mark();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Interface_subprogram_defaultContext extends ParserRuleContext {
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public TerminalNode BOX() { return getToken(vhdlParser.BOX, 0); }
		public Interface_subprogram_defaultContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_interface_subprogram_default; }
	}

	public final Interface_subprogram_defaultContext interface_subprogram_default() throws RecognitionException {
		Interface_subprogram_defaultContext _localctx = new Interface_subprogram_defaultContext(_ctx, getState());
		enterRule(_localctx, 208, RULE_interface_subprogram_default);
		try {
			setState(1348);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BASIC_IDENTIFIER:
			case EXTENDED_IDENTIFIER:
			case CHARACTER_LITERAL:
			case STRING_LITERAL:
			case SHIFT_LEFT:
				enterOuterAlt(_localctx, 1);
				{
				setState(1346);
				name(0);
				}
				break;
			case BOX:
				enterOuterAlt(_localctx, 2);
				{
				setState(1347);
				match(BOX);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Interface_package_declarationContext extends ParserRuleContext {
		public TerminalNode KW_PACKAGE() { return getToken(vhdlParser.KW_PACKAGE, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode KW_IS() { return getToken(vhdlParser.KW_IS, 0); }
		public TerminalNode KW_NEW() { return getToken(vhdlParser.KW_NEW, 0); }
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public Interface_package_generic_map_aspectContext interface_package_generic_map_aspect() {
			return getRuleContext(Interface_package_generic_map_aspectContext.class,0);
		}
		public Interface_package_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_interface_package_declaration; }
	}

	public final Interface_package_declarationContext interface_package_declaration() throws RecognitionException {
		Interface_package_declarationContext _localctx = new Interface_package_declarationContext(_ctx, getState());
		enterRule(_localctx, 210, RULE_interface_package_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1350);
			match(KW_PACKAGE);
			setState(1351);
			identifier();
			setState(1352);
			match(KW_IS);
			setState(1353);
			match(KW_NEW);
			setState(1354);
			name(0);
			setState(1355);
			interface_package_generic_map_aspect();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Interface_package_generic_map_aspectContext extends ParserRuleContext {
		public Generic_map_aspectContext generic_map_aspect() {
			return getRuleContext(Generic_map_aspectContext.class,0);
		}
		public TerminalNode KW_GENERIC() { return getToken(vhdlParser.KW_GENERIC, 0); }
		public TerminalNode KW_MAP() { return getToken(vhdlParser.KW_MAP, 0); }
		public TerminalNode LPAREN() { return getToken(vhdlParser.LPAREN, 0); }
		public TerminalNode BOX() { return getToken(vhdlParser.BOX, 0); }
		public TerminalNode RPAREN() { return getToken(vhdlParser.RPAREN, 0); }
		public TerminalNode KW_DEFAULT() { return getToken(vhdlParser.KW_DEFAULT, 0); }
		public Interface_package_generic_map_aspectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_interface_package_generic_map_aspect; }
	}

	public final Interface_package_generic_map_aspectContext interface_package_generic_map_aspect() throws RecognitionException {
		Interface_package_generic_map_aspectContext _localctx = new Interface_package_generic_map_aspectContext(_ctx, getState());
		enterRule(_localctx, 212, RULE_interface_package_generic_map_aspect);
		try {
			setState(1368);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,124,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(1357);
				generic_map_aspect();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(1358);
				match(KW_GENERIC);
				setState(1359);
				match(KW_MAP);
				setState(1360);
				match(LPAREN);
				setState(1361);
				match(BOX);
				setState(1362);
				match(RPAREN);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(1363);
				match(KW_GENERIC);
				setState(1364);
				match(KW_MAP);
				setState(1365);
				match(LPAREN);
				setState(1366);
				match(KW_DEFAULT);
				setState(1367);
				match(RPAREN);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Interface_listContext extends ParserRuleContext {
		public List<Interface_elementContext> interface_element() {
			return getRuleContexts(Interface_elementContext.class);
		}
		public Interface_elementContext interface_element(int i) {
			return getRuleContext(Interface_elementContext.class,i);
		}
		public List<TerminalNode> SEMI() { return getTokens(vhdlParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(vhdlParser.SEMI, i);
		}
		public Interface_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_interface_list; }
	}

	public final Interface_listContext interface_list() throws RecognitionException {
		Interface_listContext _localctx = new Interface_listContext(_ctx, getState());
		enterRule(_localctx, 214, RULE_interface_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1370);
			interface_element();
			setState(1375);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==SEMI) {
				{
				{
				setState(1371);
				match(SEMI);
				setState(1372);
				interface_element();
				}
				}
				setState(1377);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Interface_elementContext extends ParserRuleContext {
		public Interface_declarationContext interface_declaration() {
			return getRuleContext(Interface_declarationContext.class,0);
		}
		public Interface_elementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_interface_element; }
	}

	public final Interface_elementContext interface_element() throws RecognitionException {
		Interface_elementContext _localctx = new Interface_elementContext(_ctx, getState());
		enterRule(_localctx, 216, RULE_interface_element);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1378);
			interface_declaration();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Generic_clauseContext extends ParserRuleContext {
		public TerminalNode KW_GENERIC() { return getToken(vhdlParser.KW_GENERIC, 0); }
		public TerminalNode LPAREN() { return getToken(vhdlParser.LPAREN, 0); }
		public Generic_listContext generic_list() {
			return getRuleContext(Generic_listContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(vhdlParser.RPAREN, 0); }
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public Generic_clauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_generic_clause; }
	}

	public final Generic_clauseContext generic_clause() throws RecognitionException {
		Generic_clauseContext _localctx = new Generic_clauseContext(_ctx, getState());
		enterRule(_localctx, 218, RULE_generic_clause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1380);
			match(KW_GENERIC);
			setState(1381);
			match(LPAREN);
			setState(1382);
			generic_list();
			setState(1383);
			match(RPAREN);
			setState(1384);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Generic_listContext extends ParserRuleContext {
		public Interface_listContext interface_list() {
			return getRuleContext(Interface_listContext.class,0);
		}
		public Generic_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_generic_list; }
	}

	public final Generic_listContext generic_list() throws RecognitionException {
		Generic_listContext _localctx = new Generic_listContext(_ctx, getState());
		enterRule(_localctx, 220, RULE_generic_list);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1386);
			interface_list();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Port_clauseContext extends ParserRuleContext {
		public TerminalNode KW_PORT() { return getToken(vhdlParser.KW_PORT, 0); }
		public TerminalNode LPAREN() { return getToken(vhdlParser.LPAREN, 0); }
		public Port_listContext port_list() {
			return getRuleContext(Port_listContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(vhdlParser.RPAREN, 0); }
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public Port_clauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_port_clause; }
	}

	public final Port_clauseContext port_clause() throws RecognitionException {
		Port_clauseContext _localctx = new Port_clauseContext(_ctx, getState());
		enterRule(_localctx, 222, RULE_port_clause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1388);
			match(KW_PORT);
			setState(1389);
			match(LPAREN);
			setState(1390);
			port_list();
			setState(1391);
			match(RPAREN);
			setState(1392);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Port_listContext extends ParserRuleContext {
		public Interface_listContext interface_list() {
			return getRuleContext(Interface_listContext.class,0);
		}
		public Port_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_port_list; }
	}

	public final Port_listContext port_list() throws RecognitionException {
		Port_listContext _localctx = new Port_listContext(_ctx, getState());
		enterRule(_localctx, 224, RULE_port_list);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1394);
			interface_list();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Association_listContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(vhdlParser.LPAREN, 0); }
		public List<Association_elementContext> association_element() {
			return getRuleContexts(Association_elementContext.class);
		}
		public Association_elementContext association_element(int i) {
			return getRuleContext(Association_elementContext.class,i);
		}
		public TerminalNode RPAREN() { return getToken(vhdlParser.RPAREN, 0); }
		public List<TerminalNode> COMMA() { return getTokens(vhdlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(vhdlParser.COMMA, i);
		}
		public Association_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_association_list; }
	}

	public final Association_listContext association_list() throws RecognitionException {
		Association_listContext _localctx = new Association_listContext(_ctx, getState());
		enterRule(_localctx, 226, RULE_association_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1396);
			match(LPAREN);
			setState(1397);
			association_element();
			setState(1402);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(1398);
				match(COMMA);
				setState(1399);
				association_element();
				}
				}
				setState(1404);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(1405);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Association_elementContext extends ParserRuleContext {
		public Actual_partContext actual_part() {
			return getRuleContext(Actual_partContext.class,0);
		}
		public Formal_partContext formal_part() {
			return getRuleContext(Formal_partContext.class,0);
		}
		public TerminalNode ARROW() { return getToken(vhdlParser.ARROW, 0); }
		public Association_elementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_association_element; }
	}

	public final Association_elementContext association_element() throws RecognitionException {
		Association_elementContext _localctx = new Association_elementContext(_ctx, getState());
		enterRule(_localctx, 228, RULE_association_element);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1410);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,127,_ctx) ) {
			case 1:
				{
				setState(1407);
				formal_part();
				setState(1408);
				match(ARROW);
				}
				break;
			}
			setState(1412);
			actual_part();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Formal_partContext extends ParserRuleContext {
		public List<NameContext> name() {
			return getRuleContexts(NameContext.class);
		}
		public NameContext name(int i) {
			return getRuleContext(NameContext.class,i);
		}
		public TerminalNode LPAREN() { return getToken(vhdlParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(vhdlParser.RPAREN, 0); }
		public Formal_partContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_formal_part; }
	}

	public final Formal_partContext formal_part() throws RecognitionException {
		Formal_partContext _localctx = new Formal_partContext(_ctx, getState());
		enterRule(_localctx, 230, RULE_formal_part);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1414);
			name(0);
			setState(1419);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LPAREN) {
				{
				setState(1415);
				match(LPAREN);
				setState(1416);
				name(0);
				setState(1417);
				match(RPAREN);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Actual_partContext extends ParserRuleContext {
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public TerminalNode LPAREN() { return getToken(vhdlParser.LPAREN, 0); }
		public Actual_designatorContext actual_designator() {
			return getRuleContext(Actual_designatorContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(vhdlParser.RPAREN, 0); }
		public Actual_partContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_actual_part; }
	}

	public final Actual_partContext actual_part() throws RecognitionException {
		Actual_partContext _localctx = new Actual_partContext(_ctx, getState());
		enterRule(_localctx, 232, RULE_actual_part);
		try {
			setState(1427);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,129,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(1421);
				name(0);
				setState(1422);
				match(LPAREN);
				setState(1423);
				actual_designator();
				setState(1424);
				match(RPAREN);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(1426);
				actual_designator();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Actual_designatorContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode KW_INERTIAL() { return getToken(vhdlParser.KW_INERTIAL, 0); }
		public Subtype_indicationContext subtype_indication() {
			return getRuleContext(Subtype_indicationContext.class,0);
		}
		public TerminalNode KW_OPEN() { return getToken(vhdlParser.KW_OPEN, 0); }
		public Actual_designatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_actual_designator; }
	}

	public final Actual_designatorContext actual_designator() throws RecognitionException {
		Actual_designatorContext _localctx = new Actual_designatorContext(_ctx, getState());
		enterRule(_localctx, 234, RULE_actual_designator);
		int _la;
		try {
			setState(1435);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,131,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(1430);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==KW_INERTIAL) {
					{
					setState(1429);
					match(KW_INERTIAL);
					}
				}

				setState(1432);
				expression(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(1433);
				subtype_indication();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(1434);
				match(KW_OPEN);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Generic_map_aspectContext extends ParserRuleContext {
		public TerminalNode KW_GENERIC() { return getToken(vhdlParser.KW_GENERIC, 0); }
		public TerminalNode KW_MAP() { return getToken(vhdlParser.KW_MAP, 0); }
		public Association_listContext association_list() {
			return getRuleContext(Association_listContext.class,0);
		}
		public Generic_map_aspectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_generic_map_aspect; }
	}

	public final Generic_map_aspectContext generic_map_aspect() throws RecognitionException {
		Generic_map_aspectContext _localctx = new Generic_map_aspectContext(_ctx, getState());
		enterRule(_localctx, 236, RULE_generic_map_aspect);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1437);
			match(KW_GENERIC);
			setState(1438);
			match(KW_MAP);
			setState(1439);
			association_list();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Port_map_aspectContext extends ParserRuleContext {
		public TerminalNode KW_PORT() { return getToken(vhdlParser.KW_PORT, 0); }
		public TerminalNode KW_MAP() { return getToken(vhdlParser.KW_MAP, 0); }
		public Association_listContext association_list() {
			return getRuleContext(Association_listContext.class,0);
		}
		public Port_map_aspectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_port_map_aspect; }
	}

	public final Port_map_aspectContext port_map_aspect() throws RecognitionException {
		Port_map_aspectContext _localctx = new Port_map_aspectContext(_ctx, getState());
		enterRule(_localctx, 238, RULE_port_map_aspect);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1441);
			match(KW_PORT);
			setState(1442);
			match(KW_MAP);
			setState(1443);
			association_list();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Alias_declarationContext extends ParserRuleContext {
		public TerminalNode KW_ALIAS() { return getToken(vhdlParser.KW_ALIAS, 0); }
		public Alias_designatorContext alias_designator() {
			return getRuleContext(Alias_designatorContext.class,0);
		}
		public TerminalNode KW_IS() { return getToken(vhdlParser.KW_IS, 0); }
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public TerminalNode COLON() { return getToken(vhdlParser.COLON, 0); }
		public Subtype_indicationContext subtype_indication() {
			return getRuleContext(Subtype_indicationContext.class,0);
		}
		public SignatureContext signature() {
			return getRuleContext(SignatureContext.class,0);
		}
		public Alias_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_alias_declaration; }
	}

	public final Alias_declarationContext alias_declaration() throws RecognitionException {
		Alias_declarationContext _localctx = new Alias_declarationContext(_ctx, getState());
		enterRule(_localctx, 240, RULE_alias_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1445);
			match(KW_ALIAS);
			setState(1446);
			alias_designator();
			setState(1449);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COLON) {
				{
				setState(1447);
				match(COLON);
				setState(1448);
				subtype_indication();
				}
			}

			setState(1451);
			match(KW_IS);
			setState(1452);
			name(0);
			setState(1454);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LSQUARE_BR) {
				{
				setState(1453);
				signature();
				}
			}

			setState(1456);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Alias_designatorContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode CHARACTER_LITERAL() { return getToken(vhdlParser.CHARACTER_LITERAL, 0); }
		public Operator_symbolContext operator_symbol() {
			return getRuleContext(Operator_symbolContext.class,0);
		}
		public Alias_designatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_alias_designator; }
	}

	public final Alias_designatorContext alias_designator() throws RecognitionException {
		Alias_designatorContext _localctx = new Alias_designatorContext(_ctx, getState());
		enterRule(_localctx, 242, RULE_alias_designator);
		try {
			setState(1461);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BASIC_IDENTIFIER:
			case EXTENDED_IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(1458);
				identifier();
				}
				break;
			case CHARACTER_LITERAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(1459);
				match(CHARACTER_LITERAL);
				}
				break;
			case STRING_LITERAL:
				enterOuterAlt(_localctx, 3);
				{
				setState(1460);
				operator_symbol();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Attribute_declarationContext extends ParserRuleContext {
		public TerminalNode KW_ATTRIBUTE() { return getToken(vhdlParser.KW_ATTRIBUTE, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode COLON() { return getToken(vhdlParser.COLON, 0); }
		public Type_markContext type_mark() {
			return getRuleContext(Type_markContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public Attribute_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attribute_declaration; }
	}

	public final Attribute_declarationContext attribute_declaration() throws RecognitionException {
		Attribute_declarationContext _localctx = new Attribute_declarationContext(_ctx, getState());
		enterRule(_localctx, 244, RULE_attribute_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1463);
			match(KW_ATTRIBUTE);
			setState(1464);
			identifier();
			setState(1465);
			match(COLON);
			setState(1466);
			type_mark();
			setState(1467);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Component_declarationContext extends ParserRuleContext {
		public List<TerminalNode> KW_COMPONENT() { return getTokens(vhdlParser.KW_COMPONENT); }
		public TerminalNode KW_COMPONENT(int i) {
			return getToken(vhdlParser.KW_COMPONENT, i);
		}
		public List<IdentifierContext> identifier() {
			return getRuleContexts(IdentifierContext.class);
		}
		public IdentifierContext identifier(int i) {
			return getRuleContext(IdentifierContext.class,i);
		}
		public TerminalNode KW_END() { return getToken(vhdlParser.KW_END, 0); }
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public TerminalNode KW_IS() { return getToken(vhdlParser.KW_IS, 0); }
		public Generic_clauseContext generic_clause() {
			return getRuleContext(Generic_clauseContext.class,0);
		}
		public Port_clauseContext port_clause() {
			return getRuleContext(Port_clauseContext.class,0);
		}
		public Component_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_component_declaration; }
	}

	public final Component_declarationContext component_declaration() throws RecognitionException {
		Component_declarationContext _localctx = new Component_declarationContext(_ctx, getState());
		enterRule(_localctx, 246, RULE_component_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1469);
			match(KW_COMPONENT);
			setState(1470);
			identifier();
			setState(1472);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_IS) {
				{
				setState(1471);
				match(KW_IS);
				}
			}

			setState(1475);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_GENERIC) {
				{
				setState(1474);
				generic_clause();
				}
			}

			setState(1478);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_PORT) {
				{
				setState(1477);
				port_clause();
				}
			}

			setState(1480);
			match(KW_END);
			setState(1481);
			match(KW_COMPONENT);
			setState(1483);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==BASIC_IDENTIFIER || _la==EXTENDED_IDENTIFIER) {
				{
				setState(1482);
				identifier();
				}
			}

			setState(1485);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Group_template_declarationContext extends ParserRuleContext {
		public TerminalNode KW_GROUP() { return getToken(vhdlParser.KW_GROUP, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode KW_IS() { return getToken(vhdlParser.KW_IS, 0); }
		public TerminalNode LPAREN() { return getToken(vhdlParser.LPAREN, 0); }
		public Entity_class_entry_listContext entity_class_entry_list() {
			return getRuleContext(Entity_class_entry_listContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(vhdlParser.RPAREN, 0); }
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public Group_template_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_group_template_declaration; }
	}

	public final Group_template_declarationContext group_template_declaration() throws RecognitionException {
		Group_template_declarationContext _localctx = new Group_template_declarationContext(_ctx, getState());
		enterRule(_localctx, 248, RULE_group_template_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1487);
			match(KW_GROUP);
			setState(1488);
			identifier();
			setState(1489);
			match(KW_IS);
			setState(1490);
			match(LPAREN);
			setState(1491);
			entity_class_entry_list();
			setState(1492);
			match(RPAREN);
			setState(1493);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Entity_class_entry_listContext extends ParserRuleContext {
		public List<Entity_class_entryContext> entity_class_entry() {
			return getRuleContexts(Entity_class_entryContext.class);
		}
		public Entity_class_entryContext entity_class_entry(int i) {
			return getRuleContext(Entity_class_entryContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(vhdlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(vhdlParser.COMMA, i);
		}
		public Entity_class_entry_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entity_class_entry_list; }
	}

	public final Entity_class_entry_listContext entity_class_entry_list() throws RecognitionException {
		Entity_class_entry_listContext _localctx = new Entity_class_entry_listContext(_ctx, getState());
		enterRule(_localctx, 250, RULE_entity_class_entry_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1495);
			entity_class_entry();
			setState(1500);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(1496);
				match(COMMA);
				setState(1497);
				entity_class_entry();
				}
				}
				setState(1502);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Entity_class_entryContext extends ParserRuleContext {
		public Entity_classContext entity_class() {
			return getRuleContext(Entity_classContext.class,0);
		}
		public TerminalNode BOX() { return getToken(vhdlParser.BOX, 0); }
		public Entity_class_entryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entity_class_entry; }
	}

	public final Entity_class_entryContext entity_class_entry() throws RecognitionException {
		Entity_class_entryContext _localctx = new Entity_class_entryContext(_ctx, getState());
		enterRule(_localctx, 252, RULE_entity_class_entry);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1503);
			entity_class();
			setState(1505);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==BOX) {
				{
				setState(1504);
				match(BOX);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Group_declarationContext extends ParserRuleContext {
		public TerminalNode KW_GROUP() { return getToken(vhdlParser.KW_GROUP, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode COLON() { return getToken(vhdlParser.COLON, 0); }
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public TerminalNode LPAREN() { return getToken(vhdlParser.LPAREN, 0); }
		public Group_constituent_listContext group_constituent_list() {
			return getRuleContext(Group_constituent_listContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(vhdlParser.RPAREN, 0); }
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public Group_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_group_declaration; }
	}

	public final Group_declarationContext group_declaration() throws RecognitionException {
		Group_declarationContext _localctx = new Group_declarationContext(_ctx, getState());
		enterRule(_localctx, 254, RULE_group_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1507);
			match(KW_GROUP);
			setState(1508);
			identifier();
			setState(1509);
			match(COLON);
			setState(1510);
			name(0);
			setState(1511);
			match(LPAREN);
			setState(1512);
			group_constituent_list();
			setState(1513);
			match(RPAREN);
			setState(1514);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Group_constituent_listContext extends ParserRuleContext {
		public List<Group_constituentContext> group_constituent() {
			return getRuleContexts(Group_constituentContext.class);
		}
		public Group_constituentContext group_constituent(int i) {
			return getRuleContext(Group_constituentContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(vhdlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(vhdlParser.COMMA, i);
		}
		public Group_constituent_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_group_constituent_list; }
	}

	public final Group_constituent_listContext group_constituent_list() throws RecognitionException {
		Group_constituent_listContext _localctx = new Group_constituent_listContext(_ctx, getState());
		enterRule(_localctx, 256, RULE_group_constituent_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1516);
			group_constituent();
			setState(1521);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(1517);
				match(COMMA);
				setState(1518);
				group_constituent();
				}
				}
				setState(1523);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Group_constituentContext extends ParserRuleContext {
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public Group_constituentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_group_constituent; }
	}

	public final Group_constituentContext group_constituent() throws RecognitionException {
		Group_constituentContext _localctx = new Group_constituentContext(_ctx, getState());
		enterRule(_localctx, 258, RULE_group_constituent);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1524);
			name(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Attribute_specificationContext extends ParserRuleContext {
		public TerminalNode KW_ATTRIBUTE() { return getToken(vhdlParser.KW_ATTRIBUTE, 0); }
		public Attribute_designatorContext attribute_designator() {
			return getRuleContext(Attribute_designatorContext.class,0);
		}
		public TerminalNode KW_OF() { return getToken(vhdlParser.KW_OF, 0); }
		public Entity_specificationContext entity_specification() {
			return getRuleContext(Entity_specificationContext.class,0);
		}
		public TerminalNode KW_IS() { return getToken(vhdlParser.KW_IS, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public Attribute_specificationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attribute_specification; }
	}

	public final Attribute_specificationContext attribute_specification() throws RecognitionException {
		Attribute_specificationContext _localctx = new Attribute_specificationContext(_ctx, getState());
		enterRule(_localctx, 260, RULE_attribute_specification);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1526);
			match(KW_ATTRIBUTE);
			setState(1527);
			attribute_designator();
			setState(1528);
			match(KW_OF);
			setState(1529);
			entity_specification();
			setState(1530);
			match(KW_IS);
			setState(1531);
			expression(0);
			setState(1532);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Entity_specificationContext extends ParserRuleContext {
		public Entity_name_listContext entity_name_list() {
			return getRuleContext(Entity_name_listContext.class,0);
		}
		public TerminalNode COLON() { return getToken(vhdlParser.COLON, 0); }
		public Entity_classContext entity_class() {
			return getRuleContext(Entity_classContext.class,0);
		}
		public Entity_specificationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entity_specification; }
	}

	public final Entity_specificationContext entity_specification() throws RecognitionException {
		Entity_specificationContext _localctx = new Entity_specificationContext(_ctx, getState());
		enterRule(_localctx, 262, RULE_entity_specification);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1534);
			entity_name_list();
			setState(1535);
			match(COLON);
			setState(1536);
			entity_class();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Entity_classContext extends ParserRuleContext {
		public TerminalNode KW_ENTITY() { return getToken(vhdlParser.KW_ENTITY, 0); }
		public TerminalNode KW_ARCHITECTURE() { return getToken(vhdlParser.KW_ARCHITECTURE, 0); }
		public TerminalNode KW_CONFIGURATION() { return getToken(vhdlParser.KW_CONFIGURATION, 0); }
		public TerminalNode KW_PROCEDURE() { return getToken(vhdlParser.KW_PROCEDURE, 0); }
		public TerminalNode KW_FUNCTION() { return getToken(vhdlParser.KW_FUNCTION, 0); }
		public TerminalNode KW_PACKAGE() { return getToken(vhdlParser.KW_PACKAGE, 0); }
		public TerminalNode KW_TYPE() { return getToken(vhdlParser.KW_TYPE, 0); }
		public TerminalNode KW_SUBTYPE() { return getToken(vhdlParser.KW_SUBTYPE, 0); }
		public TerminalNode KW_CONSTANT() { return getToken(vhdlParser.KW_CONSTANT, 0); }
		public TerminalNode KW_SIGNAL() { return getToken(vhdlParser.KW_SIGNAL, 0); }
		public TerminalNode KW_VARIABLE() { return getToken(vhdlParser.KW_VARIABLE, 0); }
		public TerminalNode KW_COMPONENT() { return getToken(vhdlParser.KW_COMPONENT, 0); }
		public TerminalNode KW_LABEL() { return getToken(vhdlParser.KW_LABEL, 0); }
		public TerminalNode KW_LITERAL() { return getToken(vhdlParser.KW_LITERAL, 0); }
		public TerminalNode KW_UNITS() { return getToken(vhdlParser.KW_UNITS, 0); }
		public TerminalNode KW_GROUP() { return getToken(vhdlParser.KW_GROUP, 0); }
		public TerminalNode KW_FILE() { return getToken(vhdlParser.KW_FILE, 0); }
		public TerminalNode KW_PROPERTY() { return getToken(vhdlParser.KW_PROPERTY, 0); }
		public TerminalNode KW_SEQUENCE() { return getToken(vhdlParser.KW_SEQUENCE, 0); }
		public Entity_classContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entity_class; }
	}

	public final Entity_classContext entity_class() throws RecognitionException {
		Entity_classContext _localctx = new Entity_classContext(_ctx, getState());
		enterRule(_localctx, 264, RULE_entity_class);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1538);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << KW_COMPONENT) | (1L << KW_ENTITY) | (1L << KW_GROUP) | (1L << KW_FILE) | (1L << KW_SIGNAL) | (1L << KW_PROCEDURE) | (1L << KW_VARIABLE) | (1L << KW_PROPERTY) | (1L << KW_SUBTYPE) | (1L << KW_CONSTANT) | (1L << KW_FUNCTION) | (1L << KW_LABEL))) != 0) || ((((_la - 82)) & ~0x3f) == 0 && ((1L << (_la - 82)) & ((1L << (KW_PACKAGE - 82)) | (1L << (KW_UNITS - 82)) | (1L << (KW_LITERAL - 82)) | (1L << (KW_SEQUENCE - 82)) | (1L << (KW_TYPE - 82)) | (1L << (KW_CONFIGURATION - 82)) | (1L << (KW_ARCHITECTURE - 82)))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Entity_name_listContext extends ParserRuleContext {
		public List<Entity_designatorContext> entity_designator() {
			return getRuleContexts(Entity_designatorContext.class);
		}
		public Entity_designatorContext entity_designator(int i) {
			return getRuleContext(Entity_designatorContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(vhdlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(vhdlParser.COMMA, i);
		}
		public TerminalNode KW_OTHERS() { return getToken(vhdlParser.KW_OTHERS, 0); }
		public TerminalNode KW_ALL() { return getToken(vhdlParser.KW_ALL, 0); }
		public Entity_name_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entity_name_list; }
	}

	public final Entity_name_listContext entity_name_list() throws RecognitionException {
		Entity_name_listContext _localctx = new Entity_name_listContext(_ctx, getState());
		enterRule(_localctx, 266, RULE_entity_name_list);
		int _la;
		try {
			setState(1550);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BASIC_IDENTIFIER:
			case EXTENDED_IDENTIFIER:
			case CHARACTER_LITERAL:
			case STRING_LITERAL:
				enterOuterAlt(_localctx, 1);
				{
				setState(1540);
				entity_designator();
				setState(1545);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(1541);
					match(COMMA);
					setState(1542);
					entity_designator();
					}
					}
					setState(1547);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			case KW_OTHERS:
				enterOuterAlt(_localctx, 2);
				{
				setState(1548);
				match(KW_OTHERS);
				}
				break;
			case KW_ALL:
				enterOuterAlt(_localctx, 3);
				{
				setState(1549);
				match(KW_ALL);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Entity_designatorContext extends ParserRuleContext {
		public Entity_tagContext entity_tag() {
			return getRuleContext(Entity_tagContext.class,0);
		}
		public SignatureContext signature() {
			return getRuleContext(SignatureContext.class,0);
		}
		public Entity_designatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entity_designator; }
	}

	public final Entity_designatorContext entity_designator() throws RecognitionException {
		Entity_designatorContext _localctx = new Entity_designatorContext(_ctx, getState());
		enterRule(_localctx, 268, RULE_entity_designator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1552);
			entity_tag();
			setState(1554);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LSQUARE_BR) {
				{
				setState(1553);
				signature();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Entity_tagContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode CHARACTER_LITERAL() { return getToken(vhdlParser.CHARACTER_LITERAL, 0); }
		public Operator_symbolContext operator_symbol() {
			return getRuleContext(Operator_symbolContext.class,0);
		}
		public Entity_tagContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entity_tag; }
	}

	public final Entity_tagContext entity_tag() throws RecognitionException {
		Entity_tagContext _localctx = new Entity_tagContext(_ctx, getState());
		enterRule(_localctx, 270, RULE_entity_tag);
		try {
			setState(1559);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BASIC_IDENTIFIER:
			case EXTENDED_IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(1556);
				identifier();
				}
				break;
			case CHARACTER_LITERAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(1557);
				match(CHARACTER_LITERAL);
				}
				break;
			case STRING_LITERAL:
				enterOuterAlt(_localctx, 3);
				{
				setState(1558);
				operator_symbol();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Configuration_specificationContext extends ParserRuleContext {
		public Simple_configuration_specificationContext simple_configuration_specification() {
			return getRuleContext(Simple_configuration_specificationContext.class,0);
		}
		public Compound_configuration_specificationContext compound_configuration_specification() {
			return getRuleContext(Compound_configuration_specificationContext.class,0);
		}
		public Configuration_specificationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_configuration_specification; }
	}

	public final Configuration_specificationContext configuration_specification() throws RecognitionException {
		Configuration_specificationContext _localctx = new Configuration_specificationContext(_ctx, getState());
		enterRule(_localctx, 272, RULE_configuration_specification);
		try {
			setState(1563);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,146,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(1561);
				simple_configuration_specification();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(1562);
				compound_configuration_specification();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Simple_configuration_specificationContext extends ParserRuleContext {
		public List<TerminalNode> KW_FOR() { return getTokens(vhdlParser.KW_FOR); }
		public TerminalNode KW_FOR(int i) {
			return getToken(vhdlParser.KW_FOR, i);
		}
		public Component_specificationContext component_specification() {
			return getRuleContext(Component_specificationContext.class,0);
		}
		public Binding_indicationContext binding_indication() {
			return getRuleContext(Binding_indicationContext.class,0);
		}
		public List<TerminalNode> SEMI() { return getTokens(vhdlParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(vhdlParser.SEMI, i);
		}
		public TerminalNode KW_END() { return getToken(vhdlParser.KW_END, 0); }
		public Simple_configuration_specificationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_simple_configuration_specification; }
	}

	public final Simple_configuration_specificationContext simple_configuration_specification() throws RecognitionException {
		Simple_configuration_specificationContext _localctx = new Simple_configuration_specificationContext(_ctx, getState());
		enterRule(_localctx, 274, RULE_simple_configuration_specification);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1565);
			match(KW_FOR);
			setState(1566);
			component_specification();
			setState(1567);
			binding_indication();
			setState(1568);
			match(SEMI);
			setState(1572);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_END) {
				{
				setState(1569);
				match(KW_END);
				setState(1570);
				match(KW_FOR);
				setState(1571);
				match(SEMI);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Compound_configuration_specificationContext extends ParserRuleContext {
		public List<TerminalNode> KW_FOR() { return getTokens(vhdlParser.KW_FOR); }
		public TerminalNode KW_FOR(int i) {
			return getToken(vhdlParser.KW_FOR, i);
		}
		public Component_specificationContext component_specification() {
			return getRuleContext(Component_specificationContext.class,0);
		}
		public Binding_indicationContext binding_indication() {
			return getRuleContext(Binding_indicationContext.class,0);
		}
		public List<TerminalNode> SEMI() { return getTokens(vhdlParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(vhdlParser.SEMI, i);
		}
		public TerminalNode KW_END() { return getToken(vhdlParser.KW_END, 0); }
		public List<Verification_unit_binding_indicationContext> verification_unit_binding_indication() {
			return getRuleContexts(Verification_unit_binding_indicationContext.class);
		}
		public Verification_unit_binding_indicationContext verification_unit_binding_indication(int i) {
			return getRuleContext(Verification_unit_binding_indicationContext.class,i);
		}
		public Compound_configuration_specificationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_compound_configuration_specification; }
	}

	public final Compound_configuration_specificationContext compound_configuration_specification() throws RecognitionException {
		Compound_configuration_specificationContext _localctx = new Compound_configuration_specificationContext(_ctx, getState());
		enterRule(_localctx, 276, RULE_compound_configuration_specification);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1574);
			match(KW_FOR);
			setState(1575);
			component_specification();
			setState(1576);
			binding_indication();
			setState(1577);
			match(SEMI);
			setState(1581); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(1578);
				verification_unit_binding_indication();
				setState(1579);
				match(SEMI);
				}
				}
				setState(1583); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==KW_USE );
			setState(1585);
			match(KW_END);
			setState(1586);
			match(KW_FOR);
			setState(1587);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Component_specificationContext extends ParserRuleContext {
		public Instantiation_listContext instantiation_list() {
			return getRuleContext(Instantiation_listContext.class,0);
		}
		public TerminalNode COLON() { return getToken(vhdlParser.COLON, 0); }
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public Component_specificationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_component_specification; }
	}

	public final Component_specificationContext component_specification() throws RecognitionException {
		Component_specificationContext _localctx = new Component_specificationContext(_ctx, getState());
		enterRule(_localctx, 278, RULE_component_specification);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1589);
			instantiation_list();
			setState(1590);
			match(COLON);
			setState(1591);
			name(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Instantiation_listContext extends ParserRuleContext {
		public List<LabelContext> label() {
			return getRuleContexts(LabelContext.class);
		}
		public LabelContext label(int i) {
			return getRuleContext(LabelContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(vhdlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(vhdlParser.COMMA, i);
		}
		public TerminalNode KW_OTHERS() { return getToken(vhdlParser.KW_OTHERS, 0); }
		public TerminalNode KW_ALL() { return getToken(vhdlParser.KW_ALL, 0); }
		public Instantiation_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instantiation_list; }
	}

	public final Instantiation_listContext instantiation_list() throws RecognitionException {
		Instantiation_listContext _localctx = new Instantiation_listContext(_ctx, getState());
		enterRule(_localctx, 280, RULE_instantiation_list);
		int _la;
		try {
			setState(1603);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BASIC_IDENTIFIER:
			case EXTENDED_IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(1593);
				label();
				setState(1598);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(1594);
					match(COMMA);
					setState(1595);
					label();
					}
					}
					setState(1600);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			case KW_OTHERS:
				enterOuterAlt(_localctx, 2);
				{
				setState(1601);
				match(KW_OTHERS);
				}
				break;
			case KW_ALL:
				enterOuterAlt(_localctx, 3);
				{
				setState(1602);
				match(KW_ALL);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Binding_indicationContext extends ParserRuleContext {
		public TerminalNode KW_USE() { return getToken(vhdlParser.KW_USE, 0); }
		public Entity_aspectContext entity_aspect() {
			return getRuleContext(Entity_aspectContext.class,0);
		}
		public Generic_map_aspectContext generic_map_aspect() {
			return getRuleContext(Generic_map_aspectContext.class,0);
		}
		public Port_map_aspectContext port_map_aspect() {
			return getRuleContext(Port_map_aspectContext.class,0);
		}
		public Binding_indicationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_binding_indication; }
	}

	public final Binding_indicationContext binding_indication() throws RecognitionException {
		Binding_indicationContext _localctx = new Binding_indicationContext(_ctx, getState());
		enterRule(_localctx, 282, RULE_binding_indication);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1607);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_USE) {
				{
				setState(1605);
				match(KW_USE);
				setState(1606);
				entity_aspect();
				}
			}

			setState(1610);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_GENERIC) {
				{
				setState(1609);
				generic_map_aspect();
				}
			}

			setState(1613);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_PORT) {
				{
				setState(1612);
				port_map_aspect();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Entity_aspectContext extends ParserRuleContext {
		public TerminalNode KW_ENTITY() { return getToken(vhdlParser.KW_ENTITY, 0); }
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public TerminalNode LPAREN() { return getToken(vhdlParser.LPAREN, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(vhdlParser.RPAREN, 0); }
		public TerminalNode KW_CONFIGURATION() { return getToken(vhdlParser.KW_CONFIGURATION, 0); }
		public TerminalNode KW_OPEN() { return getToken(vhdlParser.KW_OPEN, 0); }
		public Entity_aspectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entity_aspect; }
	}

	public final Entity_aspectContext entity_aspect() throws RecognitionException {
		Entity_aspectContext _localctx = new Entity_aspectContext(_ctx, getState());
		enterRule(_localctx, 284, RULE_entity_aspect);
		int _la;
		try {
			setState(1626);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KW_ENTITY:
				enterOuterAlt(_localctx, 1);
				{
				setState(1615);
				match(KW_ENTITY);
				setState(1616);
				name(0);
				setState(1621);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==LPAREN) {
					{
					setState(1617);
					match(LPAREN);
					setState(1618);
					identifier();
					setState(1619);
					match(RPAREN);
					}
				}

				}
				break;
			case KW_CONFIGURATION:
				enterOuterAlt(_localctx, 2);
				{
				setState(1623);
				match(KW_CONFIGURATION);
				setState(1624);
				name(0);
				}
				break;
			case KW_OPEN:
				enterOuterAlt(_localctx, 3);
				{
				setState(1625);
				match(KW_OPEN);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Verification_unit_binding_indicationContext extends ParserRuleContext {
		public TerminalNode KW_USE() { return getToken(vhdlParser.KW_USE, 0); }
		public TerminalNode KW_VUNIT() { return getToken(vhdlParser.KW_VUNIT, 0); }
		public Verification_unit_listContext verification_unit_list() {
			return getRuleContext(Verification_unit_listContext.class,0);
		}
		public Verification_unit_binding_indicationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_verification_unit_binding_indication; }
	}

	public final Verification_unit_binding_indicationContext verification_unit_binding_indication() throws RecognitionException {
		Verification_unit_binding_indicationContext _localctx = new Verification_unit_binding_indicationContext(_ctx, getState());
		enterRule(_localctx, 286, RULE_verification_unit_binding_indication);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1628);
			match(KW_USE);
			setState(1629);
			match(KW_VUNIT);
			setState(1630);
			verification_unit_list();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Verification_unit_listContext extends ParserRuleContext {
		public List<NameContext> name() {
			return getRuleContexts(NameContext.class);
		}
		public NameContext name(int i) {
			return getRuleContext(NameContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(vhdlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(vhdlParser.COMMA, i);
		}
		public Verification_unit_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_verification_unit_list; }
	}

	public final Verification_unit_listContext verification_unit_list() throws RecognitionException {
		Verification_unit_listContext _localctx = new Verification_unit_listContext(_ctx, getState());
		enterRule(_localctx, 288, RULE_verification_unit_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1632);
			name(0);
			setState(1637);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(1633);
				match(COMMA);
				setState(1634);
				name(0);
				}
				}
				setState(1639);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Disconnection_specificationContext extends ParserRuleContext {
		public TerminalNode KW_DISCONNECT() { return getToken(vhdlParser.KW_DISCONNECT, 0); }
		public Guarded_signal_specificationContext guarded_signal_specification() {
			return getRuleContext(Guarded_signal_specificationContext.class,0);
		}
		public TerminalNode KW_AFTER() { return getToken(vhdlParser.KW_AFTER, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public Disconnection_specificationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_disconnection_specification; }
	}

	public final Disconnection_specificationContext disconnection_specification() throws RecognitionException {
		Disconnection_specificationContext _localctx = new Disconnection_specificationContext(_ctx, getState());
		enterRule(_localctx, 290, RULE_disconnection_specification);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1640);
			match(KW_DISCONNECT);
			setState(1641);
			guarded_signal_specification();
			setState(1642);
			match(KW_AFTER);
			setState(1643);
			expression(0);
			setState(1644);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Guarded_signal_specificationContext extends ParserRuleContext {
		public Signal_listContext signal_list() {
			return getRuleContext(Signal_listContext.class,0);
		}
		public TerminalNode COLON() { return getToken(vhdlParser.COLON, 0); }
		public Type_markContext type_mark() {
			return getRuleContext(Type_markContext.class,0);
		}
		public Guarded_signal_specificationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_guarded_signal_specification; }
	}

	public final Guarded_signal_specificationContext guarded_signal_specification() throws RecognitionException {
		Guarded_signal_specificationContext _localctx = new Guarded_signal_specificationContext(_ctx, getState());
		enterRule(_localctx, 292, RULE_guarded_signal_specification);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1646);
			signal_list();
			setState(1647);
			match(COLON);
			setState(1648);
			type_mark();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Signal_listContext extends ParserRuleContext {
		public List<NameContext> name() {
			return getRuleContexts(NameContext.class);
		}
		public NameContext name(int i) {
			return getRuleContext(NameContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(vhdlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(vhdlParser.COMMA, i);
		}
		public TerminalNode KW_OTHERS() { return getToken(vhdlParser.KW_OTHERS, 0); }
		public TerminalNode KW_ALL() { return getToken(vhdlParser.KW_ALL, 0); }
		public Signal_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_signal_list; }
	}

	public final Signal_listContext signal_list() throws RecognitionException {
		Signal_listContext _localctx = new Signal_listContext(_ctx, getState());
		enterRule(_localctx, 294, RULE_signal_list);
		int _la;
		try {
			setState(1660);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BASIC_IDENTIFIER:
			case EXTENDED_IDENTIFIER:
			case CHARACTER_LITERAL:
			case STRING_LITERAL:
			case SHIFT_LEFT:
				enterOuterAlt(_localctx, 1);
				{
				setState(1650);
				name(0);
				setState(1655);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(1651);
					match(COMMA);
					setState(1652);
					name(0);
					}
					}
					setState(1657);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			case KW_OTHERS:
				enterOuterAlt(_localctx, 2);
				{
				setState(1658);
				match(KW_OTHERS);
				}
				break;
			case KW_ALL:
				enterOuterAlt(_localctx, 3);
				{
				setState(1659);
				match(KW_ALL);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Attribute_designatorContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public Any_keywordContext any_keyword() {
			return getRuleContext(Any_keywordContext.class,0);
		}
		public Attribute_designatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attribute_designator; }
	}

	public final Attribute_designatorContext attribute_designator() throws RecognitionException {
		Attribute_designatorContext _localctx = new Attribute_designatorContext(_ctx, getState());
		enterRule(_localctx, 296, RULE_attribute_designator);
		try {
			setState(1664);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BASIC_IDENTIFIER:
			case EXTENDED_IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(1662);
				identifier();
				}
				break;
			case KW_PROCESS:
			case KW_CONTEXT:
			case KW_POSTPONED:
			case KW_LINKAGE:
			case KW_COMPONENT:
			case KW_ABS:
			case KW_DEFAULT:
			case KW_THEN:
			case KW_BLOCK:
			case KW_REM:
			case KW_INERTIAL:
			case KW_NEXT:
			case KW_ENTITY:
			case KW_ON:
			case KW_GROUP:
			case KW_XNOR:
			case KW_FILE:
			case KW_PURE:
			case KW_GUARDED:
			case KW_GENERIC:
			case KW_RANGE:
			case KW_ELSE:
			case KW_USE:
			case KW_SHARED:
			case KW_MOD:
			case KW_LOOP:
			case KW_RECORD:
			case KW_SIGNAL:
			case KW_REJECT:
			case KW_BEGIN:
			case KW_SLA:
			case KW_DISCONNECT:
			case KW_OF:
			case KW_PROCEDURE:
			case KW_SRL:
			case KW_VUNIT:
			case KW_ATTRIBUTE:
			case KW_VARIABLE:
			case KW_PROPERTY:
			case KW_UNAFFECTED:
			case KW_XOR:
			case KW_REGISTER:
			case KW_SUBTYPE:
			case KW_TO:
			case KW_NEW:
			case KW_REPORT:
			case KW_CONSTANT:
			case KW_BUFFER:
			case KW_BODY:
			case KW_AFTER:
			case KW_TRANSPORT:
			case KW_FUNCTION:
			case KW_END:
			case KW_SELECT:
			case KW_OR:
			case KW_LIBRARY:
			case KW_ELSIF:
			case KW_SLL:
			case KW_MAP:
			case KW_SRA:
			case KW_PROTECTED:
			case KW_DOWNTO:
			case KW_LABEL:
			case KW_ALL:
			case KW_ALIAS:
			case KW_GENERATE:
			case KW_NOR:
			case KW_IN:
			case KW_RELEASE:
			case KW_EXIT:
			case KW_RETURN:
			case KW_WITH:
			case KW_UNTIL:
			case KW_AND:
			case KW_INOUT:
			case KW_WAIT:
			case KW_NAND:
			case KW_ARRAY:
			case KW_FORCE:
			case KW_WHILE:
			case KW_IMPURE:
			case KW_PACKAGE:
			case KW_UNITS:
			case KW_ASSERT:
			case KW_PARAMETER:
			case KW_SEVERITY:
			case KW_LITERAL:
			case KW_FOR:
			case KW_ROR:
			case KW_IF:
			case KW_OUT:
			case KW_ROL:
			case KW_IS:
			case KW_SEQUENCE:
			case KW_OTHERS:
			case KW_TYPE:
			case KW_CASE:
			case KW_NOT:
			case KW_CONFIGURATION:
			case KW_OPEN:
			case KW_ARCHITECTURE:
			case KW_BUS:
			case KW_ACCESS:
			case KW_WHEN:
			case KW_PORT:
			case KW_NULL:
				enterOuterAlt(_localctx, 2);
				{
				setState(1663);
				any_keyword();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class External_nameContext extends ParserRuleContext {
		public TerminalNode SHIFT_LEFT() { return getToken(vhdlParser.SHIFT_LEFT, 0); }
		public External_pathnameContext external_pathname() {
			return getRuleContext(External_pathnameContext.class,0);
		}
		public TerminalNode COLON() { return getToken(vhdlParser.COLON, 0); }
		public Subtype_indicationContext subtype_indication() {
			return getRuleContext(Subtype_indicationContext.class,0);
		}
		public TerminalNode SHIFT_RIGHT() { return getToken(vhdlParser.SHIFT_RIGHT, 0); }
		public TerminalNode KW_VARIABLE() { return getToken(vhdlParser.KW_VARIABLE, 0); }
		public TerminalNode KW_CONSTANT() { return getToken(vhdlParser.KW_CONSTANT, 0); }
		public TerminalNode KW_SIGNAL() { return getToken(vhdlParser.KW_SIGNAL, 0); }
		public External_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_external_name; }
	}

	public final External_nameContext external_name() throws RecognitionException {
		External_nameContext _localctx = new External_nameContext(_ctx, getState());
		enterRule(_localctx, 298, RULE_external_name);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1666);
			match(SHIFT_LEFT);
			setState(1667);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << KW_SIGNAL) | (1L << KW_VARIABLE) | (1L << KW_CONSTANT))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(1668);
			external_pathname();
			setState(1669);
			match(COLON);
			setState(1670);
			subtype_indication();
			setState(1671);
			match(SHIFT_RIGHT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class External_pathnameContext extends ParserRuleContext {
		public Package_pathnameContext package_pathname() {
			return getRuleContext(Package_pathnameContext.class,0);
		}
		public Absolute_pathnameContext absolute_pathname() {
			return getRuleContext(Absolute_pathnameContext.class,0);
		}
		public Relative_pathnameContext relative_pathname() {
			return getRuleContext(Relative_pathnameContext.class,0);
		}
		public External_pathnameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_external_pathname; }
	}

	public final External_pathnameContext external_pathname() throws RecognitionException {
		External_pathnameContext _localctx = new External_pathnameContext(_ctx, getState());
		enterRule(_localctx, 300, RULE_external_pathname);
		try {
			setState(1676);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case AT:
				enterOuterAlt(_localctx, 1);
				{
				setState(1673);
				package_pathname();
				}
				break;
			case DOT:
				enterOuterAlt(_localctx, 2);
				{
				setState(1674);
				absolute_pathname();
				}
				break;
			case BASIC_IDENTIFIER:
			case EXTENDED_IDENTIFIER:
			case UP:
				enterOuterAlt(_localctx, 3);
				{
				setState(1675);
				relative_pathname();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Package_pathnameContext extends ParserRuleContext {
		public TerminalNode AT() { return getToken(vhdlParser.AT, 0); }
		public List<IdentifierContext> identifier() {
			return getRuleContexts(IdentifierContext.class);
		}
		public IdentifierContext identifier(int i) {
			return getRuleContext(IdentifierContext.class,i);
		}
		public List<TerminalNode> DOT() { return getTokens(vhdlParser.DOT); }
		public TerminalNode DOT(int i) {
			return getToken(vhdlParser.DOT, i);
		}
		public Package_pathnameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_package_pathname; }
	}

	public final Package_pathnameContext package_pathname() throws RecognitionException {
		Package_pathnameContext _localctx = new Package_pathnameContext(_ctx, getState());
		enterRule(_localctx, 302, RULE_package_pathname);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1678);
			match(AT);
			setState(1679);
			identifier();
			setState(1680);
			match(DOT);
			setState(1681);
			identifier();
			setState(1682);
			match(DOT);
			setState(1683);
			identifier();
			setState(1688);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==DOT) {
				{
				{
				setState(1684);
				match(DOT);
				setState(1685);
				identifier();
				}
				}
				setState(1690);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Absolute_pathnameContext extends ParserRuleContext {
		public TerminalNode DOT() { return getToken(vhdlParser.DOT, 0); }
		public Partial_pathnameContext partial_pathname() {
			return getRuleContext(Partial_pathnameContext.class,0);
		}
		public Absolute_pathnameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_absolute_pathname; }
	}

	public final Absolute_pathnameContext absolute_pathname() throws RecognitionException {
		Absolute_pathnameContext _localctx = new Absolute_pathnameContext(_ctx, getState());
		enterRule(_localctx, 304, RULE_absolute_pathname);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1691);
			match(DOT);
			setState(1692);
			partial_pathname();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Relative_pathnameContext extends ParserRuleContext {
		public Partial_pathnameContext partial_pathname() {
			return getRuleContext(Partial_pathnameContext.class,0);
		}
		public List<TerminalNode> UP() { return getTokens(vhdlParser.UP); }
		public TerminalNode UP(int i) {
			return getToken(vhdlParser.UP, i);
		}
		public List<TerminalNode> DOT() { return getTokens(vhdlParser.DOT); }
		public TerminalNode DOT(int i) {
			return getToken(vhdlParser.DOT, i);
		}
		public Relative_pathnameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relative_pathname; }
	}

	public final Relative_pathnameContext relative_pathname() throws RecognitionException {
		Relative_pathnameContext _localctx = new Relative_pathnameContext(_ctx, getState());
		enterRule(_localctx, 306, RULE_relative_pathname);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1698);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==UP) {
				{
				{
				setState(1694);
				match(UP);
				setState(1695);
				match(DOT);
				}
				}
				setState(1700);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(1701);
			partial_pathname();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Partial_pathnameContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public List<Pathname_elementContext> pathname_element() {
			return getRuleContexts(Pathname_elementContext.class);
		}
		public Pathname_elementContext pathname_element(int i) {
			return getRuleContext(Pathname_elementContext.class,i);
		}
		public List<TerminalNode> DOT() { return getTokens(vhdlParser.DOT); }
		public TerminalNode DOT(int i) {
			return getToken(vhdlParser.DOT, i);
		}
		public Partial_pathnameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_partial_pathname; }
	}

	public final Partial_pathnameContext partial_pathname() throws RecognitionException {
		Partial_pathnameContext _localctx = new Partial_pathnameContext(_ctx, getState());
		enterRule(_localctx, 308, RULE_partial_pathname);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(1708);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,163,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(1703);
					pathname_element();
					setState(1704);
					match(DOT);
					}
					} 
				}
				setState(1710);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,163,_ctx);
			}
			setState(1711);
			identifier();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Pathname_elementContext extends ParserRuleContext {
		public LabelContext label() {
			return getRuleContext(LabelContext.class,0);
		}
		public TerminalNode LPAREN() { return getToken(vhdlParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(vhdlParser.RPAREN, 0); }
		public Pathname_elementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pathname_element; }
	}

	public final Pathname_elementContext pathname_element() throws RecognitionException {
		Pathname_elementContext _localctx = new Pathname_elementContext(_ctx, getState());
		enterRule(_localctx, 310, RULE_pathname_element);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1713);
			label();
			setState(1718);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LPAREN) {
				{
				setState(1714);
				match(LPAREN);
				setState(1715);
				expression(0);
				setState(1716);
				match(RPAREN);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public TerminalNode COND_OP() { return getToken(vhdlParser.COND_OP, 0); }
		public PrimaryContext primary() {
			return getRuleContext(PrimaryContext.class,0);
		}
		public Simple_expressionContext simple_expression() {
			return getRuleContext(Simple_expressionContext.class,0);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public Shift_operatorContext shift_operator() {
			return getRuleContext(Shift_operatorContext.class,0);
		}
		public Relational_operatorContext relational_operator() {
			return getRuleContext(Relational_operatorContext.class,0);
		}
		public Logical_operatorContext logical_operator() {
			return getRuleContext(Logical_operatorContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 312;
		enterRecursionRule(_localctx, 312, RULE_expression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(1724);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COND_OP:
				{
				setState(1721);
				match(COND_OP);
				setState(1722);
				primary();
				}
				break;
			case KW_ABS:
			case KW_XNOR:
			case KW_XOR:
			case KW_NEW:
			case KW_OR:
			case KW_NOR:
			case KW_AND:
			case KW_NAND:
			case KW_NOT:
			case KW_NULL:
			case BASIC_IDENTIFIER:
			case EXTENDED_IDENTIFIER:
			case DECIMAL_LITERAL:
			case BASED_LITERAL:
			case CHARACTER_LITERAL:
			case STRING_LITERAL:
			case BIT_STRING_LITERAL:
			case LPAREN:
			case SHIFT_LEFT:
			case PLUS:
			case MINUS:
				{
				setState(1723);
				simple_expression(0);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(1740);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,167,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(1738);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,166,_ctx) ) {
					case 1:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(1726);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(1727);
						shift_operator();
						setState(1728);
						expression(4);
						}
						break;
					case 2:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(1730);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(1731);
						relational_operator();
						setState(1732);
						expression(3);
						}
						break;
					case 3:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(1734);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(1735);
						logical_operator();
						setState(1736);
						expression(2);
						}
						break;
					}
					} 
				}
				setState(1742);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,167,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Simple_expressionContext extends ParserRuleContext {
		public List<PrimaryContext> primary() {
			return getRuleContexts(PrimaryContext.class);
		}
		public PrimaryContext primary(int i) {
			return getRuleContext(PrimaryContext.class,i);
		}
		public TerminalNode DOUBLESTAR() { return getToken(vhdlParser.DOUBLESTAR, 0); }
		public List<Simple_expressionContext> simple_expression() {
			return getRuleContexts(Simple_expressionContext.class);
		}
		public Simple_expressionContext simple_expression(int i) {
			return getRuleContext(Simple_expressionContext.class,i);
		}
		public TerminalNode KW_ABS() { return getToken(vhdlParser.KW_ABS, 0); }
		public TerminalNode KW_NOT() { return getToken(vhdlParser.KW_NOT, 0); }
		public Logical_operatorContext logical_operator() {
			return getRuleContext(Logical_operatorContext.class,0);
		}
		public SignContext sign() {
			return getRuleContext(SignContext.class,0);
		}
		public Multiplying_operatorContext multiplying_operator() {
			return getRuleContext(Multiplying_operatorContext.class,0);
		}
		public Adding_operatorContext adding_operator() {
			return getRuleContext(Adding_operatorContext.class,0);
		}
		public Simple_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_simple_expression; }
	}

	public final Simple_expressionContext simple_expression() throws RecognitionException {
		return simple_expression(0);
	}

	private Simple_expressionContext simple_expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Simple_expressionContext _localctx = new Simple_expressionContext(_ctx, _parentState);
		Simple_expressionContext _prevctx = _localctx;
		int _startState = 314;
		enterRecursionRule(_localctx, 314, RULE_simple_expression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(1758);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KW_NEW:
			case KW_NULL:
			case BASIC_IDENTIFIER:
			case EXTENDED_IDENTIFIER:
			case DECIMAL_LITERAL:
			case BASED_LITERAL:
			case CHARACTER_LITERAL:
			case STRING_LITERAL:
			case BIT_STRING_LITERAL:
			case LPAREN:
			case SHIFT_LEFT:
				{
				setState(1744);
				primary();
				setState(1747);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,168,_ctx) ) {
				case 1:
					{
					setState(1745);
					match(DOUBLESTAR);
					setState(1746);
					primary();
					}
					break;
				}
				}
				break;
			case KW_ABS:
			case KW_XNOR:
			case KW_XOR:
			case KW_OR:
			case KW_NOR:
			case KW_AND:
			case KW_NAND:
			case KW_NOT:
				{
				setState(1752);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case KW_ABS:
					{
					setState(1749);
					match(KW_ABS);
					}
					break;
				case KW_NOT:
					{
					setState(1750);
					match(KW_NOT);
					}
					break;
				case KW_XNOR:
				case KW_XOR:
				case KW_OR:
				case KW_NOR:
				case KW_AND:
				case KW_NAND:
					{
					setState(1751);
					logical_operator();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(1754);
				simple_expression(4);
				}
				break;
			case PLUS:
			case MINUS:
				{
				setState(1755);
				sign();
				setState(1756);
				simple_expression(2);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(1770);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,172,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(1768);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,171,_ctx) ) {
					case 1:
						{
						_localctx = new Simple_expressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_simple_expression);
						setState(1760);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(1761);
						multiplying_operator();
						setState(1762);
						simple_expression(4);
						}
						break;
					case 2:
						{
						_localctx = new Simple_expressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_simple_expression);
						setState(1764);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(1765);
						adding_operator();
						setState(1766);
						simple_expression(2);
						}
						break;
					}
					} 
				}
				setState(1772);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,172,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class PrimaryContext extends ParserRuleContext {
		public Numeric_literalContext numeric_literal() {
			return getRuleContext(Numeric_literalContext.class,0);
		}
		public TerminalNode BIT_STRING_LITERAL() { return getToken(vhdlParser.BIT_STRING_LITERAL, 0); }
		public TerminalNode KW_NULL() { return getToken(vhdlParser.KW_NULL, 0); }
		public AllocatorContext allocator() {
			return getRuleContext(AllocatorContext.class,0);
		}
		public AggregateContext aggregate() {
			return getRuleContext(AggregateContext.class,0);
		}
		public Qualified_expressionContext qualified_expression() {
			return getRuleContext(Qualified_expressionContext.class,0);
		}
		public PrimaryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primary; }
	}

	public final PrimaryContext primary() throws RecognitionException {
		PrimaryContext _localctx = new PrimaryContext(_ctx, getState());
		enterRule(_localctx, 316, RULE_primary);
		try {
			setState(1779);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,173,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(1773);
				numeric_literal();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(1774);
				match(BIT_STRING_LITERAL);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(1775);
				match(KW_NULL);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(1776);
				allocator();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(1777);
				aggregate();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(1778);
				qualified_expression();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Logical_operatorContext extends ParserRuleContext {
		public TerminalNode KW_AND() { return getToken(vhdlParser.KW_AND, 0); }
		public TerminalNode KW_OR() { return getToken(vhdlParser.KW_OR, 0); }
		public TerminalNode KW_NAND() { return getToken(vhdlParser.KW_NAND, 0); }
		public TerminalNode KW_NOR() { return getToken(vhdlParser.KW_NOR, 0); }
		public TerminalNode KW_XOR() { return getToken(vhdlParser.KW_XOR, 0); }
		public TerminalNode KW_XNOR() { return getToken(vhdlParser.KW_XNOR, 0); }
		public Logical_operatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logical_operator; }
	}

	public final Logical_operatorContext logical_operator() throws RecognitionException {
		Logical_operatorContext _localctx = new Logical_operatorContext(_ctx, getState());
		enterRule(_localctx, 318, RULE_logical_operator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1781);
			_la = _input.LA(1);
			if ( !(((((_la - 16)) & ~0x3f) == 0 && ((1L << (_la - 16)) & ((1L << (KW_XNOR - 16)) | (1L << (KW_XOR - 16)) | (1L << (KW_OR - 16)) | (1L << (KW_NOR - 16)) | (1L << (KW_AND - 16)) | (1L << (KW_NAND - 16)))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Relational_operatorContext extends ParserRuleContext {
		public TerminalNode EQ() { return getToken(vhdlParser.EQ, 0); }
		public TerminalNode NE() { return getToken(vhdlParser.NE, 0); }
		public TerminalNode LT() { return getToken(vhdlParser.LT, 0); }
		public TerminalNode CONASGN() { return getToken(vhdlParser.CONASGN, 0); }
		public TerminalNode GT() { return getToken(vhdlParser.GT, 0); }
		public TerminalNode GE() { return getToken(vhdlParser.GE, 0); }
		public TerminalNode EQ_MATCH() { return getToken(vhdlParser.EQ_MATCH, 0); }
		public TerminalNode NE_MATCH() { return getToken(vhdlParser.NE_MATCH, 0); }
		public TerminalNode LT_MATCH() { return getToken(vhdlParser.LT_MATCH, 0); }
		public TerminalNode LE_MATCH() { return getToken(vhdlParser.LE_MATCH, 0); }
		public TerminalNode GT_MATCH() { return getToken(vhdlParser.GT_MATCH, 0); }
		public TerminalNode GE_MATCH() { return getToken(vhdlParser.GE_MATCH, 0); }
		public Relational_operatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relational_operator; }
	}

	public final Relational_operatorContext relational_operator() throws RecognitionException {
		Relational_operatorContext _localctx = new Relational_operatorContext(_ctx, getState());
		enterRule(_localctx, 320, RULE_relational_operator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1783);
			_la = _input.LA(1);
			if ( !(((((_la - 140)) & ~0x3f) == 0 && ((1L << (_la - 140)) & ((1L << (EQ - 140)) | (1L << (NE - 140)) | (1L << (LT - 140)) | (1L << (GT - 140)) | (1L << (GE - 140)) | (1L << (EQ_MATCH - 140)) | (1L << (NE_MATCH - 140)) | (1L << (LT_MATCH - 140)) | (1L << (LE_MATCH - 140)) | (1L << (GT_MATCH - 140)) | (1L << (GE_MATCH - 140)) | (1L << (CONASGN - 140)))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Shift_operatorContext extends ParserRuleContext {
		public TerminalNode KW_SLL() { return getToken(vhdlParser.KW_SLL, 0); }
		public TerminalNode KW_SRL() { return getToken(vhdlParser.KW_SRL, 0); }
		public TerminalNode KW_SLA() { return getToken(vhdlParser.KW_SLA, 0); }
		public TerminalNode KW_SRA() { return getToken(vhdlParser.KW_SRA, 0); }
		public TerminalNode KW_ROL() { return getToken(vhdlParser.KW_ROL, 0); }
		public TerminalNode KW_ROR() { return getToken(vhdlParser.KW_ROR, 0); }
		public Shift_operatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_shift_operator; }
	}

	public final Shift_operatorContext shift_operator() throws RecognitionException {
		Shift_operatorContext _localctx = new Shift_operatorContext(_ctx, getState());
		enterRule(_localctx, 322, RULE_shift_operator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1785);
			_la = _input.LA(1);
			if ( !(((((_la - 31)) & ~0x3f) == 0 && ((1L << (_la - 31)) & ((1L << (KW_SLA - 31)) | (1L << (KW_SRL - 31)) | (1L << (KW_SLL - 31)) | (1L << (KW_SRA - 31)) | (1L << (KW_ROR - 31)) | (1L << (KW_ROL - 31)))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Adding_operatorContext extends ParserRuleContext {
		public TerminalNode PLUS() { return getToken(vhdlParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(vhdlParser.MINUS, 0); }
		public TerminalNode AMPERSAND() { return getToken(vhdlParser.AMPERSAND, 0); }
		public Adding_operatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_adding_operator; }
	}

	public final Adding_operatorContext adding_operator() throws RecognitionException {
		Adding_operatorContext _localctx = new Adding_operatorContext(_ctx, getState());
		enterRule(_localctx, 324, RULE_adding_operator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1787);
			_la = _input.LA(1);
			if ( !(((((_la - 151)) & ~0x3f) == 0 && ((1L << (_la - 151)) & ((1L << (PLUS - 151)) | (1L << (MINUS - 151)) | (1L << (AMPERSAND - 151)))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SignContext extends ParserRuleContext {
		public TerminalNode PLUS() { return getToken(vhdlParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(vhdlParser.MINUS, 0); }
		public SignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sign; }
	}

	public final SignContext sign() throws RecognitionException {
		SignContext _localctx = new SignContext(_ctx, getState());
		enterRule(_localctx, 326, RULE_sign);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1789);
			_la = _input.LA(1);
			if ( !(_la==PLUS || _la==MINUS) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Multiplying_operatorContext extends ParserRuleContext {
		public TerminalNode MUL() { return getToken(vhdlParser.MUL, 0); }
		public TerminalNode DIV() { return getToken(vhdlParser.DIV, 0); }
		public TerminalNode KW_MOD() { return getToken(vhdlParser.KW_MOD, 0); }
		public TerminalNode KW_REM() { return getToken(vhdlParser.KW_REM, 0); }
		public Multiplying_operatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multiplying_operator; }
	}

	public final Multiplying_operatorContext multiplying_operator() throws RecognitionException {
		Multiplying_operatorContext _localctx = new Multiplying_operatorContext(_ctx, getState());
		enterRule(_localctx, 328, RULE_multiplying_operator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1791);
			_la = _input.LA(1);
			if ( !(_la==KW_REM || _la==KW_MOD || _la==MUL || _la==DIV) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Miscellaneous_operatorContext extends ParserRuleContext {
		public TerminalNode DOUBLESTAR() { return getToken(vhdlParser.DOUBLESTAR, 0); }
		public TerminalNode KW_ABS() { return getToken(vhdlParser.KW_ABS, 0); }
		public TerminalNode KW_NOT() { return getToken(vhdlParser.KW_NOT, 0); }
		public Miscellaneous_operatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_miscellaneous_operator; }
	}

	public final Miscellaneous_operatorContext miscellaneous_operator() throws RecognitionException {
		Miscellaneous_operatorContext _localctx = new Miscellaneous_operatorContext(_ctx, getState());
		enterRule(_localctx, 330, RULE_miscellaneous_operator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1793);
			_la = _input.LA(1);
			if ( !(_la==KW_ABS || _la==KW_NOT || _la==DOUBLESTAR) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Numeric_literalContext extends ParserRuleContext {
		public TerminalNode DECIMAL_LITERAL() { return getToken(vhdlParser.DECIMAL_LITERAL, 0); }
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public TerminalNode BASED_LITERAL() { return getToken(vhdlParser.BASED_LITERAL, 0); }
		public Numeric_literalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_numeric_literal; }
	}

	public final Numeric_literalContext numeric_literal() throws RecognitionException {
		Numeric_literalContext _localctx = new Numeric_literalContext(_ctx, getState());
		enterRule(_localctx, 332, RULE_numeric_literal);
		try {
			setState(1804);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case DECIMAL_LITERAL:
				enterOuterAlt(_localctx, 1);
				{
				setState(1795);
				match(DECIMAL_LITERAL);
				setState(1797);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,174,_ctx) ) {
				case 1:
					{
					setState(1796);
					name(0);
					}
					break;
				}
				}
				break;
			case BASED_LITERAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(1799);
				match(BASED_LITERAL);
				setState(1801);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,175,_ctx) ) {
				case 1:
					{
					setState(1800);
					name(0);
					}
					break;
				}
				}
				break;
			case BASIC_IDENTIFIER:
			case EXTENDED_IDENTIFIER:
			case CHARACTER_LITERAL:
			case STRING_LITERAL:
			case SHIFT_LEFT:
				enterOuterAlt(_localctx, 3);
				{
				setState(1803);
				name(0);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Physical_literalContext extends ParserRuleContext {
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public TerminalNode DECIMAL_LITERAL() { return getToken(vhdlParser.DECIMAL_LITERAL, 0); }
		public TerminalNode BASED_LITERAL() { return getToken(vhdlParser.BASED_LITERAL, 0); }
		public Physical_literalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_physical_literal; }
	}

	public final Physical_literalContext physical_literal() throws RecognitionException {
		Physical_literalContext _localctx = new Physical_literalContext(_ctx, getState());
		enterRule(_localctx, 334, RULE_physical_literal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1807);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==DECIMAL_LITERAL || _la==BASED_LITERAL) {
				{
				setState(1806);
				_la = _input.LA(1);
				if ( !(_la==DECIMAL_LITERAL || _la==BASED_LITERAL) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
			}

			setState(1809);
			name(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AggregateContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(vhdlParser.LPAREN, 0); }
		public List<Element_associationContext> element_association() {
			return getRuleContexts(Element_associationContext.class);
		}
		public Element_associationContext element_association(int i) {
			return getRuleContext(Element_associationContext.class,i);
		}
		public TerminalNode RPAREN() { return getToken(vhdlParser.RPAREN, 0); }
		public List<TerminalNode> COMMA() { return getTokens(vhdlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(vhdlParser.COMMA, i);
		}
		public AggregateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_aggregate; }
	}

	public final AggregateContext aggregate() throws RecognitionException {
		AggregateContext _localctx = new AggregateContext(_ctx, getState());
		enterRule(_localctx, 336, RULE_aggregate);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1811);
			match(LPAREN);
			setState(1812);
			element_association();
			setState(1817);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(1813);
				match(COMMA);
				setState(1814);
				element_association();
				}
				}
				setState(1819);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(1820);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Element_associationContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ChoicesContext choices() {
			return getRuleContext(ChoicesContext.class,0);
		}
		public TerminalNode ARROW() { return getToken(vhdlParser.ARROW, 0); }
		public Element_associationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_element_association; }
	}

	public final Element_associationContext element_association() throws RecognitionException {
		Element_associationContext _localctx = new Element_associationContext(_ctx, getState());
		enterRule(_localctx, 338, RULE_element_association);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1825);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,179,_ctx) ) {
			case 1:
				{
				setState(1822);
				choices();
				setState(1823);
				match(ARROW);
				}
				break;
			}
			setState(1827);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ChoicesContext extends ParserRuleContext {
		public List<ChoiceContext> choice() {
			return getRuleContexts(ChoiceContext.class);
		}
		public ChoiceContext choice(int i) {
			return getRuleContext(ChoiceContext.class,i);
		}
		public List<TerminalNode> BAR() { return getTokens(vhdlParser.BAR); }
		public TerminalNode BAR(int i) {
			return getToken(vhdlParser.BAR, i);
		}
		public ChoicesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_choices; }
	}

	public final ChoicesContext choices() throws RecognitionException {
		ChoicesContext _localctx = new ChoicesContext(_ctx, getState());
		enterRule(_localctx, 340, RULE_choices);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1829);
			choice();
			setState(1834);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==BAR) {
				{
				{
				setState(1830);
				match(BAR);
				setState(1831);
				choice();
				}
				}
				setState(1836);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ChoiceContext extends ParserRuleContext {
		public Discrete_rangeContext discrete_range() {
			return getRuleContext(Discrete_rangeContext.class,0);
		}
		public Simple_expressionContext simple_expression() {
			return getRuleContext(Simple_expressionContext.class,0);
		}
		public TerminalNode KW_OTHERS() { return getToken(vhdlParser.KW_OTHERS, 0); }
		public ChoiceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_choice; }
	}

	public final ChoiceContext choice() throws RecognitionException {
		ChoiceContext _localctx = new ChoiceContext(_ctx, getState());
		enterRule(_localctx, 342, RULE_choice);
		try {
			setState(1840);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,181,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(1837);
				discrete_range();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(1838);
				simple_expression(0);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(1839);
				match(KW_OTHERS);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Qualified_expressionContext extends ParserRuleContext {
		public Type_markContext type_mark() {
			return getRuleContext(Type_markContext.class,0);
		}
		public TerminalNode APOSTROPHE() { return getToken(vhdlParser.APOSTROPHE, 0); }
		public AggregateContext aggregate() {
			return getRuleContext(AggregateContext.class,0);
		}
		public Qualified_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_qualified_expression; }
	}

	public final Qualified_expressionContext qualified_expression() throws RecognitionException {
		Qualified_expressionContext _localctx = new Qualified_expressionContext(_ctx, getState());
		enterRule(_localctx, 344, RULE_qualified_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1842);
			type_mark();
			setState(1843);
			match(APOSTROPHE);
			setState(1844);
			aggregate();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AllocatorContext extends ParserRuleContext {
		public TerminalNode KW_NEW() { return getToken(vhdlParser.KW_NEW, 0); }
		public Subtype_indicationContext subtype_indication() {
			return getRuleContext(Subtype_indicationContext.class,0);
		}
		public Qualified_expressionContext qualified_expression() {
			return getRuleContext(Qualified_expressionContext.class,0);
		}
		public AllocatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_allocator; }
	}

	public final AllocatorContext allocator() throws RecognitionException {
		AllocatorContext _localctx = new AllocatorContext(_ctx, getState());
		enterRule(_localctx, 346, RULE_allocator);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1846);
			match(KW_NEW);
			setState(1849);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,182,_ctx) ) {
			case 1:
				{
				setState(1847);
				subtype_indication();
				}
				break;
			case 2:
				{
				setState(1848);
				qualified_expression();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Sequence_of_statementsContext extends ParserRuleContext {
		public List<Sequential_statementContext> sequential_statement() {
			return getRuleContexts(Sequential_statementContext.class);
		}
		public Sequential_statementContext sequential_statement(int i) {
			return getRuleContext(Sequential_statementContext.class,i);
		}
		public Sequence_of_statementsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sequence_of_statements; }
	}

	public final Sequence_of_statementsContext sequence_of_statements() throws RecognitionException {
		Sequence_of_statementsContext _localctx = new Sequence_of_statementsContext(_ctx, getState());
		enterRule(_localctx, 348, RULE_sequence_of_statements);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(1854);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,183,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(1851);
					sequential_statement();
					}
					} 
				}
				setState(1856);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,183,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Sequential_statementContext extends ParserRuleContext {
		public Wait_statementContext wait_statement() {
			return getRuleContext(Wait_statementContext.class,0);
		}
		public Assertion_statementContext assertion_statement() {
			return getRuleContext(Assertion_statementContext.class,0);
		}
		public Report_statementContext report_statement() {
			return getRuleContext(Report_statementContext.class,0);
		}
		public Signal_assignment_statementContext signal_assignment_statement() {
			return getRuleContext(Signal_assignment_statementContext.class,0);
		}
		public Variable_assignment_statementContext variable_assignment_statement() {
			return getRuleContext(Variable_assignment_statementContext.class,0);
		}
		public Procedure_call_statementContext procedure_call_statement() {
			return getRuleContext(Procedure_call_statementContext.class,0);
		}
		public If_statementContext if_statement() {
			return getRuleContext(If_statementContext.class,0);
		}
		public Case_statementContext case_statement() {
			return getRuleContext(Case_statementContext.class,0);
		}
		public Loop_statementContext loop_statement() {
			return getRuleContext(Loop_statementContext.class,0);
		}
		public Next_statementContext next_statement() {
			return getRuleContext(Next_statementContext.class,0);
		}
		public Exit_statementContext exit_statement() {
			return getRuleContext(Exit_statementContext.class,0);
		}
		public Return_statementContext return_statement() {
			return getRuleContext(Return_statementContext.class,0);
		}
		public Null_statementContext null_statement() {
			return getRuleContext(Null_statementContext.class,0);
		}
		public LabelContext label() {
			return getRuleContext(LabelContext.class,0);
		}
		public TerminalNode COLON() { return getToken(vhdlParser.COLON, 0); }
		public Sequential_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sequential_statement; }
	}

	public final Sequential_statementContext sequential_statement() throws RecognitionException {
		Sequential_statementContext _localctx = new Sequential_statementContext(_ctx, getState());
		enterRule(_localctx, 350, RULE_sequential_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1860);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,184,_ctx) ) {
			case 1:
				{
				setState(1857);
				label();
				setState(1858);
				match(COLON);
				}
				break;
			}
			setState(1875);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,185,_ctx) ) {
			case 1:
				{
				setState(1862);
				wait_statement();
				}
				break;
			case 2:
				{
				setState(1863);
				assertion_statement();
				}
				break;
			case 3:
				{
				setState(1864);
				report_statement();
				}
				break;
			case 4:
				{
				setState(1865);
				signal_assignment_statement();
				}
				break;
			case 5:
				{
				setState(1866);
				variable_assignment_statement();
				}
				break;
			case 6:
				{
				setState(1867);
				procedure_call_statement();
				}
				break;
			case 7:
				{
				setState(1868);
				if_statement();
				}
				break;
			case 8:
				{
				setState(1869);
				case_statement();
				}
				break;
			case 9:
				{
				setState(1870);
				loop_statement();
				}
				break;
			case 10:
				{
				setState(1871);
				next_statement();
				}
				break;
			case 11:
				{
				setState(1872);
				exit_statement();
				}
				break;
			case 12:
				{
				setState(1873);
				return_statement();
				}
				break;
			case 13:
				{
				setState(1874);
				null_statement();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Wait_statementContext extends ParserRuleContext {
		public TerminalNode KW_WAIT() { return getToken(vhdlParser.KW_WAIT, 0); }
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public Sensitivity_clauseContext sensitivity_clause() {
			return getRuleContext(Sensitivity_clauseContext.class,0);
		}
		public Condition_clauseContext condition_clause() {
			return getRuleContext(Condition_clauseContext.class,0);
		}
		public Timeout_clauseContext timeout_clause() {
			return getRuleContext(Timeout_clauseContext.class,0);
		}
		public Wait_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_wait_statement; }
	}

	public final Wait_statementContext wait_statement() throws RecognitionException {
		Wait_statementContext _localctx = new Wait_statementContext(_ctx, getState());
		enterRule(_localctx, 352, RULE_wait_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1877);
			match(KW_WAIT);
			setState(1879);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_ON) {
				{
				setState(1878);
				sensitivity_clause();
				}
			}

			setState(1882);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_UNTIL) {
				{
				setState(1881);
				condition_clause();
				}
			}

			setState(1885);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_FOR) {
				{
				setState(1884);
				timeout_clause();
				}
			}

			setState(1887);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Sensitivity_clauseContext extends ParserRuleContext {
		public TerminalNode KW_ON() { return getToken(vhdlParser.KW_ON, 0); }
		public Sensitivity_listContext sensitivity_list() {
			return getRuleContext(Sensitivity_listContext.class,0);
		}
		public Sensitivity_clauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sensitivity_clause; }
	}

	public final Sensitivity_clauseContext sensitivity_clause() throws RecognitionException {
		Sensitivity_clauseContext _localctx = new Sensitivity_clauseContext(_ctx, getState());
		enterRule(_localctx, 354, RULE_sensitivity_clause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1889);
			match(KW_ON);
			setState(1890);
			sensitivity_list();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Sensitivity_listContext extends ParserRuleContext {
		public List<NameContext> name() {
			return getRuleContexts(NameContext.class);
		}
		public NameContext name(int i) {
			return getRuleContext(NameContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(vhdlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(vhdlParser.COMMA, i);
		}
		public Sensitivity_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sensitivity_list; }
	}

	public final Sensitivity_listContext sensitivity_list() throws RecognitionException {
		Sensitivity_listContext _localctx = new Sensitivity_listContext(_ctx, getState());
		enterRule(_localctx, 356, RULE_sensitivity_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1892);
			name(0);
			setState(1897);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(1893);
				match(COMMA);
				setState(1894);
				name(0);
				}
				}
				setState(1899);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Condition_clauseContext extends ParserRuleContext {
		public TerminalNode KW_UNTIL() { return getToken(vhdlParser.KW_UNTIL, 0); }
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public Condition_clauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition_clause; }
	}

	public final Condition_clauseContext condition_clause() throws RecognitionException {
		Condition_clauseContext _localctx = new Condition_clauseContext(_ctx, getState());
		enterRule(_localctx, 358, RULE_condition_clause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1900);
			match(KW_UNTIL);
			setState(1901);
			condition();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ConditionContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 360, RULE_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1903);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Timeout_clauseContext extends ParserRuleContext {
		public TerminalNode KW_FOR() { return getToken(vhdlParser.KW_FOR, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Timeout_clauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_timeout_clause; }
	}

	public final Timeout_clauseContext timeout_clause() throws RecognitionException {
		Timeout_clauseContext _localctx = new Timeout_clauseContext(_ctx, getState());
		enterRule(_localctx, 362, RULE_timeout_clause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1905);
			match(KW_FOR);
			setState(1906);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Assertion_statementContext extends ParserRuleContext {
		public AssertionContext assertion() {
			return getRuleContext(AssertionContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public Assertion_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assertion_statement; }
	}

	public final Assertion_statementContext assertion_statement() throws RecognitionException {
		Assertion_statementContext _localctx = new Assertion_statementContext(_ctx, getState());
		enterRule(_localctx, 364, RULE_assertion_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1908);
			assertion();
			setState(1909);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssertionContext extends ParserRuleContext {
		public TerminalNode KW_ASSERT() { return getToken(vhdlParser.KW_ASSERT, 0); }
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public TerminalNode KW_REPORT() { return getToken(vhdlParser.KW_REPORT, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode KW_SEVERITY() { return getToken(vhdlParser.KW_SEVERITY, 0); }
		public AssertionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assertion; }
	}

	public final AssertionContext assertion() throws RecognitionException {
		AssertionContext _localctx = new AssertionContext(_ctx, getState());
		enterRule(_localctx, 366, RULE_assertion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1911);
			match(KW_ASSERT);
			setState(1912);
			condition();
			setState(1915);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_REPORT) {
				{
				setState(1913);
				match(KW_REPORT);
				setState(1914);
				expression(0);
				}
			}

			setState(1919);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_SEVERITY) {
				{
				setState(1917);
				match(KW_SEVERITY);
				setState(1918);
				expression(0);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Report_statementContext extends ParserRuleContext {
		public TerminalNode KW_REPORT() { return getToken(vhdlParser.KW_REPORT, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public TerminalNode KW_SEVERITY() { return getToken(vhdlParser.KW_SEVERITY, 0); }
		public Report_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_report_statement; }
	}

	public final Report_statementContext report_statement() throws RecognitionException {
		Report_statementContext _localctx = new Report_statementContext(_ctx, getState());
		enterRule(_localctx, 368, RULE_report_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1921);
			match(KW_REPORT);
			setState(1922);
			expression(0);
			setState(1925);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_SEVERITY) {
				{
				setState(1923);
				match(KW_SEVERITY);
				setState(1924);
				expression(0);
				}
			}

			setState(1927);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Signal_assignment_statementContext extends ParserRuleContext {
		public Simple_signal_assignmentContext simple_signal_assignment() {
			return getRuleContext(Simple_signal_assignmentContext.class,0);
		}
		public Conditional_signal_assignmentContext conditional_signal_assignment() {
			return getRuleContext(Conditional_signal_assignmentContext.class,0);
		}
		public Selected_signal_assignmentContext selected_signal_assignment() {
			return getRuleContext(Selected_signal_assignmentContext.class,0);
		}
		public Signal_assignment_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_signal_assignment_statement; }
	}

	public final Signal_assignment_statementContext signal_assignment_statement() throws RecognitionException {
		Signal_assignment_statementContext _localctx = new Signal_assignment_statementContext(_ctx, getState());
		enterRule(_localctx, 370, RULE_signal_assignment_statement);
		try {
			setState(1932);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,193,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(1929);
				simple_signal_assignment();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(1930);
				conditional_signal_assignment();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(1931);
				selected_signal_assignment();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Simple_signal_assignmentContext extends ParserRuleContext {
		public Simple_waveform_assignmentContext simple_waveform_assignment() {
			return getRuleContext(Simple_waveform_assignmentContext.class,0);
		}
		public Simple_force_assignmentContext simple_force_assignment() {
			return getRuleContext(Simple_force_assignmentContext.class,0);
		}
		public Simple_release_assignmentContext simple_release_assignment() {
			return getRuleContext(Simple_release_assignmentContext.class,0);
		}
		public Simple_signal_assignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_simple_signal_assignment; }
	}

	public final Simple_signal_assignmentContext simple_signal_assignment() throws RecognitionException {
		Simple_signal_assignmentContext _localctx = new Simple_signal_assignmentContext(_ctx, getState());
		enterRule(_localctx, 372, RULE_simple_signal_assignment);
		try {
			setState(1937);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,194,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(1934);
				simple_waveform_assignment();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(1935);
				simple_force_assignment();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(1936);
				simple_release_assignment();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Simple_waveform_assignmentContext extends ParserRuleContext {
		public TargetContext target() {
			return getRuleContext(TargetContext.class,0);
		}
		public TerminalNode CONASGN() { return getToken(vhdlParser.CONASGN, 0); }
		public WaveformContext waveform() {
			return getRuleContext(WaveformContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public Delay_mechanismContext delay_mechanism() {
			return getRuleContext(Delay_mechanismContext.class,0);
		}
		public Simple_waveform_assignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_simple_waveform_assignment; }
	}

	public final Simple_waveform_assignmentContext simple_waveform_assignment() throws RecognitionException {
		Simple_waveform_assignmentContext _localctx = new Simple_waveform_assignmentContext(_ctx, getState());
		enterRule(_localctx, 374, RULE_simple_waveform_assignment);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1939);
			target();
			setState(1940);
			match(CONASGN);
			setState(1942);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << KW_INERTIAL) | (1L << KW_REJECT) | (1L << KW_TRANSPORT))) != 0)) {
				{
				setState(1941);
				delay_mechanism();
				}
			}

			setState(1944);
			waveform();
			setState(1945);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Simple_force_assignmentContext extends ParserRuleContext {
		public TargetContext target() {
			return getRuleContext(TargetContext.class,0);
		}
		public TerminalNode CONASGN() { return getToken(vhdlParser.CONASGN, 0); }
		public TerminalNode KW_FORCE() { return getToken(vhdlParser.KW_FORCE, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public Force_modeContext force_mode() {
			return getRuleContext(Force_modeContext.class,0);
		}
		public Simple_force_assignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_simple_force_assignment; }
	}

	public final Simple_force_assignmentContext simple_force_assignment() throws RecognitionException {
		Simple_force_assignmentContext _localctx = new Simple_force_assignmentContext(_ctx, getState());
		enterRule(_localctx, 376, RULE_simple_force_assignment);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1947);
			target();
			setState(1948);
			match(CONASGN);
			setState(1949);
			match(KW_FORCE);
			setState(1951);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_IN || _la==KW_OUT) {
				{
				setState(1950);
				force_mode();
				}
			}

			setState(1953);
			expression(0);
			setState(1954);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Simple_release_assignmentContext extends ParserRuleContext {
		public TargetContext target() {
			return getRuleContext(TargetContext.class,0);
		}
		public TerminalNode CONASGN() { return getToken(vhdlParser.CONASGN, 0); }
		public TerminalNode KW_RELEASE() { return getToken(vhdlParser.KW_RELEASE, 0); }
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public Force_modeContext force_mode() {
			return getRuleContext(Force_modeContext.class,0);
		}
		public Simple_release_assignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_simple_release_assignment; }
	}

	public final Simple_release_assignmentContext simple_release_assignment() throws RecognitionException {
		Simple_release_assignmentContext _localctx = new Simple_release_assignmentContext(_ctx, getState());
		enterRule(_localctx, 378, RULE_simple_release_assignment);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1956);
			target();
			setState(1957);
			match(CONASGN);
			setState(1958);
			match(KW_RELEASE);
			setState(1960);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_IN || _la==KW_OUT) {
				{
				setState(1959);
				force_mode();
				}
			}

			setState(1962);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Force_modeContext extends ParserRuleContext {
		public TerminalNode KW_IN() { return getToken(vhdlParser.KW_IN, 0); }
		public TerminalNode KW_OUT() { return getToken(vhdlParser.KW_OUT, 0); }
		public Force_modeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_force_mode; }
	}

	public final Force_modeContext force_mode() throws RecognitionException {
		Force_modeContext _localctx = new Force_modeContext(_ctx, getState());
		enterRule(_localctx, 380, RULE_force_mode);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1964);
			_la = _input.LA(1);
			if ( !(_la==KW_IN || _la==KW_OUT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Delay_mechanismContext extends ParserRuleContext {
		public TerminalNode KW_TRANSPORT() { return getToken(vhdlParser.KW_TRANSPORT, 0); }
		public TerminalNode KW_INERTIAL() { return getToken(vhdlParser.KW_INERTIAL, 0); }
		public TerminalNode KW_REJECT() { return getToken(vhdlParser.KW_REJECT, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Delay_mechanismContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_delay_mechanism; }
	}

	public final Delay_mechanismContext delay_mechanism() throws RecognitionException {
		Delay_mechanismContext _localctx = new Delay_mechanismContext(_ctx, getState());
		enterRule(_localctx, 382, RULE_delay_mechanism);
		int _la;
		try {
			setState(1972);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KW_TRANSPORT:
				enterOuterAlt(_localctx, 1);
				{
				setState(1966);
				match(KW_TRANSPORT);
				}
				break;
			case KW_INERTIAL:
			case KW_REJECT:
				enterOuterAlt(_localctx, 2);
				{
				setState(1969);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==KW_REJECT) {
					{
					setState(1967);
					match(KW_REJECT);
					setState(1968);
					expression(0);
					}
				}

				setState(1971);
				match(KW_INERTIAL);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TargetContext extends ParserRuleContext {
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public AggregateContext aggregate() {
			return getRuleContext(AggregateContext.class,0);
		}
		public TargetContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_target; }
	}

	public final TargetContext target() throws RecognitionException {
		TargetContext _localctx = new TargetContext(_ctx, getState());
		enterRule(_localctx, 384, RULE_target);
		try {
			setState(1976);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BASIC_IDENTIFIER:
			case EXTENDED_IDENTIFIER:
			case CHARACTER_LITERAL:
			case STRING_LITERAL:
			case SHIFT_LEFT:
				enterOuterAlt(_localctx, 1);
				{
				setState(1974);
				name(0);
				}
				break;
			case LPAREN:
				enterOuterAlt(_localctx, 2);
				{
				setState(1975);
				aggregate();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class WaveformContext extends ParserRuleContext {
		public List<Waveform_elementContext> waveform_element() {
			return getRuleContexts(Waveform_elementContext.class);
		}
		public Waveform_elementContext waveform_element(int i) {
			return getRuleContext(Waveform_elementContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(vhdlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(vhdlParser.COMMA, i);
		}
		public TerminalNode KW_UNAFFECTED() { return getToken(vhdlParser.KW_UNAFFECTED, 0); }
		public WaveformContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_waveform; }
	}

	public final WaveformContext waveform() throws RecognitionException {
		WaveformContext _localctx = new WaveformContext(_ctx, getState());
		enterRule(_localctx, 386, RULE_waveform);
		int _la;
		try {
			setState(1987);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KW_ABS:
			case KW_XNOR:
			case KW_XOR:
			case KW_NEW:
			case KW_OR:
			case KW_NOR:
			case KW_AND:
			case KW_NAND:
			case KW_NOT:
			case KW_NULL:
			case BASIC_IDENTIFIER:
			case EXTENDED_IDENTIFIER:
			case DECIMAL_LITERAL:
			case BASED_LITERAL:
			case CHARACTER_LITERAL:
			case STRING_LITERAL:
			case BIT_STRING_LITERAL:
			case LPAREN:
			case SHIFT_LEFT:
			case PLUS:
			case MINUS:
			case COND_OP:
				enterOuterAlt(_localctx, 1);
				{
				setState(1978);
				waveform_element();
				setState(1983);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(1979);
					match(COMMA);
					setState(1980);
					waveform_element();
					}
					}
					setState(1985);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			case KW_UNAFFECTED:
				enterOuterAlt(_localctx, 2);
				{
				setState(1986);
				match(KW_UNAFFECTED);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Waveform_elementContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode KW_AFTER() { return getToken(vhdlParser.KW_AFTER, 0); }
		public TerminalNode KW_NULL() { return getToken(vhdlParser.KW_NULL, 0); }
		public Waveform_elementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_waveform_element; }
	}

	public final Waveform_elementContext waveform_element() throws RecognitionException {
		Waveform_elementContext _localctx = new Waveform_elementContext(_ctx, getState());
		enterRule(_localctx, 388, RULE_waveform_element);
		int _la;
		try {
			setState(1999);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,205,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(1989);
				expression(0);
				setState(1992);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==KW_AFTER) {
					{
					setState(1990);
					match(KW_AFTER);
					setState(1991);
					expression(0);
					}
				}

				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(1994);
				match(KW_NULL);
				setState(1997);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==KW_AFTER) {
					{
					setState(1995);
					match(KW_AFTER);
					setState(1996);
					expression(0);
					}
				}

				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Conditional_signal_assignmentContext extends ParserRuleContext {
		public Conditional_waveform_assignmentContext conditional_waveform_assignment() {
			return getRuleContext(Conditional_waveform_assignmentContext.class,0);
		}
		public Conditional_force_assignmentContext conditional_force_assignment() {
			return getRuleContext(Conditional_force_assignmentContext.class,0);
		}
		public Conditional_signal_assignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_conditional_signal_assignment; }
	}

	public final Conditional_signal_assignmentContext conditional_signal_assignment() throws RecognitionException {
		Conditional_signal_assignmentContext _localctx = new Conditional_signal_assignmentContext(_ctx, getState());
		enterRule(_localctx, 390, RULE_conditional_signal_assignment);
		try {
			setState(2003);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,206,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(2001);
				conditional_waveform_assignment();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(2002);
				conditional_force_assignment();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Conditional_waveform_assignmentContext extends ParserRuleContext {
		public TargetContext target() {
			return getRuleContext(TargetContext.class,0);
		}
		public TerminalNode CONASGN() { return getToken(vhdlParser.CONASGN, 0); }
		public Conditional_waveformsContext conditional_waveforms() {
			return getRuleContext(Conditional_waveformsContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public Delay_mechanismContext delay_mechanism() {
			return getRuleContext(Delay_mechanismContext.class,0);
		}
		public Conditional_waveform_assignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_conditional_waveform_assignment; }
	}

	public final Conditional_waveform_assignmentContext conditional_waveform_assignment() throws RecognitionException {
		Conditional_waveform_assignmentContext _localctx = new Conditional_waveform_assignmentContext(_ctx, getState());
		enterRule(_localctx, 392, RULE_conditional_waveform_assignment);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2005);
			target();
			setState(2006);
			match(CONASGN);
			setState(2008);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << KW_INERTIAL) | (1L << KW_REJECT) | (1L << KW_TRANSPORT))) != 0)) {
				{
				setState(2007);
				delay_mechanism();
				}
			}

			setState(2010);
			conditional_waveforms();
			setState(2011);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Conditional_waveformsContext extends ParserRuleContext {
		public List<WaveformContext> waveform() {
			return getRuleContexts(WaveformContext.class);
		}
		public WaveformContext waveform(int i) {
			return getRuleContext(WaveformContext.class,i);
		}
		public List<TerminalNode> KW_WHEN() { return getTokens(vhdlParser.KW_WHEN); }
		public TerminalNode KW_WHEN(int i) {
			return getToken(vhdlParser.KW_WHEN, i);
		}
		public List<ConditionContext> condition() {
			return getRuleContexts(ConditionContext.class);
		}
		public ConditionContext condition(int i) {
			return getRuleContext(ConditionContext.class,i);
		}
		public List<TerminalNode> KW_ELSE() { return getTokens(vhdlParser.KW_ELSE); }
		public TerminalNode KW_ELSE(int i) {
			return getToken(vhdlParser.KW_ELSE, i);
		}
		public Conditional_waveformsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_conditional_waveforms; }
	}

	public final Conditional_waveformsContext conditional_waveforms() throws RecognitionException {
		Conditional_waveformsContext _localctx = new Conditional_waveformsContext(_ctx, getState());
		enterRule(_localctx, 394, RULE_conditional_waveforms);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(2013);
			waveform();
			setState(2014);
			match(KW_WHEN);
			setState(2015);
			condition();
			setState(2023);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,208,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(2016);
					match(KW_ELSE);
					setState(2017);
					waveform();
					setState(2018);
					match(KW_WHEN);
					setState(2019);
					condition();
					}
					} 
				}
				setState(2025);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,208,_ctx);
			}
			setState(2029);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,209,_ctx) ) {
			case 1:
				{
				setState(2026);
				match(KW_ELSE);
				setState(2027);
				waveform();
				}
				break;
			case 2:
				{
				setState(2028);
				if (!(_input->LA(1) != KW_ELSE)) throw new FailedPredicateException(this, "_input->LA(1) != KW_ELSE");
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Conditional_force_assignmentContext extends ParserRuleContext {
		public TargetContext target() {
			return getRuleContext(TargetContext.class,0);
		}
		public TerminalNode CONASGN() { return getToken(vhdlParser.CONASGN, 0); }
		public TerminalNode KW_FORCE() { return getToken(vhdlParser.KW_FORCE, 0); }
		public Conditional_expressionsContext conditional_expressions() {
			return getRuleContext(Conditional_expressionsContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public Force_modeContext force_mode() {
			return getRuleContext(Force_modeContext.class,0);
		}
		public Conditional_force_assignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_conditional_force_assignment; }
	}

	public final Conditional_force_assignmentContext conditional_force_assignment() throws RecognitionException {
		Conditional_force_assignmentContext _localctx = new Conditional_force_assignmentContext(_ctx, getState());
		enterRule(_localctx, 396, RULE_conditional_force_assignment);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2031);
			target();
			setState(2032);
			match(CONASGN);
			setState(2033);
			match(KW_FORCE);
			setState(2035);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_IN || _la==KW_OUT) {
				{
				setState(2034);
				force_mode();
				}
			}

			setState(2037);
			conditional_expressions();
			setState(2038);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Conditional_expressionsContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> KW_WHEN() { return getTokens(vhdlParser.KW_WHEN); }
		public TerminalNode KW_WHEN(int i) {
			return getToken(vhdlParser.KW_WHEN, i);
		}
		public List<ConditionContext> condition() {
			return getRuleContexts(ConditionContext.class);
		}
		public ConditionContext condition(int i) {
			return getRuleContext(ConditionContext.class,i);
		}
		public List<TerminalNode> KW_ELSE() { return getTokens(vhdlParser.KW_ELSE); }
		public TerminalNode KW_ELSE(int i) {
			return getToken(vhdlParser.KW_ELSE, i);
		}
		public Conditional_expressionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_conditional_expressions; }
	}

	public final Conditional_expressionsContext conditional_expressions() throws RecognitionException {
		Conditional_expressionsContext _localctx = new Conditional_expressionsContext(_ctx, getState());
		enterRule(_localctx, 398, RULE_conditional_expressions);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(2040);
			expression(0);
			setState(2041);
			match(KW_WHEN);
			setState(2042);
			condition();
			setState(2050);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,211,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(2043);
					match(KW_ELSE);
					setState(2044);
					expression(0);
					setState(2045);
					match(KW_WHEN);
					setState(2046);
					condition();
					}
					} 
				}
				setState(2052);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,211,_ctx);
			}
			setState(2056);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,212,_ctx) ) {
			case 1:
				{
				setState(2053);
				match(KW_ELSE);
				setState(2054);
				expression(0);
				}
				break;
			case 2:
				{
				setState(2055);
				if (!(_input->LA(1) != KW_ELSE)) throw new FailedPredicateException(this, "_input->LA(1) != KW_ELSE");
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Selected_signal_assignmentContext extends ParserRuleContext {
		public Selected_waveform_assignmentContext selected_waveform_assignment() {
			return getRuleContext(Selected_waveform_assignmentContext.class,0);
		}
		public Selected_force_assignmentContext selected_force_assignment() {
			return getRuleContext(Selected_force_assignmentContext.class,0);
		}
		public Selected_signal_assignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_selected_signal_assignment; }
	}

	public final Selected_signal_assignmentContext selected_signal_assignment() throws RecognitionException {
		Selected_signal_assignmentContext _localctx = new Selected_signal_assignmentContext(_ctx, getState());
		enterRule(_localctx, 400, RULE_selected_signal_assignment);
		try {
			setState(2060);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,213,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(2058);
				selected_waveform_assignment();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(2059);
				selected_force_assignment();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Selected_waveform_assignmentContext extends ParserRuleContext {
		public TerminalNode KW_WITH() { return getToken(vhdlParser.KW_WITH, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode KW_SELECT() { return getToken(vhdlParser.KW_SELECT, 0); }
		public TargetContext target() {
			return getRuleContext(TargetContext.class,0);
		}
		public TerminalNode CONASGN() { return getToken(vhdlParser.CONASGN, 0); }
		public Selected_waveformsContext selected_waveforms() {
			return getRuleContext(Selected_waveformsContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public TerminalNode QUESTIONMARK() { return getToken(vhdlParser.QUESTIONMARK, 0); }
		public Delay_mechanismContext delay_mechanism() {
			return getRuleContext(Delay_mechanismContext.class,0);
		}
		public Selected_waveform_assignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_selected_waveform_assignment; }
	}

	public final Selected_waveform_assignmentContext selected_waveform_assignment() throws RecognitionException {
		Selected_waveform_assignmentContext _localctx = new Selected_waveform_assignmentContext(_ctx, getState());
		enterRule(_localctx, 402, RULE_selected_waveform_assignment);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2062);
			match(KW_WITH);
			setState(2063);
			expression(0);
			setState(2064);
			match(KW_SELECT);
			setState(2066);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==QUESTIONMARK) {
				{
				setState(2065);
				match(QUESTIONMARK);
				}
			}

			setState(2068);
			target();
			setState(2069);
			match(CONASGN);
			setState(2071);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << KW_INERTIAL) | (1L << KW_REJECT) | (1L << KW_TRANSPORT))) != 0)) {
				{
				setState(2070);
				delay_mechanism();
				}
			}

			setState(2073);
			selected_waveforms();
			setState(2074);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Selected_waveformsContext extends ParserRuleContext {
		public List<WaveformContext> waveform() {
			return getRuleContexts(WaveformContext.class);
		}
		public WaveformContext waveform(int i) {
			return getRuleContext(WaveformContext.class,i);
		}
		public List<TerminalNode> KW_WHEN() { return getTokens(vhdlParser.KW_WHEN); }
		public TerminalNode KW_WHEN(int i) {
			return getToken(vhdlParser.KW_WHEN, i);
		}
		public List<ChoicesContext> choices() {
			return getRuleContexts(ChoicesContext.class);
		}
		public ChoicesContext choices(int i) {
			return getRuleContext(ChoicesContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(vhdlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(vhdlParser.COMMA, i);
		}
		public Selected_waveformsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_selected_waveforms; }
	}

	public final Selected_waveformsContext selected_waveforms() throws RecognitionException {
		Selected_waveformsContext _localctx = new Selected_waveformsContext(_ctx, getState());
		enterRule(_localctx, 404, RULE_selected_waveforms);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2076);
			waveform();
			setState(2077);
			match(KW_WHEN);
			setState(2078);
			choices();
			setState(2086);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(2079);
				match(COMMA);
				setState(2080);
				waveform();
				setState(2081);
				match(KW_WHEN);
				setState(2082);
				choices();
				}
				}
				setState(2088);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Selected_force_assignmentContext extends ParserRuleContext {
		public TerminalNode KW_WITH() { return getToken(vhdlParser.KW_WITH, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode KW_SELECT() { return getToken(vhdlParser.KW_SELECT, 0); }
		public TargetContext target() {
			return getRuleContext(TargetContext.class,0);
		}
		public TerminalNode CONASGN() { return getToken(vhdlParser.CONASGN, 0); }
		public TerminalNode KW_FORCE() { return getToken(vhdlParser.KW_FORCE, 0); }
		public Selected_expressionsContext selected_expressions() {
			return getRuleContext(Selected_expressionsContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public TerminalNode QUESTIONMARK() { return getToken(vhdlParser.QUESTIONMARK, 0); }
		public Force_modeContext force_mode() {
			return getRuleContext(Force_modeContext.class,0);
		}
		public Selected_force_assignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_selected_force_assignment; }
	}

	public final Selected_force_assignmentContext selected_force_assignment() throws RecognitionException {
		Selected_force_assignmentContext _localctx = new Selected_force_assignmentContext(_ctx, getState());
		enterRule(_localctx, 406, RULE_selected_force_assignment);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2089);
			match(KW_WITH);
			setState(2090);
			expression(0);
			setState(2091);
			match(KW_SELECT);
			setState(2093);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==QUESTIONMARK) {
				{
				setState(2092);
				match(QUESTIONMARK);
				}
			}

			setState(2095);
			target();
			setState(2096);
			match(CONASGN);
			setState(2097);
			match(KW_FORCE);
			setState(2099);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_IN || _la==KW_OUT) {
				{
				setState(2098);
				force_mode();
				}
			}

			setState(2101);
			selected_expressions();
			setState(2102);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Selected_expressionsContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> KW_WHEN() { return getTokens(vhdlParser.KW_WHEN); }
		public TerminalNode KW_WHEN(int i) {
			return getToken(vhdlParser.KW_WHEN, i);
		}
		public List<ChoicesContext> choices() {
			return getRuleContexts(ChoicesContext.class);
		}
		public ChoicesContext choices(int i) {
			return getRuleContext(ChoicesContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(vhdlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(vhdlParser.COMMA, i);
		}
		public Selected_expressionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_selected_expressions; }
	}

	public final Selected_expressionsContext selected_expressions() throws RecognitionException {
		Selected_expressionsContext _localctx = new Selected_expressionsContext(_ctx, getState());
		enterRule(_localctx, 408, RULE_selected_expressions);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2104);
			expression(0);
			setState(2105);
			match(KW_WHEN);
			setState(2106);
			choices();
			setState(2114);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(2107);
				match(COMMA);
				setState(2108);
				expression(0);
				setState(2109);
				match(KW_WHEN);
				setState(2110);
				choices();
				}
				}
				setState(2116);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Variable_assignment_statementContext extends ParserRuleContext {
		public Simple_variable_assignmentContext simple_variable_assignment() {
			return getRuleContext(Simple_variable_assignmentContext.class,0);
		}
		public Conditional_variable_assignmentContext conditional_variable_assignment() {
			return getRuleContext(Conditional_variable_assignmentContext.class,0);
		}
		public Selected_variable_assignmentContext selected_variable_assignment() {
			return getRuleContext(Selected_variable_assignmentContext.class,0);
		}
		public Variable_assignment_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable_assignment_statement; }
	}

	public final Variable_assignment_statementContext variable_assignment_statement() throws RecognitionException {
		Variable_assignment_statementContext _localctx = new Variable_assignment_statementContext(_ctx, getState());
		enterRule(_localctx, 410, RULE_variable_assignment_statement);
		try {
			setState(2120);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,220,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(2117);
				simple_variable_assignment();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(2118);
				conditional_variable_assignment();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(2119);
				selected_variable_assignment();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Simple_variable_assignmentContext extends ParserRuleContext {
		public TargetContext target() {
			return getRuleContext(TargetContext.class,0);
		}
		public TerminalNode VARASGN() { return getToken(vhdlParser.VARASGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public Simple_variable_assignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_simple_variable_assignment; }
	}

	public final Simple_variable_assignmentContext simple_variable_assignment() throws RecognitionException {
		Simple_variable_assignmentContext _localctx = new Simple_variable_assignmentContext(_ctx, getState());
		enterRule(_localctx, 412, RULE_simple_variable_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2122);
			target();
			setState(2123);
			match(VARASGN);
			setState(2124);
			expression(0);
			setState(2125);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Conditional_variable_assignmentContext extends ParserRuleContext {
		public TargetContext target() {
			return getRuleContext(TargetContext.class,0);
		}
		public TerminalNode VARASGN() { return getToken(vhdlParser.VARASGN, 0); }
		public Conditional_expressionsContext conditional_expressions() {
			return getRuleContext(Conditional_expressionsContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public Conditional_variable_assignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_conditional_variable_assignment; }
	}

	public final Conditional_variable_assignmentContext conditional_variable_assignment() throws RecognitionException {
		Conditional_variable_assignmentContext _localctx = new Conditional_variable_assignmentContext(_ctx, getState());
		enterRule(_localctx, 414, RULE_conditional_variable_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2127);
			target();
			setState(2128);
			match(VARASGN);
			setState(2129);
			conditional_expressions();
			setState(2130);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Selected_variable_assignmentContext extends ParserRuleContext {
		public TerminalNode KW_WITH() { return getToken(vhdlParser.KW_WITH, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode KW_SELECT() { return getToken(vhdlParser.KW_SELECT, 0); }
		public TargetContext target() {
			return getRuleContext(TargetContext.class,0);
		}
		public TerminalNode VARASGN() { return getToken(vhdlParser.VARASGN, 0); }
		public Selected_expressionsContext selected_expressions() {
			return getRuleContext(Selected_expressionsContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public TerminalNode QUESTIONMARK() { return getToken(vhdlParser.QUESTIONMARK, 0); }
		public Selected_variable_assignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_selected_variable_assignment; }
	}

	public final Selected_variable_assignmentContext selected_variable_assignment() throws RecognitionException {
		Selected_variable_assignmentContext _localctx = new Selected_variable_assignmentContext(_ctx, getState());
		enterRule(_localctx, 416, RULE_selected_variable_assignment);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2132);
			match(KW_WITH);
			setState(2133);
			expression(0);
			setState(2134);
			match(KW_SELECT);
			setState(2136);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==QUESTIONMARK) {
				{
				setState(2135);
				match(QUESTIONMARK);
				}
			}

			setState(2138);
			target();
			setState(2139);
			match(VARASGN);
			setState(2140);
			selected_expressions();
			setState(2141);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Procedure_call_statementContext extends ParserRuleContext {
		public Procedure_callContext procedure_call() {
			return getRuleContext(Procedure_callContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public Procedure_call_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_procedure_call_statement; }
	}

	public final Procedure_call_statementContext procedure_call_statement() throws RecognitionException {
		Procedure_call_statementContext _localctx = new Procedure_call_statementContext(_ctx, getState());
		enterRule(_localctx, 418, RULE_procedure_call_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2143);
			procedure_call();
			setState(2144);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Procedure_callContext extends ParserRuleContext {
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public Procedure_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_procedure_call; }
	}

	public final Procedure_callContext procedure_call() throws RecognitionException {
		Procedure_callContext _localctx = new Procedure_callContext(_ctx, getState());
		enterRule(_localctx, 420, RULE_procedure_call);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2146);
			name(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class If_statementContext extends ParserRuleContext {
		public List<TerminalNode> KW_IF() { return getTokens(vhdlParser.KW_IF); }
		public TerminalNode KW_IF(int i) {
			return getToken(vhdlParser.KW_IF, i);
		}
		public List<ConditionContext> condition() {
			return getRuleContexts(ConditionContext.class);
		}
		public ConditionContext condition(int i) {
			return getRuleContext(ConditionContext.class,i);
		}
		public List<TerminalNode> KW_THEN() { return getTokens(vhdlParser.KW_THEN); }
		public TerminalNode KW_THEN(int i) {
			return getToken(vhdlParser.KW_THEN, i);
		}
		public List<Sequence_of_statementsContext> sequence_of_statements() {
			return getRuleContexts(Sequence_of_statementsContext.class);
		}
		public Sequence_of_statementsContext sequence_of_statements(int i) {
			return getRuleContext(Sequence_of_statementsContext.class,i);
		}
		public TerminalNode KW_END() { return getToken(vhdlParser.KW_END, 0); }
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public TerminalNode KW_ELSE() { return getToken(vhdlParser.KW_ELSE, 0); }
		public List<TerminalNode> KW_ELSIF() { return getTokens(vhdlParser.KW_ELSIF); }
		public TerminalNode KW_ELSIF(int i) {
			return getToken(vhdlParser.KW_ELSIF, i);
		}
		public LabelContext label() {
			return getRuleContext(LabelContext.class,0);
		}
		public If_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_statement; }
	}

	public final If_statementContext if_statement() throws RecognitionException {
		If_statementContext _localctx = new If_statementContext(_ctx, getState());
		enterRule(_localctx, 422, RULE_if_statement);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(2148);
			match(KW_IF);
			setState(2149);
			condition();
			setState(2150);
			match(KW_THEN);
			setState(2151);
			sequence_of_statements();
			setState(2159);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,222,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(2152);
					match(KW_ELSIF);
					setState(2153);
					condition();
					setState(2154);
					match(KW_THEN);
					setState(2155);
					sequence_of_statements();
					}
					} 
				}
				setState(2161);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,222,_ctx);
			}
			setState(2166);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,223,_ctx) ) {
			case 1:
				{
				setState(2162);
				match(KW_ELSE);
				setState(2163);
				sequence_of_statements();
				}
				break;
			case 2:
				{
				}
				break;
			case 3:
				{
				setState(2165);
				if (!(_input->LA(1) != KW_ELSE)) throw new FailedPredicateException(this, "_input->LA(1) != KW_ELSE");
				}
				break;
			}
			setState(2168);
			match(KW_END);
			setState(2169);
			match(KW_IF);
			setState(2171);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==BASIC_IDENTIFIER || _la==EXTENDED_IDENTIFIER) {
				{
				setState(2170);
				label();
				}
			}

			setState(2173);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Case_statementContext extends ParserRuleContext {
		public List<TerminalNode> KW_CASE() { return getTokens(vhdlParser.KW_CASE); }
		public TerminalNode KW_CASE(int i) {
			return getToken(vhdlParser.KW_CASE, i);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode KW_IS() { return getToken(vhdlParser.KW_IS, 0); }
		public TerminalNode KW_END() { return getToken(vhdlParser.KW_END, 0); }
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public List<TerminalNode> QUESTIONMARK() { return getTokens(vhdlParser.QUESTIONMARK); }
		public TerminalNode QUESTIONMARK(int i) {
			return getToken(vhdlParser.QUESTIONMARK, i);
		}
		public List<Case_statement_alternativeContext> case_statement_alternative() {
			return getRuleContexts(Case_statement_alternativeContext.class);
		}
		public Case_statement_alternativeContext case_statement_alternative(int i) {
			return getRuleContext(Case_statement_alternativeContext.class,i);
		}
		public LabelContext label() {
			return getRuleContext(LabelContext.class,0);
		}
		public Case_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_case_statement; }
	}

	public final Case_statementContext case_statement() throws RecognitionException {
		Case_statementContext _localctx = new Case_statementContext(_ctx, getState());
		enterRule(_localctx, 424, RULE_case_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2175);
			match(KW_CASE);
			setState(2177);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==QUESTIONMARK) {
				{
				setState(2176);
				match(QUESTIONMARK);
				}
			}

			setState(2179);
			expression(0);
			setState(2180);
			match(KW_IS);
			setState(2182); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(2181);
				case_statement_alternative();
				}
				}
				setState(2184); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==KW_WHEN );
			setState(2186);
			match(KW_END);
			setState(2187);
			match(KW_CASE);
			setState(2189);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==QUESTIONMARK) {
				{
				setState(2188);
				match(QUESTIONMARK);
				}
			}

			setState(2192);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==BASIC_IDENTIFIER || _la==EXTENDED_IDENTIFIER) {
				{
				setState(2191);
				label();
				}
			}

			setState(2194);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Case_statement_alternativeContext extends ParserRuleContext {
		public TerminalNode KW_WHEN() { return getToken(vhdlParser.KW_WHEN, 0); }
		public ChoicesContext choices() {
			return getRuleContext(ChoicesContext.class,0);
		}
		public TerminalNode ARROW() { return getToken(vhdlParser.ARROW, 0); }
		public Sequence_of_statementsContext sequence_of_statements() {
			return getRuleContext(Sequence_of_statementsContext.class,0);
		}
		public Case_statement_alternativeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_case_statement_alternative; }
	}

	public final Case_statement_alternativeContext case_statement_alternative() throws RecognitionException {
		Case_statement_alternativeContext _localctx = new Case_statement_alternativeContext(_ctx, getState());
		enterRule(_localctx, 426, RULE_case_statement_alternative);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2196);
			match(KW_WHEN);
			setState(2197);
			choices();
			setState(2198);
			match(ARROW);
			setState(2199);
			sequence_of_statements();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Loop_statementContext extends ParserRuleContext {
		public List<TerminalNode> KW_LOOP() { return getTokens(vhdlParser.KW_LOOP); }
		public TerminalNode KW_LOOP(int i) {
			return getToken(vhdlParser.KW_LOOP, i);
		}
		public Sequence_of_statementsContext sequence_of_statements() {
			return getRuleContext(Sequence_of_statementsContext.class,0);
		}
		public TerminalNode KW_END() { return getToken(vhdlParser.KW_END, 0); }
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public Iteration_schemeContext iteration_scheme() {
			return getRuleContext(Iteration_schemeContext.class,0);
		}
		public LabelContext label() {
			return getRuleContext(LabelContext.class,0);
		}
		public Loop_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_loop_statement; }
	}

	public final Loop_statementContext loop_statement() throws RecognitionException {
		Loop_statementContext _localctx = new Loop_statementContext(_ctx, getState());
		enterRule(_localctx, 428, RULE_loop_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2202);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_WHILE || _la==KW_FOR) {
				{
				setState(2201);
				iteration_scheme();
				}
			}

			setState(2204);
			match(KW_LOOP);
			setState(2205);
			sequence_of_statements();
			setState(2206);
			match(KW_END);
			setState(2207);
			match(KW_LOOP);
			setState(2209);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==BASIC_IDENTIFIER || _la==EXTENDED_IDENTIFIER) {
				{
				setState(2208);
				label();
				}
			}

			setState(2211);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Iteration_schemeContext extends ParserRuleContext {
		public TerminalNode KW_WHILE() { return getToken(vhdlParser.KW_WHILE, 0); }
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public TerminalNode KW_FOR() { return getToken(vhdlParser.KW_FOR, 0); }
		public Parameter_specificationContext parameter_specification() {
			return getRuleContext(Parameter_specificationContext.class,0);
		}
		public Iteration_schemeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_iteration_scheme; }
	}

	public final Iteration_schemeContext iteration_scheme() throws RecognitionException {
		Iteration_schemeContext _localctx = new Iteration_schemeContext(_ctx, getState());
		enterRule(_localctx, 430, RULE_iteration_scheme);
		try {
			setState(2217);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KW_WHILE:
				enterOuterAlt(_localctx, 1);
				{
				setState(2213);
				match(KW_WHILE);
				setState(2214);
				condition();
				}
				break;
			case KW_FOR:
				enterOuterAlt(_localctx, 2);
				{
				setState(2215);
				match(KW_FOR);
				setState(2216);
				parameter_specification();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Parameter_specificationContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode KW_IN() { return getToken(vhdlParser.KW_IN, 0); }
		public Discrete_rangeContext discrete_range() {
			return getRuleContext(Discrete_rangeContext.class,0);
		}
		public Parameter_specificationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameter_specification; }
	}

	public final Parameter_specificationContext parameter_specification() throws RecognitionException {
		Parameter_specificationContext _localctx = new Parameter_specificationContext(_ctx, getState());
		enterRule(_localctx, 432, RULE_parameter_specification);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2219);
			identifier();
			setState(2220);
			match(KW_IN);
			setState(2221);
			discrete_range();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Next_statementContext extends ParserRuleContext {
		public TerminalNode KW_NEXT() { return getToken(vhdlParser.KW_NEXT, 0); }
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public LabelContext label() {
			return getRuleContext(LabelContext.class,0);
		}
		public TerminalNode KW_WHEN() { return getToken(vhdlParser.KW_WHEN, 0); }
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public Next_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_next_statement; }
	}

	public final Next_statementContext next_statement() throws RecognitionException {
		Next_statementContext _localctx = new Next_statementContext(_ctx, getState());
		enterRule(_localctx, 434, RULE_next_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2223);
			match(KW_NEXT);
			setState(2225);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==BASIC_IDENTIFIER || _la==EXTENDED_IDENTIFIER) {
				{
				setState(2224);
				label();
				}
			}

			setState(2229);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_WHEN) {
				{
				setState(2227);
				match(KW_WHEN);
				setState(2228);
				condition();
				}
			}

			setState(2231);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Exit_statementContext extends ParserRuleContext {
		public TerminalNode KW_EXIT() { return getToken(vhdlParser.KW_EXIT, 0); }
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public LabelContext label() {
			return getRuleContext(LabelContext.class,0);
		}
		public TerminalNode KW_WHEN() { return getToken(vhdlParser.KW_WHEN, 0); }
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public Exit_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exit_statement; }
	}

	public final Exit_statementContext exit_statement() throws RecognitionException {
		Exit_statementContext _localctx = new Exit_statementContext(_ctx, getState());
		enterRule(_localctx, 436, RULE_exit_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2233);
			match(KW_EXIT);
			setState(2235);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==BASIC_IDENTIFIER || _la==EXTENDED_IDENTIFIER) {
				{
				setState(2234);
				label();
				}
			}

			setState(2239);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_WHEN) {
				{
				setState(2237);
				match(KW_WHEN);
				setState(2238);
				condition();
				}
			}

			setState(2241);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Return_statementContext extends ParserRuleContext {
		public TerminalNode KW_RETURN() { return getToken(vhdlParser.KW_RETURN, 0); }
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Return_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_statement; }
	}

	public final Return_statementContext return_statement() throws RecognitionException {
		Return_statementContext _localctx = new Return_statementContext(_ctx, getState());
		enterRule(_localctx, 438, RULE_return_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2243);
			match(KW_RETURN);
			setState(2245);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << KW_ABS) | (1L << KW_XNOR) | (1L << KW_XOR) | (1L << KW_NEW) | (1L << KW_OR))) != 0) || ((((_la - 67)) & ~0x3f) == 0 && ((1L << (_la - 67)) & ((1L << (KW_NOR - 67)) | (1L << (KW_AND - 67)) | (1L << (KW_NAND - 67)) | (1L << (KW_NOT - 67)) | (1L << (KW_NULL - 67)) | (1L << (BASIC_IDENTIFIER - 67)) | (1L << (EXTENDED_IDENTIFIER - 67)) | (1L << (DECIMAL_LITERAL - 67)) | (1L << (BASED_LITERAL - 67)) | (1L << (CHARACTER_LITERAL - 67)) | (1L << (STRING_LITERAL - 67)) | (1L << (BIT_STRING_LITERAL - 67)) | (1L << (LPAREN - 67)))) != 0) || ((((_la - 132)) & ~0x3f) == 0 && ((1L << (_la - 132)) & ((1L << (SHIFT_LEFT - 132)) | (1L << (PLUS - 132)) | (1L << (MINUS - 132)) | (1L << (COND_OP - 132)))) != 0)) {
				{
				setState(2244);
				expression(0);
				}
			}

			setState(2247);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Null_statementContext extends ParserRuleContext {
		public TerminalNode KW_NULL() { return getToken(vhdlParser.KW_NULL, 0); }
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public Null_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_null_statement; }
	}

	public final Null_statementContext null_statement() throws RecognitionException {
		Null_statementContext _localctx = new Null_statementContext(_ctx, getState());
		enterRule(_localctx, 440, RULE_null_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2249);
			match(KW_NULL);
			setState(2250);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Concurrent_statement_with_optional_labelContext extends ParserRuleContext {
		public Process_statementContext process_statement() {
			return getRuleContext(Process_statementContext.class,0);
		}
		public Concurrent_procedure_call_statementContext concurrent_procedure_call_statement() {
			return getRuleContext(Concurrent_procedure_call_statementContext.class,0);
		}
		public Concurrent_assertion_statementContext concurrent_assertion_statement() {
			return getRuleContext(Concurrent_assertion_statementContext.class,0);
		}
		public Concurrent_signal_assignment_statementContext concurrent_signal_assignment_statement() {
			return getRuleContext(Concurrent_signal_assignment_statementContext.class,0);
		}
		public Concurrent_statement_with_optional_labelContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_concurrent_statement_with_optional_label; }
	}

	public final Concurrent_statement_with_optional_labelContext concurrent_statement_with_optional_label() throws RecognitionException {
		Concurrent_statement_with_optional_labelContext _localctx = new Concurrent_statement_with_optional_labelContext(_ctx, getState());
		enterRule(_localctx, 442, RULE_concurrent_statement_with_optional_label);
		try {
			setState(2256);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,237,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(2252);
				process_statement();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(2253);
				concurrent_procedure_call_statement();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(2254);
				concurrent_assertion_statement();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(2255);
				concurrent_signal_assignment_statement();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Concurrent_statementContext extends ParserRuleContext {
		public LabelContext label() {
			return getRuleContext(LabelContext.class,0);
		}
		public TerminalNode COLON() { return getToken(vhdlParser.COLON, 0); }
		public Block_statementContext block_statement() {
			return getRuleContext(Block_statementContext.class,0);
		}
		public Component_instantiation_statementContext component_instantiation_statement() {
			return getRuleContext(Component_instantiation_statementContext.class,0);
		}
		public Generate_statementContext generate_statement() {
			return getRuleContext(Generate_statementContext.class,0);
		}
		public Concurrent_statement_with_optional_labelContext concurrent_statement_with_optional_label() {
			return getRuleContext(Concurrent_statement_with_optional_labelContext.class,0);
		}
		public Concurrent_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_concurrent_statement; }
	}

	public final Concurrent_statementContext concurrent_statement() throws RecognitionException {
		Concurrent_statementContext _localctx = new Concurrent_statementContext(_ctx, getState());
		enterRule(_localctx, 444, RULE_concurrent_statement);
		try {
			setState(2267);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,239,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(2258);
				label();
				setState(2259);
				match(COLON);
				setState(2264);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,238,_ctx) ) {
				case 1:
					{
					setState(2260);
					block_statement();
					}
					break;
				case 2:
					{
					setState(2261);
					component_instantiation_statement();
					}
					break;
				case 3:
					{
					setState(2262);
					generate_statement();
					}
					break;
				case 4:
					{
					setState(2263);
					concurrent_statement_with_optional_label();
					}
					break;
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(2266);
				concurrent_statement_with_optional_label();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Block_statementContext extends ParserRuleContext {
		public List<TerminalNode> KW_BLOCK() { return getTokens(vhdlParser.KW_BLOCK); }
		public TerminalNode KW_BLOCK(int i) {
			return getToken(vhdlParser.KW_BLOCK, i);
		}
		public Block_headerContext block_header() {
			return getRuleContext(Block_headerContext.class,0);
		}
		public TerminalNode KW_BEGIN() { return getToken(vhdlParser.KW_BEGIN, 0); }
		public TerminalNode KW_END() { return getToken(vhdlParser.KW_END, 0); }
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public TerminalNode LPAREN() { return getToken(vhdlParser.LPAREN, 0); }
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(vhdlParser.RPAREN, 0); }
		public TerminalNode KW_IS() { return getToken(vhdlParser.KW_IS, 0); }
		public List<Block_declarative_itemContext> block_declarative_item() {
			return getRuleContexts(Block_declarative_itemContext.class);
		}
		public Block_declarative_itemContext block_declarative_item(int i) {
			return getRuleContext(Block_declarative_itemContext.class,i);
		}
		public List<Concurrent_statementContext> concurrent_statement() {
			return getRuleContexts(Concurrent_statementContext.class);
		}
		public Concurrent_statementContext concurrent_statement(int i) {
			return getRuleContext(Concurrent_statementContext.class,i);
		}
		public LabelContext label() {
			return getRuleContext(LabelContext.class,0);
		}
		public Block_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block_statement; }
	}

	public final Block_statementContext block_statement() throws RecognitionException {
		Block_statementContext _localctx = new Block_statementContext(_ctx, getState());
		enterRule(_localctx, 446, RULE_block_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2269);
			match(KW_BLOCK);
			setState(2274);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LPAREN) {
				{
				setState(2270);
				match(LPAREN);
				setState(2271);
				condition();
				setState(2272);
				match(RPAREN);
				}
			}

			setState(2277);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_IS) {
				{
				setState(2276);
				match(KW_IS);
				}
			}

			setState(2279);
			block_header();
			setState(2283);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << KW_COMPONENT) | (1L << KW_GROUP) | (1L << KW_FILE) | (1L << KW_PURE) | (1L << KW_USE) | (1L << KW_SHARED) | (1L << KW_SIGNAL) | (1L << KW_DISCONNECT) | (1L << KW_PROCEDURE) | (1L << KW_ATTRIBUTE) | (1L << KW_VARIABLE) | (1L << KW_SUBTYPE) | (1L << KW_CONSTANT) | (1L << KW_FUNCTION))) != 0) || ((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & ((1L << (KW_ALIAS - 65)) | (1L << (KW_IMPURE - 65)) | (1L << (KW_PACKAGE - 65)) | (1L << (KW_FOR - 65)) | (1L << (KW_TYPE - 65)))) != 0)) {
				{
				{
				setState(2280);
				block_declarative_item();
				}
				}
				setState(2285);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(2286);
			match(KW_BEGIN);
			setState(2290);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==KW_PROCESS || _la==KW_POSTPONED || ((((_la - 72)) & ~0x3f) == 0 && ((1L << (_la - 72)) & ((1L << (KW_WITH - 72)) | (1L << (KW_ASSERT - 72)) | (1L << (BASIC_IDENTIFIER - 72)) | (1L << (EXTENDED_IDENTIFIER - 72)) | (1L << (CHARACTER_LITERAL - 72)) | (1L << (STRING_LITERAL - 72)) | (1L << (LPAREN - 72)) | (1L << (SHIFT_LEFT - 72)))) != 0)) {
				{
				{
				setState(2287);
				concurrent_statement();
				}
				}
				setState(2292);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(2293);
			match(KW_END);
			setState(2294);
			match(KW_BLOCK);
			setState(2296);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==BASIC_IDENTIFIER || _la==EXTENDED_IDENTIFIER) {
				{
				setState(2295);
				label();
				}
			}

			setState(2298);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Block_headerContext extends ParserRuleContext {
		public Generic_clauseContext generic_clause() {
			return getRuleContext(Generic_clauseContext.class,0);
		}
		public Port_clauseContext port_clause() {
			return getRuleContext(Port_clauseContext.class,0);
		}
		public Generic_map_aspectContext generic_map_aspect() {
			return getRuleContext(Generic_map_aspectContext.class,0);
		}
		public List<TerminalNode> SEMI() { return getTokens(vhdlParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(vhdlParser.SEMI, i);
		}
		public Port_map_aspectContext port_map_aspect() {
			return getRuleContext(Port_map_aspectContext.class,0);
		}
		public Block_headerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block_header; }
	}

	public final Block_headerContext block_header() throws RecognitionException {
		Block_headerContext _localctx = new Block_headerContext(_ctx, getState());
		enterRule(_localctx, 448, RULE_block_header);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2306);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_GENERIC) {
				{
				setState(2300);
				generic_clause();
				setState(2304);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==KW_GENERIC) {
					{
					setState(2301);
					generic_map_aspect();
					setState(2302);
					match(SEMI);
					}
				}

				}
			}

			setState(2314);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_PORT) {
				{
				setState(2308);
				port_clause();
				setState(2312);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==KW_PORT) {
					{
					setState(2309);
					port_map_aspect();
					setState(2310);
					match(SEMI);
					}
				}

				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Process_statementContext extends ParserRuleContext {
		public List<TerminalNode> KW_PROCESS() { return getTokens(vhdlParser.KW_PROCESS); }
		public TerminalNode KW_PROCESS(int i) {
			return getToken(vhdlParser.KW_PROCESS, i);
		}
		public TerminalNode KW_BEGIN() { return getToken(vhdlParser.KW_BEGIN, 0); }
		public TerminalNode KW_END() { return getToken(vhdlParser.KW_END, 0); }
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public List<TerminalNode> KW_POSTPONED() { return getTokens(vhdlParser.KW_POSTPONED); }
		public TerminalNode KW_POSTPONED(int i) {
			return getToken(vhdlParser.KW_POSTPONED, i);
		}
		public TerminalNode LPAREN() { return getToken(vhdlParser.LPAREN, 0); }
		public Process_sensitivity_listContext process_sensitivity_list() {
			return getRuleContext(Process_sensitivity_listContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(vhdlParser.RPAREN, 0); }
		public TerminalNode KW_IS() { return getToken(vhdlParser.KW_IS, 0); }
		public List<Process_declarative_itemContext> process_declarative_item() {
			return getRuleContexts(Process_declarative_itemContext.class);
		}
		public Process_declarative_itemContext process_declarative_item(int i) {
			return getRuleContext(Process_declarative_itemContext.class,i);
		}
		public List<Sequential_statementContext> sequential_statement() {
			return getRuleContexts(Sequential_statementContext.class);
		}
		public Sequential_statementContext sequential_statement(int i) {
			return getRuleContext(Sequential_statementContext.class,i);
		}
		public LabelContext label() {
			return getRuleContext(LabelContext.class,0);
		}
		public Process_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_process_statement; }
	}

	public final Process_statementContext process_statement() throws RecognitionException {
		Process_statementContext _localctx = new Process_statementContext(_ctx, getState());
		enterRule(_localctx, 450, RULE_process_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2317);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_POSTPONED) {
				{
				setState(2316);
				match(KW_POSTPONED);
				}
			}

			setState(2319);
			match(KW_PROCESS);
			setState(2324);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LPAREN) {
				{
				setState(2320);
				match(LPAREN);
				setState(2321);
				process_sensitivity_list();
				setState(2322);
				match(RPAREN);
				}
			}

			setState(2327);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_IS) {
				{
				setState(2326);
				match(KW_IS);
				}
			}

			setState(2332);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << KW_GROUP) | (1L << KW_FILE) | (1L << KW_PURE) | (1L << KW_USE) | (1L << KW_SHARED) | (1L << KW_PROCEDURE) | (1L << KW_ATTRIBUTE) | (1L << KW_VARIABLE) | (1L << KW_SUBTYPE) | (1L << KW_CONSTANT) | (1L << KW_FUNCTION))) != 0) || ((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & ((1L << (KW_ALIAS - 65)) | (1L << (KW_IMPURE - 65)) | (1L << (KW_PACKAGE - 65)) | (1L << (KW_TYPE - 65)))) != 0)) {
				{
				{
				setState(2329);
				process_declarative_item();
				}
				}
				setState(2334);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(2335);
			match(KW_BEGIN);
			setState(2339);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << KW_NEXT) | (1L << KW_LOOP) | (1L << KW_REPORT))) != 0) || ((((_la - 70)) & ~0x3f) == 0 && ((1L << (_la - 70)) & ((1L << (KW_EXIT - 70)) | (1L << (KW_RETURN - 70)) | (1L << (KW_WITH - 70)) | (1L << (KW_WAIT - 70)) | (1L << (KW_WHILE - 70)) | (1L << (KW_ASSERT - 70)) | (1L << (KW_FOR - 70)) | (1L << (KW_IF - 70)) | (1L << (KW_CASE - 70)) | (1L << (KW_NULL - 70)) | (1L << (BASIC_IDENTIFIER - 70)) | (1L << (EXTENDED_IDENTIFIER - 70)) | (1L << (CHARACTER_LITERAL - 70)) | (1L << (STRING_LITERAL - 70)) | (1L << (LPAREN - 70)) | (1L << (SHIFT_LEFT - 70)))) != 0)) {
				{
				{
				setState(2336);
				sequential_statement();
				}
				}
				setState(2341);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(2342);
			match(KW_END);
			setState(2344);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_POSTPONED) {
				{
				setState(2343);
				match(KW_POSTPONED);
				}
			}

			setState(2346);
			match(KW_PROCESS);
			setState(2348);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==BASIC_IDENTIFIER || _la==EXTENDED_IDENTIFIER) {
				{
				setState(2347);
				label();
				}
			}

			setState(2350);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Process_sensitivity_listContext extends ParserRuleContext {
		public TerminalNode KW_ALL() { return getToken(vhdlParser.KW_ALL, 0); }
		public Sensitivity_listContext sensitivity_list() {
			return getRuleContext(Sensitivity_listContext.class,0);
		}
		public Process_sensitivity_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_process_sensitivity_list; }
	}

	public final Process_sensitivity_listContext process_sensitivity_list() throws RecognitionException {
		Process_sensitivity_listContext _localctx = new Process_sensitivity_listContext(_ctx, getState());
		enterRule(_localctx, 452, RULE_process_sensitivity_list);
		try {
			setState(2354);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KW_ALL:
				enterOuterAlt(_localctx, 1);
				{
				setState(2352);
				match(KW_ALL);
				}
				break;
			case BASIC_IDENTIFIER:
			case EXTENDED_IDENTIFIER:
			case CHARACTER_LITERAL:
			case STRING_LITERAL:
			case SHIFT_LEFT:
				enterOuterAlt(_localctx, 2);
				{
				setState(2353);
				sensitivity_list();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Process_or_package_declarative_itemContext extends ParserRuleContext {
		public Subprogram_declarationContext subprogram_declaration() {
			return getRuleContext(Subprogram_declarationContext.class,0);
		}
		public Subprogram_instantiation_declarationContext subprogram_instantiation_declaration() {
			return getRuleContext(Subprogram_instantiation_declarationContext.class,0);
		}
		public Package_declarationContext package_declaration() {
			return getRuleContext(Package_declarationContext.class,0);
		}
		public Package_instantiation_declarationContext package_instantiation_declaration() {
			return getRuleContext(Package_instantiation_declarationContext.class,0);
		}
		public Type_declarationContext type_declaration() {
			return getRuleContext(Type_declarationContext.class,0);
		}
		public Subtype_declarationContext subtype_declaration() {
			return getRuleContext(Subtype_declarationContext.class,0);
		}
		public Constant_declarationContext constant_declaration() {
			return getRuleContext(Constant_declarationContext.class,0);
		}
		public Variable_declarationContext variable_declaration() {
			return getRuleContext(Variable_declarationContext.class,0);
		}
		public File_declarationContext file_declaration() {
			return getRuleContext(File_declarationContext.class,0);
		}
		public Alias_declarationContext alias_declaration() {
			return getRuleContext(Alias_declarationContext.class,0);
		}
		public Attribute_declarationContext attribute_declaration() {
			return getRuleContext(Attribute_declarationContext.class,0);
		}
		public Attribute_specificationContext attribute_specification() {
			return getRuleContext(Attribute_specificationContext.class,0);
		}
		public Use_clauseContext use_clause() {
			return getRuleContext(Use_clauseContext.class,0);
		}
		public Group_template_declarationContext group_template_declaration() {
			return getRuleContext(Group_template_declarationContext.class,0);
		}
		public Group_declarationContext group_declaration() {
			return getRuleContext(Group_declarationContext.class,0);
		}
		public Process_or_package_declarative_itemContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_process_or_package_declarative_item; }
	}

	public final Process_or_package_declarative_itemContext process_or_package_declarative_item() throws RecognitionException {
		Process_or_package_declarative_itemContext _localctx = new Process_or_package_declarative_itemContext(_ctx, getState());
		enterRule(_localctx, 454, RULE_process_or_package_declarative_item);
		try {
			setState(2371);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,257,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(2356);
				subprogram_declaration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(2357);
				subprogram_instantiation_declaration();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(2358);
				package_declaration();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(2359);
				package_instantiation_declaration();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(2360);
				type_declaration();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(2361);
				subtype_declaration();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(2362);
				constant_declaration();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(2363);
				variable_declaration();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(2364);
				file_declaration();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(2365);
				alias_declaration();
				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(2366);
				attribute_declaration();
				}
				break;
			case 12:
				enterOuterAlt(_localctx, 12);
				{
				setState(2367);
				attribute_specification();
				}
				break;
			case 13:
				enterOuterAlt(_localctx, 13);
				{
				setState(2368);
				use_clause();
				}
				break;
			case 14:
				enterOuterAlt(_localctx, 14);
				{
				setState(2369);
				group_template_declaration();
				}
				break;
			case 15:
				enterOuterAlt(_localctx, 15);
				{
				setState(2370);
				group_declaration();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Process_declarative_itemContext extends ParserRuleContext {
		public Process_or_package_declarative_itemContext process_or_package_declarative_item() {
			return getRuleContext(Process_or_package_declarative_itemContext.class,0);
		}
		public Subprogram_bodyContext subprogram_body() {
			return getRuleContext(Subprogram_bodyContext.class,0);
		}
		public Package_bodyContext package_body() {
			return getRuleContext(Package_bodyContext.class,0);
		}
		public Process_declarative_itemContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_process_declarative_item; }
	}

	public final Process_declarative_itemContext process_declarative_item() throws RecognitionException {
		Process_declarative_itemContext _localctx = new Process_declarative_itemContext(_ctx, getState());
		enterRule(_localctx, 456, RULE_process_declarative_item);
		try {
			setState(2376);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,258,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(2373);
				process_or_package_declarative_item();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(2374);
				subprogram_body();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(2375);
				package_body();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Concurrent_procedure_call_statementContext extends ParserRuleContext {
		public Procedure_call_statementContext procedure_call_statement() {
			return getRuleContext(Procedure_call_statementContext.class,0);
		}
		public TerminalNode KW_POSTPONED() { return getToken(vhdlParser.KW_POSTPONED, 0); }
		public Concurrent_procedure_call_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_concurrent_procedure_call_statement; }
	}

	public final Concurrent_procedure_call_statementContext concurrent_procedure_call_statement() throws RecognitionException {
		Concurrent_procedure_call_statementContext _localctx = new Concurrent_procedure_call_statementContext(_ctx, getState());
		enterRule(_localctx, 458, RULE_concurrent_procedure_call_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2379);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_POSTPONED) {
				{
				setState(2378);
				match(KW_POSTPONED);
				}
			}

			setState(2381);
			procedure_call_statement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Concurrent_assertion_statementContext extends ParserRuleContext {
		public Assertion_statementContext assertion_statement() {
			return getRuleContext(Assertion_statementContext.class,0);
		}
		public TerminalNode KW_POSTPONED() { return getToken(vhdlParser.KW_POSTPONED, 0); }
		public Concurrent_assertion_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_concurrent_assertion_statement; }
	}

	public final Concurrent_assertion_statementContext concurrent_assertion_statement() throws RecognitionException {
		Concurrent_assertion_statementContext _localctx = new Concurrent_assertion_statementContext(_ctx, getState());
		enterRule(_localctx, 460, RULE_concurrent_assertion_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2384);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_POSTPONED) {
				{
				setState(2383);
				match(KW_POSTPONED);
				}
			}

			setState(2386);
			assertion_statement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Concurrent_signal_assignment_statementContext extends ParserRuleContext {
		public Concurrent_signal_assignment_anyContext concurrent_signal_assignment_any() {
			return getRuleContext(Concurrent_signal_assignment_anyContext.class,0);
		}
		public Concurrent_selected_signal_assignmentContext concurrent_selected_signal_assignment() {
			return getRuleContext(Concurrent_selected_signal_assignmentContext.class,0);
		}
		public TerminalNode KW_POSTPONED() { return getToken(vhdlParser.KW_POSTPONED, 0); }
		public Concurrent_signal_assignment_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_concurrent_signal_assignment_statement; }
	}

	public final Concurrent_signal_assignment_statementContext concurrent_signal_assignment_statement() throws RecognitionException {
		Concurrent_signal_assignment_statementContext _localctx = new Concurrent_signal_assignment_statementContext(_ctx, getState());
		enterRule(_localctx, 462, RULE_concurrent_signal_assignment_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2389);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_POSTPONED) {
				{
				setState(2388);
				match(KW_POSTPONED);
				}
			}

			setState(2393);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BASIC_IDENTIFIER:
			case EXTENDED_IDENTIFIER:
			case CHARACTER_LITERAL:
			case STRING_LITERAL:
			case LPAREN:
			case SHIFT_LEFT:
				{
				setState(2391);
				concurrent_signal_assignment_any();
				}
				break;
			case KW_WITH:
				{
				setState(2392);
				concurrent_selected_signal_assignment();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Concurrent_signal_assignment_anyContext extends ParserRuleContext {
		public TargetContext target() {
			return getRuleContext(TargetContext.class,0);
		}
		public TerminalNode CONASGN() { return getToken(vhdlParser.CONASGN, 0); }
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public WaveformContext waveform() {
			return getRuleContext(WaveformContext.class,0);
		}
		public Conditional_waveformsContext conditional_waveforms() {
			return getRuleContext(Conditional_waveformsContext.class,0);
		}
		public TerminalNode KW_GUARDED() { return getToken(vhdlParser.KW_GUARDED, 0); }
		public Delay_mechanismContext delay_mechanism() {
			return getRuleContext(Delay_mechanismContext.class,0);
		}
		public Concurrent_signal_assignment_anyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_concurrent_signal_assignment_any; }
	}

	public final Concurrent_signal_assignment_anyContext concurrent_signal_assignment_any() throws RecognitionException {
		Concurrent_signal_assignment_anyContext _localctx = new Concurrent_signal_assignment_anyContext(_ctx, getState());
		enterRule(_localctx, 464, RULE_concurrent_signal_assignment_any);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2395);
			target();
			setState(2396);
			match(CONASGN);
			setState(2398);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_GUARDED) {
				{
				setState(2397);
				match(KW_GUARDED);
				}
			}

			setState(2401);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << KW_INERTIAL) | (1L << KW_REJECT) | (1L << KW_TRANSPORT))) != 0)) {
				{
				setState(2400);
				delay_mechanism();
				}
			}

			setState(2405);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,265,_ctx) ) {
			case 1:
				{
				setState(2403);
				waveform();
				}
				break;
			case 2:
				{
				setState(2404);
				conditional_waveforms();
				}
				break;
			}
			setState(2407);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Concurrent_selected_signal_assignmentContext extends ParserRuleContext {
		public TerminalNode KW_WITH() { return getToken(vhdlParser.KW_WITH, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode KW_SELECT() { return getToken(vhdlParser.KW_SELECT, 0); }
		public TargetContext target() {
			return getRuleContext(TargetContext.class,0);
		}
		public TerminalNode CONASGN() { return getToken(vhdlParser.CONASGN, 0); }
		public Selected_waveformsContext selected_waveforms() {
			return getRuleContext(Selected_waveformsContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public TerminalNode QUESTIONMARK() { return getToken(vhdlParser.QUESTIONMARK, 0); }
		public TerminalNode KW_GUARDED() { return getToken(vhdlParser.KW_GUARDED, 0); }
		public Delay_mechanismContext delay_mechanism() {
			return getRuleContext(Delay_mechanismContext.class,0);
		}
		public Concurrent_selected_signal_assignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_concurrent_selected_signal_assignment; }
	}

	public final Concurrent_selected_signal_assignmentContext concurrent_selected_signal_assignment() throws RecognitionException {
		Concurrent_selected_signal_assignmentContext _localctx = new Concurrent_selected_signal_assignmentContext(_ctx, getState());
		enterRule(_localctx, 466, RULE_concurrent_selected_signal_assignment);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2409);
			match(KW_WITH);
			setState(2410);
			expression(0);
			setState(2411);
			match(KW_SELECT);
			setState(2413);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==QUESTIONMARK) {
				{
				setState(2412);
				match(QUESTIONMARK);
				}
			}

			setState(2415);
			target();
			setState(2416);
			match(CONASGN);
			setState(2418);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_GUARDED) {
				{
				setState(2417);
				match(KW_GUARDED);
				}
			}

			setState(2421);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << KW_INERTIAL) | (1L << KW_REJECT) | (1L << KW_TRANSPORT))) != 0)) {
				{
				setState(2420);
				delay_mechanism();
				}
			}

			setState(2423);
			selected_waveforms();
			setState(2424);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Component_instantiation_statementContext extends ParserRuleContext {
		public Instantiated_unitContext instantiated_unit() {
			return getRuleContext(Instantiated_unitContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public Generic_map_aspectContext generic_map_aspect() {
			return getRuleContext(Generic_map_aspectContext.class,0);
		}
		public Port_map_aspectContext port_map_aspect() {
			return getRuleContext(Port_map_aspectContext.class,0);
		}
		public Component_instantiation_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_component_instantiation_statement; }
	}

	public final Component_instantiation_statementContext component_instantiation_statement() throws RecognitionException {
		Component_instantiation_statementContext _localctx = new Component_instantiation_statementContext(_ctx, getState());
		enterRule(_localctx, 468, RULE_component_instantiation_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2426);
			instantiated_unit();
			setState(2428);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_GENERIC) {
				{
				setState(2427);
				generic_map_aspect();
				}
			}

			setState(2431);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_PORT) {
				{
				setState(2430);
				port_map_aspect();
				}
			}

			setState(2433);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Instantiated_unitContext extends ParserRuleContext {
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public TerminalNode KW_COMPONENT() { return getToken(vhdlParser.KW_COMPONENT, 0); }
		public TerminalNode KW_ENTITY() { return getToken(vhdlParser.KW_ENTITY, 0); }
		public TerminalNode LPAREN() { return getToken(vhdlParser.LPAREN, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(vhdlParser.RPAREN, 0); }
		public TerminalNode KW_CONFIGURATION() { return getToken(vhdlParser.KW_CONFIGURATION, 0); }
		public Instantiated_unitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instantiated_unit; }
	}

	public final Instantiated_unitContext instantiated_unit() throws RecognitionException {
		Instantiated_unitContext _localctx = new Instantiated_unitContext(_ctx, getState());
		enterRule(_localctx, 470, RULE_instantiated_unit);
		int _la;
		try {
			setState(2449);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KW_COMPONENT:
			case BASIC_IDENTIFIER:
			case EXTENDED_IDENTIFIER:
			case CHARACTER_LITERAL:
			case STRING_LITERAL:
			case SHIFT_LEFT:
				enterOuterAlt(_localctx, 1);
				{
				setState(2436);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==KW_COMPONENT) {
					{
					setState(2435);
					match(KW_COMPONENT);
					}
				}

				setState(2438);
				name(0);
				}
				break;
			case KW_ENTITY:
				enterOuterAlt(_localctx, 2);
				{
				setState(2439);
				match(KW_ENTITY);
				setState(2440);
				name(0);
				setState(2445);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==LPAREN) {
					{
					setState(2441);
					match(LPAREN);
					setState(2442);
					identifier();
					setState(2443);
					match(RPAREN);
					}
				}

				}
				break;
			case KW_CONFIGURATION:
				enterOuterAlt(_localctx, 3);
				{
				setState(2447);
				match(KW_CONFIGURATION);
				setState(2448);
				name(0);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Generate_statementContext extends ParserRuleContext {
		public For_generate_statementContext for_generate_statement() {
			return getRuleContext(For_generate_statementContext.class,0);
		}
		public If_generate_statementContext if_generate_statement() {
			return getRuleContext(If_generate_statementContext.class,0);
		}
		public Case_generate_statementContext case_generate_statement() {
			return getRuleContext(Case_generate_statementContext.class,0);
		}
		public Generate_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_generate_statement; }
	}

	public final Generate_statementContext generate_statement() throws RecognitionException {
		Generate_statementContext _localctx = new Generate_statementContext(_ctx, getState());
		enterRule(_localctx, 472, RULE_generate_statement);
		try {
			setState(2454);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KW_FOR:
				enterOuterAlt(_localctx, 1);
				{
				setState(2451);
				for_generate_statement();
				}
				break;
			case KW_IF:
				enterOuterAlt(_localctx, 2);
				{
				setState(2452);
				if_generate_statement();
				}
				break;
			case KW_CASE:
				enterOuterAlt(_localctx, 3);
				{
				setState(2453);
				case_generate_statement();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class For_generate_statementContext extends ParserRuleContext {
		public TerminalNode KW_FOR() { return getToken(vhdlParser.KW_FOR, 0); }
		public Parameter_specificationContext parameter_specification() {
			return getRuleContext(Parameter_specificationContext.class,0);
		}
		public List<TerminalNode> KW_GENERATE() { return getTokens(vhdlParser.KW_GENERATE); }
		public TerminalNode KW_GENERATE(int i) {
			return getToken(vhdlParser.KW_GENERATE, i);
		}
		public Generate_statement_bodyContext generate_statement_body() {
			return getRuleContext(Generate_statement_bodyContext.class,0);
		}
		public TerminalNode KW_END() { return getToken(vhdlParser.KW_END, 0); }
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public LabelContext label() {
			return getRuleContext(LabelContext.class,0);
		}
		public For_generate_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_generate_statement; }
	}

	public final For_generate_statementContext for_generate_statement() throws RecognitionException {
		For_generate_statementContext _localctx = new For_generate_statementContext(_ctx, getState());
		enterRule(_localctx, 474, RULE_for_generate_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2456);
			match(KW_FOR);
			setState(2457);
			parameter_specification();
			setState(2458);
			match(KW_GENERATE);
			setState(2459);
			generate_statement_body();
			setState(2460);
			match(KW_END);
			setState(2461);
			match(KW_GENERATE);
			setState(2463);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==BASIC_IDENTIFIER || _la==EXTENDED_IDENTIFIER) {
				{
				setState(2462);
				label();
				}
			}

			setState(2465);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class If_generate_statementContext extends ParserRuleContext {
		public TerminalNode KW_IF() { return getToken(vhdlParser.KW_IF, 0); }
		public List<ConditionContext> condition() {
			return getRuleContexts(ConditionContext.class);
		}
		public ConditionContext condition(int i) {
			return getRuleContext(ConditionContext.class,i);
		}
		public List<TerminalNode> KW_GENERATE() { return getTokens(vhdlParser.KW_GENERATE); }
		public TerminalNode KW_GENERATE(int i) {
			return getToken(vhdlParser.KW_GENERATE, i);
		}
		public List<Generate_statement_bodyContext> generate_statement_body() {
			return getRuleContexts(Generate_statement_bodyContext.class);
		}
		public Generate_statement_bodyContext generate_statement_body(int i) {
			return getRuleContext(Generate_statement_bodyContext.class,i);
		}
		public TerminalNode KW_END() { return getToken(vhdlParser.KW_END, 0); }
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public TerminalNode KW_ELSE() { return getToken(vhdlParser.KW_ELSE, 0); }
		public List<LabelContext> label() {
			return getRuleContexts(LabelContext.class);
		}
		public LabelContext label(int i) {
			return getRuleContext(LabelContext.class,i);
		}
		public List<TerminalNode> COLON() { return getTokens(vhdlParser.COLON); }
		public TerminalNode COLON(int i) {
			return getToken(vhdlParser.COLON, i);
		}
		public List<TerminalNode> KW_ELSIF() { return getTokens(vhdlParser.KW_ELSIF); }
		public TerminalNode KW_ELSIF(int i) {
			return getToken(vhdlParser.KW_ELSIF, i);
		}
		public If_generate_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_generate_statement; }
	}

	public final If_generate_statementContext if_generate_statement() throws RecognitionException {
		If_generate_statementContext _localctx = new If_generate_statementContext(_ctx, getState());
		enterRule(_localctx, 476, RULE_if_generate_statement);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(2467);
			match(KW_IF);
			setState(2471);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,276,_ctx) ) {
			case 1:
				{
				setState(2468);
				label();
				setState(2469);
				match(COLON);
				}
				break;
			}
			setState(2473);
			condition();
			setState(2474);
			match(KW_GENERATE);
			setState(2475);
			generate_statement_body();
			setState(2488);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,278,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(2476);
					match(KW_ELSIF);
					setState(2480);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,277,_ctx) ) {
					case 1:
						{
						setState(2477);
						label();
						setState(2478);
						match(COLON);
						}
						break;
					}
					setState(2482);
					condition();
					setState(2483);
					match(KW_GENERATE);
					setState(2484);
					generate_statement_body();
					}
					} 
				}
				setState(2490);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,278,_ctx);
			}
			setState(2500);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,280,_ctx) ) {
			case 1:
				{
				setState(2491);
				match(KW_ELSE);
				setState(2495);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==BASIC_IDENTIFIER || _la==EXTENDED_IDENTIFIER) {
					{
					setState(2492);
					label();
					setState(2493);
					match(COLON);
					}
				}

				setState(2497);
				match(KW_GENERATE);
				setState(2498);
				generate_statement_body();
				}
				break;
			case 2:
				{
				setState(2499);
				if (!(_input->LA(1) != KW_ELSE)) throw new FailedPredicateException(this, "_input->LA(1) != KW_ELSE");
				}
				break;
			}
			setState(2502);
			match(KW_END);
			setState(2503);
			match(KW_GENERATE);
			setState(2505);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==BASIC_IDENTIFIER || _la==EXTENDED_IDENTIFIER) {
				{
				setState(2504);
				label();
				}
			}

			setState(2507);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Case_generate_statementContext extends ParserRuleContext {
		public TerminalNode KW_CASE() { return getToken(vhdlParser.KW_CASE, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<TerminalNode> KW_GENERATE() { return getTokens(vhdlParser.KW_GENERATE); }
		public TerminalNode KW_GENERATE(int i) {
			return getToken(vhdlParser.KW_GENERATE, i);
		}
		public TerminalNode KW_END() { return getToken(vhdlParser.KW_END, 0); }
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public List<Case_generate_alternativeContext> case_generate_alternative() {
			return getRuleContexts(Case_generate_alternativeContext.class);
		}
		public Case_generate_alternativeContext case_generate_alternative(int i) {
			return getRuleContext(Case_generate_alternativeContext.class,i);
		}
		public LabelContext label() {
			return getRuleContext(LabelContext.class,0);
		}
		public Case_generate_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_case_generate_statement; }
	}

	public final Case_generate_statementContext case_generate_statement() throws RecognitionException {
		Case_generate_statementContext _localctx = new Case_generate_statementContext(_ctx, getState());
		enterRule(_localctx, 478, RULE_case_generate_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2509);
			match(KW_CASE);
			setState(2510);
			expression(0);
			setState(2511);
			match(KW_GENERATE);
			setState(2513); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(2512);
				case_generate_alternative();
				}
				}
				setState(2515); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==KW_WHEN );
			setState(2517);
			match(KW_END);
			setState(2518);
			match(KW_GENERATE);
			setState(2520);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==BASIC_IDENTIFIER || _la==EXTENDED_IDENTIFIER) {
				{
				setState(2519);
				label();
				}
			}

			setState(2522);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Case_generate_alternativeContext extends ParserRuleContext {
		public TerminalNode KW_WHEN() { return getToken(vhdlParser.KW_WHEN, 0); }
		public ChoicesContext choices() {
			return getRuleContext(ChoicesContext.class,0);
		}
		public TerminalNode ARROW() { return getToken(vhdlParser.ARROW, 0); }
		public Generate_statement_body_with_begin_endContext generate_statement_body_with_begin_end() {
			return getRuleContext(Generate_statement_body_with_begin_endContext.class,0);
		}
		public LabelContext label() {
			return getRuleContext(LabelContext.class,0);
		}
		public TerminalNode COLON() { return getToken(vhdlParser.COLON, 0); }
		public Case_generate_alternativeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_case_generate_alternative; }
	}

	public final Case_generate_alternativeContext case_generate_alternative() throws RecognitionException {
		Case_generate_alternativeContext _localctx = new Case_generate_alternativeContext(_ctx, getState());
		enterRule(_localctx, 480, RULE_case_generate_alternative);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2524);
			match(KW_WHEN);
			setState(2528);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,284,_ctx) ) {
			case 1:
				{
				setState(2525);
				label();
				setState(2526);
				match(COLON);
				}
				break;
			}
			setState(2530);
			choices();
			setState(2531);
			match(ARROW);
			setState(2532);
			generate_statement_body_with_begin_end();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Generate_statement_body_with_begin_endContext extends ParserRuleContext {
		public TerminalNode KW_BEGIN() { return getToken(vhdlParser.KW_BEGIN, 0); }
		public TerminalNode KW_END() { return getToken(vhdlParser.KW_END, 0); }
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public List<Block_declarative_itemContext> block_declarative_item() {
			return getRuleContexts(Block_declarative_itemContext.class);
		}
		public Block_declarative_itemContext block_declarative_item(int i) {
			return getRuleContext(Block_declarative_itemContext.class,i);
		}
		public List<Concurrent_statementContext> concurrent_statement() {
			return getRuleContexts(Concurrent_statementContext.class);
		}
		public Concurrent_statementContext concurrent_statement(int i) {
			return getRuleContext(Concurrent_statementContext.class,i);
		}
		public LabelContext label() {
			return getRuleContext(LabelContext.class,0);
		}
		public Generate_statement_body_with_begin_endContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_generate_statement_body_with_begin_end; }
	}

	public final Generate_statement_body_with_begin_endContext generate_statement_body_with_begin_end() throws RecognitionException {
		Generate_statement_body_with_begin_endContext _localctx = new Generate_statement_body_with_begin_endContext(_ctx, getState());
		enterRule(_localctx, 482, RULE_generate_statement_body_with_begin_end);
		int _la;
		try {
			setState(2558);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KW_COMPONENT:
			case KW_GROUP:
			case KW_FILE:
			case KW_PURE:
			case KW_USE:
			case KW_SHARED:
			case KW_SIGNAL:
			case KW_BEGIN:
			case KW_DISCONNECT:
			case KW_PROCEDURE:
			case KW_ATTRIBUTE:
			case KW_VARIABLE:
			case KW_SUBTYPE:
			case KW_CONSTANT:
			case KW_FUNCTION:
			case KW_ALIAS:
			case KW_IMPURE:
			case KW_PACKAGE:
			case KW_FOR:
			case KW_TYPE:
				enterOuterAlt(_localctx, 1);
				{
				{
				setState(2537);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << KW_COMPONENT) | (1L << KW_GROUP) | (1L << KW_FILE) | (1L << KW_PURE) | (1L << KW_USE) | (1L << KW_SHARED) | (1L << KW_SIGNAL) | (1L << KW_DISCONNECT) | (1L << KW_PROCEDURE) | (1L << KW_ATTRIBUTE) | (1L << KW_VARIABLE) | (1L << KW_SUBTYPE) | (1L << KW_CONSTANT) | (1L << KW_FUNCTION))) != 0) || ((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & ((1L << (KW_ALIAS - 65)) | (1L << (KW_IMPURE - 65)) | (1L << (KW_PACKAGE - 65)) | (1L << (KW_FOR - 65)) | (1L << (KW_TYPE - 65)))) != 0)) {
					{
					{
					setState(2534);
					block_declarative_item();
					}
					}
					setState(2539);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(2540);
				match(KW_BEGIN);
				setState(2544);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==KW_PROCESS || _la==KW_POSTPONED || ((((_la - 72)) & ~0x3f) == 0 && ((1L << (_la - 72)) & ((1L << (KW_WITH - 72)) | (1L << (KW_ASSERT - 72)) | (1L << (BASIC_IDENTIFIER - 72)) | (1L << (EXTENDED_IDENTIFIER - 72)) | (1L << (CHARACTER_LITERAL - 72)) | (1L << (STRING_LITERAL - 72)) | (1L << (LPAREN - 72)) | (1L << (SHIFT_LEFT - 72)))) != 0)) {
					{
					{
					setState(2541);
					concurrent_statement();
					}
					}
					setState(2546);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(2547);
				match(KW_END);
				setState(2549);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==BASIC_IDENTIFIER || _la==EXTENDED_IDENTIFIER) {
					{
					setState(2548);
					label();
					}
				}

				setState(2551);
				match(SEMI);
				}
				}
				break;
			case KW_PROCESS:
			case KW_POSTPONED:
			case KW_END:
			case KW_WITH:
			case KW_ASSERT:
			case KW_WHEN:
			case BASIC_IDENTIFIER:
			case EXTENDED_IDENTIFIER:
			case CHARACTER_LITERAL:
			case STRING_LITERAL:
			case LPAREN:
			case SHIFT_LEFT:
				enterOuterAlt(_localctx, 2);
				{
				setState(2555);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==KW_PROCESS || _la==KW_POSTPONED || ((((_la - 72)) & ~0x3f) == 0 && ((1L << (_la - 72)) & ((1L << (KW_WITH - 72)) | (1L << (KW_ASSERT - 72)) | (1L << (BASIC_IDENTIFIER - 72)) | (1L << (EXTENDED_IDENTIFIER - 72)) | (1L << (CHARACTER_LITERAL - 72)) | (1L << (STRING_LITERAL - 72)) | (1L << (LPAREN - 72)) | (1L << (SHIFT_LEFT - 72)))) != 0)) {
					{
					{
					setState(2552);
					concurrent_statement();
					}
					}
					setState(2557);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Generate_statement_bodyContext extends ParserRuleContext {
		public TerminalNode KW_BEGIN() { return getToken(vhdlParser.KW_BEGIN, 0); }
		public List<Block_declarative_itemContext> block_declarative_item() {
			return getRuleContexts(Block_declarative_itemContext.class);
		}
		public Block_declarative_itemContext block_declarative_item(int i) {
			return getRuleContext(Block_declarative_itemContext.class,i);
		}
		public List<Concurrent_statementContext> concurrent_statement() {
			return getRuleContexts(Concurrent_statementContext.class);
		}
		public Concurrent_statementContext concurrent_statement(int i) {
			return getRuleContext(Concurrent_statementContext.class,i);
		}
		public Generate_statement_bodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_generate_statement_body; }
	}

	public final Generate_statement_bodyContext generate_statement_body() throws RecognitionException {
		Generate_statement_bodyContext _localctx = new Generate_statement_bodyContext(_ctx, getState());
		enterRule(_localctx, 484, RULE_generate_statement_body);
		int _la;
		try {
			int _alt;
			setState(2579);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,293,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				{
				setState(2563);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << KW_COMPONENT) | (1L << KW_GROUP) | (1L << KW_FILE) | (1L << KW_PURE) | (1L << KW_USE) | (1L << KW_SHARED) | (1L << KW_SIGNAL) | (1L << KW_DISCONNECT) | (1L << KW_PROCEDURE) | (1L << KW_ATTRIBUTE) | (1L << KW_VARIABLE) | (1L << KW_SUBTYPE) | (1L << KW_CONSTANT) | (1L << KW_FUNCTION))) != 0) || ((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & ((1L << (KW_ALIAS - 65)) | (1L << (KW_IMPURE - 65)) | (1L << (KW_PACKAGE - 65)) | (1L << (KW_FOR - 65)) | (1L << (KW_TYPE - 65)))) != 0)) {
					{
					{
					setState(2560);
					block_declarative_item();
					}
					}
					setState(2565);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(2566);
				match(KW_BEGIN);
				setState(2570);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,291,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(2567);
						concurrent_statement();
						}
						} 
					}
					setState(2572);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,291,_ctx);
				}
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(2576);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,292,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(2573);
						concurrent_statement();
						}
						} 
					}
					setState(2578);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,292,_ctx);
				}
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LabelContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public LabelContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_label; }
	}

	public final LabelContext label() throws RecognitionException {
		LabelContext _localctx = new LabelContext(_ctx, getState());
		enterRule(_localctx, 486, RULE_label);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2581);
			identifier();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Use_clauseContext extends ParserRuleContext {
		public TerminalNode KW_USE() { return getToken(vhdlParser.KW_USE, 0); }
		public List<Selected_nameContext> selected_name() {
			return getRuleContexts(Selected_nameContext.class);
		}
		public Selected_nameContext selected_name(int i) {
			return getRuleContext(Selected_nameContext.class,i);
		}
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public List<TerminalNode> COMMA() { return getTokens(vhdlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(vhdlParser.COMMA, i);
		}
		public Use_clauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_use_clause; }
	}

	public final Use_clauseContext use_clause() throws RecognitionException {
		Use_clauseContext _localctx = new Use_clauseContext(_ctx, getState());
		enterRule(_localctx, 488, RULE_use_clause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2583);
			match(KW_USE);
			setState(2584);
			selected_name();
			setState(2589);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(2585);
				match(COMMA);
				setState(2586);
				selected_name();
				}
				}
				setState(2591);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(2592);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Design_fileContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(vhdlParser.EOF, 0); }
		public List<Design_unitContext> design_unit() {
			return getRuleContexts(Design_unitContext.class);
		}
		public Design_unitContext design_unit(int i) {
			return getRuleContext(Design_unitContext.class,i);
		}
		public Design_fileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_design_file; }
	}

	public final Design_fileContext design_file() throws RecognitionException {
		Design_fileContext _localctx = new Design_fileContext(_ctx, getState());
		enterRule(_localctx, 490, RULE_design_file);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2597);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << KW_CONTEXT) | (1L << KW_ENTITY) | (1L << KW_USE) | (1L << KW_LIBRARY))) != 0) || ((((_la - 82)) & ~0x3f) == 0 && ((1L << (_la - 82)) & ((1L << (KW_PACKAGE - 82)) | (1L << (KW_CONFIGURATION - 82)) | (1L << (KW_ARCHITECTURE - 82)))) != 0)) {
				{
				{
				setState(2594);
				design_unit();
				}
				}
				setState(2599);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(2600);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Design_unitContext extends ParserRuleContext {
		public Context_clauseContext context_clause() {
			return getRuleContext(Context_clauseContext.class,0);
		}
		public Library_unitContext library_unit() {
			return getRuleContext(Library_unitContext.class,0);
		}
		public Design_unitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_design_unit; }
	}

	public final Design_unitContext design_unit() throws RecognitionException {
		Design_unitContext _localctx = new Design_unitContext(_ctx, getState());
		enterRule(_localctx, 492, RULE_design_unit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2602);
			context_clause();
			setState(2603);
			library_unit();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Library_unitContext extends ParserRuleContext {
		public Primary_unitContext primary_unit() {
			return getRuleContext(Primary_unitContext.class,0);
		}
		public Secondary_unitContext secondary_unit() {
			return getRuleContext(Secondary_unitContext.class,0);
		}
		public Library_unitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_library_unit; }
	}

	public final Library_unitContext library_unit() throws RecognitionException {
		Library_unitContext _localctx = new Library_unitContext(_ctx, getState());
		enterRule(_localctx, 494, RULE_library_unit);
		try {
			setState(2607);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,296,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(2605);
				primary_unit();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(2606);
				secondary_unit();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Primary_unitContext extends ParserRuleContext {
		public Entity_declarationContext entity_declaration() {
			return getRuleContext(Entity_declarationContext.class,0);
		}
		public Configuration_declarationContext configuration_declaration() {
			return getRuleContext(Configuration_declarationContext.class,0);
		}
		public Package_declarationContext package_declaration() {
			return getRuleContext(Package_declarationContext.class,0);
		}
		public Package_instantiation_declarationContext package_instantiation_declaration() {
			return getRuleContext(Package_instantiation_declarationContext.class,0);
		}
		public Context_declarationContext context_declaration() {
			return getRuleContext(Context_declarationContext.class,0);
		}
		public Primary_unitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primary_unit; }
	}

	public final Primary_unitContext primary_unit() throws RecognitionException {
		Primary_unitContext _localctx = new Primary_unitContext(_ctx, getState());
		enterRule(_localctx, 496, RULE_primary_unit);
		try {
			setState(2614);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,297,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(2609);
				entity_declaration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(2610);
				configuration_declaration();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(2611);
				package_declaration();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(2612);
				package_instantiation_declaration();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(2613);
				context_declaration();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Secondary_unitContext extends ParserRuleContext {
		public Architecture_bodyContext architecture_body() {
			return getRuleContext(Architecture_bodyContext.class,0);
		}
		public Package_bodyContext package_body() {
			return getRuleContext(Package_bodyContext.class,0);
		}
		public Secondary_unitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_secondary_unit; }
	}

	public final Secondary_unitContext secondary_unit() throws RecognitionException {
		Secondary_unitContext _localctx = new Secondary_unitContext(_ctx, getState());
		enterRule(_localctx, 498, RULE_secondary_unit);
		try {
			setState(2618);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KW_ARCHITECTURE:
				enterOuterAlt(_localctx, 1);
				{
				setState(2616);
				architecture_body();
				}
				break;
			case KW_PACKAGE:
				enterOuterAlt(_localctx, 2);
				{
				setState(2617);
				package_body();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Library_clauseContext extends ParserRuleContext {
		public TerminalNode KW_LIBRARY() { return getToken(vhdlParser.KW_LIBRARY, 0); }
		public Logical_name_listContext logical_name_list() {
			return getRuleContext(Logical_name_listContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public Library_clauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_library_clause; }
	}

	public final Library_clauseContext library_clause() throws RecognitionException {
		Library_clauseContext _localctx = new Library_clauseContext(_ctx, getState());
		enterRule(_localctx, 500, RULE_library_clause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2620);
			match(KW_LIBRARY);
			setState(2621);
			logical_name_list();
			setState(2622);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Logical_name_listContext extends ParserRuleContext {
		public Identifier_listContext identifier_list() {
			return getRuleContext(Identifier_listContext.class,0);
		}
		public Logical_name_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logical_name_list; }
	}

	public final Logical_name_listContext logical_name_list() throws RecognitionException {
		Logical_name_listContext _localctx = new Logical_name_listContext(_ctx, getState());
		enterRule(_localctx, 502, RULE_logical_name_list);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2624);
			identifier_list();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Context_declarationContext extends ParserRuleContext {
		public List<TerminalNode> KW_CONTEXT() { return getTokens(vhdlParser.KW_CONTEXT); }
		public TerminalNode KW_CONTEXT(int i) {
			return getToken(vhdlParser.KW_CONTEXT, i);
		}
		public List<IdentifierContext> identifier() {
			return getRuleContexts(IdentifierContext.class);
		}
		public IdentifierContext identifier(int i) {
			return getRuleContext(IdentifierContext.class,i);
		}
		public TerminalNode KW_IS() { return getToken(vhdlParser.KW_IS, 0); }
		public Context_clauseContext context_clause() {
			return getRuleContext(Context_clauseContext.class,0);
		}
		public TerminalNode KW_END() { return getToken(vhdlParser.KW_END, 0); }
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public Context_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_context_declaration; }
	}

	public final Context_declarationContext context_declaration() throws RecognitionException {
		Context_declarationContext _localctx = new Context_declarationContext(_ctx, getState());
		enterRule(_localctx, 504, RULE_context_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2626);
			match(KW_CONTEXT);
			setState(2627);
			identifier();
			setState(2628);
			match(KW_IS);
			setState(2629);
			context_clause();
			setState(2630);
			match(KW_END);
			setState(2632);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KW_CONTEXT) {
				{
				setState(2631);
				match(KW_CONTEXT);
				}
			}

			setState(2635);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==BASIC_IDENTIFIER || _la==EXTENDED_IDENTIFIER) {
				{
				setState(2634);
				identifier();
				}
			}

			setState(2637);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Context_clauseContext extends ParserRuleContext {
		public List<Context_itemContext> context_item() {
			return getRuleContexts(Context_itemContext.class);
		}
		public Context_itemContext context_item(int i) {
			return getRuleContext(Context_itemContext.class,i);
		}
		public Context_clauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_context_clause; }
	}

	public final Context_clauseContext context_clause() throws RecognitionException {
		Context_clauseContext _localctx = new Context_clauseContext(_ctx, getState());
		enterRule(_localctx, 506, RULE_context_clause);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(2642);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,301,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(2639);
					context_item();
					}
					} 
				}
				setState(2644);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,301,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Context_itemContext extends ParserRuleContext {
		public Library_clauseContext library_clause() {
			return getRuleContext(Library_clauseContext.class,0);
		}
		public Use_clauseContext use_clause() {
			return getRuleContext(Use_clauseContext.class,0);
		}
		public Context_referenceContext context_reference() {
			return getRuleContext(Context_referenceContext.class,0);
		}
		public Context_itemContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_context_item; }
	}

	public final Context_itemContext context_item() throws RecognitionException {
		Context_itemContext _localctx = new Context_itemContext(_ctx, getState());
		enterRule(_localctx, 508, RULE_context_item);
		try {
			setState(2648);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KW_LIBRARY:
				enterOuterAlt(_localctx, 1);
				{
				setState(2645);
				library_clause();
				}
				break;
			case KW_USE:
				enterOuterAlt(_localctx, 2);
				{
				setState(2646);
				use_clause();
				}
				break;
			case KW_CONTEXT:
				enterOuterAlt(_localctx, 3);
				{
				setState(2647);
				context_reference();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Context_referenceContext extends ParserRuleContext {
		public TerminalNode KW_CONTEXT() { return getToken(vhdlParser.KW_CONTEXT, 0); }
		public List<Selected_nameContext> selected_name() {
			return getRuleContexts(Selected_nameContext.class);
		}
		public Selected_nameContext selected_name(int i) {
			return getRuleContext(Selected_nameContext.class,i);
		}
		public TerminalNode SEMI() { return getToken(vhdlParser.SEMI, 0); }
		public List<TerminalNode> COMMA() { return getTokens(vhdlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(vhdlParser.COMMA, i);
		}
		public Context_referenceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_context_reference; }
	}

	public final Context_referenceContext context_reference() throws RecognitionException {
		Context_referenceContext _localctx = new Context_referenceContext(_ctx, getState());
		enterRule(_localctx, 510, RULE_context_reference);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2650);
			match(KW_CONTEXT);
			setState(2651);
			selected_name();
			setState(2656);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(2652);
				match(COMMA);
				setState(2653);
				selected_name();
				}
				}
				setState(2658);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(2659);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IdentifierContext extends ParserRuleContext {
		public TerminalNode BASIC_IDENTIFIER() { return getToken(vhdlParser.BASIC_IDENTIFIER, 0); }
		public TerminalNode EXTENDED_IDENTIFIER() { return getToken(vhdlParser.EXTENDED_IDENTIFIER, 0); }
		public IdentifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifier; }
	}

	public final IdentifierContext identifier() throws RecognitionException {
		IdentifierContext _localctx = new IdentifierContext(_ctx, getState());
		enterRule(_localctx, 512, RULE_identifier);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2661);
			_la = _input.LA(1);
			if ( !(_la==BASIC_IDENTIFIER || _la==EXTENDED_IDENTIFIER) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 2:
			return name_sempred((NameContext)_localctx, predIndex);
		case 156:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		case 157:
			return simple_expression_sempred((Simple_expressionContext)_localctx, predIndex);
		case 197:
			return conditional_waveforms_sempred((Conditional_waveformsContext)_localctx, predIndex);
		case 199:
			return conditional_expressions_sempred((Conditional_expressionsContext)_localctx, predIndex);
		case 211:
			return if_statement_sempred((If_statementContext)_localctx, predIndex);
		case 238:
			return if_generate_statement_sempred((If_generate_statementContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean name_sempred(NameContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 3);
		case 2:
			return precpred(_ctx, 2);
		case 3:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean simple_expression_sempred(Simple_expressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 4:
			return precpred(_ctx, 3);
		case 5:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean conditional_waveforms_sempred(Conditional_waveformsContext _localctx, int predIndex) {
		switch (predIndex) {
		case 6:
			return _input->LA(1) != KW_ELSE;
		}
		return true;
	}
	private boolean conditional_expressions_sempred(Conditional_expressionsContext _localctx, int predIndex) {
		switch (predIndex) {
		case 7:
			return _input->LA(1) != KW_ELSE;
		}
		return true;
	}
	private boolean if_statement_sempred(If_statementContext _localctx, int predIndex) {
		switch (predIndex) {
		case 8:
			return _input->LA(1) != KW_ELSE;
		}
		return true;
	}
	private boolean if_generate_statement_sempred(If_generate_statementContext _localctx, int predIndex) {
		switch (predIndex) {
		case 9:
			return _input->LA(1) != KW_ELSE;
		}
		return true;
	}

	private static final int _serializedATNSegments = 2;
	private static final String _serializedATNSegment0 =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\u00a7\u0a6a\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I"+
		"\tI\4J\tJ\4K\tK\4L\tL\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT"+
		"\4U\tU\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4^\t^\4_\t_\4"+
		"`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4g\tg\4h\th\4i\ti\4j\tj\4k\t"+
		"k\4l\tl\4m\tm\4n\tn\4o\to\4p\tp\4q\tq\4r\tr\4s\ts\4t\tt\4u\tu\4v\tv\4"+
		"w\tw\4x\tx\4y\ty\4z\tz\4{\t{\4|\t|\4}\t}\4~\t~\4\177\t\177\4\u0080\t\u0080"+
		"\4\u0081\t\u0081\4\u0082\t\u0082\4\u0083\t\u0083\4\u0084\t\u0084\4\u0085"+
		"\t\u0085\4\u0086\t\u0086\4\u0087\t\u0087\4\u0088\t\u0088\4\u0089\t\u0089"+
		"\4\u008a\t\u008a\4\u008b\t\u008b\4\u008c\t\u008c\4\u008d\t\u008d\4\u008e"+
		"\t\u008e\4\u008f\t\u008f\4\u0090\t\u0090\4\u0091\t\u0091\4\u0092\t\u0092"+
		"\4\u0093\t\u0093\4\u0094\t\u0094\4\u0095\t\u0095\4\u0096\t\u0096\4\u0097"+
		"\t\u0097\4\u0098\t\u0098\4\u0099\t\u0099\4\u009a\t\u009a\4\u009b\t\u009b"+
		"\4\u009c\t\u009c\4\u009d\t\u009d\4\u009e\t\u009e\4\u009f\t\u009f\4\u00a0"+
		"\t\u00a0\4\u00a1\t\u00a1\4\u00a2\t\u00a2\4\u00a3\t\u00a3\4\u00a4\t\u00a4"+
		"\4\u00a5\t\u00a5\4\u00a6\t\u00a6\4\u00a7\t\u00a7\4\u00a8\t\u00a8\4\u00a9"+
		"\t\u00a9\4\u00aa\t\u00aa\4\u00ab\t\u00ab\4\u00ac\t\u00ac\4\u00ad\t\u00ad"+
		"\4\u00ae\t\u00ae\4\u00af\t\u00af\4\u00b0\t\u00b0\4\u00b1\t\u00b1\4\u00b2"+
		"\t\u00b2\4\u00b3\t\u00b3\4\u00b4\t\u00b4\4\u00b5\t\u00b5\4\u00b6\t\u00b6"+
		"\4\u00b7\t\u00b7\4\u00b8\t\u00b8\4\u00b9\t\u00b9\4\u00ba\t\u00ba\4\u00bb"+
		"\t\u00bb\4\u00bc\t\u00bc\4\u00bd\t\u00bd\4\u00be\t\u00be\4\u00bf\t\u00bf"+
		"\4\u00c0\t\u00c0\4\u00c1\t\u00c1\4\u00c2\t\u00c2\4\u00c3\t\u00c3\4\u00c4"+
		"\t\u00c4\4\u00c5\t\u00c5\4\u00c6\t\u00c6\4\u00c7\t\u00c7\4\u00c8\t\u00c8"+
		"\4\u00c9\t\u00c9\4\u00ca\t\u00ca\4\u00cb\t\u00cb\4\u00cc\t\u00cc\4\u00cd"+
		"\t\u00cd\4\u00ce\t\u00ce\4\u00cf\t\u00cf\4\u00d0\t\u00d0\4\u00d1\t\u00d1"+
		"\4\u00d2\t\u00d2\4\u00d3\t\u00d3\4\u00d4\t\u00d4\4\u00d5\t\u00d5\4\u00d6"+
		"\t\u00d6\4\u00d7\t\u00d7\4\u00d8\t\u00d8\4\u00d9\t\u00d9\4\u00da\t\u00da"+
		"\4\u00db\t\u00db\4\u00dc\t\u00dc\4\u00dd\t\u00dd\4\u00de\t\u00de\4\u00df"+
		"\t\u00df\4\u00e0\t\u00e0\4\u00e1\t\u00e1\4\u00e2\t\u00e2\4\u00e3\t\u00e3"+
		"\4\u00e4\t\u00e4\4\u00e5\t\u00e5\4\u00e6\t\u00e6\4\u00e7\t\u00e7\4\u00e8"+
		"\t\u00e8\4\u00e9\t\u00e9\4\u00ea\t\u00ea\4\u00eb\t\u00eb\4\u00ec\t\u00ec"+
		"\4\u00ed\t\u00ed\4\u00ee\t\u00ee\4\u00ef\t\u00ef\4\u00f0\t\u00f0\4\u00f1"+
		"\t\u00f1\4\u00f2\t\u00f2\4\u00f3\t\u00f3\4\u00f4\t\u00f4\4\u00f5\t\u00f5"+
		"\4\u00f6\t\u00f6\4\u00f7\t\u00f7\4\u00f8\t\u00f8\4\u00f9\t\u00f9\4\u00fa"+
		"\t\u00fa\4\u00fb\t\u00fb\4\u00fc\t\u00fc\4\u00fd\t\u00fd\4\u00fe\t\u00fe"+
		"\4\u00ff\t\u00ff\4\u0100\t\u0100\4\u0101\t\u0101\4\u0102\t\u0102\3\2\3"+
		"\2\3\3\3\3\3\3\5\3\u020a\n\3\3\4\3\4\3\4\5\4\u020f\n\4\3\4\3\4\3\4\3\4"+
		"\3\4\3\4\5\4\u0217\n\4\7\4\u0219\n\4\f\4\16\4\u021c\13\4\3\5\3\5\3\5\3"+
		"\5\3\6\5\6\u0223\n\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\5\b\u022d\n\b\3\t"+
		"\3\t\3\t\3\t\3\n\3\n\3\n\7\n\u0236\n\n\f\n\16\n\u0239\13\n\3\13\3\13\3"+
		"\13\3\13\5\13\u023f\n\13\3\13\5\13\u0242\n\13\3\13\7\13\u0245\n\13\f\13"+
		"\16\13\u0248\13\13\3\13\3\13\7\13\u024c\n\13\f\13\16\13\u024f\13\13\5"+
		"\13\u0251\n\13\3\13\3\13\5\13\u0255\n\13\3\13\5\13\u0258\n\13\3\13\3\13"+
		"\3\f\3\f\3\f\5\f\u025f\n\f\3\r\3\r\3\r\5\r\u0264\n\r\3\r\3\r\3\r\5\r\u0269"+
		"\n\r\3\16\3\16\3\16\3\16\3\16\3\16\7\16\u0271\n\16\f\16\16\16\u0274\13"+
		"\16\3\16\3\16\7\16\u0278\n\16\f\16\16\16\u027b\13\16\3\16\3\16\5\16\u027f"+
		"\n\16\3\16\5\16\u0282\n\16\3\16\3\16\3\17\3\17\3\17\5\17\u0289\n\17\3"+
		"\20\3\20\3\20\3\20\3\20\3\20\7\20\u0291\n\20\f\20\16\20\u0294\13\20\3"+
		"\20\3\20\3\20\7\20\u0299\n\20\f\20\16\20\u029c\13\20\3\20\3\20\3\20\5"+
		"\20\u02a1\n\20\3\20\5\20\u02a4\n\20\3\20\3\20\3\21\3\21\3\21\5\21\u02ab"+
		"\n\21\3\22\3\22\3\22\7\22\u02b0\n\22\f\22\16\22\u02b3\13\22\3\22\7\22"+
		"\u02b6\n\22\f\22\16\22\u02b9\13\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23"+
		"\3\23\3\23\5\23\u02c4\n\23\3\24\3\24\3\24\5\24\u02c9\n\24\3\25\3\25\5"+
		"\25\u02cd\n\25\3\26\3\26\3\26\3\26\3\26\5\26\u02d4\n\26\3\26\3\26\3\26"+
		"\7\26\u02d9\n\26\f\26\16\26\u02dc\13\26\3\26\5\26\u02df\n\26\3\26\3\26"+
		"\3\26\3\26\3\27\3\27\3\27\3\30\3\30\5\30\u02ea\n\30\3\31\3\31\3\31\5\31"+
		"\u02ef\n\31\3\31\5\31\u02f2\n\31\3\31\3\31\3\31\3\31\5\31\u02f8\n\31\3"+
		"\32\5\32\u02fb\n\32\3\32\3\32\3\32\5\32\u0300\n\32\3\32\5\32\u0303\n\32"+
		"\3\32\3\32\3\32\3\32\5\32\u0309\n\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33"+
		"\3\33\5\33\u0313\n\33\3\34\3\34\5\34\u0317\n\34\3\35\3\35\3\36\3\36\3"+
		"\37\3\37\3\37\7\37\u0320\n\37\f\37\16\37\u0323\13\37\3\37\3\37\7\37\u0327"+
		"\n\37\f\37\16\37\u032a\13\37\3\37\3\37\5\37\u032e\n\37\3\37\5\37\u0331"+
		"\n\37\3\37\3\37\3 \3 \3!\3!\3!\3!\3!\3!\5!\u033d\n!\3!\5!\u0340\n!\3!"+
		"\3!\3\"\3\"\3\"\3\"\7\"\u0348\n\"\f\"\16\"\u034b\13\"\5\"\u034d\n\"\3"+
		"\"\3\"\5\"\u0351\n\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\5#\u035c\n#\5#\u035e"+
		"\n#\3#\7#\u0361\n#\f#\16#\u0364\13#\3#\3#\5#\u0368\n#\3#\5#\u036b\n#\3"+
		"#\3#\3$\3$\3$\3$\5$\u0373\n$\3%\3%\3%\3%\3%\7%\u037a\n%\f%\16%\u037d\13"+
		"%\3%\3%\3%\5%\u0382\n%\3%\5%\u0385\n%\3%\3%\3&\3&\3&\3&\3&\3&\5&\u038f"+
		"\n&\3&\3&\3\'\3\'\3\'\3\'\5\'\u0397\n\'\3(\3(\3(\3)\3)\3)\3)\3)\5)\u03a1"+
		"\n)\3*\3*\3+\3+\3+\3+\7+\u03a9\n+\f+\16+\u03ac\13+\3+\3+\3,\3,\5,\u03b2"+
		"\n,\3-\3-\3.\3.\3.\3.\7.\u03ba\n.\f.\16.\u03bd\13.\3.\3.\3.\5.\u03c2\n"+
		".\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\62\3\62\5\62\u03d0\n\62"+
		"\3\63\3\63\5\63\u03d4\n\63\3\64\3\64\3\64\3\64\3\64\7\64\u03db\n\64\f"+
		"\64\16\64\u03de\13\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\66"+
		"\3\66\3\66\3\66\3\67\3\67\5\67\u03ef\n\67\3\67\3\67\3\67\3\67\5\67\u03f5"+
		"\n\67\5\67\u03f7\n\67\38\38\39\39\39\39\79\u03ff\n9\f9\169\u0402\139\3"+
		"9\39\3:\3:\5:\u0408\n:\3;\3;\6;\u040c\n;\r;\16;\u040d\3;\3;\3;\5;\u0413"+
		"\n;\3<\3<\3<\3<\3<\3=\3=\3=\7=\u041d\n=\f=\16=\u0420\13=\3>\3>\3?\3?\3"+
		"?\3?\7?\u0428\n?\f?\16?\u042b\13?\3?\3?\3@\3@\3@\3A\3A\3A\3B\3B\3B\3B"+
		"\3C\3C\3C\3C\3D\3D\5D\u043f\nD\3E\3E\7E\u0443\nE\fE\16E\u0446\13E\3E\3"+
		"E\3E\5E\u044b\nE\3F\3F\3F\3F\5F\u0451\nF\3G\3G\3G\7G\u0456\nG\fG\16G\u0459"+
		"\13G\3G\3G\3G\3G\5G\u045f\nG\3H\3H\5H\u0463\nH\3I\3I\3I\3I\3I\3I\3J\3"+
		"J\3J\3J\3J\5J\u0470\nJ\3K\3K\3K\3K\3K\3K\3L\5L\u0479\nL\3L\3L\5L\u047d"+
		"\nL\3M\3M\3M\3M\3M\5M\u0484\nM\3N\3N\5N\u0488\nN\3O\3O\3P\3P\3P\7P\u048f"+
		"\nP\fP\16P\u0492\13P\3Q\3Q\3Q\3R\3R\3S\3S\5S\u049b\nS\3T\3T\5T\u049f\n"+
		"T\3U\3U\3U\3U\5U\u04a5\nU\3V\3V\3V\3V\3V\3V\5V\u04ad\nV\3V\3V\3W\3W\3"+
		"W\3W\3W\5W\u04b6\nW\3W\3W\5W\u04ba\nW\3W\3W\3X\3X\3Y\5Y\u04c1\nY\3Y\3"+
		"Y\3Y\3Y\3Y\3Y\5Y\u04c9\nY\3Y\3Y\3Z\3Z\3Z\3Z\3Z\5Z\u04d2\nZ\3Z\3Z\3[\3"+
		"[\5[\u04d8\n[\3[\3[\5[\u04dc\n[\3[\3[\3\\\3\\\3]\3]\3]\3]\5]\u04e6\n]"+
		"\3^\3^\3^\3^\5^\u04ec\n^\3_\3_\3_\3_\5_\u04f2\n_\3_\3_\3_\5_\u04f7\n_"+
		"\3`\5`\u04fa\n`\3`\3`\3`\5`\u04ff\n`\3`\3`\5`\u0503\n`\3`\3`\5`\u0507"+
		"\n`\3a\3a\3a\3a\5a\u050d\na\3a\3a\3a\5a\u0512\na\3b\3b\3b\3b\3b\3c\3c"+
		"\3d\3d\3e\3e\3e\3f\3f\3f\5f\u0523\nf\3g\3g\5g\u0527\ng\3h\3h\3h\5h\u052c"+
		"\nh\3h\3h\3h\3h\5h\u0532\nh\3i\5i\u0535\ni\3i\3i\3i\5i\u053a\ni\3i\3i"+
		"\3i\3i\5i\u0540\ni\3i\3i\3i\3j\3j\5j\u0547\nj\3k\3k\3k\3k\3k\3k\3k\3l"+
		"\3l\3l\3l\3l\3l\3l\3l\3l\3l\3l\5l\u055b\nl\3m\3m\3m\7m\u0560\nm\fm\16"+
		"m\u0563\13m\3n\3n\3o\3o\3o\3o\3o\3o\3p\3p\3q\3q\3q\3q\3q\3q\3r\3r\3s\3"+
		"s\3s\3s\7s\u057b\ns\fs\16s\u057e\13s\3s\3s\3t\3t\3t\5t\u0585\nt\3t\3t"+
		"\3u\3u\3u\3u\3u\5u\u058e\nu\3v\3v\3v\3v\3v\3v\5v\u0596\nv\3w\5w\u0599"+
		"\nw\3w\3w\3w\5w\u059e\nw\3x\3x\3x\3x\3y\3y\3y\3y\3z\3z\3z\3z\5z\u05ac"+
		"\nz\3z\3z\3z\5z\u05b1\nz\3z\3z\3{\3{\3{\5{\u05b8\n{\3|\3|\3|\3|\3|\3|"+
		"\3}\3}\3}\5}\u05c3\n}\3}\5}\u05c6\n}\3}\5}\u05c9\n}\3}\3}\3}\5}\u05ce"+
		"\n}\3}\3}\3~\3~\3~\3~\3~\3~\3~\3~\3\177\3\177\3\177\7\177\u05dd\n\177"+
		"\f\177\16\177\u05e0\13\177\3\u0080\3\u0080\5\u0080\u05e4\n\u0080\3\u0081"+
		"\3\u0081\3\u0081\3\u0081\3\u0081\3\u0081\3\u0081\3\u0081\3\u0081\3\u0082"+
		"\3\u0082\3\u0082\7\u0082\u05f2\n\u0082\f\u0082\16\u0082\u05f5\13\u0082"+
		"\3\u0083\3\u0083\3\u0084\3\u0084\3\u0084\3\u0084\3\u0084\3\u0084\3\u0084"+
		"\3\u0084\3\u0085\3\u0085\3\u0085\3\u0085\3\u0086\3\u0086\3\u0087\3\u0087"+
		"\3\u0087\7\u0087\u060a\n\u0087\f\u0087\16\u0087\u060d\13\u0087\3\u0087"+
		"\3\u0087\5\u0087\u0611\n\u0087\3\u0088\3\u0088\5\u0088\u0615\n\u0088\3"+
		"\u0089\3\u0089\3\u0089\5\u0089\u061a\n\u0089\3\u008a\3\u008a\5\u008a\u061e"+
		"\n\u008a\3\u008b\3\u008b\3\u008b\3\u008b\3\u008b\3\u008b\3\u008b\5\u008b"+
		"\u0627\n\u008b\3\u008c\3\u008c\3\u008c\3\u008c\3\u008c\3\u008c\3\u008c"+
		"\6\u008c\u0630\n\u008c\r\u008c\16\u008c\u0631\3\u008c\3\u008c\3\u008c"+
		"\3\u008c\3\u008d\3\u008d\3\u008d\3\u008d\3\u008e\3\u008e\3\u008e\7\u008e"+
		"\u063f\n\u008e\f\u008e\16\u008e\u0642\13\u008e\3\u008e\3\u008e\5\u008e"+
		"\u0646\n\u008e\3\u008f\3\u008f\5\u008f\u064a\n\u008f\3\u008f\5\u008f\u064d"+
		"\n\u008f\3\u008f\5\u008f\u0650\n\u008f\3\u0090\3\u0090\3\u0090\3\u0090"+
		"\3\u0090\3\u0090\5\u0090\u0658\n\u0090\3\u0090\3\u0090\3\u0090\5\u0090"+
		"\u065d\n\u0090\3\u0091\3\u0091\3\u0091\3\u0091\3\u0092\3\u0092\3\u0092"+
		"\7\u0092\u0666\n\u0092\f\u0092\16\u0092\u0669\13\u0092\3\u0093\3\u0093"+
		"\3\u0093\3\u0093\3\u0093\3\u0093\3\u0094\3\u0094\3\u0094\3\u0094\3\u0095"+
		"\3\u0095\3\u0095\7\u0095\u0678\n\u0095\f\u0095\16\u0095\u067b\13\u0095"+
		"\3\u0095\3\u0095\5\u0095\u067f\n\u0095\3\u0096\3\u0096\5\u0096\u0683\n"+
		"\u0096\3\u0097\3\u0097\3\u0097\3\u0097\3\u0097\3\u0097\3\u0097\3\u0098"+
		"\3\u0098\3\u0098\5\u0098\u068f\n\u0098\3\u0099\3\u0099\3\u0099\3\u0099"+
		"\3\u0099\3\u0099\3\u0099\3\u0099\7\u0099\u0699\n\u0099\f\u0099\16\u0099"+
		"\u069c\13\u0099\3\u009a\3\u009a\3\u009a\3\u009b\3\u009b\7\u009b\u06a3"+
		"\n\u009b\f\u009b\16\u009b\u06a6\13\u009b\3\u009b\3\u009b\3\u009c\3\u009c"+
		"\3\u009c\7\u009c\u06ad\n\u009c\f\u009c\16\u009c\u06b0\13\u009c\3\u009c"+
		"\3\u009c\3\u009d\3\u009d\3\u009d\3\u009d\3\u009d\5\u009d\u06b9\n\u009d"+
		"\3\u009e\3\u009e\3\u009e\3\u009e\5\u009e\u06bf\n\u009e\3\u009e\3\u009e"+
		"\3\u009e\3\u009e\3\u009e\3\u009e\3\u009e\3\u009e\3\u009e\3\u009e\3\u009e"+
		"\3\u009e\7\u009e\u06cd\n\u009e\f\u009e\16\u009e\u06d0\13\u009e\3\u009f"+
		"\3\u009f\3\u009f\3\u009f\5\u009f\u06d6\n\u009f\3\u009f\3\u009f\3\u009f"+
		"\5\u009f\u06db\n\u009f\3\u009f\3\u009f\3\u009f\3\u009f\5\u009f\u06e1\n"+
		"\u009f\3\u009f\3\u009f\3\u009f\3\u009f\3\u009f\3\u009f\3\u009f\3\u009f"+
		"\7\u009f\u06eb\n\u009f\f\u009f\16\u009f\u06ee\13\u009f\3\u00a0\3\u00a0"+
		"\3\u00a0\3\u00a0\3\u00a0\3\u00a0\5\u00a0\u06f6\n\u00a0\3\u00a1\3\u00a1"+
		"\3\u00a2\3\u00a2\3\u00a3\3\u00a3\3\u00a4\3\u00a4\3\u00a5\3\u00a5\3\u00a6"+
		"\3\u00a6\3\u00a7\3\u00a7\3\u00a8\3\u00a8\5\u00a8\u0708\n\u00a8\3\u00a8"+
		"\3\u00a8\5\u00a8\u070c\n\u00a8\3\u00a8\5\u00a8\u070f\n\u00a8\3\u00a9\5"+
		"\u00a9\u0712\n\u00a9\3\u00a9\3\u00a9\3\u00aa\3\u00aa\3\u00aa\3\u00aa\7"+
		"\u00aa\u071a\n\u00aa\f\u00aa\16\u00aa\u071d\13\u00aa\3\u00aa\3\u00aa\3"+
		"\u00ab\3\u00ab\3\u00ab\5\u00ab\u0724\n\u00ab\3\u00ab\3\u00ab\3\u00ac\3"+
		"\u00ac\3\u00ac\7\u00ac\u072b\n\u00ac\f\u00ac\16\u00ac\u072e\13\u00ac\3"+
		"\u00ad\3\u00ad\3\u00ad\5\u00ad\u0733\n\u00ad\3\u00ae\3\u00ae\3\u00ae\3"+
		"\u00ae\3\u00af\3\u00af\3\u00af\5\u00af\u073c\n\u00af\3\u00b0\7\u00b0\u073f"+
		"\n\u00b0\f\u00b0\16\u00b0\u0742\13\u00b0\3\u00b1\3\u00b1\3\u00b1\5\u00b1"+
		"\u0747\n\u00b1\3\u00b1\3\u00b1\3\u00b1\3\u00b1\3\u00b1\3\u00b1\3\u00b1"+
		"\3\u00b1\3\u00b1\3\u00b1\3\u00b1\3\u00b1\3\u00b1\5\u00b1\u0756\n\u00b1"+
		"\3\u00b2\3\u00b2\5\u00b2\u075a\n\u00b2\3\u00b2\5\u00b2\u075d\n\u00b2\3"+
		"\u00b2\5\u00b2\u0760\n\u00b2\3\u00b2\3\u00b2\3\u00b3\3\u00b3\3\u00b3\3"+
		"\u00b4\3\u00b4\3\u00b4\7\u00b4\u076a\n\u00b4\f\u00b4\16\u00b4\u076d\13"+
		"\u00b4\3\u00b5\3\u00b5\3\u00b5\3\u00b6\3\u00b6\3\u00b7\3\u00b7\3\u00b7"+
		"\3\u00b8\3\u00b8\3\u00b8\3\u00b9\3\u00b9\3\u00b9\3\u00b9\5\u00b9\u077e"+
		"\n\u00b9\3\u00b9\3\u00b9\5\u00b9\u0782\n\u00b9\3\u00ba\3\u00ba\3\u00ba"+
		"\3\u00ba\5\u00ba\u0788\n\u00ba\3\u00ba\3\u00ba\3\u00bb\3\u00bb\3\u00bb"+
		"\5\u00bb\u078f\n\u00bb\3\u00bc\3\u00bc\3\u00bc\5\u00bc\u0794\n\u00bc\3"+
		"\u00bd\3\u00bd\3\u00bd\5\u00bd\u0799\n\u00bd\3\u00bd\3\u00bd\3\u00bd\3"+
		"\u00be\3\u00be\3\u00be\3\u00be\5\u00be\u07a2\n\u00be\3\u00be\3\u00be\3"+
		"\u00be\3\u00bf\3\u00bf\3\u00bf\3\u00bf\5\u00bf\u07ab\n\u00bf\3\u00bf\3"+
		"\u00bf\3\u00c0\3\u00c0\3\u00c1\3\u00c1\3\u00c1\5\u00c1\u07b4\n\u00c1\3"+
		"\u00c1\5\u00c1\u07b7\n\u00c1\3\u00c2\3\u00c2\5\u00c2\u07bb\n\u00c2\3\u00c3"+
		"\3\u00c3\3\u00c3\7\u00c3\u07c0\n\u00c3\f\u00c3\16\u00c3\u07c3\13\u00c3"+
		"\3\u00c3\5\u00c3\u07c6\n\u00c3\3\u00c4\3\u00c4\3\u00c4\5\u00c4\u07cb\n"+
		"\u00c4\3\u00c4\3\u00c4\3\u00c4\5\u00c4\u07d0\n\u00c4\5\u00c4\u07d2\n\u00c4"+
		"\3\u00c5\3\u00c5\5\u00c5\u07d6\n\u00c5\3\u00c6\3\u00c6\3\u00c6\5\u00c6"+
		"\u07db\n\u00c6\3\u00c6\3\u00c6\3\u00c6\3\u00c7\3\u00c7\3\u00c7\3\u00c7"+
		"\3\u00c7\3\u00c7\3\u00c7\3\u00c7\7\u00c7\u07e8\n\u00c7\f\u00c7\16\u00c7"+
		"\u07eb\13\u00c7\3\u00c7\3\u00c7\3\u00c7\5\u00c7\u07f0\n\u00c7\3\u00c8"+
		"\3\u00c8\3\u00c8\3\u00c8\5\u00c8\u07f6\n\u00c8\3\u00c8\3\u00c8\3\u00c8"+
		"\3\u00c9\3\u00c9\3\u00c9\3\u00c9\3\u00c9\3\u00c9\3\u00c9\3\u00c9\7\u00c9"+
		"\u0803\n\u00c9\f\u00c9\16\u00c9\u0806\13\u00c9\3\u00c9\3\u00c9\3\u00c9"+
		"\5\u00c9\u080b\n\u00c9\3\u00ca\3\u00ca\5\u00ca\u080f\n\u00ca\3\u00cb\3"+
		"\u00cb\3\u00cb\3\u00cb\5\u00cb\u0815\n\u00cb\3\u00cb\3\u00cb\3\u00cb\5"+
		"\u00cb\u081a\n\u00cb\3\u00cb\3\u00cb\3\u00cb\3\u00cc\3\u00cc\3\u00cc\3"+
		"\u00cc\3\u00cc\3\u00cc\3\u00cc\3\u00cc\7\u00cc\u0827\n\u00cc\f\u00cc\16"+
		"\u00cc\u082a\13\u00cc\3\u00cd\3\u00cd\3\u00cd\3\u00cd\5\u00cd\u0830\n"+
		"\u00cd\3\u00cd\3\u00cd\3\u00cd\3\u00cd\5\u00cd\u0836\n\u00cd\3\u00cd\3"+
		"\u00cd\3\u00cd\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce"+
		"\3\u00ce\7\u00ce\u0843\n\u00ce\f\u00ce\16\u00ce\u0846\13\u00ce\3\u00cf"+
		"\3\u00cf\3\u00cf\5\u00cf\u084b\n\u00cf\3\u00d0\3\u00d0\3\u00d0\3\u00d0"+
		"\3\u00d0\3\u00d1\3\u00d1\3\u00d1\3\u00d1\3\u00d1\3\u00d2\3\u00d2\3\u00d2"+
		"\3\u00d2\5\u00d2\u085b\n\u00d2\3\u00d2\3\u00d2\3\u00d2\3\u00d2\3\u00d2"+
		"\3\u00d3\3\u00d3\3\u00d3\3\u00d4\3\u00d4\3\u00d5\3\u00d5\3\u00d5\3\u00d5"+
		"\3\u00d5\3\u00d5\3\u00d5\3\u00d5\3\u00d5\7\u00d5\u0870\n\u00d5\f\u00d5"+
		"\16\u00d5\u0873\13\u00d5\3\u00d5\3\u00d5\3\u00d5\3\u00d5\5\u00d5\u0879"+
		"\n\u00d5\3\u00d5\3\u00d5\3\u00d5\5\u00d5\u087e\n\u00d5\3\u00d5\3\u00d5"+
		"\3\u00d6\3\u00d6\5\u00d6\u0884\n\u00d6\3\u00d6\3\u00d6\3\u00d6\6\u00d6"+
		"\u0889\n\u00d6\r\u00d6\16\u00d6\u088a\3\u00d6\3\u00d6\3\u00d6\5\u00d6"+
		"\u0890\n\u00d6\3\u00d6\5\u00d6\u0893\n\u00d6\3\u00d6\3\u00d6\3\u00d7\3"+
		"\u00d7\3\u00d7\3\u00d7\3\u00d7\3\u00d8\5\u00d8\u089d\n\u00d8\3\u00d8\3"+
		"\u00d8\3\u00d8\3\u00d8\3\u00d8\5\u00d8\u08a4\n\u00d8\3\u00d8\3\u00d8\3"+
		"\u00d9\3\u00d9\3\u00d9\3\u00d9\5\u00d9\u08ac\n\u00d9\3\u00da\3\u00da\3"+
		"\u00da\3\u00da\3\u00db\3\u00db\5\u00db\u08b4\n\u00db\3\u00db\3\u00db\5"+
		"\u00db\u08b8\n\u00db\3\u00db\3\u00db\3\u00dc\3\u00dc\5\u00dc\u08be\n\u00dc"+
		"\3\u00dc\3\u00dc\5\u00dc\u08c2\n\u00dc\3\u00dc\3\u00dc\3\u00dd\3\u00dd"+
		"\5\u00dd\u08c8\n\u00dd\3\u00dd\3\u00dd\3\u00de\3\u00de\3\u00de\3\u00df"+
		"\3\u00df\3\u00df\3\u00df\5\u00df\u08d3\n\u00df\3\u00e0\3\u00e0\3\u00e0"+
		"\3\u00e0\3\u00e0\3\u00e0\5\u00e0\u08db\n\u00e0\3\u00e0\5\u00e0\u08de\n"+
		"\u00e0\3\u00e1\3\u00e1\3\u00e1\3\u00e1\3\u00e1\5\u00e1\u08e5\n\u00e1\3"+
		"\u00e1\5\u00e1\u08e8\n\u00e1\3\u00e1\3\u00e1\7\u00e1\u08ec\n\u00e1\f\u00e1"+
		"\16\u00e1\u08ef\13\u00e1\3\u00e1\3\u00e1\7\u00e1\u08f3\n\u00e1\f\u00e1"+
		"\16\u00e1\u08f6\13\u00e1\3\u00e1\3\u00e1\3\u00e1\5\u00e1\u08fb\n\u00e1"+
		"\3\u00e1\3\u00e1\3\u00e2\3\u00e2\3\u00e2\3\u00e2\5\u00e2\u0903\n\u00e2"+
		"\5\u00e2\u0905\n\u00e2\3\u00e2\3\u00e2\3\u00e2\3\u00e2\5\u00e2\u090b\n"+
		"\u00e2\5\u00e2\u090d\n\u00e2\3\u00e3\5\u00e3\u0910\n\u00e3\3\u00e3\3\u00e3"+
		"\3\u00e3\3\u00e3\3\u00e3\5\u00e3\u0917\n\u00e3\3\u00e3\5\u00e3\u091a\n"+
		"\u00e3\3\u00e3\7\u00e3\u091d\n\u00e3\f\u00e3\16\u00e3\u0920\13\u00e3\3"+
		"\u00e3\3\u00e3\7\u00e3\u0924\n\u00e3\f\u00e3\16\u00e3\u0927\13\u00e3\3"+
		"\u00e3\3\u00e3\5\u00e3\u092b\n\u00e3\3\u00e3\3\u00e3\5\u00e3\u092f\n\u00e3"+
		"\3\u00e3\3\u00e3\3\u00e4\3\u00e4\5\u00e4\u0935\n\u00e4\3\u00e5\3\u00e5"+
		"\3\u00e5\3\u00e5\3\u00e5\3\u00e5\3\u00e5\3\u00e5\3\u00e5\3\u00e5\3\u00e5"+
		"\3\u00e5\3\u00e5\3\u00e5\3\u00e5\5\u00e5\u0946\n\u00e5\3\u00e6\3\u00e6"+
		"\3\u00e6\5\u00e6\u094b\n\u00e6\3\u00e7\5\u00e7\u094e\n\u00e7\3\u00e7\3"+
		"\u00e7\3\u00e8\5\u00e8\u0953\n\u00e8\3\u00e8\3\u00e8\3\u00e9\5\u00e9\u0958"+
		"\n\u00e9\3\u00e9\3\u00e9\5\u00e9\u095c\n\u00e9\3\u00ea\3\u00ea\3\u00ea"+
		"\5\u00ea\u0961\n\u00ea\3\u00ea\5\u00ea\u0964\n\u00ea\3\u00ea\3\u00ea\5"+
		"\u00ea\u0968\n\u00ea\3\u00ea\3\u00ea\3\u00eb\3\u00eb\3\u00eb\3\u00eb\5"+
		"\u00eb\u0970\n\u00eb\3\u00eb\3\u00eb\3\u00eb\5\u00eb\u0975\n\u00eb\3\u00eb"+
		"\5\u00eb\u0978\n\u00eb\3\u00eb\3\u00eb\3\u00eb\3\u00ec\3\u00ec\5\u00ec"+
		"\u097f\n\u00ec\3\u00ec\5\u00ec\u0982\n\u00ec\3\u00ec\3\u00ec\3\u00ed\5"+
		"\u00ed\u0987\n\u00ed\3\u00ed\3\u00ed\3\u00ed\3\u00ed\3\u00ed\3\u00ed\3"+
		"\u00ed\5\u00ed\u0990\n\u00ed\3\u00ed\3\u00ed\5\u00ed\u0994\n\u00ed\3\u00ee"+
		"\3\u00ee\3\u00ee\5\u00ee\u0999\n\u00ee\3\u00ef\3\u00ef\3\u00ef\3\u00ef"+
		"\3\u00ef\3\u00ef\3\u00ef\5\u00ef\u09a2\n\u00ef\3\u00ef\3\u00ef\3\u00f0"+
		"\3\u00f0\3\u00f0\3\u00f0\5\u00f0\u09aa\n\u00f0\3\u00f0\3\u00f0\3\u00f0"+
		"\3\u00f0\3\u00f0\3\u00f0\3\u00f0\5\u00f0\u09b3\n\u00f0\3\u00f0\3\u00f0"+
		"\3\u00f0\3\u00f0\7\u00f0\u09b9\n\u00f0\f\u00f0\16\u00f0\u09bc\13\u00f0"+
		"\3\u00f0\3\u00f0\3\u00f0\3\u00f0\5\u00f0\u09c2\n\u00f0\3\u00f0\3\u00f0"+
		"\3\u00f0\5\u00f0\u09c7\n\u00f0\3\u00f0\3\u00f0\3\u00f0\5\u00f0\u09cc\n"+
		"\u00f0\3\u00f0\3\u00f0\3\u00f1\3\u00f1\3\u00f1\3\u00f1\6\u00f1\u09d4\n"+
		"\u00f1\r\u00f1\16\u00f1\u09d5\3\u00f1\3\u00f1\3\u00f1\5\u00f1\u09db\n"+
		"\u00f1\3\u00f1\3\u00f1\3\u00f2\3\u00f2\3\u00f2\3\u00f2\5\u00f2\u09e3\n"+
		"\u00f2\3\u00f2\3\u00f2\3\u00f2\3\u00f2\3\u00f3\7\u00f3\u09ea\n\u00f3\f"+
		"\u00f3\16\u00f3\u09ed\13\u00f3\3\u00f3\3\u00f3\7\u00f3\u09f1\n\u00f3\f"+
		"\u00f3\16\u00f3\u09f4\13\u00f3\3\u00f3\3\u00f3\5\u00f3\u09f8\n\u00f3\3"+
		"\u00f3\3\u00f3\7\u00f3\u09fc\n\u00f3\f\u00f3\16\u00f3\u09ff\13\u00f3\5"+
		"\u00f3\u0a01\n\u00f3\3\u00f4\7\u00f4\u0a04\n\u00f4\f\u00f4\16\u00f4\u0a07"+
		"\13\u00f4\3\u00f4\3\u00f4\7\u00f4\u0a0b\n\u00f4\f\u00f4\16\u00f4\u0a0e"+
		"\13\u00f4\3\u00f4\7\u00f4\u0a11\n\u00f4\f\u00f4\16\u00f4\u0a14\13\u00f4"+
		"\5\u00f4\u0a16\n\u00f4\3\u00f5\3\u00f5\3\u00f6\3\u00f6\3\u00f6\3\u00f6"+
		"\7\u00f6\u0a1e\n\u00f6\f\u00f6\16\u00f6\u0a21\13\u00f6\3\u00f6\3\u00f6"+
		"\3\u00f7\7\u00f7\u0a26\n\u00f7\f\u00f7\16\u00f7\u0a29\13\u00f7\3\u00f7"+
		"\3\u00f7\3\u00f8\3\u00f8\3\u00f8\3\u00f9\3\u00f9\5\u00f9\u0a32\n\u00f9"+
		"\3\u00fa\3\u00fa\3\u00fa\3\u00fa\3\u00fa\5\u00fa\u0a39\n\u00fa\3\u00fb"+
		"\3\u00fb\5\u00fb\u0a3d\n\u00fb\3\u00fc\3\u00fc\3\u00fc\3\u00fc\3\u00fd"+
		"\3\u00fd\3\u00fe\3\u00fe\3\u00fe\3\u00fe\3\u00fe\3\u00fe\5\u00fe\u0a4b"+
		"\n\u00fe\3\u00fe\5\u00fe\u0a4e\n\u00fe\3\u00fe\3\u00fe\3\u00ff\7\u00ff"+
		"\u0a53\n\u00ff\f\u00ff\16\u00ff\u0a56\13\u00ff\3\u0100\3\u0100\3\u0100"+
		"\5\u0100\u0a5b\n\u0100\3\u0101\3\u0101\3\u0101\3\u0101\7\u0101\u0a61\n"+
		"\u0101\f\u0101\16\u0101\u0a64\13\u0101\3\u0101\3\u0101\3\u0102\3\u0102"+
		"\3\u0102\2\5\6\u013a\u013c\u0103\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36"+
		" \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082"+
		"\u0084\u0086\u0088\u008a\u008c\u008e\u0090\u0092\u0094\u0096\u0098\u009a"+
		"\u009c\u009e\u00a0\u00a2\u00a4\u00a6\u00a8\u00aa\u00ac\u00ae\u00b0\u00b2"+
		"\u00b4\u00b6\u00b8\u00ba\u00bc\u00be\u00c0\u00c2\u00c4\u00c6\u00c8\u00ca"+
		"\u00cc\u00ce\u00d0\u00d2\u00d4\u00d6\u00d8\u00da\u00dc\u00de\u00e0\u00e2"+
		"\u00e4\u00e6\u00e8\u00ea\u00ec\u00ee\u00f0\u00f2\u00f4\u00f6\u00f8\u00fa"+
		"\u00fc\u00fe\u0100\u0102\u0104\u0106\u0108\u010a\u010c\u010e\u0110\u0112"+
		"\u0114\u0116\u0118\u011a\u011c\u011e\u0120\u0122\u0124\u0126\u0128\u012a"+
		"\u012c\u012e\u0130\u0132\u0134\u0136\u0138\u013a\u013c\u013e\u0140\u0142"+
		"\u0144\u0146\u0148\u014a\u014c\u014e\u0150\u0152\u0154\u0156\u0158\u015a"+
		"\u015c\u015e\u0160\u0162\u0164\u0166\u0168\u016a\u016c\u016e\u0170\u0172"+
		"\u0174\u0176\u0178\u017a\u017c\u017e\u0180\u0182\u0184\u0186\u0188\u018a"+
		"\u018c\u018e\u0190\u0192\u0194\u0196\u0198\u019a\u019c\u019e\u01a0\u01a2"+
		"\u01a4\u01a6\u01a8\u01aa\u01ac\u01ae\u01b0\u01b2\u01b4\u01b6\u01b8\u01ba"+
		"\u01bc\u01be\u01c0\u01c2\u01c4\u01c6\u01c8\u01ca\u01cc\u01ce\u01d0\u01d2"+
		"\u01d4\u01d6\u01d8\u01da\u01dc\u01de\u01e0\u01e2\u01e4\u01e6\u01e8\u01ea"+
		"\u01ec\u01ee\u01f0\u01f2\u01f4\u01f6\u01f8\u01fa\u01fc\u01fe\u0200\u0202"+
		"\2\24\3\2\3l\4\2\24\24SS\4\2$$\66\66\4\2..@@\4\2,,hh\4\2FF]]\7\2\6\6\62"+
		"\62FFMM]]\23\2\7\7\17\17\21\21\23\23\36\36$$()--\61\61\66\66AATUYY``b"+
		"beegg\5\2\36\36((\61\61\b\2\22\22++99EELLOO\4\2\u008e\u0098\u00a1\u00a1"+
		"\b\2!!%%<<>>[[^^\3\2\u0099\u009b\3\2\u0099\u009a\5\2\f\f\33\33\u009e\u009f"+
		"\5\2\b\bdd\u00a0\u00a0\4\2oorr\3\2mn\2\u0ae8\2\u0204\3\2\2\2\4\u0209\3"+
		"\2\2\2\6\u020e\3\2\2\2\b\u021d\3\2\2\2\n\u0222\3\2\2\2\f\u0227\3\2\2\2"+
		"\16\u022c\3\2\2\2\20\u022e\3\2\2\2\22\u0232\3\2\2\2\24\u023a\3\2\2\2\26"+
		"\u025e\3\2\2\2\30\u0263\3\2\2\2\32\u026a\3\2\2\2\34\u0288\3\2\2\2\36\u028a"+
		"\3\2\2\2 \u02aa\3\2\2\2\"\u02ac\3\2\2\2$\u02be\3\2\2\2&\u02c8\3\2\2\2"+
		"(\u02cc\3\2\2\2*\u02ce\3\2\2\2,\u02e4\3\2\2\2.\u02e9\3\2\2\2\60\u02eb"+
		"\3\2\2\2\62\u02fa\3\2\2\2\64\u030d\3\2\2\2\66\u0316\3\2\2\28\u0318\3\2"+
		"\2\2:\u031a\3\2\2\2<\u031c\3\2\2\2>\u0334\3\2\2\2@\u0336\3\2\2\2B\u0343"+
		"\3\2\2\2D\u0354\3\2\2\2F\u0372\3\2\2\2H\u0374\3\2\2\2J\u0388\3\2\2\2L"+
		"\u0396\3\2\2\2N\u0398\3\2\2\2P\u03a0\3\2\2\2R\u03a2\3\2\2\2T\u03a4\3\2"+
		"\2\2V\u03b1\3\2\2\2X\u03b3\3\2\2\2Z\u03b5\3\2\2\2\\\u03c3\3\2\2\2^\u03c6"+
		"\3\2\2\2`\u03cb\3\2\2\2b\u03cf\3\2\2\2d\u03d3\3\2\2\2f\u03d5\3\2\2\2h"+
		"\u03e3\3\2\2\2j\u03e8\3\2\2\2l\u03f6\3\2\2\2n\u03f8\3\2\2\2p\u03fa\3\2"+
		"\2\2r\u0407\3\2\2\2t\u0409\3\2\2\2v\u0414\3\2\2\2x\u0419\3\2\2\2z\u0421"+
		"\3\2\2\2|\u0423\3\2\2\2~\u042e\3\2\2\2\u0080\u0431\3\2\2\2\u0082\u0434"+
		"\3\2\2\2\u0084\u0438\3\2\2\2\u0086\u043e\3\2\2\2\u0088\u0440\3\2\2\2\u008a"+
		"\u0450\3\2\2\2\u008c\u0452\3\2\2\2\u008e\u0462\3\2\2\2\u0090\u0464\3\2"+
		"\2\2\u0092\u046f\3\2\2\2\u0094\u0471\3\2\2\2\u0096\u0478\3\2\2\2\u0098"+
		"\u0483\3\2\2\2\u009a\u0487\3\2\2\2\u009c\u0489\3\2\2\2\u009e\u048b\3\2"+
		"\2\2\u00a0\u0493\3\2\2\2\u00a2\u0496\3\2\2\2\u00a4\u049a\3\2\2\2\u00a6"+
		"\u049e\3\2\2\2\u00a8\u04a4\3\2\2\2\u00aa\u04a6\3\2\2\2\u00ac\u04b0\3\2"+
		"\2\2\u00ae\u04bd\3\2\2\2\u00b0\u04c0\3\2\2\2\u00b2\u04cc\3\2\2\2\u00b4"+
		"\u04d7\3\2\2\2\u00b6\u04df\3\2\2\2\u00b8\u04e5\3\2\2\2\u00ba\u04eb\3\2"+
		"\2\2\u00bc\u04ed\3\2\2\2\u00be\u04f9\3\2\2\2\u00c0\u0508\3\2\2\2\u00c2"+
		"\u0513\3\2\2\2\u00c4\u0518\3\2\2\2\u00c6\u051a\3\2\2\2\u00c8\u051c\3\2"+
		"\2\2\u00ca\u051f\3\2\2\2\u00cc\u0526\3\2\2\2\u00ce\u0528\3\2\2\2\u00d0"+
		"\u0534\3\2\2\2\u00d2\u0546\3\2\2\2\u00d4\u0548\3\2\2\2\u00d6\u055a\3\2"+
		"\2\2\u00d8\u055c\3\2\2\2\u00da\u0564\3\2\2\2\u00dc\u0566\3\2\2\2\u00de"+
		"\u056c\3\2\2\2\u00e0\u056e\3\2\2\2\u00e2\u0574\3\2\2\2\u00e4\u0576\3\2"+
		"\2\2\u00e6\u0584\3\2\2\2\u00e8\u0588\3\2\2\2\u00ea\u0595\3\2\2\2\u00ec"+
		"\u059d\3\2\2\2\u00ee\u059f\3\2\2\2\u00f0\u05a3\3\2\2\2\u00f2\u05a7\3\2"+
		"\2\2\u00f4\u05b7\3\2\2\2\u00f6\u05b9\3\2\2\2\u00f8\u05bf\3\2\2\2\u00fa"+
		"\u05d1\3\2\2\2\u00fc\u05d9\3\2\2\2\u00fe\u05e1\3\2\2\2\u0100\u05e5\3\2"+
		"\2\2\u0102\u05ee\3\2\2\2\u0104\u05f6\3\2\2\2\u0106\u05f8\3\2\2\2\u0108"+
		"\u0600\3\2\2\2\u010a\u0604\3\2\2\2\u010c\u0610\3\2\2\2\u010e\u0612\3\2"+
		"\2\2\u0110\u0619\3\2\2\2\u0112\u061d\3\2\2\2\u0114\u061f\3\2\2\2\u0116"+
		"\u0628\3\2\2\2\u0118\u0637\3\2\2\2\u011a\u0645\3\2\2\2\u011c\u0649\3\2"+
		"\2\2\u011e\u065c\3\2\2\2\u0120\u065e\3\2\2\2\u0122\u0662\3\2\2\2\u0124"+
		"\u066a\3\2\2\2\u0126\u0670\3\2\2\2\u0128\u067e\3\2\2\2\u012a\u0682\3\2"+
		"\2\2\u012c\u0684\3\2\2\2\u012e\u068e\3\2\2\2\u0130\u0690\3\2\2\2\u0132"+
		"\u069d\3\2\2\2\u0134\u06a4\3\2\2\2\u0136\u06ae\3\2\2\2\u0138\u06b3\3\2"+
		"\2\2\u013a\u06be\3\2\2\2\u013c\u06e0\3\2\2\2\u013e\u06f5\3\2\2\2\u0140"+
		"\u06f7\3\2\2\2\u0142\u06f9\3\2\2\2\u0144\u06fb\3\2\2\2\u0146\u06fd\3\2"+
		"\2\2\u0148\u06ff\3\2\2\2\u014a\u0701\3\2\2\2\u014c\u0703\3\2\2\2\u014e"+
		"\u070e\3\2\2\2\u0150\u0711\3\2\2\2\u0152\u0715\3\2\2\2\u0154\u0723\3\2"+
		"\2\2\u0156\u0727\3\2\2\2\u0158\u0732\3\2\2\2\u015a\u0734\3\2\2\2\u015c"+
		"\u0738\3\2\2\2\u015e\u0740\3\2\2\2\u0160\u0746\3\2\2\2\u0162\u0757\3\2"+
		"\2\2\u0164\u0763\3\2\2\2\u0166\u0766\3\2\2\2\u0168\u076e\3\2\2\2\u016a"+
		"\u0771\3\2\2\2\u016c\u0773\3\2\2\2\u016e\u0776\3\2\2\2\u0170\u0779\3\2"+
		"\2\2\u0172\u0783\3\2\2\2\u0174\u078e\3\2\2\2\u0176\u0793\3\2\2\2\u0178"+
		"\u0795\3\2\2\2\u017a\u079d\3\2\2\2\u017c\u07a6\3\2\2\2\u017e\u07ae\3\2"+
		"\2\2\u0180\u07b6\3\2\2\2\u0182\u07ba\3\2\2\2\u0184\u07c5\3\2\2\2\u0186"+
		"\u07d1\3\2\2\2\u0188\u07d5\3\2\2\2\u018a\u07d7\3\2\2\2\u018c\u07df\3\2"+
		"\2\2\u018e\u07f1\3\2\2\2\u0190\u07fa\3\2\2\2\u0192\u080e\3\2\2\2\u0194"+
		"\u0810\3\2\2\2\u0196\u081e\3\2\2\2\u0198\u082b\3\2\2\2\u019a\u083a\3\2"+
		"\2\2\u019c\u084a\3\2\2\2\u019e\u084c\3\2\2\2\u01a0\u0851\3\2\2\2\u01a2"+
		"\u0856\3\2\2\2\u01a4\u0861\3\2\2\2\u01a6\u0864\3\2\2\2\u01a8\u0866\3\2"+
		"\2\2\u01aa\u0881\3\2\2\2\u01ac\u0896\3\2\2\2\u01ae\u089c\3\2\2\2\u01b0"+
		"\u08ab\3\2\2\2\u01b2\u08ad\3\2\2\2\u01b4\u08b1\3\2\2\2\u01b6\u08bb\3\2"+
		"\2\2\u01b8\u08c5\3\2\2\2\u01ba\u08cb\3\2\2\2\u01bc\u08d2\3\2\2\2\u01be"+
		"\u08dd\3\2\2\2\u01c0\u08df\3\2\2\2\u01c2\u0904\3\2\2\2\u01c4\u090f\3\2"+
		"\2\2\u01c6\u0934\3\2\2\2\u01c8\u0945\3\2\2\2\u01ca\u094a\3\2\2\2\u01cc"+
		"\u094d\3\2\2\2\u01ce\u0952\3\2\2\2\u01d0\u0957\3\2\2\2\u01d2\u095d\3\2"+
		"\2\2\u01d4\u096b\3\2\2\2\u01d6\u097c\3\2\2\2\u01d8\u0993\3\2\2\2\u01da"+
		"\u0998\3\2\2\2\u01dc\u099a\3\2\2\2\u01de\u09a5\3\2\2\2\u01e0\u09cf\3\2"+
		"\2\2\u01e2\u09de\3\2\2\2\u01e4\u0a00\3\2\2\2\u01e6\u0a15\3\2\2\2\u01e8"+
		"\u0a17\3\2\2\2\u01ea\u0a19\3\2\2\2\u01ec\u0a27\3\2\2\2\u01ee\u0a2c\3\2"+
		"\2\2\u01f0\u0a31\3\2\2\2\u01f2\u0a38\3\2\2\2\u01f4\u0a3c\3\2\2\2\u01f6"+
		"\u0a3e\3\2\2\2\u01f8\u0a42\3\2\2\2\u01fa\u0a44\3\2\2\2\u01fc\u0a54\3\2"+
		"\2\2\u01fe\u0a5a\3\2\2\2\u0200\u0a5c\3\2\2\2\u0202\u0a67\3\2\2\2\u0204"+
		"\u0205\t\2\2\2\u0205\3\3\2\2\2\u0206\u020a\5\u0202\u0102\2\u0207\u020a"+
		"\58\35\2\u0208\u020a\7s\2\2\u0209\u0206\3\2\2\2\u0209\u0207\3\2\2\2\u0209"+
		"\u0208\3\2\2\2\u020a\5\3\2\2\2\u020b\u020c\b\4\1\2\u020c\u020f\5\4\3\2"+
		"\u020d\u020f\5\u012c\u0097\2\u020e\u020b\3\2\2\2\u020e\u020d\3\2\2\2\u020f"+
		"\u021a\3\2\2\2\u0210\u0216\f\4\2\2\u0211\u0217\5\b\5\2\u0212\u0217\5\n"+
		"\6\2\u0213\u0217\5\u00e4s\2\u0214\u0215\7\u008b\2\2\u0215\u0217\5\16\b"+
		"\2\u0216\u0211\3\2\2\2\u0216\u0212\3\2\2\2\u0216\u0213\3\2\2\2\u0216\u0214"+
		"\3\2\2\2\u0217\u0219\3\2\2\2\u0218\u0210\3\2\2\2\u0219\u021c\3\2\2\2\u021a"+
		"\u0218\3\2\2\2\u021a\u021b\3\2\2\2\u021b\7\3\2\2\2\u021c\u021a\3\2\2\2"+
		"\u021d\u021e\7\u0081\2\2\u021e\u021f\5\20\t\2\u021f\u0220\7\u0082\2\2"+
		"\u0220\t\3\2\2\2\u0221\u0223\5B\"\2\u0222\u0221\3\2\2\2\u0222\u0223\3"+
		"\2\2\2\u0223\u0224\3\2\2\2\u0224\u0225\7\u0085\2\2\u0225\u0226\5\u012a"+
		"\u0096\2\u0226\13\3\2\2\2\u0227\u0228\5\6\4\2\u0228\u0229\5\n\6\2\u0229"+
		"\r\3\2\2\2\u022a\u022d\5\4\3\2\u022b\u022d\7B\2\2\u022c\u022a\3\2\2\2"+
		"\u022c\u022b\3\2\2\2\u022d\17\3\2\2\2\u022e\u022f\5\u013c\u009f\2\u022f"+
		"\u0230\5R*\2\u0230\u0231\5\u013c\u009f\2\u0231\21\3\2\2\2\u0232\u0237"+
		"\5\u0202\u0102\2\u0233\u0234\7\u008b\2\2\u0234\u0236\5\16\b\2\u0235\u0233"+
		"\3\2\2\2\u0236\u0239\3\2\2\2\u0237\u0235\3\2\2\2\u0237\u0238\3\2\2\2\u0238"+
		"\23\3\2\2\2\u0239\u0237\3\2\2\2\u023a\u023b\7\17\2\2\u023b\u023c\5\u0202"+
		"\u0102\2\u023c\u023e\7_\2\2\u023d\u023f\5\u00dco\2\u023e\u023d\3\2\2\2"+
		"\u023e\u023f\3\2\2\2\u023f\u0241\3\2\2\2\u0240\u0242\5\u00e0q\2\u0241"+
		"\u0240\3\2\2\2\u0241\u0242\3\2\2\2\u0242\u0246\3\2\2\2\u0243\u0245\5\26"+
		"\f\2\u0244\u0243\3\2\2\2\u0245\u0248\3\2\2\2\u0246\u0244\3\2\2\2\u0246"+
		"\u0247\3\2\2\2\u0247\u0250\3\2\2\2\u0248\u0246\3\2\2\2\u0249\u024d\7 "+
		"\2\2\u024a\u024c\5\30\r\2\u024b\u024a\3\2\2\2\u024c\u024f\3\2\2\2\u024d"+
		"\u024b\3\2\2\2\u024d\u024e\3\2\2\2\u024e\u0251\3\2\2\2\u024f\u024d\3\2"+
		"\2\2\u0250\u0249\3\2\2\2\u0250\u0251\3\2\2\2\u0251\u0252\3\2\2\2\u0252"+
		"\u0254\7\67\2\2\u0253\u0255\7\17\2\2\u0254\u0253\3\2\2\2\u0254\u0255\3"+
		"\2\2\2\u0255\u0257\3\2\2\2\u0256\u0258\5\u0202\u0102\2\u0257\u0256\3\2"+
		"\2\2\u0257\u0258\3\2\2\2\u0258\u0259\3\2\2\2\u0259\u025a\7\u0080\2\2\u025a"+
		"\25\3\2\2\2\u025b\u025f\5\u00acW\2\u025c\u025f\5\u01ca\u00e6\2\u025d\u025f"+
		"\5\u0124\u0093\2\u025e\u025b\3\2\2\2\u025e\u025c\3\2\2\2\u025e\u025d\3"+
		"\2\2\2\u025f\27\3\2\2\2\u0260\u0261\5\u01e8\u00f5\2\u0261\u0262\7\u008d"+
		"\2\2\u0262\u0264\3\2\2\2\u0263\u0260\3\2\2\2\u0263\u0264\3\2\2\2\u0264"+
		"\u0268\3\2\2\2\u0265\u0269\5\u01ce\u00e8\2\u0266\u0269\5\u01cc\u00e7\2"+
		"\u0267\u0269\5\u01c4\u00e3\2\u0268\u0265\3\2\2\2\u0268\u0266\3\2\2\2\u0268"+
		"\u0267\3\2\2\2\u0269\31\3\2\2\2\u026a\u026b\7g\2\2\u026b\u026c\5\u0202"+
		"\u0102\2\u026c\u026d\7#\2\2\u026d\u026e\5\6\4\2\u026e\u0272\7_\2\2\u026f"+
		"\u0271\5\34\17\2\u0270\u026f\3\2\2\2\u0271\u0274\3\2\2\2\u0272\u0270\3"+
		"\2\2\2\u0272\u0273\3\2\2\2\u0273\u0275\3\2\2\2\u0274\u0272\3\2\2\2\u0275"+
		"\u0279\7 \2\2\u0276\u0278\5\u01be\u00e0\2\u0277\u0276\3\2\2\2\u0278\u027b"+
		"\3\2\2\2\u0279\u0277\3\2\2\2\u0279\u027a\3\2\2\2\u027a\u027c\3\2\2\2\u027b"+
		"\u0279\3\2\2\2\u027c\u027e\7\67\2\2\u027d\u027f\7g\2\2\u027e\u027d\3\2"+
		"\2\2\u027e\u027f\3\2\2\2\u027f\u0281\3\2\2\2\u0280\u0282\5\u0202\u0102"+
		"\2\u0281\u0280\3\2\2\2\u0281\u0282\3\2\2\2\u0282\u0283\3\2\2\2\u0283\u0284"+
		"\7\u0080\2\2\u0284\33\3\2\2\2\u0285\u0289\5\26\f\2\u0286\u0289\5\u00f8"+
		"}\2\u0287\u0289\5\u0112\u008a\2\u0288\u0285\3\2\2\2\u0288\u0286\3\2\2"+
		"\2\u0288\u0287\3\2\2\2\u0289\35\3\2\2\2\u028a\u028b\7e\2\2\u028b\u028c"+
		"\5\u0202\u0102\2\u028c\u028d\7#\2\2\u028d\u028e\5\6\4\2\u028e\u0292\7"+
		"_\2\2\u028f\u0291\5 \21\2\u0290\u028f\3\2\2\2\u0291\u0294\3\2\2\2\u0292"+
		"\u0290\3\2\2\2\u0292\u0293\3\2\2\2\u0293\u029a\3\2\2\2\u0294\u0292\3\2"+
		"\2\2\u0295\u0296\5\u0120\u0091\2\u0296\u0297\7\u0080\2\2\u0297\u0299\3"+
		"\2\2\2\u0298\u0295\3\2\2\2\u0299\u029c\3\2\2\2\u029a\u0298\3\2\2\2\u029a"+
		"\u029b\3\2\2\2\u029b\u029d\3\2\2\2\u029c\u029a\3\2\2\2\u029d\u029e\5\""+
		"\22\2\u029e\u02a0\7\67\2\2\u029f\u02a1\7e\2\2\u02a0\u029f\3\2\2\2\u02a0"+
		"\u02a1\3\2\2\2\u02a1\u02a3\3\2\2\2\u02a2\u02a4\5\u0202\u0102\2\u02a3\u02a2"+
		"\3\2\2\2\u02a3\u02a4\3\2\2\2\u02a4\u02a5\3\2\2\2\u02a5\u02a6\7\u0080\2"+
		"\2\u02a6\37\3\2\2\2\u02a7\u02ab\5\u01ea\u00f6\2\u02a8\u02ab\5\u0106\u0084"+
		"\2\u02a9\u02ab\5\u0100\u0081\2\u02aa\u02a7\3\2\2\2\u02aa\u02a8\3\2\2\2"+
		"\u02aa\u02a9\3\2\2\2\u02ab!\3\2\2\2\u02ac\u02ad\7Z\2\2\u02ad\u02b1\5$"+
		"\23\2\u02ae\u02b0\5\u01ea\u00f6\2\u02af\u02ae\3\2\2\2\u02b0\u02b3\3\2"+
		"\2\2\u02b1\u02af\3\2\2\2\u02b1\u02b2\3\2\2\2\u02b2\u02b7\3\2\2\2\u02b3"+
		"\u02b1\3\2\2\2\u02b4\u02b6\5(\25\2\u02b5\u02b4\3\2\2\2\u02b6\u02b9\3\2"+
		"\2\2\u02b7\u02b5\3\2\2\2\u02b7\u02b8\3\2\2\2\u02b8\u02ba\3\2\2\2\u02b9"+
		"\u02b7\3\2\2\2\u02ba\u02bb\7\67\2\2\u02bb\u02bc\7Z\2\2\u02bc\u02bd\7\u0080"+
		"\2\2\u02bd#\3\2\2\2\u02be\u02c3\5\u01e8\u00f5\2\u02bf\u02c0\7\u0081\2"+
		"\2\u02c0\u02c1\5&\24\2\u02c1\u02c2\7\u0082\2\2\u02c2\u02c4\3\2\2\2\u02c3"+
		"\u02bf\3\2\2\2\u02c3\u02c4\3\2\2\2\u02c4%\3\2\2\2\u02c5\u02c9\5r:\2\u02c6"+
		"\u02c9\5\u013a\u009e\2\u02c7\u02c9\5\u01e8\u00f5\2\u02c8\u02c5\3\2\2\2"+
		"\u02c8\u02c6\3\2\2\2\u02c8\u02c7\3\2\2\2\u02c9\'\3\2\2\2\u02ca\u02cd\5"+
		"\"\22\2\u02cb\u02cd\5*\26\2\u02cc\u02ca\3\2\2\2\u02cc\u02cb\3\2\2\2\u02cd"+
		")\3\2\2\2\u02ce\u02cf\7Z\2\2\u02cf\u02d3\5\u0118\u008d\2\u02d0\u02d1\5"+
		"\u011c\u008f\2\u02d1\u02d2\7\u0080\2\2\u02d2\u02d4\3\2\2\2\u02d3\u02d0"+
		"\3\2\2\2\u02d3\u02d4\3\2\2\2\u02d4\u02da\3\2\2\2\u02d5\u02d6\5\u0120\u0091"+
		"\2\u02d6\u02d7\7\u0080\2\2\u02d7\u02d9\3\2\2\2\u02d8\u02d5\3\2\2\2\u02d9"+
		"\u02dc\3\2\2\2\u02da\u02d8\3\2\2\2\u02da\u02db\3\2\2\2\u02db\u02de\3\2"+
		"\2\2\u02dc\u02da\3\2\2\2\u02dd\u02df\5\"\22\2\u02de\u02dd\3\2\2\2\u02de"+
		"\u02df\3\2\2\2\u02df\u02e0\3\2\2\2\u02e0\u02e1\7\67\2\2\u02e1\u02e2\7"+
		"Z\2\2\u02e2\u02e3\7\u0080\2\2\u02e3+\3\2\2\2\u02e4\u02e5\5.\30\2\u02e5"+
		"\u02e6\7\u0080\2\2\u02e6-\3\2\2\2\u02e7\u02ea\5\60\31\2\u02e8\u02ea\5"+
		"\62\32\2\u02e9\u02e7\3\2\2\2\u02e9\u02e8\3\2\2\2\u02ea/\3\2\2\2\u02eb"+
		"\u02ec\7$\2\2\u02ec\u02ee\5\66\34\2\u02ed\u02ef\5\64\33\2\u02ee\u02ed"+
		"\3\2\2\2\u02ee\u02ef\3\2\2\2\u02ef\u02f7\3\2\2\2\u02f0\u02f2\7W\2\2\u02f1"+
		"\u02f0\3\2\2\2\u02f1\u02f2\3\2\2\2\u02f2\u02f3\3\2\2\2\u02f3\u02f4\7\u0081"+
		"\2\2\u02f4\u02f5\5:\36\2\u02f5\u02f6\7\u0082\2\2\u02f6\u02f8\3\2\2\2\u02f7"+
		"\u02f1\3\2\2\2\u02f7\u02f8\3\2\2\2\u02f8\61\3\2\2\2\u02f9\u02fb\t\3\2"+
		"\2\u02fa\u02f9\3\2\2\2\u02fa\u02fb\3\2\2\2\u02fb\u02fc\3\2\2\2\u02fc\u02fd"+
		"\7\66\2\2\u02fd\u02ff\5\66\34\2\u02fe\u0300\5\64\33\2\u02ff\u02fe\3\2"+
		"\2\2\u02ff\u0300\3\2\2\2\u0300\u0308\3\2\2\2\u0301\u0303\7W\2\2\u0302"+
		"\u0301\3\2\2\2\u0302\u0303\3\2\2\2\u0303\u0304\3\2\2\2\u0304\u0305\7\u0081"+
		"\2\2\u0305\u0306\5:\36\2\u0306\u0307\7\u0082\2\2\u0307\u0309\3\2\2\2\u0308"+
		"\u0302\3\2\2\2\u0308\u0309\3\2\2\2\u0309\u030a\3\2\2\2\u030a\u030b\7I"+
		"\2\2\u030b\u030c\5\u00a2R\2\u030c\63\3\2\2\2\u030d\u030e\7\26\2\2\u030e"+
		"\u030f\7\u0081\2\2\u030f\u0310\5\u00dep\2\u0310\u0312\7\u0082\2\2\u0311"+
		"\u0313\5\u00eex\2\u0312\u0311\3\2\2\2\u0312\u0313\3\2\2\2\u0313\65\3\2"+
		"\2\2\u0314\u0317\5\u0202\u0102\2\u0315\u0317\58\35\2\u0316\u0314\3\2\2"+
		"\2\u0316\u0315\3\2\2\2\u0317\67\3\2\2\2\u0318\u0319\7t\2\2\u03199\3\2"+
		"\2\2\u031a\u031b\5\u00d8m\2\u031b;\3\2\2\2\u031c\u031d\5.\30\2\u031d\u0321"+
		"\7_\2\2\u031e\u0320\5\u01ca\u00e6\2\u031f\u031e\3\2\2\2\u0320\u0323\3"+
		"\2\2\2\u0321\u031f\3\2\2\2\u0321\u0322\3\2\2\2\u0322\u0324\3\2\2\2\u0323"+
		"\u0321\3\2\2\2\u0324\u0328\7 \2\2\u0325\u0327\5\u0160\u00b1\2\u0326\u0325"+
		"\3\2\2\2\u0327\u032a\3\2\2\2\u0328\u0326\3\2\2\2\u0328\u0329\3\2\2\2\u0329"+
		"\u032b\3\2\2\2\u032a\u0328\3\2\2\2\u032b\u032d\7\67\2\2\u032c\u032e\5"+
		"> \2\u032d\u032c\3\2\2\2\u032d\u032e\3\2\2\2\u032e\u0330\3\2\2\2\u032f"+
		"\u0331\5\66\34\2\u0330\u032f\3\2\2\2\u0330\u0331\3\2\2\2\u0331\u0332\3"+
		"\2\2\2\u0332\u0333\7\u0080\2\2\u0333=\3\2\2\2\u0334\u0335\t\4\2\2\u0335"+
		"?\3\2\2\2\u0336\u0337\5> \2\u0337\u0338\5\66\34\2\u0338\u0339\7_\2\2\u0339"+
		"\u033a\7/\2\2\u033a\u033c\5\6\4\2\u033b\u033d\5B\"\2\u033c\u033b\3\2\2"+
		"\2\u033c\u033d\3\2\2\2\u033d\u033f\3\2\2\2\u033e\u0340\5\u00eex\2\u033f"+
		"\u033e\3\2\2\2\u033f\u0340\3\2\2\2\u0340\u0341\3\2\2\2\u0341\u0342\7\u0080"+
		"\2\2\u0342A\3\2\2\2\u0343\u034c\7\u0083\2\2\u0344\u0349\5\u00a2R\2\u0345"+
		"\u0346\7\u008a\2\2\u0346\u0348\5\u00a2R\2\u0347\u0345\3\2\2\2\u0348\u034b"+
		"\3\2\2\2\u0349\u0347\3\2\2\2\u0349\u034a\3\2\2\2\u034a\u034d\3\2\2\2\u034b"+
		"\u0349\3\2\2\2\u034c\u0344\3\2\2\2\u034c\u034d\3\2\2\2\u034d\u0350\3\2"+
		"\2\2\u034e\u034f\7I\2\2\u034f\u0351\5\u00a2R\2\u0350\u034e\3\2\2\2\u0350"+
		"\u0351\3\2\2\2\u0351\u0352\3\2\2\2\u0352\u0353\7\u0084\2\2\u0353C\3\2"+
		"\2\2\u0354\u0355\7T\2\2\u0355\u0356\5\u0202\u0102\2\u0356\u035d\7_\2\2"+
		"\u0357\u035b\5\u00dco\2\u0358\u0359\5\u00eex\2\u0359\u035a\7\u0080\2\2"+
		"\u035a\u035c\3\2\2\2\u035b\u0358\3\2\2\2\u035b\u035c\3\2\2\2\u035c\u035e"+
		"\3\2\2\2\u035d\u0357\3\2\2\2\u035d\u035e\3\2\2\2\u035e\u0362\3\2\2\2\u035f"+
		"\u0361\5F$\2\u0360\u035f\3\2\2\2\u0361\u0364\3\2\2\2\u0362\u0360\3\2\2"+
		"\2\u0362\u0363\3\2\2\2\u0363\u0365\3\2\2\2\u0364\u0362\3\2\2\2\u0365\u0367"+
		"\7\67\2\2\u0366\u0368\7T\2\2\u0367\u0366\3\2\2\2\u0367\u0368\3\2\2\2\u0368"+
		"\u036a\3\2\2\2\u0369\u036b\5\u0202\u0102\2\u036a\u0369\3\2\2\2\u036a\u036b"+
		"\3\2\2\2\u036b\u036c\3\2\2\2\u036c\u036d\7\u0080\2\2\u036dE\3\2\2\2\u036e"+
		"\u0373\5\u01c8\u00e5\2\u036f\u0373\5\u00acW\2\u0370\u0373\5\u00f8}\2\u0371"+
		"\u0373\5\u0124\u0093\2\u0372\u036e\3\2\2\2\u0372\u036f\3\2\2\2\u0372\u0370"+
		"\3\2\2\2\u0372\u0371\3\2\2\2\u0373G\3\2\2\2\u0374\u0375\7T\2\2\u0375\u0376"+
		"\7\63\2\2\u0376\u0377\5\u0202\u0102\2\u0377\u037b\7_\2\2\u0378\u037a\5"+
		"\u01ca\u00e6\2\u0379\u0378\3\2\2\2\u037a\u037d\3\2\2\2\u037b\u0379\3\2"+
		"\2\2\u037b\u037c\3\2\2\2\u037c\u037e\3\2\2\2\u037d\u037b\3\2\2\2\u037e"+
		"\u0381\7\67\2\2\u037f\u0380\7T\2\2\u0380\u0382\7\63\2\2\u0381\u037f\3"+
		"\2\2\2\u0381\u0382\3\2\2\2\u0382\u0384\3\2\2\2\u0383\u0385\5\u0202\u0102"+
		"\2\u0384\u0383\3\2\2\2\u0384\u0385\3\2\2\2\u0385\u0386\3\2\2\2\u0386\u0387"+
		"\7\u0080\2\2\u0387I\3\2\2\2\u0388\u0389\7T\2\2\u0389\u038a\5\u0202\u0102"+
		"\2\u038a\u038b\7_\2\2\u038b\u038c\7/\2\2\u038c\u038e\5\6\4\2\u038d\u038f"+
		"\5\u00eex\2\u038e\u038d\3\2\2\2\u038e\u038f\3\2\2\2\u038f\u0390\3\2\2"+
		"\2\u0390\u0391\7\u0080\2\2\u0391K\3\2\2\2\u0392\u0397\5T+\2\u0393\u0397"+
		"\5X-\2\u0394\u0397\5`\61\2\u0395\u0397\5Z.\2\u0396\u0392\3\2\2\2\u0396"+
		"\u0393\3\2\2\2\u0396\u0394\3\2\2\2\u0396\u0395\3\2\2\2\u0397M\3\2\2\2"+
		"\u0398\u0399\7\27\2\2\u0399\u039a\5P)\2\u039aO\3\2\2\2\u039b\u03a1\5\f"+
		"\7\2\u039c\u039d\5\u013c\u009f\2\u039d\u039e\5R*\2\u039e\u039f\5\u013c"+
		"\u009f\2\u039f\u03a1\3\2\2\2\u03a0\u039b\3\2\2\2\u03a0\u039c\3\2\2\2\u03a1"+
		"Q\3\2\2\2\u03a2\u03a3\t\5\2\2\u03a3S\3\2\2\2\u03a4\u03a5\7\u0081\2\2\u03a5"+
		"\u03aa\5V,\2\u03a6\u03a7\7\u008a\2\2\u03a7\u03a9\5V,\2\u03a8\u03a6\3\2"+
		"\2\2\u03a9\u03ac\3\2\2\2\u03aa\u03a8\3\2\2\2\u03aa\u03ab\3\2\2\2\u03ab"+
		"\u03ad\3\2\2\2\u03ac\u03aa\3\2\2\2\u03ad\u03ae\7\u0082\2\2\u03aeU\3\2"+
		"\2\2\u03af\u03b2\5\u0202\u0102\2\u03b0\u03b2\7s\2\2\u03b1\u03af\3\2\2"+
		"\2\u03b1\u03b0\3\2\2\2\u03b2W\3\2\2\2\u03b3\u03b4\5N(\2\u03b4Y\3\2\2\2"+
		"\u03b5\u03b6\5N(\2\u03b6\u03b7\7U\2\2\u03b7\u03bb\5\\/\2\u03b8\u03ba\5"+
		"^\60\2\u03b9\u03b8\3\2\2\2\u03ba\u03bd\3\2\2\2\u03bb\u03b9\3\2\2\2\u03bb"+
		"\u03bc\3\2\2\2\u03bc\u03be\3\2\2\2\u03bd\u03bb\3\2\2\2\u03be\u03bf\7\67"+
		"\2\2\u03bf\u03c1\7U\2\2\u03c0\u03c2\5\u0202\u0102\2\u03c1\u03c0\3\2\2"+
		"\2\u03c1\u03c2\3\2\2\2\u03c2[\3\2\2\2\u03c3\u03c4\5\u0202\u0102\2\u03c4"+
		"\u03c5\7\u0080\2\2\u03c5]\3\2\2\2\u03c6\u03c7\5\u0202\u0102\2\u03c7\u03c8"+
		"\7\u008e\2\2\u03c8\u03c9\5\u0150\u00a9\2\u03c9\u03ca\7\u0080\2\2\u03ca"+
		"_\3\2\2\2\u03cb\u03cc\5N(\2\u03cca\3\2\2\2\u03cd\u03d0\5d\63\2\u03ce\u03d0"+
		"\5t;\2\u03cf\u03cd\3\2\2\2\u03cf\u03ce\3\2\2\2\u03d0c\3\2\2\2\u03d1\u03d4"+
		"\5f\64\2\u03d2\u03d4\5h\65\2\u03d3\u03d1\3\2\2\2\u03d3\u03d2\3\2\2\2\u03d4"+
		"e\3\2\2\2\u03d5\u03d6\7P\2\2\u03d6\u03d7\7\u0081\2\2\u03d7\u03dc\5j\66"+
		"\2\u03d8\u03d9\7\u008a\2\2\u03d9\u03db\5j\66\2\u03da\u03d8\3\2\2\2\u03db"+
		"\u03de\3\2\2\2\u03dc\u03da\3\2\2\2\u03dc\u03dd\3\2\2\2\u03dd\u03df\3\2"+
		"\2\2\u03de\u03dc\3\2\2\2\u03df\u03e0\7\u0082\2\2\u03e0\u03e1\7#\2\2\u03e1"+
		"\u03e2\5\u0096L\2\u03e2g\3\2\2\2\u03e3\u03e4\7P\2\2\u03e4\u03e5\5p9\2"+
		"\u03e5\u03e6\7#\2\2\u03e6\u03e7\5\u0096L\2\u03e7i\3\2\2\2\u03e8\u03e9"+
		"\5\u00a2R\2\u03e9\u03ea\7\27\2\2\u03ea\u03eb\7\u00a5\2\2\u03ebk\3\2\2"+
		"\2\u03ec\u03ee\5p9\2\u03ed\u03ef\5n8\2\u03ee\u03ed\3\2\2\2\u03ee\u03ef"+
		"\3\2\2\2\u03ef\u03f7\3\2\2\2\u03f0\u03f1\7\u0081\2\2\u03f1\u03f2\7f\2"+
		"\2\u03f2\u03f4\7\u0082\2\2\u03f3\u03f5\5n8\2\u03f4\u03f3\3\2\2\2\u03f4"+
		"\u03f5\3\2\2\2\u03f5\u03f7\3\2\2\2\u03f6\u03ec\3\2\2\2\u03f6\u03f0\3\2"+
		"\2\2\u03f7m\3\2\2\2\u03f8\u03f9\5\u00a6T\2\u03f9o\3\2\2\2\u03fa\u03fb"+
		"\7\u0081\2\2\u03fb\u0400\5r:\2\u03fc\u03fd\7\u008a\2\2\u03fd\u03ff\5r"+
		":\2\u03fe\u03fc\3\2\2\2\u03ff\u0402\3\2\2\2\u0400\u03fe\3\2\2\2\u0400"+
		"\u0401\3\2\2\2\u0401\u0403\3\2\2\2\u0402\u0400\3\2\2\2\u0403\u0404\7\u0082"+
		"\2\2\u0404q\3\2\2\2\u0405\u0408\5\u0096L\2\u0406\u0408\5P)\2\u0407\u0405"+
		"\3\2\2\2\u0407\u0406\3\2\2\2\u0408s\3\2\2\2\u0409\u040b\7\35\2\2\u040a"+
		"\u040c\5v<\2\u040b\u040a\3\2\2\2\u040c\u040d\3\2\2\2\u040d\u040b\3\2\2"+
		"\2\u040d\u040e\3\2\2\2\u040e\u040f\3\2\2\2\u040f\u0410\7\67\2\2\u0410"+
		"\u0412\7\35\2\2\u0411\u0413\5\u0202\u0102\2\u0412\u0411\3\2\2\2\u0412"+
		"\u0413\3\2\2\2\u0413u\3\2\2\2\u0414\u0415\5x=\2\u0415\u0416\7\u008d\2"+
		"\2\u0416\u0417\5z>\2\u0417\u0418\7\u0080\2\2\u0418w\3\2\2\2\u0419\u041e"+
		"\5\u0202\u0102\2\u041a\u041b\7\u008a\2\2\u041b\u041d\5\u0202\u0102\2\u041c"+
		"\u041a\3\2\2\2\u041d\u0420\3\2\2\2\u041e\u041c\3\2\2\2\u041e\u041f\3\2"+
		"\2\2\u041fy\3\2\2\2\u0420\u041e\3\2\2\2\u0421\u0422\5\u0096L\2\u0422{"+
		"\3\2\2\2\u0423\u0424\7\u0081\2\2\u0424\u0429\5~@\2\u0425\u0426\7\u008a"+
		"\2\2\u0426\u0428\5~@\2\u0427\u0425\3\2\2\2\u0428\u042b\3\2\2\2\u0429\u0427"+
		"\3\2\2\2\u0429\u042a\3\2\2\2\u042a\u042c\3\2\2\2\u042b\u0429\3\2\2\2\u042c"+
		"\u042d\7\u0082\2\2\u042d}\3\2\2\2\u042e\u042f\5\u0202\u0102\2\u042f\u0430"+
		"\5\u00a6T\2\u0430\177\3\2\2\2\u0431\u0432\7i\2\2\u0432\u0433\5\u0096L"+
		"\2\u0433\u0081\3\2\2\2\u0434\u0435\7b\2\2\u0435\u0436\5\u0202\u0102\2"+
		"\u0436\u0437\7\u0080\2\2\u0437\u0083\3\2\2\2\u0438\u0439\7\23\2\2\u0439"+
		"\u043a\7#\2\2\u043a\u043b\5\u00a2R\2\u043b\u0085\3\2\2\2\u043c\u043f\5"+
		"\u0088E\2\u043d\u043f\5\u008cG\2\u043e\u043c\3\2\2\2\u043e\u043d\3\2\2"+
		"\2\u043f\u0087\3\2\2\2\u0440\u0444\7?\2\2\u0441\u0443\5\u008aF\2\u0442"+
		"\u0441\3\2\2\2\u0443\u0446\3\2\2\2\u0444\u0442\3\2\2\2\u0444\u0445\3\2"+
		"\2\2\u0445\u0447\3\2\2\2\u0446\u0444\3\2\2\2\u0447\u0448\7\67\2\2\u0448"+
		"\u044a\7?\2\2\u0449\u044b\5\u0202\u0102\2\u044a\u0449\3\2\2\2\u044a\u044b"+
		"\3\2\2\2\u044b\u0089\3\2\2\2\u044c\u0451\5,\27\2\u044d\u0451\5@!\2\u044e"+
		"\u0451\5\u0106\u0084\2\u044f\u0451\5\u01ea\u00f6\2\u0450\u044c\3\2\2\2"+
		"\u0450\u044d\3\2\2\2\u0450\u044e\3\2\2\2\u0450\u044f\3\2\2\2\u0451\u008b"+
		"\3\2\2\2\u0452\u0453\7?\2\2\u0453\u0457\7\63\2\2\u0454\u0456\5\u01ca\u00e6"+
		"\2\u0455\u0454\3\2\2\2\u0456\u0459\3\2\2\2\u0457\u0455\3\2\2\2\u0457\u0458"+
		"\3\2\2\2\u0458\u045a\3\2\2\2\u0459\u0457\3\2\2\2\u045a\u045b\7\67\2\2"+
		"\u045b\u045c\7?\2\2\u045c\u045e\7\63\2\2\u045d\u045f\5\u0202\u0102\2\u045e"+
		"\u045d\3\2\2\2\u045e\u045f\3\2\2\2\u045f\u008d\3\2\2\2\u0460\u0463\5\u0090"+
		"I\2\u0461\u0463\5\u0082B\2\u0462\u0460\3\2\2\2\u0462\u0461\3\2\2\2\u0463"+
		"\u008f\3\2\2\2\u0464\u0465\7b\2\2\u0465\u0466\5\u0202\u0102\2\u0466\u0467"+
		"\7_\2\2\u0467\u0468\5\u0092J\2\u0468\u0469\7\u0080\2\2\u0469\u0091\3\2"+
		"\2\2\u046a\u0470\5L\'\2\u046b\u0470\5b\62\2\u046c\u0470\5\u0080A\2\u046d"+
		"\u0470\5\u0084C\2\u046e\u0470\5\u0086D\2\u046f\u046a\3\2\2\2\u046f\u046b"+
		"\3\2\2\2\u046f\u046c\3\2\2\2\u046f\u046d\3\2\2\2\u046f\u046e\3\2\2\2\u0470"+
		"\u0093\3\2\2\2\u0471\u0472\7-\2\2\u0472\u0473\5\u0202\u0102\2\u0473\u0474"+
		"\7_\2\2\u0474\u0475\5\u0096L\2\u0475\u0476\7\u0080\2\2\u0476\u0095\3\2"+
		"\2\2\u0477\u0479\5\u0098M\2\u0478\u0477\3\2\2\2\u0478\u0479\3\2\2\2\u0479"+
		"\u047a\3\2\2\2\u047a\u047c\5\u00a2R\2\u047b\u047d\5\u00a4S\2\u047c\u047b"+
		"\3\2\2\2\u047c\u047d\3\2\2\2\u047d\u0097\3\2\2\2\u047e\u0484\5\6\4\2\u047f"+
		"\u0480\7\u0081\2\2\u0480\u0481\5\u009aN\2\u0481\u0482\7\u0082\2\2\u0482"+
		"\u0484\3\2\2\2\u0483\u047e\3\2\2\2\u0483\u047f\3\2\2\2\u0484\u0099\3\2"+
		"\2\2\u0485\u0488\5\u009cO\2\u0486\u0488\5\u009eP\2\u0487\u0485\3\2\2\2"+
		"\u0487\u0486\3\2\2\2\u0488\u009b\3\2\2\2\u0489\u048a\5\u0098M\2\u048a"+
		"\u009d\3\2\2\2\u048b\u0490\5\u00a0Q\2\u048c\u048d\7\u008a\2\2\u048d\u048f"+
		"\5\u00a0Q\2\u048e\u048c\3\2\2\2\u048f\u0492\3\2\2\2\u0490\u048e\3\2\2"+
		"\2\u0490\u0491\3\2\2\2\u0491\u009f\3\2\2\2\u0492\u0490\3\2\2\2\u0493\u0494"+
		"\5\u0202\u0102\2\u0494\u0495\5\u0098M\2\u0495\u00a1\3\2\2\2\u0496\u0497"+
		"\5\6\4\2\u0497\u00a3\3\2\2\2\u0498\u049b\5N(\2\u0499\u049b\5\u00a6T\2"+
		"\u049a\u0498\3\2\2\2\u049a\u0499\3\2\2\2\u049b\u00a5\3\2\2\2\u049c\u049f"+
		"\5l\67\2\u049d\u049f\5|?\2\u049e\u049c\3\2\2\2\u049e\u049d\3\2\2\2\u049f"+
		"\u00a7\3\2\2\2\u04a0\u04a5\5\u00aaV\2\u04a1\u04a5\5\u00acW\2\u04a2\u04a5"+
		"\5\u00b0Y\2\u04a3\u04a5\5\u00b2Z\2\u04a4\u04a0\3\2\2\2\u04a4\u04a1\3\2"+
		"\2\2\u04a4\u04a2\3\2\2\2\u04a4\u04a3\3\2\2\2\u04a5\u00a9\3\2\2\2\u04a6"+
		"\u04a7\7\61\2\2\u04a7\u04a8\5x=\2\u04a8\u04a9\7\u008d\2\2\u04a9\u04ac"+
		"\5\u0096L\2\u04aa\u04ab\7\u00a4\2\2\u04ab\u04ad\5\u013a\u009e\2\u04ac"+
		"\u04aa\3\2\2\2\u04ac\u04ad\3\2\2\2\u04ad\u04ae\3\2\2\2\u04ae\u04af\7\u0080"+
		"\2\2\u04af\u00ab\3\2\2\2\u04b0\u04b1\7\36\2\2\u04b1\u04b2\5x=\2\u04b2"+
		"\u04b3\7\u008d\2\2\u04b3\u04b5\5\u0096L\2\u04b4\u04b6\5\u00aeX\2\u04b5"+
		"\u04b4\3\2\2\2\u04b5\u04b6\3\2\2\2\u04b6\u04b9\3\2\2\2\u04b7\u04b8\7\u00a4"+
		"\2\2\u04b8\u04ba\5\u013a\u009e\2\u04b9\u04b7\3\2\2\2\u04b9\u04ba\3\2\2"+
		"\2\u04ba\u04bb\3\2\2\2\u04bb\u04bc\7\u0080\2\2\u04bc\u00ad\3\2\2\2\u04bd"+
		"\u04be\t\6\2\2\u04be\u00af\3\2\2\2\u04bf\u04c1\7\32\2\2\u04c0\u04bf\3"+
		"\2\2\2\u04c0\u04c1\3\2\2\2\u04c1\u04c2\3\2\2\2\u04c2\u04c3\7(\2\2\u04c3"+
		"\u04c4\5x=\2\u04c4\u04c5\7\u008d\2\2\u04c5\u04c8\5\u0096L\2\u04c6\u04c7"+
		"\7\u00a4\2\2\u04c7\u04c9\5\u013a\u009e\2\u04c8\u04c6\3\2\2\2\u04c8\u04c9"+
		"\3\2\2\2\u04c9\u04ca\3\2\2\2\u04ca\u04cb\7\u0080\2\2\u04cb\u00b1\3\2\2"+
		"\2\u04cc\u04cd\7\23\2\2\u04cd\u04ce\5x=\2\u04ce\u04cf\7\u008d\2\2\u04cf"+
		"\u04d1\5\u0096L\2\u04d0\u04d2\5\u00b4[\2\u04d1\u04d0\3\2\2\2\u04d1\u04d2"+
		"\3\2\2\2\u04d2\u04d3\3\2\2\2\u04d3\u04d4\7\u0080\2\2\u04d4\u00b3\3\2\2"+
		"\2\u04d5\u04d6\7f\2\2\u04d6\u04d8\5\u013a\u009e\2\u04d7\u04d5\3\2\2\2"+
		"\u04d7\u04d8\3\2\2\2\u04d8\u04d9\3\2\2\2\u04d9\u04db\7_\2\2\u04da\u04dc"+
		"\t\7\2\2\u04db\u04da\3\2\2\2\u04db\u04dc\3\2\2\2\u04dc\u04dd\3\2\2\2\u04dd"+
		"\u04de\5\u00b6\\\2\u04de\u00b5\3\2\2\2\u04df\u04e0\5\u013a\u009e\2\u04e0"+
		"\u00b7\3\2\2\2\u04e1\u04e6\5\u00ba^\2\u04e2\u04e6\5\u00c6d\2\u04e3\u04e6"+
		"\5\u00caf\2\u04e4\u04e6\5\u00d4k\2\u04e5\u04e1\3\2\2\2\u04e5\u04e2\3\2"+
		"\2\2\u04e5\u04e3\3\2\2\2\u04e5\u04e4\3\2\2\2\u04e6\u00b9\3\2\2\2\u04e7"+
		"\u04ec\5\u00bc_\2\u04e8\u04ec\5\u00be`\2\u04e9\u04ec\5\u00c0a\2\u04ea"+
		"\u04ec\5\u00c2b\2\u04eb\u04e7\3\2\2\2\u04eb\u04e8\3\2\2\2\u04eb\u04e9"+
		"\3\2\2\2\u04eb\u04ea\3\2\2\2\u04ec\u00bb\3\2\2\2\u04ed\u04ee\7\61\2\2"+
		"\u04ee\u04ef\5x=\2\u04ef\u04f1\7\u008d\2\2\u04f0\u04f2\7F\2\2\u04f1\u04f0"+
		"\3\2\2\2\u04f1\u04f2\3\2\2\2\u04f2\u04f3\3\2\2\2\u04f3\u04f6\5\u0096L"+
		"\2\u04f4\u04f5\7\u00a4\2\2\u04f5\u04f7\5\u013a\u009e\2\u04f6\u04f4\3\2"+
		"\2\2\u04f6\u04f7\3\2\2\2\u04f7\u00bd\3\2\2\2\u04f8\u04fa\7\36\2\2\u04f9"+
		"\u04f8\3\2\2\2\u04f9\u04fa\3\2\2\2\u04fa\u04fb\3\2\2\2\u04fb\u04fc\5x"+
		"=\2\u04fc\u04fe\7\u008d\2\2\u04fd\u04ff\5\u00c4c\2\u04fe\u04fd\3\2\2\2"+
		"\u04fe\u04ff\3\2\2\2\u04ff\u0500\3\2\2\2\u0500\u0502\5\u0096L\2\u0501"+
		"\u0503\7h\2\2\u0502\u0501\3\2\2\2\u0502\u0503\3\2\2\2\u0503\u0506\3\2"+
		"\2\2\u0504\u0505\7\u00a4\2\2\u0505\u0507\5\u013a\u009e\2\u0506\u0504\3"+
		"\2\2\2\u0506\u0507\3\2\2\2\u0507\u00bf\3\2\2\2\u0508\u0509\7(\2\2\u0509"+
		"\u050a\5x=\2\u050a\u050c\7\u008d\2\2\u050b\u050d\5\u00c4c\2\u050c\u050b"+
		"\3\2\2\2\u050c\u050d\3\2\2\2\u050d\u050e\3\2\2\2\u050e\u0511\5\u0096L"+
		"\2\u050f\u0510\7\u00a4\2\2\u0510\u0512\5\u013a\u009e\2\u0511\u050f\3\2"+
		"\2\2\u0511\u0512\3\2\2\2\u0512\u00c1\3\2\2\2\u0513\u0514\7\23\2\2\u0514"+
		"\u0515\5x=\2\u0515\u0516\7\u008d\2\2\u0516\u0517\5\u0096L\2\u0517\u00c3"+
		"\3\2\2\2\u0518\u0519\t\b\2\2\u0519\u00c5\3\2\2\2\u051a\u051b\5\u00c8e"+
		"\2\u051b\u00c7\3\2\2\2\u051c\u051d\7b\2\2\u051d\u051e\5\u0202\u0102\2"+
		"\u051e\u00c9\3\2\2\2\u051f\u0522\5\u00ccg\2\u0520\u0521\7_\2\2\u0521\u0523"+
		"\5\u00d2j\2\u0522\u0520\3\2\2\2\u0522\u0523\3\2\2\2\u0523\u00cb\3\2\2"+
		"\2\u0524\u0527\5\u00ceh\2\u0525\u0527\5\u00d0i\2\u0526\u0524\3\2\2\2\u0526"+
		"\u0525\3\2\2\2\u0527\u00cd\3\2\2\2\u0528\u0529\7$\2\2\u0529\u0531\5\66"+
		"\34\2\u052a\u052c\7W\2\2\u052b\u052a\3\2\2\2\u052b\u052c\3\2\2\2\u052c"+
		"\u052d\3\2\2\2\u052d\u052e\7\u0081\2\2\u052e\u052f\5:\36\2\u052f\u0530"+
		"\7\u0082\2\2\u0530\u0532\3\2\2\2\u0531\u052b\3\2\2\2\u0531\u0532\3\2\2"+
		"\2\u0532\u00cf\3\2\2\2\u0533\u0535\t\3\2\2\u0534\u0533\3\2\2\2\u0534\u0535"+
		"\3\2\2\2\u0535\u0536\3\2\2\2\u0536\u0537\7\66\2\2\u0537\u053f\5\66\34"+
		"\2\u0538\u053a\7W\2\2\u0539\u0538\3\2\2\2\u0539\u053a\3\2\2\2\u053a\u053b"+
		"\3\2\2\2\u053b\u053c\7\u0081\2\2\u053c\u053d\5:\36\2\u053d\u053e\7\u0082"+
		"\2\2\u053e\u0540\3\2\2\2\u053f\u0539\3\2\2\2\u053f\u0540\3\2\2\2\u0540"+
		"\u0541\3\2\2\2\u0541\u0542\7I\2\2\u0542\u0543\5\u00a2R\2\u0543\u00d1\3"+
		"\2\2\2\u0544\u0547\5\6\4\2\u0545\u0547\7\u00a5\2\2\u0546\u0544\3\2\2\2"+
		"\u0546\u0545\3\2\2\2\u0547\u00d3\3\2\2\2\u0548\u0549\7T\2\2\u0549\u054a"+
		"\5\u0202\u0102\2\u054a\u054b\7_\2\2\u054b\u054c\7/\2\2\u054c\u054d\5\6"+
		"\4\2\u054d\u054e\5\u00d6l\2\u054e\u00d5\3\2\2\2\u054f\u055b\5\u00eex\2"+
		"\u0550\u0551\7\26\2\2\u0551\u0552\7=\2\2\u0552\u0553\7\u0081\2\2\u0553"+
		"\u0554\7\u00a5\2\2\u0554\u055b\7\u0082\2\2\u0555\u0556\7\26\2\2\u0556"+
		"\u0557\7=\2\2\u0557\u0558\7\u0081\2\2\u0558\u0559\7\t\2\2\u0559\u055b"+
		"\7\u0082\2\2\u055a\u054f\3\2\2\2\u055a\u0550\3\2\2\2\u055a\u0555\3\2\2"+
		"\2\u055b\u00d7\3\2\2\2\u055c\u0561\5\u00dan\2\u055d\u055e\7\u0080\2\2"+
		"\u055e\u0560\5\u00dan\2\u055f\u055d\3\2\2\2\u0560\u0563\3\2\2\2\u0561"+
		"\u055f\3\2\2\2\u0561\u0562\3\2\2\2\u0562\u00d9\3\2\2\2\u0563\u0561\3\2"+
		"\2\2\u0564\u0565\5\u00b8]\2\u0565\u00db\3\2\2\2\u0566\u0567\7\26\2\2\u0567"+
		"\u0568\7\u0081\2\2\u0568\u0569\5\u00dep\2\u0569\u056a\7\u0082\2\2\u056a"+
		"\u056b\7\u0080\2\2\u056b\u00dd\3\2\2\2\u056c\u056d\5\u00d8m\2\u056d\u00df"+
		"\3\2\2\2\u056e\u056f\7k\2\2\u056f\u0570\7\u0081\2\2\u0570\u0571\5\u00e2"+
		"r\2\u0571\u0572\7\u0082\2\2\u0572\u0573\7\u0080\2\2\u0573\u00e1\3\2\2"+
		"\2\u0574\u0575\5\u00d8m\2\u0575\u00e3\3\2\2\2\u0576\u0577\7\u0081\2\2"+
		"\u0577\u057c\5\u00e6t\2\u0578\u0579\7\u008a\2\2\u0579\u057b\5\u00e6t\2"+
		"\u057a\u0578\3\2\2\2\u057b\u057e\3\2\2\2\u057c\u057a\3\2\2\2\u057c\u057d"+
		"\3\2\2\2\u057d\u057f\3\2\2\2\u057e\u057c\3\2\2\2\u057f\u0580\7\u0082\2"+
		"\2\u0580\u00e5\3\2\2\2\u0581\u0582\5\u00e8u\2\u0582\u0583\7\u00a6\2\2"+
		"\u0583\u0585\3\2\2\2\u0584\u0581\3\2\2\2\u0584\u0585\3\2\2\2\u0585\u0586"+
		"\3\2\2\2\u0586\u0587\5\u00eav\2\u0587\u00e7\3\2\2\2\u0588\u058d\5\6\4"+
		"\2\u0589\u058a\7\u0081\2\2\u058a\u058b\5\6\4\2\u058b\u058c\7\u0082\2\2"+
		"\u058c\u058e\3\2\2\2\u058d\u0589\3\2\2\2\u058d\u058e\3\2\2\2\u058e\u00e9"+
		"\3\2\2\2\u058f\u0590\5\6\4\2\u0590\u0591\7\u0081\2\2\u0591\u0592\5\u00ec"+
		"w\2\u0592\u0593\7\u0082\2\2\u0593\u0596\3\2\2\2\u0594\u0596\5\u00ecw\2"+
		"\u0595\u058f\3\2\2\2\u0595\u0594\3\2\2\2\u0596\u00eb\3\2\2\2\u0597\u0599"+
		"\7\r\2\2\u0598\u0597\3\2\2\2\u0598\u0599\3\2\2\2\u0599\u059a\3\2\2\2\u059a"+
		"\u059e\5\u013a\u009e\2\u059b\u059e\5\u0096L\2\u059c\u059e\7f\2\2\u059d"+
		"\u0598\3\2\2\2\u059d\u059b\3\2\2\2\u059d\u059c\3\2\2\2\u059e\u00ed\3\2"+
		"\2\2\u059f\u05a0\7\26\2\2\u05a0\u05a1\7=\2\2\u05a1\u05a2\5\u00e4s\2\u05a2"+
		"\u00ef\3\2\2\2\u05a3\u05a4\7k\2\2\u05a4\u05a5\7=\2\2\u05a5\u05a6\5\u00e4"+
		"s\2\u05a6\u00f1\3\2\2\2\u05a7\u05a8\7C\2\2\u05a8\u05ab\5\u00f4{\2\u05a9"+
		"\u05aa\7\u008d\2\2\u05aa\u05ac\5\u0096L\2\u05ab\u05a9\3\2\2\2\u05ab\u05ac"+
		"\3\2\2\2\u05ac\u05ad\3\2\2\2\u05ad\u05ae\7_\2\2\u05ae\u05b0\5\6\4\2\u05af"+
		"\u05b1\5B\"\2\u05b0\u05af\3\2\2\2\u05b0\u05b1\3\2\2\2\u05b1\u05b2\3\2"+
		"\2\2\u05b2\u05b3\7\u0080\2\2\u05b3\u00f3\3\2\2\2\u05b4\u05b8\5\u0202\u0102"+
		"\2\u05b5\u05b8\7s\2\2\u05b6\u05b8\58\35\2\u05b7\u05b4\3\2\2\2\u05b7\u05b5"+
		"\3\2\2\2\u05b7\u05b6\3\2\2\2\u05b8\u00f5\3\2\2\2\u05b9\u05ba\7\'\2\2\u05ba"+
		"\u05bb\5\u0202\u0102\2\u05bb\u05bc\7\u008d\2\2\u05bc\u05bd\5\u00a2R\2"+
		"\u05bd\u05be\7\u0080\2\2\u05be\u00f7\3\2\2\2\u05bf\u05c0\7\7\2\2\u05c0"+
		"\u05c2\5\u0202\u0102\2\u05c1\u05c3\7_\2\2\u05c2\u05c1\3\2\2\2\u05c2\u05c3"+
		"\3\2\2\2\u05c3\u05c5\3\2\2\2\u05c4\u05c6\5\u00dco\2\u05c5\u05c4\3\2\2"+
		"\2\u05c5\u05c6\3\2\2\2\u05c6\u05c8\3\2\2\2\u05c7\u05c9\5\u00e0q\2\u05c8"+
		"\u05c7\3\2\2\2\u05c8\u05c9\3\2\2\2\u05c9\u05ca\3\2\2\2\u05ca\u05cb\7\67"+
		"\2\2\u05cb\u05cd\7\7\2\2\u05cc\u05ce\5\u0202\u0102\2\u05cd\u05cc\3\2\2"+
		"\2\u05cd\u05ce\3\2\2\2\u05ce\u05cf\3\2\2\2\u05cf\u05d0\7\u0080\2\2\u05d0"+
		"\u00f9\3\2\2\2\u05d1\u05d2\7\21\2\2\u05d2\u05d3\5\u0202\u0102\2\u05d3"+
		"\u05d4\7_\2\2\u05d4\u05d5\7\u0081\2\2\u05d5\u05d6\5\u00fc\177\2\u05d6"+
		"\u05d7\7\u0082\2\2\u05d7\u05d8\7\u0080\2\2\u05d8\u00fb\3\2\2\2\u05d9\u05de"+
		"\5\u00fe\u0080\2\u05da\u05db\7\u008a\2\2\u05db\u05dd\5\u00fe\u0080\2\u05dc"+
		"\u05da\3\2\2\2\u05dd\u05e0\3\2\2\2\u05de\u05dc\3\2\2\2\u05de\u05df\3\2"+
		"\2\2\u05df\u00fd\3\2\2\2\u05e0\u05de\3\2\2\2\u05e1\u05e3\5\u010a\u0086"+
		"\2\u05e2\u05e4\7\u00a5\2\2\u05e3\u05e2\3\2\2\2\u05e3\u05e4\3\2\2\2\u05e4"+
		"\u00ff\3\2\2\2\u05e5\u05e6\7\21\2\2\u05e6\u05e7\5\u0202\u0102\2\u05e7"+
		"\u05e8\7\u008d\2\2\u05e8\u05e9\5\6\4\2\u05e9\u05ea\7\u0081\2\2\u05ea\u05eb"+
		"\5\u0102\u0082\2\u05eb\u05ec\7\u0082\2\2\u05ec\u05ed\7\u0080\2\2\u05ed"+
		"\u0101\3\2\2\2\u05ee\u05f3\5\u0104\u0083\2\u05ef\u05f0\7\u008a\2\2\u05f0"+
		"\u05f2\5\u0104\u0083\2\u05f1\u05ef\3\2\2\2\u05f2\u05f5\3\2\2\2\u05f3\u05f1"+
		"\3\2\2\2\u05f3\u05f4\3\2\2\2\u05f4\u0103\3\2\2\2\u05f5\u05f3\3\2\2\2\u05f6"+
		"\u05f7\5\6\4\2\u05f7\u0105\3\2\2\2\u05f8\u05f9\7\'\2\2\u05f9\u05fa\5\u012a"+
		"\u0096\2\u05fa\u05fb\7#\2\2\u05fb\u05fc\5\u0108\u0085\2\u05fc\u05fd\7"+
		"_\2\2\u05fd\u05fe\5\u013a\u009e\2\u05fe\u05ff\7\u0080\2\2\u05ff\u0107"+
		"\3\2\2\2\u0600\u0601\5\u010c\u0087\2\u0601\u0602\7\u008d\2\2\u0602\u0603"+
		"\5\u010a\u0086\2\u0603\u0109\3\2\2\2\u0604\u0605\t\t\2\2\u0605\u010b\3"+
		"\2\2\2\u0606\u060b\5\u010e\u0088\2\u0607\u0608\7\u008a\2\2\u0608\u060a"+
		"\5\u010e\u0088\2\u0609\u0607\3\2\2\2\u060a\u060d\3\2\2\2\u060b\u0609\3"+
		"\2\2\2\u060b\u060c\3\2\2\2\u060c\u0611\3\2\2\2\u060d\u060b\3\2\2\2\u060e"+
		"\u0611\7a\2\2\u060f\u0611\7B\2\2\u0610\u0606\3\2\2\2\u0610\u060e\3\2\2"+
		"\2\u0610\u060f\3\2\2\2\u0611\u010d\3\2\2\2\u0612\u0614\5\u0110\u0089\2"+
		"\u0613\u0615\5B\"\2\u0614\u0613\3\2\2\2\u0614\u0615\3\2\2\2\u0615\u010f"+
		"\3\2\2\2\u0616\u061a\5\u0202\u0102\2\u0617\u061a\7s\2\2\u0618\u061a\5"+
		"8\35\2\u0619\u0616\3\2\2\2\u0619\u0617\3\2\2\2\u0619\u0618\3\2\2\2\u061a"+
		"\u0111\3\2\2\2\u061b\u061e\5\u0114\u008b\2\u061c\u061e\5\u0116\u008c\2"+
		"\u061d\u061b\3\2\2\2\u061d\u061c\3\2\2\2\u061e\u0113\3\2\2\2\u061f\u0620"+
		"\7Z\2\2\u0620\u0621\5\u0118\u008d\2\u0621\u0622\5\u011c\u008f\2\u0622"+
		"\u0626\7\u0080\2\2\u0623\u0624\7\67\2\2\u0624\u0625\7Z\2\2\u0625\u0627"+
		"\7\u0080\2\2\u0626\u0623\3\2\2\2\u0626\u0627\3\2\2\2\u0627\u0115\3\2\2"+
		"\2\u0628\u0629\7Z\2\2\u0629\u062a\5\u0118\u008d\2\u062a\u062b\5\u011c"+
		"\u008f\2\u062b\u062f\7\u0080\2\2\u062c\u062d\5\u0120\u0091\2\u062d\u062e"+
		"\7\u0080\2\2\u062e\u0630\3\2\2\2\u062f\u062c\3\2\2\2\u0630\u0631\3\2\2"+
		"\2\u0631\u062f\3\2\2\2\u0631\u0632\3\2\2\2\u0632\u0633\3\2\2\2\u0633\u0634"+
		"\7\67\2\2\u0634\u0635\7Z\2\2\u0635\u0636\7\u0080\2\2\u0636\u0117\3\2\2"+
		"\2\u0637\u0638\5\u011a\u008e\2\u0638\u0639\7\u008d\2\2\u0639\u063a\5\6"+
		"\4\2\u063a\u0119\3\2\2\2\u063b\u0640\5\u01e8\u00f5\2\u063c\u063d\7\u008a"+
		"\2\2\u063d\u063f\5\u01e8\u00f5\2\u063e\u063c\3\2\2\2\u063f\u0642\3\2\2"+
		"\2\u0640\u063e\3\2\2\2\u0640\u0641\3\2\2\2\u0641\u0646\3\2\2\2\u0642\u0640"+
		"\3\2\2\2\u0643\u0646\7a\2\2\u0644\u0646\7B\2\2\u0645\u063b\3\2\2\2\u0645"+
		"\u0643\3\2\2\2\u0645\u0644\3\2\2\2\u0646\u011b\3\2\2\2\u0647\u0648\7\31"+
		"\2\2\u0648\u064a\5\u011e\u0090\2\u0649\u0647\3\2\2\2\u0649\u064a\3\2\2"+
		"\2\u064a\u064c\3\2\2\2\u064b\u064d\5\u00eex\2\u064c\u064b\3\2\2\2\u064c"+
		"\u064d\3\2\2\2\u064d\u064f\3\2\2\2\u064e\u0650\5\u00f0y\2\u064f\u064e"+
		"\3\2\2\2\u064f\u0650\3\2\2\2\u0650\u011d\3\2\2\2\u0651\u0652\7\17\2\2"+
		"\u0652\u0657\5\6\4\2\u0653\u0654\7\u0081\2\2\u0654\u0655\5\u0202\u0102"+
		"\2\u0655\u0656\7\u0082\2\2\u0656\u0658\3\2\2\2\u0657\u0653\3\2\2\2\u0657"+
		"\u0658\3\2\2\2\u0658\u065d\3\2\2\2\u0659\u065a\7e\2\2\u065a\u065d\5\6"+
		"\4\2\u065b\u065d\7f\2\2\u065c\u0651\3\2\2\2\u065c\u0659\3\2\2\2\u065c"+
		"\u065b\3\2\2\2\u065d\u011f\3\2\2\2\u065e\u065f\7\31\2\2\u065f\u0660\7"+
		"&\2\2\u0660\u0661\5\u0122\u0092\2\u0661\u0121\3\2\2\2\u0662\u0667\5\6"+
		"\4\2\u0663\u0664\7\u008a\2\2\u0664\u0666\5\6\4\2\u0665\u0663\3\2\2\2\u0666"+
		"\u0669\3\2\2\2\u0667\u0665\3\2\2\2\u0667\u0668\3\2\2\2\u0668\u0123\3\2"+
		"\2\2\u0669\u0667\3\2\2\2\u066a\u066b\7\"\2\2\u066b\u066c\5\u0126\u0094"+
		"\2\u066c\u066d\7\64\2\2\u066d\u066e\5\u013a\u009e\2\u066e\u066f\7\u0080"+
		"\2\2\u066f\u0125\3\2\2\2\u0670\u0671\5\u0128\u0095\2\u0671\u0672\7\u008d"+
		"\2\2\u0672\u0673\5\u00a2R\2\u0673\u0127\3\2\2\2\u0674\u0679\5\6\4\2\u0675"+
		"\u0676\7\u008a\2\2\u0676\u0678\5\6\4\2\u0677\u0675\3\2\2\2\u0678\u067b"+
		"\3\2\2\2\u0679\u0677\3\2\2\2\u0679\u067a\3\2\2\2\u067a\u067f\3\2\2\2\u067b"+
		"\u0679\3\2\2\2\u067c\u067f\7a\2\2\u067d\u067f\7B\2\2\u067e\u0674\3\2\2"+
		"\2\u067e\u067c\3\2\2\2\u067e\u067d\3\2\2\2\u067f\u0129\3\2\2\2\u0680\u0683"+
		"\5\u0202\u0102\2\u0681\u0683\5\2\2\2\u0682\u0680\3\2\2\2\u0682\u0681\3"+
		"\2\2\2\u0683\u012b\3\2\2\2\u0684\u0685\7\u0086\2\2\u0685\u0686\t\n\2\2"+
		"\u0686\u0687\5\u012e\u0098\2\u0687\u0688\7\u008d\2\2\u0688\u0689\5\u0096"+
		"L\2\u0689\u068a\7\u0087\2\2\u068a\u012d\3\2\2\2\u068b\u068f\5\u0130\u0099"+
		"\2\u068c\u068f\5\u0132\u009a\2\u068d\u068f\5\u0134\u009b\2\u068e\u068b"+
		"\3\2\2\2\u068e\u068c\3\2\2\2\u068e\u068d\3\2\2\2\u068f\u012f\3\2\2\2\u0690"+
		"\u0691\7\u0088\2\2\u0691\u0692\5\u0202\u0102\2\u0692\u0693\7\u008b\2\2"+
		"\u0693\u0694\5\u0202\u0102\2\u0694\u0695\7\u008b\2\2\u0695\u069a\5\u0202"+
		"\u0102\2\u0696\u0697\7\u008b\2\2\u0697\u0699\5\u0202\u0102\2\u0698\u0696"+
		"\3\2\2\2\u0699\u069c\3\2\2\2\u069a\u0698\3\2\2\2\u069a\u069b\3\2\2\2\u069b"+
		"\u0131\3\2\2\2\u069c\u069a\3\2\2\2\u069d\u069e\7\u008b\2\2\u069e\u069f"+
		"\5\u0136\u009c\2\u069f\u0133\3\2\2\2\u06a0\u06a1\7\u00a3\2\2\u06a1\u06a3"+
		"\7\u008b\2\2\u06a2\u06a0\3\2\2\2\u06a3\u06a6\3\2\2\2\u06a4\u06a2\3\2\2"+
		"\2\u06a4\u06a5\3\2\2\2\u06a5\u06a7\3\2\2\2\u06a6\u06a4\3\2\2\2\u06a7\u06a8"+
		"\5\u0136\u009c\2\u06a8\u0135\3\2\2\2\u06a9\u06aa\5\u0138\u009d\2\u06aa"+
		"\u06ab\7\u008b\2\2\u06ab\u06ad\3\2\2\2\u06ac\u06a9\3\2\2\2\u06ad\u06b0"+
		"\3\2\2\2\u06ae\u06ac\3\2\2\2\u06ae\u06af\3\2\2\2\u06af\u06b1\3\2\2\2\u06b0"+
		"\u06ae\3\2\2\2\u06b1\u06b2\5\u0202\u0102\2\u06b2\u0137\3\2\2\2\u06b3\u06b8"+
		"\5\u01e8\u00f5\2\u06b4\u06b5\7\u0081\2\2\u06b5\u06b6\5\u013a\u009e\2\u06b6"+
		"\u06b7\7\u0082\2\2\u06b7\u06b9\3\2\2\2\u06b8\u06b4\3\2\2\2\u06b8\u06b9"+
		"\3\2\2\2\u06b9\u0139\3\2\2\2\u06ba\u06bb\b\u009e\1\2\u06bb\u06bc\7\u00a7"+
		"\2\2\u06bc\u06bf\5\u013e\u00a0\2\u06bd\u06bf\5\u013c\u009f\2\u06be\u06ba"+
		"\3\2\2\2\u06be\u06bd\3\2\2\2\u06bf\u06ce\3\2\2\2\u06c0\u06c1\f\5\2\2\u06c1"+
		"\u06c2\5\u0144\u00a3\2\u06c2\u06c3\5\u013a\u009e\6\u06c3\u06cd\3\2\2\2"+
		"\u06c4\u06c5\f\4\2\2\u06c5\u06c6\5\u0142\u00a2\2\u06c6\u06c7\5\u013a\u009e"+
		"\5\u06c7\u06cd\3\2\2\2\u06c8\u06c9\f\3\2\2\u06c9\u06ca\5\u0140\u00a1\2"+
		"\u06ca\u06cb\5\u013a\u009e\4\u06cb\u06cd\3\2\2\2\u06cc\u06c0\3\2\2\2\u06cc"+
		"\u06c4\3\2\2\2\u06cc\u06c8\3\2\2\2\u06cd\u06d0\3\2\2\2\u06ce\u06cc\3\2"+
		"\2\2\u06ce\u06cf\3\2\2\2\u06cf\u013b\3\2\2\2\u06d0\u06ce\3\2\2\2\u06d1"+
		"\u06d2\b\u009f\1\2\u06d2\u06d5\5\u013e\u00a0\2\u06d3\u06d4\7\u00a0\2\2"+
		"\u06d4\u06d6\5\u013e\u00a0\2\u06d5\u06d3\3\2\2\2\u06d5\u06d6\3\2\2\2\u06d6"+
		"\u06e1\3\2\2\2\u06d7\u06db\7\b\2\2\u06d8\u06db\7d\2\2\u06d9\u06db\5\u0140"+
		"\u00a1\2\u06da\u06d7\3\2\2\2\u06da\u06d8\3\2\2\2\u06da\u06d9\3\2\2\2\u06db"+
		"\u06dc\3\2\2\2\u06dc\u06e1\5\u013c\u009f\6\u06dd\u06de\5\u0148\u00a5\2"+
		"\u06de\u06df\5\u013c\u009f\4\u06df\u06e1\3\2\2\2\u06e0\u06d1\3\2\2\2\u06e0"+
		"\u06da\3\2\2\2\u06e0\u06dd\3\2\2\2\u06e1\u06ec\3\2\2\2\u06e2\u06e3\f\5"+
		"\2\2\u06e3\u06e4\5\u014a\u00a6\2\u06e4\u06e5\5\u013c\u009f\6\u06e5\u06eb"+
		"\3\2\2\2\u06e6\u06e7\f\3\2\2\u06e7\u06e8\5\u0146\u00a4\2\u06e8\u06e9\5"+
		"\u013c\u009f\4\u06e9\u06eb\3\2\2\2\u06ea\u06e2\3\2\2\2\u06ea\u06e6\3\2"+
		"\2\2\u06eb\u06ee\3\2\2\2\u06ec\u06ea\3\2\2\2\u06ec\u06ed\3\2\2\2\u06ed"+
		"\u013d\3\2\2\2\u06ee\u06ec\3\2\2\2\u06ef\u06f6\5\u014e\u00a8\2\u06f0\u06f6"+
		"\7u\2\2\u06f1\u06f6\7l\2\2\u06f2\u06f6\5\u015c\u00af\2\u06f3\u06f6\5\u0152"+
		"\u00aa\2\u06f4\u06f6\5\u015a\u00ae\2\u06f5\u06ef\3\2\2\2\u06f5\u06f0\3"+
		"\2\2\2\u06f5\u06f1\3\2\2\2\u06f5\u06f2\3\2\2\2\u06f5\u06f3\3\2\2\2\u06f5"+
		"\u06f4\3\2\2\2\u06f6\u013f\3\2\2\2\u06f7\u06f8\t\13\2\2\u06f8\u0141\3"+
		"\2\2\2\u06f9\u06fa\t\f\2\2\u06fa\u0143\3\2\2\2\u06fb\u06fc\t\r\2\2\u06fc"+
		"\u0145\3\2\2\2\u06fd\u06fe\t\16\2\2\u06fe\u0147\3\2\2\2\u06ff\u0700\t"+
		"\17\2\2\u0700\u0149\3\2\2\2\u0701\u0702\t\20\2\2\u0702\u014b\3\2\2\2\u0703"+
		"\u0704\t\21\2\2\u0704\u014d\3\2\2\2\u0705\u0707\7o\2\2\u0706\u0708\5\6"+
		"\4\2\u0707\u0706\3\2\2\2\u0707\u0708\3\2\2\2\u0708\u070f\3\2\2\2\u0709"+
		"\u070b\7r\2\2\u070a\u070c\5\6\4\2\u070b\u070a\3\2\2\2\u070b\u070c\3\2"+
		"\2\2\u070c\u070f\3\2\2\2\u070d\u070f\5\6\4\2\u070e\u0705\3\2\2\2\u070e"+
		"\u0709\3\2\2\2\u070e\u070d\3\2\2\2\u070f\u014f\3\2\2\2\u0710\u0712\t\22"+
		"\2\2\u0711\u0710\3\2\2\2\u0711\u0712\3\2\2\2\u0712\u0713\3\2\2\2\u0713"+
		"\u0714\5\6\4\2\u0714\u0151\3\2\2\2\u0715\u0716\7\u0081\2\2\u0716\u071b"+
		"\5\u0154\u00ab\2\u0717\u0718\7\u008a\2\2\u0718\u071a\5\u0154\u00ab\2\u0719"+
		"\u0717\3\2\2\2\u071a\u071d\3\2\2\2\u071b\u0719\3\2\2\2\u071b\u071c\3\2"+
		"\2\2\u071c\u071e\3\2\2\2\u071d\u071b\3\2\2\2\u071e\u071f\7\u0082\2\2\u071f"+
		"\u0153\3\2\2\2\u0720\u0721\5\u0156\u00ac\2\u0721\u0722\7\u00a6\2\2\u0722"+
		"\u0724\3\2\2\2\u0723\u0720\3\2\2\2\u0723\u0724\3\2\2\2\u0724\u0725\3\2"+
		"\2\2\u0725\u0726\5\u013a\u009e\2\u0726\u0155\3\2\2\2\u0727\u072c\5\u0158"+
		"\u00ad\2\u0728\u0729\7\u009c\2\2\u0729\u072b\5\u0158\u00ad\2\u072a\u0728"+
		"\3\2\2\2\u072b\u072e\3\2\2\2\u072c\u072a\3\2\2\2\u072c\u072d\3\2\2\2\u072d"+
		"\u0157\3\2\2\2\u072e\u072c\3\2\2\2\u072f\u0733\5r:\2\u0730\u0733\5\u013c"+
		"\u009f\2\u0731\u0733\7a\2\2\u0732\u072f\3\2\2\2\u0732\u0730\3\2\2\2\u0732"+
		"\u0731\3\2\2\2\u0733\u0159\3\2\2\2\u0734\u0735\5\u00a2R\2\u0735\u0736"+
		"\7\u0085\2\2\u0736\u0737\5\u0152\u00aa\2\u0737\u015b\3\2\2\2\u0738\u073b"+
		"\7/\2\2\u0739\u073c\5\u0096L\2\u073a\u073c\5\u015a\u00ae\2\u073b\u0739"+
		"\3\2\2\2\u073b\u073a\3\2\2\2\u073c\u015d\3\2\2\2\u073d\u073f\5\u0160\u00b1"+
		"\2\u073e\u073d\3\2\2\2\u073f\u0742\3\2\2\2\u0740\u073e\3\2\2\2\u0740\u0741"+
		"\3\2\2\2\u0741\u015f\3\2\2\2\u0742\u0740\3\2\2\2\u0743\u0744\5\u01e8\u00f5"+
		"\2\u0744\u0745\7\u008d\2\2\u0745\u0747\3\2\2\2\u0746\u0743\3\2\2\2\u0746"+
		"\u0747\3\2\2\2\u0747\u0755\3\2\2\2\u0748\u0756\5\u0162\u00b2\2\u0749\u0756"+
		"\5\u016e\u00b8\2\u074a\u0756\5\u0172\u00ba\2\u074b\u0756\5\u0174\u00bb"+
		"\2\u074c\u0756\5\u019c\u00cf\2\u074d\u0756\5\u01a4\u00d3\2\u074e\u0756"+
		"\5\u01a8\u00d5\2\u074f\u0756\5\u01aa\u00d6\2\u0750\u0756\5\u01ae\u00d8"+
		"\2\u0751\u0756\5\u01b4\u00db\2\u0752\u0756\5\u01b6\u00dc\2\u0753\u0756"+
		"\5\u01b8\u00dd\2\u0754\u0756\5\u01ba\u00de\2\u0755\u0748\3\2\2\2\u0755"+
		"\u0749\3\2\2\2\u0755\u074a\3\2\2\2\u0755\u074b\3\2\2\2\u0755\u074c\3\2"+
		"\2\2\u0755\u074d\3\2\2\2\u0755\u074e\3\2\2\2\u0755\u074f\3\2\2\2\u0755"+
		"\u0750\3\2\2\2\u0755\u0751\3\2\2\2\u0755\u0752\3\2\2\2\u0755\u0753\3\2"+
		"\2\2\u0755\u0754\3\2\2\2\u0756\u0161\3\2\2\2\u0757\u0759\7N\2\2\u0758"+
		"\u075a\5\u0164\u00b3\2\u0759\u0758\3\2\2\2\u0759\u075a\3\2\2\2\u075a\u075c"+
		"\3\2\2\2\u075b\u075d\5\u0168\u00b5\2\u075c\u075b\3\2\2\2\u075c\u075d\3"+
		"\2\2\2\u075d\u075f\3\2\2\2\u075e\u0760\5\u016c\u00b7\2\u075f\u075e\3\2"+
		"\2\2\u075f\u0760\3\2\2\2\u0760\u0761\3\2\2\2\u0761\u0762\7\u0080\2\2\u0762"+
		"\u0163\3\2\2\2\u0763\u0764\7\20\2\2\u0764\u0765\5\u0166\u00b4\2\u0765"+
		"\u0165\3\2\2\2\u0766\u076b\5\6\4\2\u0767\u0768\7\u008a\2\2\u0768\u076a"+
		"\5\6\4\2\u0769\u0767\3\2\2\2\u076a\u076d\3\2\2\2\u076b\u0769\3\2\2\2\u076b"+
		"\u076c\3\2\2\2\u076c\u0167\3\2\2\2\u076d\u076b\3\2\2\2\u076e\u076f\7K"+
		"\2\2\u076f\u0770\5\u016a\u00b6\2\u0770\u0169\3\2\2\2\u0771\u0772\5\u013a"+
		"\u009e\2\u0772\u016b\3\2\2\2\u0773\u0774\7Z\2\2\u0774\u0775\5\u013a\u009e"+
		"\2\u0775\u016d\3\2\2\2\u0776\u0777\5\u0170\u00b9\2\u0777\u0778\7\u0080"+
		"\2\2\u0778\u016f\3\2\2\2\u0779\u077a\7V\2\2\u077a\u077d\5\u016a\u00b6"+
		"\2\u077b\u077c\7\60\2\2\u077c\u077e\5\u013a\u009e\2\u077d\u077b\3\2\2"+
		"\2\u077d\u077e\3\2\2\2\u077e\u0781\3\2\2\2\u077f\u0780\7X\2\2\u0780\u0782"+
		"\5\u013a\u009e\2\u0781\u077f\3\2\2\2\u0781\u0782\3\2\2\2\u0782\u0171\3"+
		"\2\2\2\u0783\u0784\7\60\2\2\u0784\u0787\5\u013a\u009e\2\u0785\u0786\7"+
		"X\2\2\u0786\u0788\5\u013a\u009e\2\u0787\u0785\3\2\2\2\u0787\u0788\3\2"+
		"\2\2\u0788\u0789\3\2\2\2\u0789\u078a\7\u0080\2\2\u078a\u0173\3\2\2\2\u078b"+
		"\u078f\5\u0176\u00bc\2\u078c\u078f\5\u0188\u00c5\2\u078d\u078f\5\u0192"+
		"\u00ca\2\u078e\u078b\3\2\2\2\u078e\u078c\3\2\2\2\u078e\u078d\3\2\2\2\u078f"+
		"\u0175\3\2\2\2\u0790\u0794\5\u0178\u00bd\2\u0791\u0794\5\u017a\u00be\2"+
		"\u0792\u0794\5\u017c\u00bf\2\u0793\u0790\3\2\2\2\u0793\u0791\3\2\2\2\u0793"+
		"\u0792\3\2\2\2\u0794\u0177\3\2\2\2\u0795\u0796\5\u0182\u00c2\2\u0796\u0798"+
		"\7\u00a1\2\2\u0797\u0799\5\u0180\u00c1\2\u0798\u0797\3\2\2\2\u0798\u0799"+
		"\3\2\2\2\u0799\u079a\3\2\2\2\u079a\u079b\5\u0184\u00c3\2\u079b\u079c\7"+
		"\u0080\2\2\u079c\u0179\3\2\2\2\u079d\u079e\5\u0182\u00c2\2\u079e\u079f"+
		"\7\u00a1\2\2\u079f\u07a1\7Q\2\2\u07a0\u07a2\5\u017e\u00c0\2\u07a1\u07a0"+
		"\3\2\2\2\u07a1\u07a2\3\2\2\2\u07a2\u07a3\3\2\2\2\u07a3\u07a4\5\u013a\u009e"+
		"\2\u07a4\u07a5\7\u0080\2\2\u07a5\u017b\3\2\2\2\u07a6\u07a7\5\u0182\u00c2"+
		"\2\u07a7\u07a8\7\u00a1\2\2\u07a8\u07aa\7G\2\2\u07a9\u07ab\5\u017e\u00c0"+
		"\2\u07aa\u07a9\3\2\2\2\u07aa\u07ab\3\2\2\2\u07ab\u07ac\3\2\2\2\u07ac\u07ad"+
		"\7\u0080\2\2\u07ad\u017d\3\2\2\2\u07ae\u07af\t\7\2\2\u07af\u017f\3\2\2"+
		"\2\u07b0\u07b7\7\65\2\2\u07b1\u07b2\7\37\2\2\u07b2\u07b4\5\u013a\u009e"+
		"\2\u07b3\u07b1\3\2\2\2\u07b3\u07b4\3\2\2\2\u07b4\u07b5\3\2\2\2\u07b5\u07b7"+
		"\7\r\2\2\u07b6\u07b0\3\2\2\2\u07b6\u07b3\3\2\2\2\u07b7\u0181\3\2\2\2\u07b8"+
		"\u07bb\5\6\4\2\u07b9\u07bb\5\u0152\u00aa\2\u07ba\u07b8\3\2\2\2\u07ba\u07b9"+
		"\3\2\2\2\u07bb\u0183\3\2\2\2\u07bc\u07c1\5\u0186\u00c4\2\u07bd\u07be\7"+
		"\u008a\2\2\u07be\u07c0\5\u0186\u00c4\2\u07bf\u07bd\3\2\2\2\u07c0\u07c3"+
		"\3\2\2\2\u07c1\u07bf\3\2\2\2\u07c1\u07c2\3\2\2\2\u07c2\u07c6\3\2\2\2\u07c3"+
		"\u07c1\3\2\2\2\u07c4\u07c6\7*\2\2\u07c5\u07bc\3\2\2\2\u07c5\u07c4\3\2"+
		"\2\2\u07c6\u0185\3\2\2\2\u07c7\u07ca\5\u013a\u009e\2\u07c8\u07c9\7\64"+
		"\2\2\u07c9\u07cb\5\u013a\u009e\2\u07ca\u07c8\3\2\2\2\u07ca\u07cb\3\2\2"+
		"\2\u07cb\u07d2\3\2\2\2\u07cc\u07cf\7l\2\2\u07cd\u07ce\7\64\2\2\u07ce\u07d0"+
		"\5\u013a\u009e\2\u07cf\u07cd\3\2\2\2\u07cf\u07d0\3\2\2\2\u07d0\u07d2\3"+
		"\2\2\2\u07d1\u07c7\3\2\2\2\u07d1\u07cc\3\2\2\2\u07d2\u0187\3\2\2\2\u07d3"+
		"\u07d6\5\u018a\u00c6\2\u07d4\u07d6\5\u018e\u00c8\2\u07d5\u07d3\3\2\2\2"+
		"\u07d5\u07d4\3\2\2\2\u07d6\u0189\3\2\2\2\u07d7\u07d8\5\u0182\u00c2\2\u07d8"+
		"\u07da\7\u00a1\2\2\u07d9\u07db\5\u0180\u00c1\2\u07da\u07d9\3\2\2\2\u07da"+
		"\u07db\3\2\2\2\u07db\u07dc\3\2\2\2\u07dc\u07dd\5\u018c\u00c7\2\u07dd\u07de"+
		"\7\u0080\2\2\u07de\u018b\3\2\2\2\u07df\u07e0\5\u0184\u00c3\2\u07e0\u07e1"+
		"\7j\2\2\u07e1\u07e9\5\u016a\u00b6\2\u07e2\u07e3\7\30\2\2\u07e3\u07e4\5"+
		"\u0184\u00c3\2\u07e4\u07e5\7j\2\2\u07e5\u07e6\5\u016a\u00b6\2\u07e6\u07e8"+
		"\3\2\2\2\u07e7\u07e2\3\2\2\2\u07e8\u07eb\3\2\2\2\u07e9\u07e7\3\2\2\2\u07e9"+
		"\u07ea\3\2\2\2\u07ea\u07ef\3\2\2\2\u07eb\u07e9\3\2\2\2\u07ec\u07ed\7\30"+
		"\2\2\u07ed\u07f0\5\u0184\u00c3\2\u07ee\u07f0\6\u00c7\b\2\u07ef\u07ec\3"+
		"\2\2\2\u07ef\u07ee\3\2\2\2\u07f0\u018d\3\2\2\2\u07f1\u07f2\5\u0182\u00c2"+
		"\2\u07f2\u07f3\7\u00a1\2\2\u07f3\u07f5\7Q\2\2\u07f4\u07f6\5\u017e\u00c0"+
		"\2\u07f5\u07f4\3\2\2\2\u07f5\u07f6\3\2\2\2\u07f6\u07f7\3\2\2\2\u07f7\u07f8"+
		"\5\u0190\u00c9\2\u07f8\u07f9\7\u0080\2\2\u07f9\u018f\3\2\2\2\u07fa\u07fb"+
		"\5\u013a\u009e\2\u07fb\u07fc\7j\2\2\u07fc\u0804\5\u016a\u00b6\2\u07fd"+
		"\u07fe\7\30\2\2\u07fe\u07ff\5\u013a\u009e\2\u07ff\u0800\7j\2\2\u0800\u0801"+
		"\5\u016a\u00b6\2\u0801\u0803\3\2\2\2\u0802\u07fd\3\2\2\2\u0803\u0806\3"+
		"\2\2\2\u0804\u0802\3\2\2\2\u0804\u0805\3\2\2\2\u0805\u080a\3\2\2\2\u0806"+
		"\u0804\3\2\2\2\u0807\u0808\7\30\2\2\u0808\u080b\5\u013a\u009e\2\u0809"+
		"\u080b\6\u00c9\t\2\u080a\u0807\3\2\2\2\u080a\u0809\3\2\2\2\u080b\u0191"+
		"\3\2\2\2\u080c\u080f\5\u0194\u00cb\2\u080d\u080f\5\u0198\u00cd\2\u080e"+
		"\u080c\3\2\2\2\u080e\u080d\3\2\2\2\u080f\u0193\3\2\2\2\u0810\u0811\7J"+
		"\2\2\u0811\u0812\5\u013a\u009e\2\u0812\u0814\78\2\2\u0813\u0815\7\u008c"+
		"\2\2\u0814\u0813\3\2\2\2\u0814\u0815\3\2\2\2\u0815\u0816\3\2\2\2\u0816"+
		"\u0817\5\u0182\u00c2\2\u0817\u0819\7\u00a1\2\2\u0818\u081a\5\u0180\u00c1"+
		"\2\u0819\u0818\3\2\2\2\u0819\u081a\3\2\2\2\u081a\u081b\3\2\2\2\u081b\u081c"+
		"\5\u0196\u00cc\2\u081c\u081d\7\u0080\2\2\u081d\u0195\3\2\2\2\u081e\u081f"+
		"\5\u0184\u00c3\2\u081f\u0820\7j\2\2\u0820\u0828\5\u0156\u00ac\2\u0821"+
		"\u0822\7\u008a\2\2\u0822\u0823\5\u0184\u00c3\2\u0823\u0824\7j\2\2\u0824"+
		"\u0825\5\u0156\u00ac\2\u0825\u0827\3\2\2\2\u0826\u0821\3\2\2\2\u0827\u082a"+
		"\3\2\2\2\u0828\u0826\3\2\2\2\u0828\u0829\3\2\2\2\u0829\u0197\3\2\2\2\u082a"+
		"\u0828\3\2\2\2\u082b\u082c\7J\2\2\u082c\u082d\5\u013a\u009e\2\u082d\u082f"+
		"\78\2\2\u082e\u0830\7\u008c\2\2\u082f\u082e\3\2\2\2\u082f\u0830\3\2\2"+
		"\2\u0830\u0831\3\2\2\2\u0831\u0832\5\u0182\u00c2\2\u0832\u0833\7\u00a1"+
		"\2\2\u0833\u0835\7Q\2\2\u0834\u0836\5\u017e\u00c0\2\u0835\u0834\3\2\2"+
		"\2\u0835\u0836\3\2\2\2\u0836\u0837\3\2\2\2\u0837\u0838\5\u019a\u00ce\2"+
		"\u0838\u0839\7\u0080\2\2\u0839\u0199\3\2\2\2\u083a\u083b\5\u013a\u009e"+
		"\2\u083b\u083c\7j\2\2\u083c\u0844\5\u0156\u00ac\2\u083d\u083e\7\u008a"+
		"\2\2\u083e\u083f\5\u013a\u009e\2\u083f\u0840\7j\2\2\u0840\u0841\5\u0156"+
		"\u00ac\2\u0841\u0843\3\2\2\2\u0842\u083d\3\2\2\2\u0843\u0846\3\2\2\2\u0844"+
		"\u0842\3\2\2\2\u0844\u0845\3\2\2\2\u0845\u019b\3\2\2\2\u0846\u0844\3\2"+
		"\2\2\u0847\u084b\5\u019e\u00d0\2\u0848\u084b\5\u01a0\u00d1\2\u0849\u084b"+
		"\5\u01a2\u00d2\2\u084a\u0847\3\2\2\2\u084a\u0848\3\2\2\2\u084a\u0849\3"+
		"\2\2\2\u084b\u019d\3\2\2\2\u084c\u084d\5\u0182\u00c2\2\u084d\u084e\7\u00a4"+
		"\2\2\u084e\u084f\5\u013a\u009e\2\u084f\u0850\7\u0080\2\2\u0850\u019f\3"+
		"\2\2\2\u0851\u0852\5\u0182\u00c2\2\u0852\u0853\7\u00a4\2\2\u0853\u0854"+
		"\5\u0190\u00c9\2\u0854\u0855\7\u0080\2\2\u0855\u01a1\3\2\2\2\u0856\u0857"+
		"\7J\2\2\u0857\u0858\5\u013a\u009e\2\u0858\u085a\78\2\2\u0859\u085b\7\u008c"+
		"\2\2\u085a\u0859\3\2\2\2\u085a\u085b\3\2\2\2\u085b\u085c\3\2\2\2\u085c"+
		"\u085d\5\u0182\u00c2\2\u085d\u085e\7\u00a4\2\2\u085e\u085f\5\u019a\u00ce"+
		"\2\u085f\u0860\7\u0080\2\2\u0860\u01a3\3\2\2\2\u0861\u0862\5\u01a6\u00d4"+
		"\2\u0862\u0863\7\u0080\2\2\u0863\u01a5\3\2\2\2\u0864\u0865\5\6\4\2\u0865"+
		"\u01a7\3\2\2\2\u0866\u0867\7\\\2\2\u0867\u0868\5\u016a\u00b6\2\u0868\u0869"+
		"\7\n\2\2\u0869\u0871\5\u015e\u00b0\2\u086a\u086b\7;\2\2\u086b\u086c\5"+
		"\u016a\u00b6\2\u086c\u086d\7\n\2\2\u086d\u086e\5\u015e\u00b0\2\u086e\u0870"+
		"\3\2\2\2\u086f\u086a\3\2\2\2\u0870\u0873\3\2\2\2\u0871\u086f\3\2\2\2\u0871"+
		"\u0872\3\2\2\2\u0872\u0878\3\2\2\2\u0873\u0871\3\2\2\2\u0874\u0875\7\30"+
		"\2\2\u0875\u0879\5\u015e\u00b0\2\u0876\u0879\3\2\2\2\u0877\u0879\6\u00d5"+
		"\n\2\u0878\u0874\3\2\2\2\u0878\u0876\3\2\2\2\u0878\u0877\3\2\2\2\u0879"+
		"\u087a\3\2\2\2\u087a\u087b\7\67\2\2\u087b\u087d\7\\\2\2\u087c\u087e\5"+
		"\u01e8\u00f5\2\u087d\u087c\3\2\2\2\u087d\u087e\3\2\2\2\u087e\u087f\3\2"+
		"\2\2\u087f\u0880\7\u0080\2\2\u0880\u01a9\3\2\2\2\u0881\u0883\7c\2\2\u0882"+
		"\u0884\7\u008c\2\2\u0883\u0882\3\2\2\2\u0883\u0884\3\2\2\2\u0884\u0885"+
		"\3\2\2\2\u0885\u0886\5\u013a\u009e\2\u0886\u0888\7_\2\2\u0887\u0889\5"+
		"\u01ac\u00d7\2\u0888\u0887\3\2\2\2\u0889\u088a\3\2\2\2\u088a\u0888\3\2"+
		"\2\2\u088a\u088b\3\2\2\2\u088b\u088c\3\2\2\2\u088c\u088d\7\67\2\2\u088d"+
		"\u088f\7c\2\2\u088e\u0890\7\u008c\2\2\u088f\u088e\3\2\2\2\u088f\u0890"+
		"\3\2\2\2\u0890\u0892\3\2\2\2\u0891\u0893\5\u01e8\u00f5\2\u0892\u0891\3"+
		"\2\2\2\u0892\u0893\3\2\2\2\u0893\u0894\3\2\2\2\u0894\u0895\7\u0080\2\2"+
		"\u0895\u01ab\3\2\2\2\u0896\u0897\7j\2\2\u0897\u0898\5\u0156\u00ac\2\u0898"+
		"\u0899\7\u00a6\2\2\u0899\u089a\5\u015e\u00b0\2\u089a\u01ad\3\2\2\2\u089b"+
		"\u089d\5\u01b0\u00d9\2\u089c\u089b\3\2\2\2\u089c\u089d\3\2\2\2\u089d\u089e"+
		"\3\2\2\2\u089e\u089f\7\34\2\2\u089f\u08a0\5\u015e\u00b0\2\u08a0\u08a1"+
		"\7\67\2\2\u08a1\u08a3\7\34\2\2\u08a2\u08a4\5\u01e8\u00f5\2\u08a3\u08a2"+
		"\3\2\2\2\u08a3\u08a4\3\2\2\2\u08a4\u08a5\3\2\2\2\u08a5\u08a6\7\u0080\2"+
		"\2\u08a6\u01af\3\2\2\2\u08a7\u08a8\7R\2\2\u08a8\u08ac\5\u016a\u00b6\2"+
		"\u08a9\u08aa\7Z\2\2\u08aa\u08ac\5\u01b2\u00da\2\u08ab\u08a7\3\2\2\2\u08ab"+
		"\u08a9\3\2\2\2\u08ac\u01b1\3\2\2\2\u08ad\u08ae\5\u0202\u0102\2\u08ae\u08af"+
		"\7F\2\2\u08af\u08b0\5r:\2\u08b0\u01b3\3\2\2\2\u08b1\u08b3\7\16\2\2\u08b2"+
		"\u08b4\5\u01e8\u00f5\2\u08b3\u08b2\3\2\2\2\u08b3\u08b4\3\2\2\2\u08b4\u08b7"+
		"\3\2\2\2\u08b5\u08b6\7j\2\2\u08b6\u08b8\5\u016a\u00b6\2\u08b7\u08b5\3"+
		"\2\2\2\u08b7\u08b8\3\2\2\2\u08b8\u08b9\3\2\2\2\u08b9\u08ba\7\u0080\2\2"+
		"\u08ba\u01b5\3\2\2\2\u08bb\u08bd\7H\2\2\u08bc\u08be\5\u01e8\u00f5\2\u08bd"+
		"\u08bc\3\2\2\2\u08bd\u08be\3\2\2\2\u08be\u08c1\3\2\2\2\u08bf\u08c0\7j"+
		"\2\2\u08c0\u08c2\5\u016a\u00b6\2\u08c1\u08bf\3\2\2\2\u08c1\u08c2\3\2\2"+
		"\2\u08c2\u08c3\3\2\2\2\u08c3\u08c4\7\u0080\2\2\u08c4\u01b7\3\2\2\2\u08c5"+
		"\u08c7\7I\2\2\u08c6\u08c8\5\u013a\u009e\2\u08c7\u08c6\3\2\2\2\u08c7\u08c8"+
		"\3\2\2\2\u08c8\u08c9\3\2\2\2\u08c9\u08ca\7\u0080\2\2\u08ca\u01b9\3\2\2"+
		"\2\u08cb\u08cc\7l\2\2\u08cc\u08cd\7\u0080\2\2\u08cd\u01bb\3\2\2\2\u08ce"+
		"\u08d3\5\u01c4\u00e3\2\u08cf\u08d3\5\u01cc\u00e7\2\u08d0\u08d3\5\u01ce"+
		"\u00e8\2\u08d1\u08d3\5\u01d0\u00e9\2\u08d2\u08ce\3\2\2\2\u08d2\u08cf\3"+
		"\2\2\2\u08d2\u08d0\3\2\2\2\u08d2\u08d1\3\2\2\2\u08d3\u01bd\3\2\2\2\u08d4"+
		"\u08d5\5\u01e8\u00f5\2\u08d5\u08da\7\u008d\2\2\u08d6\u08db\5\u01c0\u00e1"+
		"\2\u08d7\u08db\5\u01d6\u00ec\2\u08d8\u08db\5\u01da\u00ee\2\u08d9\u08db"+
		"\5\u01bc\u00df\2\u08da\u08d6\3\2\2\2\u08da\u08d7\3\2\2\2\u08da\u08d8\3"+
		"\2\2\2\u08da\u08d9\3\2\2\2\u08db\u08de\3\2\2\2\u08dc\u08de\5\u01bc\u00df"+
		"\2\u08dd\u08d4\3\2\2\2\u08dd\u08dc\3\2\2\2\u08de\u01bf\3\2\2\2\u08df\u08e4"+
		"\7\13\2\2\u08e0\u08e1\7\u0081\2\2\u08e1\u08e2\5\u016a\u00b6\2\u08e2\u08e3"+
		"\7\u0082\2\2\u08e3\u08e5\3\2\2\2\u08e4\u08e0\3\2\2\2\u08e4\u08e5\3\2\2"+
		"\2\u08e5\u08e7\3\2\2\2\u08e6\u08e8\7_\2\2\u08e7\u08e6\3\2\2\2\u08e7\u08e8"+
		"\3\2\2\2\u08e8\u08e9\3\2\2\2\u08e9\u08ed\5\u01c2\u00e2\2\u08ea\u08ec\5"+
		"\34\17\2\u08eb\u08ea\3\2\2\2\u08ec\u08ef\3\2\2\2\u08ed\u08eb\3\2\2\2\u08ed"+
		"\u08ee\3\2\2\2\u08ee\u08f0\3\2\2\2\u08ef\u08ed\3\2\2\2\u08f0\u08f4\7 "+
		"\2\2\u08f1\u08f3\5\u01be\u00e0\2\u08f2\u08f1\3\2\2\2\u08f3\u08f6\3\2\2"+
		"\2\u08f4\u08f2\3\2\2\2\u08f4\u08f5\3\2\2\2\u08f5\u08f7\3\2\2\2\u08f6\u08f4"+
		"\3\2\2\2\u08f7\u08f8\7\67\2\2\u08f8\u08fa\7\13\2\2\u08f9\u08fb\5\u01e8"+
		"\u00f5\2\u08fa\u08f9\3\2\2\2\u08fa\u08fb\3\2\2\2\u08fb\u08fc\3\2\2\2\u08fc"+
		"\u08fd\7\u0080\2\2\u08fd\u01c1\3\2\2\2\u08fe\u0902\5\u00dco\2\u08ff\u0900"+
		"\5\u00eex\2\u0900\u0901\7\u0080\2\2\u0901\u0903\3\2\2\2\u0902\u08ff\3"+
		"\2\2\2\u0902\u0903\3\2\2\2\u0903\u0905\3\2\2\2\u0904\u08fe\3\2\2\2\u0904"+
		"\u0905\3\2\2\2\u0905\u090c\3\2\2\2\u0906\u090a\5\u00e0q\2\u0907\u0908"+
		"\5\u00f0y\2\u0908\u0909\7\u0080\2\2\u0909\u090b\3\2\2\2\u090a\u0907\3"+
		"\2\2\2\u090a\u090b\3\2\2\2\u090b\u090d\3\2\2\2\u090c\u0906\3\2\2\2\u090c"+
		"\u090d\3\2\2\2\u090d\u01c3\3\2\2\2\u090e\u0910\7\5\2\2\u090f\u090e\3\2"+
		"\2\2\u090f\u0910\3\2\2\2\u0910\u0911\3\2\2\2\u0911\u0916\7\3\2\2\u0912"+
		"\u0913\7\u0081\2\2\u0913\u0914\5\u01c6\u00e4\2\u0914\u0915\7\u0082\2\2"+
		"\u0915\u0917\3\2\2\2\u0916\u0912\3\2\2\2\u0916\u0917\3\2\2\2\u0917\u0919"+
		"\3\2\2\2\u0918\u091a\7_\2\2\u0919\u0918\3\2\2\2\u0919\u091a\3\2\2\2\u091a"+
		"\u091e\3\2\2\2\u091b\u091d\5\u01ca\u00e6\2\u091c\u091b\3\2\2\2\u091d\u0920"+
		"\3\2\2\2\u091e\u091c\3\2\2\2\u091e\u091f\3\2\2\2\u091f\u0921\3\2\2\2\u0920"+
		"\u091e\3\2\2\2\u0921\u0925\7 \2\2\u0922\u0924\5\u0160\u00b1\2\u0923\u0922"+
		"\3\2\2\2\u0924\u0927\3\2\2\2\u0925\u0923\3\2\2\2\u0925\u0926\3\2\2\2\u0926"+
		"\u0928\3\2\2\2\u0927\u0925\3\2\2\2\u0928\u092a\7\67\2\2\u0929\u092b\7"+
		"\5\2\2\u092a\u0929\3\2\2\2\u092a\u092b\3\2\2\2\u092b\u092c\3\2\2\2\u092c"+
		"\u092e\7\3\2\2\u092d\u092f\5\u01e8\u00f5\2\u092e\u092d\3\2\2\2\u092e\u092f"+
		"\3\2\2\2\u092f\u0930\3\2\2\2\u0930\u0931\7\u0080\2\2\u0931\u01c5\3\2\2"+
		"\2\u0932\u0935\7B\2\2\u0933\u0935\5\u0166\u00b4\2\u0934\u0932\3\2\2\2"+
		"\u0934\u0933\3\2\2\2\u0935\u01c7\3\2\2\2\u0936\u0946\5,\27\2\u0937\u0946"+
		"\5@!\2\u0938\u0946\5D#\2\u0939\u0946\5J&\2\u093a\u0946\5\u008eH\2\u093b"+
		"\u0946\5\u0094K\2\u093c\u0946\5\u00aaV\2\u093d\u0946\5\u00b0Y\2\u093e"+
		"\u0946\5\u00b2Z\2\u093f\u0946\5\u00f2z\2\u0940\u0946\5\u00f6|\2\u0941"+
		"\u0946\5\u0106\u0084\2\u0942\u0946\5\u01ea\u00f6\2\u0943\u0946\5\u00fa"+
		"~\2\u0944\u0946\5\u0100\u0081\2\u0945\u0936\3\2\2\2\u0945\u0937\3\2\2"+
		"\2\u0945\u0938\3\2\2\2\u0945\u0939\3\2\2\2\u0945\u093a\3\2\2\2\u0945\u093b"+
		"\3\2\2\2\u0945\u093c\3\2\2\2\u0945\u093d\3\2\2\2\u0945\u093e\3\2\2\2\u0945"+
		"\u093f\3\2\2\2\u0945\u0940\3\2\2\2\u0945\u0941\3\2\2\2\u0945\u0942\3\2"+
		"\2\2\u0945\u0943\3\2\2\2\u0945\u0944\3\2\2\2\u0946\u01c9\3\2\2\2\u0947"+
		"\u094b\5\u01c8\u00e5\2\u0948\u094b\5<\37\2\u0949\u094b\5H%\2\u094a\u0947"+
		"\3\2\2\2\u094a\u0948\3\2\2\2\u094a\u0949\3\2\2\2\u094b\u01cb\3\2\2\2\u094c"+
		"\u094e\7\5\2\2\u094d\u094c\3\2\2\2\u094d\u094e\3\2\2\2\u094e\u094f\3\2"+
		"\2\2\u094f\u0950\5\u01a4\u00d3\2\u0950\u01cd\3\2\2\2\u0951\u0953\7\5\2"+
		"\2\u0952\u0951\3\2\2\2\u0952\u0953\3\2\2\2\u0953\u0954\3\2\2\2\u0954\u0955"+
		"\5\u016e\u00b8\2\u0955\u01cf\3\2\2\2\u0956\u0958\7\5\2\2\u0957\u0956\3"+
		"\2\2\2\u0957\u0958\3\2\2\2\u0958\u095b\3\2\2\2\u0959\u095c\5\u01d2\u00ea"+
		"\2\u095a\u095c\5\u01d4\u00eb\2\u095b\u0959\3\2\2\2\u095b\u095a\3\2\2\2"+
		"\u095c\u01d1\3\2\2\2\u095d\u095e\5\u0182\u00c2\2\u095e\u0960\7\u00a1\2"+
		"\2\u095f\u0961\7\25\2\2\u0960\u095f\3\2\2\2\u0960\u0961\3\2\2\2\u0961"+
		"\u0963\3\2\2\2\u0962\u0964\5\u0180\u00c1\2\u0963\u0962\3\2\2\2\u0963\u0964"+
		"\3\2\2\2\u0964\u0967\3\2\2\2\u0965\u0968\5\u0184\u00c3\2\u0966\u0968\5"+
		"\u018c\u00c7\2\u0967\u0965\3\2\2\2\u0967\u0966\3\2\2\2\u0968\u0969\3\2"+
		"\2\2\u0969\u096a\7\u0080\2\2\u096a\u01d3\3\2\2\2\u096b\u096c\7J\2\2\u096c"+
		"\u096d\5\u013a\u009e\2\u096d\u096f\78\2\2\u096e\u0970\7\u008c\2\2\u096f"+
		"\u096e\3\2\2\2\u096f\u0970\3\2\2\2\u0970\u0971\3\2\2\2\u0971\u0972\5\u0182"+
		"\u00c2\2\u0972\u0974\7\u00a1\2\2\u0973\u0975\7\25\2\2\u0974\u0973\3\2"+
		"\2\2\u0974\u0975\3\2\2\2\u0975\u0977\3\2\2\2\u0976\u0978\5\u0180\u00c1"+
		"\2\u0977\u0976\3\2\2\2\u0977\u0978\3\2\2\2\u0978\u0979\3\2\2\2\u0979\u097a"+
		"\5\u0196\u00cc\2\u097a\u097b\7\u0080\2\2\u097b\u01d5\3\2\2\2\u097c\u097e"+
		"\5\u01d8\u00ed\2\u097d\u097f\5\u00eex\2\u097e\u097d\3\2\2\2\u097e\u097f"+
		"\3\2\2\2\u097f\u0981\3\2\2\2\u0980\u0982\5\u00f0y\2\u0981\u0980\3\2\2"+
		"\2\u0981\u0982\3\2\2\2\u0982\u0983\3\2\2\2\u0983\u0984\7\u0080\2\2\u0984"+
		"\u01d7\3\2\2\2\u0985\u0987\7\7\2\2\u0986\u0985\3\2\2\2\u0986\u0987\3\2"+
		"\2\2\u0987\u0988\3\2\2\2\u0988\u0994\5\6\4\2\u0989\u098a\7\17\2\2\u098a"+
		"\u098f\5\6\4\2\u098b\u098c\7\u0081\2\2\u098c\u098d\5\u0202\u0102\2\u098d"+
		"\u098e\7\u0082\2\2\u098e\u0990\3\2\2\2\u098f\u098b\3\2\2\2\u098f\u0990"+
		"\3\2\2\2\u0990\u0994\3\2\2\2\u0991\u0992\7e\2\2\u0992\u0994\5\6\4\2\u0993"+
		"\u0986\3\2\2\2\u0993\u0989\3\2\2\2\u0993\u0991\3\2\2\2\u0994\u01d9\3\2"+
		"\2\2\u0995\u0999\5\u01dc\u00ef\2\u0996\u0999\5\u01de\u00f0\2\u0997\u0999"+
		"\5\u01e0\u00f1\2\u0998\u0995\3\2\2\2\u0998\u0996\3\2\2\2\u0998\u0997\3"+
		"\2\2\2\u0999\u01db\3\2\2\2\u099a\u099b\7Z\2\2\u099b\u099c\5\u01b2\u00da"+
		"\2\u099c\u099d\7D\2\2\u099d\u099e\5\u01e6\u00f4\2\u099e\u099f\7\67\2\2"+
		"\u099f\u09a1\7D\2\2\u09a0\u09a2\5\u01e8\u00f5\2\u09a1\u09a0\3\2\2\2\u09a1"+
		"\u09a2\3\2\2\2\u09a2\u09a3\3\2\2\2\u09a3\u09a4\7\u0080\2\2\u09a4\u01dd"+
		"\3\2\2\2\u09a5\u09a9\7\\\2\2\u09a6\u09a7\5\u01e8\u00f5\2\u09a7\u09a8\7"+
		"\u008d\2\2\u09a8\u09aa\3\2\2\2\u09a9\u09a6\3\2\2\2\u09a9\u09aa\3\2\2\2"+
		"\u09aa\u09ab\3\2\2\2\u09ab\u09ac\5\u016a\u00b6\2\u09ac\u09ad\7D\2\2\u09ad"+
		"\u09ba\5\u01e6\u00f4\2\u09ae\u09b2\7;\2\2\u09af\u09b0\5\u01e8\u00f5\2"+
		"\u09b0\u09b1\7\u008d\2\2\u09b1\u09b3\3\2\2\2\u09b2\u09af\3\2\2\2\u09b2"+
		"\u09b3\3\2\2\2\u09b3\u09b4\3\2\2\2\u09b4\u09b5\5\u016a\u00b6\2\u09b5\u09b6"+
		"\7D\2\2\u09b6\u09b7\5\u01e6\u00f4\2\u09b7\u09b9\3\2\2\2\u09b8\u09ae\3"+
		"\2\2\2\u09b9\u09bc\3\2\2\2\u09ba\u09b8\3\2\2\2\u09ba\u09bb\3\2\2\2\u09bb"+
		"\u09c6\3\2\2\2\u09bc\u09ba\3\2\2\2\u09bd\u09c1\7\30\2\2\u09be\u09bf\5"+
		"\u01e8\u00f5\2\u09bf\u09c0\7\u008d\2\2\u09c0\u09c2\3\2\2\2\u09c1\u09be"+
		"\3\2\2\2\u09c1\u09c2\3\2\2\2\u09c2\u09c3\3\2\2\2\u09c3\u09c4\7D\2\2\u09c4"+
		"\u09c7\5\u01e6\u00f4\2\u09c5\u09c7\6\u00f0\13\2\u09c6\u09bd\3\2\2\2\u09c6"+
		"\u09c5\3\2\2\2\u09c7\u09c8\3\2\2\2\u09c8\u09c9\7\67\2\2\u09c9\u09cb\7"+
		"D\2\2\u09ca\u09cc\5\u01e8\u00f5\2\u09cb\u09ca\3\2\2\2\u09cb\u09cc\3\2"+
		"\2\2\u09cc\u09cd\3\2\2\2\u09cd\u09ce\7\u0080\2\2\u09ce\u01df\3\2\2\2\u09cf"+
		"\u09d0\7c\2\2\u09d0\u09d1\5\u013a\u009e\2\u09d1\u09d3\7D\2\2\u09d2\u09d4"+
		"\5\u01e2\u00f2\2\u09d3\u09d2\3\2\2\2\u09d4\u09d5\3\2\2\2\u09d5\u09d3\3"+
		"\2\2\2\u09d5\u09d6\3\2\2\2\u09d6\u09d7\3";
	private static final String _serializedATNSegment1 =
		"\2\2\2\u09d7\u09d8\7\67\2\2\u09d8\u09da\7D\2\2\u09d9\u09db\5\u01e8\u00f5"+
		"\2\u09da\u09d9\3\2\2\2\u09da\u09db\3\2\2\2\u09db\u09dc\3\2\2\2\u09dc\u09dd"+
		"\7\u0080\2\2\u09dd\u01e1\3\2\2\2\u09de\u09e2\7j\2\2\u09df\u09e0\5\u01e8"+
		"\u00f5\2\u09e0\u09e1\7\u008d\2\2\u09e1\u09e3\3\2\2\2\u09e2\u09df\3\2\2"+
		"\2\u09e2\u09e3\3\2\2\2\u09e3\u09e4\3\2\2\2\u09e4\u09e5\5\u0156\u00ac\2"+
		"\u09e5\u09e6\7\u00a6\2\2\u09e6\u09e7\5\u01e4\u00f3\2\u09e7\u01e3\3\2\2"+
		"\2\u09e8\u09ea\5\34\17\2\u09e9\u09e8\3\2\2\2\u09ea\u09ed\3\2\2\2\u09eb"+
		"\u09e9\3\2\2\2\u09eb\u09ec\3\2\2\2\u09ec\u09ee\3\2\2\2\u09ed\u09eb\3\2"+
		"\2\2\u09ee\u09f2\7 \2\2\u09ef\u09f1\5\u01be\u00e0\2\u09f0\u09ef\3\2\2"+
		"\2\u09f1\u09f4\3\2\2\2\u09f2\u09f0\3\2\2\2\u09f2\u09f3\3\2\2\2\u09f3\u09f5"+
		"\3\2\2\2\u09f4\u09f2\3\2\2\2\u09f5\u09f7\7\67\2\2\u09f6\u09f8\5\u01e8"+
		"\u00f5\2\u09f7\u09f6\3\2\2\2\u09f7\u09f8\3\2\2\2\u09f8\u09f9\3\2\2\2\u09f9"+
		"\u0a01\7\u0080\2\2\u09fa\u09fc\5\u01be\u00e0\2\u09fb\u09fa\3\2\2\2\u09fc"+
		"\u09ff\3\2\2\2\u09fd\u09fb\3\2\2\2\u09fd\u09fe\3\2\2\2\u09fe\u0a01\3\2"+
		"\2\2\u09ff\u09fd\3\2\2\2\u0a00\u09eb\3\2\2\2\u0a00\u09fd\3\2\2\2\u0a01"+
		"\u01e5\3\2\2\2\u0a02\u0a04\5\34\17\2\u0a03\u0a02\3\2\2\2\u0a04\u0a07\3"+
		"\2\2\2\u0a05\u0a03\3\2\2\2\u0a05\u0a06\3\2\2\2\u0a06\u0a08\3\2\2\2\u0a07"+
		"\u0a05\3\2\2\2\u0a08\u0a0c\7 \2\2\u0a09\u0a0b\5\u01be\u00e0\2\u0a0a\u0a09"+
		"\3\2\2\2\u0a0b\u0a0e\3\2\2\2\u0a0c\u0a0a\3\2\2\2\u0a0c\u0a0d\3\2\2\2\u0a0d"+
		"\u0a16\3\2\2\2\u0a0e\u0a0c\3\2\2\2\u0a0f\u0a11\5\u01be\u00e0\2\u0a10\u0a0f"+
		"\3\2\2\2\u0a11\u0a14\3\2\2\2\u0a12\u0a10\3\2\2\2\u0a12\u0a13\3\2\2\2\u0a13"+
		"\u0a16\3\2\2\2\u0a14\u0a12\3\2\2\2\u0a15\u0a05\3\2\2\2\u0a15\u0a12\3\2"+
		"\2\2\u0a16\u01e7\3\2\2\2\u0a17\u0a18\5\u0202\u0102\2\u0a18\u01e9\3\2\2"+
		"\2\u0a19\u0a1a\7\31\2\2\u0a1a\u0a1f\5\22\n\2\u0a1b\u0a1c\7\u008a\2\2\u0a1c"+
		"\u0a1e\5\22\n\2\u0a1d\u0a1b\3\2\2\2\u0a1e\u0a21\3\2\2\2\u0a1f\u0a1d\3"+
		"\2\2\2\u0a1f\u0a20\3\2\2\2\u0a20\u0a22\3\2\2\2\u0a21\u0a1f\3\2\2\2\u0a22"+
		"\u0a23\7\u0080\2\2\u0a23\u01eb\3\2\2\2\u0a24\u0a26\5\u01ee\u00f8\2\u0a25"+
		"\u0a24\3\2\2\2\u0a26\u0a29\3\2\2\2\u0a27\u0a25\3\2\2\2\u0a27\u0a28\3\2"+
		"\2\2\u0a28\u0a2a\3\2\2\2\u0a29\u0a27\3\2\2\2\u0a2a\u0a2b\7\2\2\3\u0a2b"+
		"\u01ed\3\2\2\2\u0a2c\u0a2d\5\u01fc\u00ff\2\u0a2d\u0a2e\5\u01f0\u00f9\2"+
		"\u0a2e\u01ef\3\2\2\2\u0a2f\u0a32\5\u01f2\u00fa\2\u0a30\u0a32\5\u01f4\u00fb"+
		"\2\u0a31\u0a2f\3\2\2\2\u0a31\u0a30\3\2\2\2\u0a32\u01f1\3\2\2\2\u0a33\u0a39"+
		"\5\24\13\2\u0a34\u0a39\5\36\20\2\u0a35\u0a39\5D#\2\u0a36\u0a39\5J&\2\u0a37"+
		"\u0a39\5\u01fa\u00fe\2\u0a38\u0a33\3\2\2\2\u0a38\u0a34\3\2\2\2\u0a38\u0a35"+
		"\3\2\2\2\u0a38\u0a36\3\2\2\2\u0a38\u0a37\3\2\2\2\u0a39\u01f3\3\2\2\2\u0a3a"+
		"\u0a3d\5\32\16\2\u0a3b\u0a3d\5H%\2\u0a3c\u0a3a\3\2\2\2\u0a3c\u0a3b\3\2"+
		"\2\2\u0a3d\u01f5\3\2\2\2\u0a3e\u0a3f\7:\2\2\u0a3f\u0a40\5\u01f8\u00fd"+
		"\2\u0a40\u0a41\7\u0080\2\2\u0a41\u01f7\3\2\2\2\u0a42\u0a43\5x=\2\u0a43"+
		"\u01f9\3\2\2\2\u0a44\u0a45\7\4\2\2\u0a45\u0a46\5\u0202\u0102\2\u0a46\u0a47"+
		"\7_\2\2\u0a47\u0a48\5\u01fc\u00ff\2\u0a48\u0a4a\7\67\2\2\u0a49\u0a4b\7"+
		"\4\2\2\u0a4a\u0a49\3\2\2\2\u0a4a\u0a4b\3\2\2\2\u0a4b\u0a4d\3\2\2\2\u0a4c"+
		"\u0a4e\5\u0202\u0102\2\u0a4d\u0a4c\3\2\2\2\u0a4d\u0a4e\3\2\2\2\u0a4e\u0a4f"+
		"\3\2\2\2\u0a4f\u0a50\7\u0080\2\2\u0a50\u01fb\3\2\2\2\u0a51\u0a53\5\u01fe"+
		"\u0100\2\u0a52\u0a51\3\2\2\2\u0a53\u0a56\3\2\2\2\u0a54\u0a52\3\2\2\2\u0a54"+
		"\u0a55\3\2\2\2\u0a55\u01fd\3\2\2\2\u0a56\u0a54\3\2\2\2\u0a57\u0a5b\5\u01f6"+
		"\u00fc\2\u0a58\u0a5b\5\u01ea\u00f6\2\u0a59\u0a5b\5\u0200\u0101\2\u0a5a"+
		"\u0a57\3\2\2\2\u0a5a\u0a58\3\2\2\2\u0a5a\u0a59\3\2\2\2\u0a5b\u01ff\3\2"+
		"\2\2\u0a5c\u0a5d\7\4\2\2\u0a5d\u0a62\5\22\n\2\u0a5e\u0a5f\7\u008a\2\2"+
		"\u0a5f\u0a61\5\22\n\2\u0a60\u0a5e\3\2\2\2\u0a61\u0a64\3\2\2\2\u0a62\u0a60"+
		"\3\2\2\2\u0a62\u0a63\3\2\2\2\u0a63\u0a65\3\2\2\2\u0a64\u0a62\3\2\2\2\u0a65"+
		"\u0a66\7\u0080\2\2\u0a66\u0201\3\2\2\2\u0a67\u0a68\t\23\2\2\u0a68\u0203"+
		"\3\2\2\2\u0132\u0209\u020e\u0216\u021a\u0222\u022c\u0237\u023e\u0241\u0246"+
		"\u024d\u0250\u0254\u0257\u025e\u0263\u0268\u0272\u0279\u027e\u0281\u0288"+
		"\u0292\u029a\u02a0\u02a3\u02aa\u02b1\u02b7\u02c3\u02c8\u02cc\u02d3\u02da"+
		"\u02de\u02e9\u02ee\u02f1\u02f7\u02fa\u02ff\u0302\u0308\u0312\u0316\u0321"+
		"\u0328\u032d\u0330\u033c\u033f\u0349\u034c\u0350\u035b\u035d\u0362\u0367"+
		"\u036a\u0372\u037b\u0381\u0384\u038e\u0396\u03a0\u03aa\u03b1\u03bb\u03c1"+
		"\u03cf\u03d3\u03dc\u03ee\u03f4\u03f6\u0400\u0407\u040d\u0412\u041e\u0429"+
		"\u043e\u0444\u044a\u0450\u0457\u045e\u0462\u046f\u0478\u047c\u0483\u0487"+
		"\u0490\u049a\u049e\u04a4\u04ac\u04b5\u04b9\u04c0\u04c8\u04d1\u04d7\u04db"+
		"\u04e5\u04eb\u04f1\u04f6\u04f9\u04fe\u0502\u0506\u050c\u0511\u0522\u0526"+
		"\u052b\u0531\u0534\u0539\u053f\u0546\u055a\u0561\u057c\u0584\u058d\u0595"+
		"\u0598\u059d\u05ab\u05b0\u05b7\u05c2\u05c5\u05c8\u05cd\u05de\u05e3\u05f3"+
		"\u060b\u0610\u0614\u0619\u061d\u0626\u0631\u0640\u0645\u0649\u064c\u064f"+
		"\u0657\u065c\u0667\u0679\u067e\u0682\u068e\u069a\u06a4\u06ae\u06b8\u06be"+
		"\u06cc\u06ce\u06d5\u06da\u06e0\u06ea\u06ec\u06f5\u0707\u070b\u070e\u0711"+
		"\u071b\u0723\u072c\u0732\u073b\u0740\u0746\u0755\u0759\u075c\u075f\u076b"+
		"\u077d\u0781\u0787\u078e\u0793\u0798\u07a1\u07aa\u07b3\u07b6\u07ba\u07c1"+
		"\u07c5\u07ca\u07cf\u07d1\u07d5\u07da\u07e9\u07ef\u07f5\u0804\u080a\u080e"+
		"\u0814\u0819\u0828\u082f\u0835\u0844\u084a\u085a\u0871\u0878\u087d\u0883"+
		"\u088a\u088f\u0892\u089c\u08a3\u08ab\u08b3\u08b7\u08bd\u08c1\u08c7\u08d2"+
		"\u08da\u08dd\u08e4\u08e7\u08ed\u08f4\u08fa\u0902\u0904\u090a\u090c\u090f"+
		"\u0916\u0919\u091e\u0925\u092a\u092e\u0934\u0945\u094a\u094d\u0952\u0957"+
		"\u095b\u0960\u0963\u0967\u096f\u0974\u0977\u097e\u0981\u0986\u098f\u0993"+
		"\u0998\u09a1\u09a9\u09b2\u09ba\u09c1\u09c6\u09cb\u09d5\u09da\u09e2\u09eb"+
		"\u09f2\u09f7\u09fd\u0a00\u0a05\u0a0c\u0a12\u0a15\u0a1f\u0a27\u0a31\u0a38"+
		"\u0a3c\u0a4a\u0a4d\u0a54\u0a5a\u0a62";
	public static final String _serializedATN = Utils.join(
		new String[] {
			_serializedATNSegment0,
			_serializedATNSegment1
		},
		""
	);
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}