-- libraries read from the module to be boxed
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use ieee.math_real.all;
use work.arm_types.all;

entity box is
  port (
    clk: in std_logic
    );
end entity box;

architecture box_arch of box is
  attribute DONT_TOUCH : string;
  attribute DONT_TOUCH of BOXED : label is "TRUE";
begin
  BOXED:  entity Work.cpu
    generic map(
CACHE_BLOCK_BITWIDTH => 5
)
    port map(
    clk => clk,
    -- remaining input ports are attached to internal clocks
    reset => '1',
avm_inst_waitrequest => '1',
avm_inst_readdatavalid => '1',
avm_inst_readdata => std_logic_vector'((others => '1')),
avm_data_waitrequest => '1',
avm_data_readdatavalid => '1',
avm_data_readdata => std_logic_vector'((others => '1')),
inr_irq => std_logic_vector'((others => '1'))

    );

end architecture box_arch;
