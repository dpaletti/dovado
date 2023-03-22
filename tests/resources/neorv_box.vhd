library ieee;
use ieee.std_logic_1164.all;

entity box is
  port (
    clk: in std_logic
    );
end entity box;

architecture box_arch of box is
  attribute DONT_TOUCH : string;
  attribute DONT_TOUCH of BOXED : label is "TRUE";
begin
  BOXED:  entity neorv32_top
    port map(
    clk_i => clk,
    -- remaining input ports are attached to internal clocks
    rstn_i => '1',

    );

end architecture box_arch;
