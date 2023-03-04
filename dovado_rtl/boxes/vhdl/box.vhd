-- libraries read from the module to be boxed
library ieee;
use ieee.std_logic_1164.all;
use work.pp_types.all;
use work.pp_utilities.all;

entity box is
  port (
    clk: in std_logic
    );
end entity box;

architecture box_arch of box is
  attribute DONT_TOUCH : string;
  attribute DONT_TOUCH of BOXED : label is "TRUE";
begin
  BOXED:  entity Work.pp_potato
    generic map(
ICACHE_LINE_SIZE => 2)
    port map(
    clk => clk,
    -- remaining input ports are attached to internal clocks
    reset => '1',
irq => std_logic_vector'((others => '1')),
wb_dat_in => std_logic_vector'((others => '1')),
wb_ack_in => '1'

    );

end architecture box_arch;
