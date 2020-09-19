-- libraries read from the module to be boxed
library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_unsigned.all;
use work.GenericsPack.all;
use work.OpCodePack.all;

entity box is
  port (
    clk: in std_logic
    );
end entity box;

architecture box_arch of box is
  attribute DONT_TOUCH : string;
  attribute DONT_TOUCH of BOXED : label is "TRUE";
begin
  BOXED:  entity Work.Tile port map(
    clk => clk,
    -- remaining input ports are attached to internal clocks
    rst => '1',
addr_start_instr => std_logic_vector'((others => '1')),
first_character => std_logic_vector'((others => '1')),
ending_character => std_logic_vector'((others => '1')),
reload_complete => '1',
src_en => '1',
instr_address_wr => std_logic_vector'((others => '1')),
instr_data_in => std_logic_vector'((others => '1')),
instr_we_data => '1',
instr_we_opcode => '1',
data_address_wr => std_logic_vector'((others => '1')),
data_data_in => std_logic_vector'((others => '1')),
data_we => '1'

    );

end architecture box_arch;
