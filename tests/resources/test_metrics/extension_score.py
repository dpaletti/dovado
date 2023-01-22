#Test metric defining that each configuration of neorv32 should have a total of 3 or more extensions

def extension_score(**kwargs) -> float:
	print("kwargs:")
	print(kwargs)
	return float(__helper_function([int(kwargs["CPU_EXTENSION_RISCV_A"]), int(kwargs["CPU_EXTENSION_RISCV_C"]), int(kwargs["CPU_EXTENSION_RISCV_E"]), int(kwargs["CPU_EXTENSION_RISCV_M"]), int(kwargs["CPU_EXTENSION_RISCV_U"]), int(kwargs["CPU_EXTENSION_RISCV_Zfinx"]), int(kwargs["CPU_EXTENSION_RISCV_Zicsr"]), int(kwargs["CPU_EXTENSION_RISCV_Zifencei"])]))

def __helper_function(variants):
	print(variants)
	return sum(variants) * -1000.00
